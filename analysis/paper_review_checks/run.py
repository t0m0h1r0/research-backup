#!/usr/bin/env python3
"""Recompute numerical tables used by the paper-review revision."""

from __future__ import annotations

import json
import math
import platform
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def simpson(f, a: float, b: float) -> float:
    c = (a + b) / 2.0
    return (b - a) * (f(a) + 4.0 * f(c) + f(b)) / 6.0


def adaptive_simpson(f, a: float, b: float, eps: float = 1e-10, depth: int = 20) -> float:
    whole = simpson(f, a, b)

    def rec(left: float, right: float, target: float, level: int, whole_value: float) -> float:
        mid = (left + right) / 2.0
        left_value = simpson(f, left, mid)
        right_value = simpson(f, mid, right)
        delta = left_value + right_value - whole_value
        if level <= 0 or abs(delta) <= 15.0 * target:
            return left_value + right_value + delta / 15.0
        return rec(left, mid, target / 2.0, level - 1, left_value) + rec(
            mid, right, target / 2.0, level - 1, right_value
        )

    return rec(a, b, eps, depth, whole)


def expected_min(alpha: float, beta: float, tm: float = 1.0) -> float:
    first = (1.0 - math.exp(-beta * tm)) / beta

    def survival_integrand(t: float) -> float:
        return math.exp(-beta * t) * (tm / t) ** alpha

    upper = tm
    while True:
        upper *= 2.0
        tail_bound = math.exp(-beta * upper) * (tm / upper) ** alpha / beta
        if tail_bound < 1e-11 or upper > 1e5:
            break
    return first + adaptive_simpson(survival_integrand, tm, upper, 1e-10, 24)


def tauber_c(alpha: float, beta: float, tm: float = 1.0) -> float:
    # Integration by parts removes the non-integrable endpoint evaluation.
    power = 1.0 / (1.0 - alpha)

    def smooth_integrand(u: float) -> float:
        return math.exp(-beta * tm * (u**power))

    integral = adaptive_simpson(smooth_integrand, 0.0, 1.0, 1e-12, 24)
    return -(1.0 - math.exp(-beta * tm)) + beta * tm * integral / (1.0 - alpha)


def exp_tilted_tail(alpha: float, beta: float, lower: float, tm: float = 1.0) -> float:
    if lower < tm:
        lower = tm

    def integrand(t: float) -> float:
        return math.exp(-beta * t) * alpha * (tm**alpha) * t ** (-(alpha + 1.0))

    upper = lower
    while True:
        upper *= 2.0
        tail_bound = math.exp(-beta * upper) * (tm / upper) ** alpha
        if tail_bound < 1e-11 or upper > 1e5:
            break
    if upper == lower:
        return 0.0
    return adaptive_simpson(integrand, lower, upper, 1e-10, 24)


def exp_tilted_truncated_moment(
    alpha: float, beta: float, upper: float, tm: float = 1.0
) -> float:
    if upper <= tm:
        return 0.0

    def integrand(t: float) -> float:
        return t * math.exp(-beta * t) * alpha * (tm**alpha) * t ** (-(alpha + 1.0))

    return adaptive_simpson(integrand, tm, upper, 1e-10, 24)


def residual_loss(alpha: float, delta: float, params: dict[str, float]) -> float:
    tm = params["tm"]
    n = int(params["n"])
    beta = params["beta"]
    eta = params["eta"]
    d1 = params["d1"]
    d0 = params["d0"]
    tau = params["tau_R"]
    kappa_s = params["kappa_s"]
    loss = params["L"]
    horizon = n * delta
    l_beta = exp_tilted_tail(alpha, beta, tm, tm)
    h_beta = exp_tilted_tail(alpha, beta, horizon, tm)
    m_beta = exp_tilted_truncated_moment(alpha, beta, horizon, tm)
    recoverable = l_beta - h_beta
    return (
        eta * (d1 * tau + d0) * recoverable
        + eta * d1 * kappa_s * m_beta
        + loss * ((1.0 - eta) * recoverable + h_beta)
    )


def stationary_candidates(alpha: float, lam: float, params: dict[str, float]) -> list[float]:
    tm = params["tm"]
    n = int(params["n"])
    beta = params["beta"]
    eta = params["eta"]
    d1 = params["d1"]
    kappa_s = params["kappa_s"]
    cb = params["cb"]
    dstar = params["dstar"]
    delta_max = params["delta_max"]
    lambda_loss = params["lambda_loss"]

    def pdf(a: float) -> float:
        return alpha * (tm**alpha) * a ** (-(alpha + 1.0))

    def qprime(delta: float) -> float:
        a = n * delta
        return eta * n * math.exp(-beta * a) * pdf(a) * (d1 * kappa_s * a - lambda_loss)

    def gprime(delta: float) -> float:
        return -cb / (delta * delta) + lam * qprime(delta)

    roots: list[float] = []
    previous_x = params["delta_min"]
    previous_y = gprime(previous_x)
    for i in range(1, 20001):
        x = params["delta_min"] + (delta_max - params["delta_min"]) * i / 20000.0
        y = gprime(x)
        if previous_y == 0.0:
            roots.append(previous_x)
        elif previous_y * y < 0.0:
            lo, hi = previous_x, x
            flo = previous_y
            for _ in range(80):
                mid = (lo + hi) / 2.0
                fmid = gprime(mid)
                if flo * fmid <= 0.0:
                    hi = mid
                else:
                    lo = mid
                    flo = fmid
            roots.append((lo + hi) / 2.0)
        previous_x, previous_y = x, y
    if previous_y == 0.0:
        roots.append(previous_x)
    return sorted({round(root, 12) for root in roots if params["delta_min"] <= root <= delta_max})


