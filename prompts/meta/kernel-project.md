# kernel-project.md - Project-Specific Profile v1.0.0
# ABSTRACT LAYER - PROJECT: rules, conventions, and constraints specific to THIS research project.
# This file is the SINGLE SOURCE OF TRUTH for project-specific rules.
#
# Separation principle:
#   - kernel-constitution.md -> Universal axioms - valid for ANY project
#   - kernel-domains.md      -> Generic research domain framework
#   - kernel-project.md      -> THIS file: project-type + project-instance rules
#
# Derived output: docs/03_PROJECT_RULES.md
# FOUNDATION: kernel-constitution.md §AXIOMS

<meta_section id="META-PROJECT" version="1.0.0" axiom_refs="phi6,A7,A10">
<purpose>Project-specific profile for AI-assisted anomaly detection research and for the deployable AI-agent workflow that supports that research.</purpose>
<authority>The Root Admin (ResearchArchitect) edits this file when onboarding a new research project or changing project-specific acceptance rules. All other agents consult `docs/03_PROJECT_RULES.md`.</authority>
<rules>
- MUST NOT place project-specific rules in kernel-constitution.md, kernel-domains.md, kernel-ops.md, kernel-workflow.md, or kernel-antipatterns.md.
- MUST regenerate `docs/03_PROJECT_RULES.md` after any PR-{N} edit.
- MUST treat this project as AI/ML anomaly detection research supported by an auditable agent workflow.
- MUST preserve source papers, datasets, experiment configs, model code, run logs, and derived critique artifacts as external memory.
- MUST NOT promote model-performance, novelty, or deployment-readiness claims without traceable evidence.
</rules>
<see_also>docs/03_PROJECT_RULES.md, docs/01_PROJECT_MAP.md, docs/interface/ResearchBrief.md</see_also>

--------------------------------------------------------
# § PROJECT IDENTITY

| Field | Value |
|-------|-------|
| Project type | AI-assisted anomaly detection research + deployable research-agent workflow |
| Research artifacts | Research brief, papers, datasets, model specs, code, experiment configs/results, figures, manuscript drafts, and presentation materials |
| Research focus | AI/ML anomaly detection, including problem framing, normal/anomaly definitions, model design, anomaly scoring, thresholding, evaluation, robustness, interpretability, and deployment constraints |
| Primary method | Literature grounding, hypothesis/model design, reproducible implementation, controlled experiments, ablation/statistical analysis, error analysis, and academic writing |
| Target output | Review-ready anomaly detection research artifacts, paper-grounded presentation materials, plus reusable AI-agent prompts/workflow artifacts |
| Primary objective | Produce credible, reproducible anomaly detection research outcomes |
| Secondary objective | Improve the reusable AI-agent research workflow through traceable lessons |

--------------------------------------------------------
# § PR - Project-Specific Rules

These rules apply to agents working on this project. They are intentionally portable:
only the anomaly-detection topic, active artifacts, and local project paths are
project-specific.

## PR-1 - Research Outcome and Agent-Workflow Co-Primacy

The agent system exists to advance the anomaly detection research. At the same
time, substantial tasks should preserve workflow learning so the research process
itself becomes more reliable.

Every substantial research task SHOULD produce two outputs:

| Output | Purpose |
|--------|---------|
| Research artifact | question map, literature note, model spec, code patch, experiment package, error analysis, figure, or manuscript patch |
| Workflow artifact | routing lesson, evidence need, prompt limitation, failure mode, or reusable task pattern |

If these conflict, protect the research evidence first and record the workflow
lesson without delaying a valid research deliverable.

## PR-2 - Source, Dataset, and Experiment Traceability

Agents MUST preserve traceability across source material, datasets, code, configs,
logs, metrics, figures, and prose claims. Active source papers and immutable data
inputs MUST NOT be overwritten.

Allowed source and derived locations:

| Artifact type | Directory |
|---------------|-----------|
| Source papers and source text | `paper/source/` |
| Immutable/raw datasets | `data/raw/` |
| Processed datasets with provenance | `data/processed/` |
| Research plans and model audits | `docs/memo/` |
| Literature, benchmark, and citation checks | `docs/evidence/` |
| Interface contracts | `docs/interface/` |
| Reusable model/evaluation code | `src/` |
| Reproducible experiments | `analysis/{study}/` |
| Exploratory notebooks | `notebooks/` |
| Manuscript sections and figures | `paper/sections/`, `paper/figures/`, `artifacts/A/` |
| Presentation decks and visual communication assets | `paper/presentations/`, `paper/figures/`, `artifacts/A/` |
| Workflow lessons | `artifacts/M/` and `docs/02_ACTIVE_LEDGER.md` |

Any performance value, table, or figure promoted to writing MUST cite dataset
version, split protocol, config path, command, run log, commit or artifact hash
when available, and creation date.

## PR-3 - Model and Claim Rigor Gate

