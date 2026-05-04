# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-project.md and regenerate.

# 03_PROJECT_RULES

## PR-1 - Research Outcome and Agent-Workflow Co-Primacy

The agent system exists to advance AI/ML anomaly detection research while also
capturing workflow lessons. Substantial tasks should produce a research artifact
and, when useful, a workflow artifact.

## PR-2 - Source, Dataset, and Experiment Traceability

Source papers, datasets, configs, code, logs, metrics, figures, and prose claims
must remain traceable. Active source papers and immutable/raw data must not be
overwritten.

## PR-3 - Model and Claim Rigor Gate

Claims about model novelty, detection accuracy, anomaly scores, thresholds,
calibration, robustness, interpretability, or deployment readiness require
independent checks of definitions, assumptions, baselines, metrics, leakage,
uncertainty, and failure modes.

## PR-4 - Literature, Benchmark, and Citation Hygiene

Internal design evidence, external literature, dataset/benchmark evidence, and
numerical evidence must be separated. No invented citations, SOTA claims,
dataset facts, or empirical numbers are allowed.

## PR-5 - Reproducible Coding and Experiment Standard

Promoted experiments must be runnable from repository files plus registered data
sources. Use `analysis/{study}/run.py`, a stored config, and
`analysis/{study}/results/manifest.json` with command, dependencies, parameters,
seed, split protocol, metrics, outputs, timestamp, and verdict.

## PR-6 - Paper and Deployment Readiness Standard

Outputs prioritize clear problem framing, prior-work positioning, fair baselines,
reproducibility, error analysis, robustness checks, honest limitations, concise
academic prose, and redeployable agent workflow artifacts.
