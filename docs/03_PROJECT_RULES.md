# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-project.md and regenerate.

# 03_PROJECT_RULES

## PR-1 - Agent-Workflow Primacy

The primary objective is to create a reusable, auditable research-agent workflow.
Paper edits are test cases for improving the workflow.

## PR-2 - Source Preservation and Traceability

The original PDF and extracted text under `paper/source/` are source artifacts and
must not be overwritten. Derived outputs cite section, theorem, equation, page, or
text location whenever possible.

## PR-3 - Mathematical Rigor Gate

Optimality, convergence, compactness, Tauberian, renewal-reward, and phase-transition
claims require independent verification of definitions, assumptions, existence,
uniqueness, asymptotics, and dependencies.

## PR-4 - Evidence and Citation Hygiene

Internal proof evidence, external literature evidence, and numerical evidence must
be separated. No invented citations or empirical facts are allowed.

## PR-5 - Reproducible Analysis Standard

Numerical or symbolic checks must be reproducible from repository files and include
script/notebook, inputs, outputs, command, and PASS/FAIL/INCONCLUSIVE interpretation.

Python numerical evaluation uses `analysis/{study}/run.py` plus
`analysis/{study}/results/manifest.json`. The manifest records purpose, source
references, command, Python/package versions, parameters, random seed or `null`,
output files, timestamp, and verdict. Notebook-only evidence is not sufficient.

## PR-6 - Review-Readiness Standard

Paper improvements prioritize proof correctness, contribution clarity, notation
consistency, prior-work credibility, reproducibility, and concise Japanese academic prose.