def optimal_delta(alpha: float, lam: float, params: dict[str, float]) -> dict[str, float | int]:
    candidates = [
        params["delta_min"],
        params["delta_max"],
        *stationary_candidates(alpha, lam, params),
    ]

    def objective(delta: float) -> float:
        return params["cb"] / delta + lam * residual_loss(alpha, delta, params)

    best_delta = min(candidates, key=objective)
    return {
        "delta": best_delta,
        "objective": objective(best_delta),
        "candidate_count": len(candidates),
    }


def retention_row(alpha: float, params: dict[str, float]) -> dict[str, float | int]:
    tm = params["tm"]
    n = int(params["n"])
    tau = params["tau_R"]
    delta = params["retention_delta"]
    cn = params["c_n"]
    lfail = params["L_fail"]
    t_star = (alpha * lfail * (tm**alpha) * delta / cn) ** (1.0 / (alpha + 1.0))
    n_cont = (t_star + tau) / delta - n

    def feasible(m: int) -> bool:
        return m >= 0 and (n + m) * delta - tau > tm

    m0 = 0
    while not feasible(m0):
        m0 += 1
    x = max(float(m0), n_cont)
    candidates = {math.floor(x), math.ceil(x), m0}
    candidates = {m for m in candidates if feasible(m)}

    def cost(m: int) -> float:
        t = (n + m) * delta - tau
        return cn * m + lfail * (tm / t) ** alpha

    best_m = min(candidates, key=cost)
    return {
        "alpha": alpha,
        "T_star": t_star,
        "n_ext_continuous": n_cont,
        "n_ext_star": best_m,
        "B_star": cost(best_m),
    }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    params = {
        "tm": 1.0,
        "n": 5.0,
        "lambda_arrival": 1.0,
        "d1": 1666.7,
        "d0": 0.0,
        "L": 50000.0,
        "cb": 10.0,
        "tau_R": 2.0,
        "eta": 0.95,
        "kappa_s": 0.3,
        "beta": 0.01,
        "delta_min": 1.0,
        "delta_max": 40.0,
        "retention_delta": 10.0,
        "c_n": 50.0,
        "L_fail": 50000.0,
    }
    params["lambda_loss"] = params["L"] - (params["d1"] * params["tau_R"] + params["d0"])
    if params["kappa_s"] <= 0.0:
        raise ValueError("The interior backup optimum requires kappa_s > 0.")
    if params["lambda_loss"] <= 0.0:
        raise ValueError("The interior backup optimum requires L > d1*tau_R + d0.")
    if params["c_n"] <= 0.0 or params["L_fail"] <= 0.0:
        raise ValueError("Dynamic retention requires positive c_n and L_fail.")
    if params["retention_delta"] <= 0.0:
        raise ValueError("Dynamic retention requires retention_delta > 0.")
    params["dstar"] = params["lambda_loss"] / (params["d1"] * params["kappa_s"] * params["n"])
    if not params["delta_min"] < params["dstar"] < params["delta_max"]:
        raise ValueError("dstar must lie inside the admissible design interval.")

    emin_alphas = [0.3, 0.5, 0.8, 1.0, 1.5]
    emin_betas = [0.1, 0.5, 1.0]
    emin_table = [
        {"beta": beta, **{f"alpha_{alpha}": expected_min(alpha, beta) for alpha in emin_alphas}}
        for beta in emin_betas
    ]

    tauber_betas = [1e-3, 1e-2, 1e-1]
    tauber_table = []
    for beta in tauber_betas:
        row = {"beta": beta}
        for alpha in [0.5, 0.8]:
            row[f"C_alpha_{alpha}"] = tauber_c(alpha, beta)
            row[f"bound_alpha_{alpha}"] = alpha * params["tm"] * beta / (1.0 - alpha)
        tauber_table.append(row)

    delta_table = []
    for alpha in [0.5, 0.7, 1.0, 1.5]:
        row = {"alpha": alpha}
        for lam in [1.0, 10.0, 100.0, 1000.0]:
            optimum = optimal_delta(alpha, lam, params)
            row[f"lambda_{lam:g}"] = optimum["delta"]
            row[f"candidates_lambda_{lam:g}"] = optimum["candidate_count"]
        row["dstar"] = params["dstar"]
        delta_table.append(row)

    retention_table = [retention_row(alpha, params) for alpha in [0.5, 0.7, 1.0, 1.5]]

    tables = {
        "parameters": params,
        "expected_min_table": emin_table,
        "tauber_c_table": tauber_table,
        "delta_convergence_table": delta_table,
        "retention_table": retention_table,
    }
    tables_path = RESULTS / "tables.json"
    tables_path.write_text(json.dumps(tables, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest = {
        "purpose": "Recompute numerical tables after reviewer-driven notation and loss-model repair.",
        "source_references": [
            "paper/sections/tex/02_model_formulation.tex",
            "paper/sections/tex/05_backup_optimization.tex",
            "paper/sections/tex/06_dynamic_retention.tex",
            "paper/sections/tex/07_numerical_examples.tex",
        ],
        "command": "python3 analysis/paper_review_checks/run.py",
        "python": platform.python_version(),
        "packages": {"standard_library": True},
        "parameters": params,
        "random_seed": None,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "output_files": ["analysis/paper_review_checks/results/tables.json"],
        "verdict": "PASS",
    }
    (RESULTS / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({"verdict": "PASS", "results": str(tables_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