Claims involving model novelty, detection accuracy, anomaly score validity,
threshold design, calibration, robustness, interpretability, causal/security
implications, or deployment readiness MUST be independently checked.

Minimum audit standard:

| Check | Acceptance |
|-------|------------|
| Definitions | normal class, anomaly class, unit of observation, time horizon, label semantics, and alert action are explicit |
| Assumptions | stationarity, contamination, label quality, class imbalance, temporal ordering, and operating constraints are stated |
| Baselines | comparison methods, preprocessing, hyperparameter budget, and selection protocol are documented |
| Metrics | AUROC/AUPRC/F1 or domain metrics are justified; false alarm rate and detection delay are considered when relevant |
| Leakage | train/validation/test boundaries, temporal leakage, entity leakage, and threshold tuning leakage are checked |
| Uncertainty | confidence intervals, repeated seeds, or sensitivity analysis are used for material quantitative claims |
| Failure modes | known blind spots, false positives/negatives, drift, and out-of-distribution behavior are recorded |

Unverified effectiveness claims remain hypotheses or audit findings, not paper
conclusions.

## PR-4 - Literature, Benchmark, and Citation Hygiene

Agents MUST separate four evidence classes:

| Class | Examples | Rule |
|-------|----------|------|
| Internal design evidence | model spec, loss, score function, threshold rule, ablation rationale | Cite exact artifact path and section |
| External literature evidence | anomaly detection methods, benchmark papers, surveys, deployment constraints | Verify against bibliographic source before adding claims |
| Dataset/benchmark evidence | dataset card, split file, preprocessing, label definition, license, known caveats | Record provenance and compatibility with the experiment protocol |
| Numerical evidence | scripts, configs, logs, metrics, figures | Record command, parameters, output path, and date |

No agent may invent citations, benchmark facts, SOTA claims, dataset properties,
or empirical numbers. If a source is unavailable, mark the claim as needing
source verification. Benchmark comparisons require compatible data splits,
metrics, preprocessing, and tuning budgets; otherwise they are reported as
non-comparable context.

## PR-5 - Reproducible Coding and Experiment Standard

Any coding or experiment artifact introduced by agents MUST be reproducible from
repository files plus explicitly registered external data sources.

Required for each promoted experiment:

| Item | Requirement |
|------|-------------|
| Script/notebook | Final evidence uses a non-interactive script under `analysis/{study}/`; notebooks are exploratory unless promoted |
| Inputs | Local files, registered external source, or explicit synthetic-data generator |
| Config | Stored config or parameter table, including model, preprocessing, split, seed, and threshold policy |
| Output | Metrics, logs, figures, and manifest under `analysis/{study}/results/` |
| Command | Captured in the manifest and ledger |
| Interpretation | PASS/FAIL/INCONCLUSIVE with reason and scope |

Standard experiment layout:

```text
analysis/{study}/
  run.py
  README.md
  config.yaml or config.json
  results/
    manifest.json
    metrics.csv or metrics.json
    figures/*.pdf or *.png
    run.log
```

`manifest.json` MUST include: purpose, source_refs, dataset_refs, command,
python_version, package_versions for core dependencies used, parameters,
random_seed or `null`, split protocol, metrics, output_files, created_at_utc,
and verdict.

Python scripts MUST be non-interactive, deterministic when randomness is used,
and safe to rerun. Exploratory scratch work may exist temporarily, but only
curated outputs can support manuscript or research-summary claims.

## PR-6 - Paper and Deployment Readiness Standard

Research outputs should move the project toward peer-reviewable anomaly detection
work and a redeployable agent workflow.

Agents MUST prioritize:

1. clear problem setting and anomaly taxonomy,
2. credible relation to prior anomaly detection work,
3. fair baseline and benchmark protocol,
4. reproducible implementation and experiments,
5. error analysis, ablation, and robustness checks,
6. honest limitation and failure-mode reporting,
7. concise academic prose in the chosen manuscript language,
8. presentation materials that preserve the paper's claims while using a clear narrative spine, slide-budget discipline, strong lead lines, evidence-grounded visuals, and third-party audience critique,
9. deployable prompts, docs, and workflow artifacts.

Stylistic rewrites that do not improve at least one of these points are out of
scope.

--------------------------------------------------------
# § PORTABILITY NOTES

To adapt this system for another research project:

1. Replace only `kernel-project.md` with a new project profile.
2. Keep the generic kernel files unchanged unless a workflow limitation is discovered.
3. Regenerate `docs/03_PROJECT_RULES.md`.
4. Update source-artifact paths and active assumptions in `docs/01_PROJECT_MAP.md`.
5. Run prompt audit for project-specific leakage.

The PR-{N} numbering is local to this file. Universal rules use A-{N}, C-{N},
P-{N}, Q-{N}, AU-{N}, and AP-{N}.
</meta_section>
