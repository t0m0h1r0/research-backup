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
<purpose>Project-specific profile for improving the attached research paper while also improving the AI-agent research workflow that performs the improvement.</purpose>
<authority>The Root Admin (ResearchArchitect) edits this file when onboarding a new research project or changing project-specific acceptance rules. All other agents consult `docs/03_PROJECT_RULES.md`.</authority>
<rules>
- MUST NOT place project-specific rules in kernel-constitution.md, kernel-domains.md, kernel-ops.md, kernel-workflow.md, or kernel-antipatterns.md.
- MUST regenerate `docs/03_PROJECT_RULES.md` after any PR-{N} edit.
- MUST treat this project as an agent-improvement project first and a paper-completion project second.
- MUST preserve the source paper and all derived critique artifacts as external memory.
</rules>
<see_also>docs/03_PROJECT_RULES.md, paper/source/heavy_tail_backup_v13.pdf, paper/source/heavy_tail_backup_v13.txt</see_also>

--------------------------------------------------------
# § PROJECT IDENTITY

| Field | Value |
|-------|-------|
| Project type | General research workflow improvement + paper refinement |
| Research artifact | `paper/source/heavy_tail_backup_v13.pdf` |
| Research focus | Heavy-tailed ransomware dwell time, semi-Markov attack/defense model, optimal backup interval, detection-investment phase transition |
| Primary method | Mathematical proof audit, model consistency review, literature positioning, numerical reproducibility check, writing refinement |
| Target output | A deployable generic research-agent kernel plus review-ready paper improvement artifacts |
| Primary objective | Improve and operationalize the AI-agent workflow |
| Secondary objective | Improve the attached paper through traceable, evidence-backed critique and edits |

--------------------------------------------------------
# § PR - Project-Specific Rules

These rules apply to agents working on this project. They are intentionally portable:
only the paper topic and local artifact paths are project-specific.

## PR-1 - Agent-Workflow Primacy

The first success condition is not "finish the paper"; it is "create a reusable,
auditable research-agent workflow that can improve papers." Paper edits are test
cases for the workflow.

Every substantial paper-improvement task MUST produce two outputs:

| Output | Purpose |
|--------|---------|
| Research artifact | critique, proof patch, literature note, numerical check, or prose patch |
| Workflow artifact | what the agent learned about task routing, evidence needs, failure modes, or prompt rules |

If these conflict, preserve workflow learning and defer paper polish.

## PR-2 - Source Preservation and Traceability

The original PDF and extracted text are immutable source artifacts. Agents MUST NOT
overwrite them. Derived files MUST cite the source section, theorem, proposition,
equation, page, or extracted-text line range whenever possible.

Allowed derived locations:

| Artifact type | Directory |
|---------------|-----------|
| Mathematical audits | `docs/memo/` |
| Literature and citation checks | `docs/evidence/` |
| Numerical or symbolic checks | `analysis/` or `notebooks/` |
| Paper edit proposals | `paper/sections/` or `artifacts/A/` |
| Workflow lessons | `artifacts/M/` and `docs/02_ACTIVE_LEDGER.md` |

## PR-3 - Mathematical Rigor Gate

Claims involving optimality, convergence, compactness, Tauberian expansions,
renewal-reward applicability, or phase transitions MUST be independently checked.

Minimum audit standard:

| Check | Acceptance |
|-------|------------|
| Definitions | variables, domains, and parameter constraints are explicit |
| Existence | integrability or compactness assumptions are stated and justified |
| Uniqueness | derivative/sign/convexity argument is complete |
| Asymptotics | limits and remainder terms state uniformity conditions |
| Dependencies | theorem conclusions list which assumptions they use |

Unproved or underspecified steps become audit findings, not silent rewrites.

## PR-4 - Evidence and Citation Hygiene

Agents MUST separate three evidence classes:

| Class | Examples | Rule |
|-------|----------|------|
| Internal proof evidence | equations, lemmas, derivations in the paper | Cite exact source location |
| External literature evidence | cyber-risk, heavy-tail, semi-Markov, backup practice literature | Verify against bibliographic source before adding claims |
| Numerical evidence | scripts, logs, tables, figures | Record command, parameters, output path, and date |

No agent may invent citations or empirical facts. If a source is unavailable, mark the claim as needing source verification.

## PR-5 - Reproducible Analysis Standard

Any numerical or symbolic check introduced by the agents MUST be reproducible from
repository files alone.

Required for each check:

| Item | Requirement |
|------|-------------|
| Script/notebook | Stored under `analysis/` or `notebooks/` |
| Inputs | Local files or explicit parameter table |
| Output | CSV/JSON/Markdown/PDF figure as appropriate |
| Command | Captured in the artifact header or ledger |
| Interpretation | PASS/FAIL/INCONCLUSIVE with reason |

Python numerical evaluation SHOULD use the standard study layout:

```text
analysis/{study}/
  run.py
  README.md
  results/
    manifest.json
    metrics.csv or metrics.json
    figures/*.pdf
    run.log
```

`manifest.json` MUST include: purpose, source_refs, command, python_version,
package_versions for numpy/scipy/pandas/matplotlib when used, parameters, random_seed
or `null`, output_files, created_at_utc, and verdict.

Python scripts MUST be non-interactive, deterministic when randomness is used, and
safe to rerun. Scripts SHOULD accept command-line parameters and MUST NOT require
notebook state. Notebooks may be used for exploration, but promoted evidence must
be runnable as a script under `analysis/{study}/`.

Exploratory scratch work may exist temporarily, but only curated outputs can support paper changes.

## PR-6 - Review-Readiness Standard

Paper improvements should move the manuscript toward anonymous peer review.
Agents MUST prioritize:

1. correctness of proofs and assumptions,
2. clarity of contribution claims,
3. consistency of notation,
4. credible relation to prior work,
5. reproducibility of numerical examples,
6. concise Japanese academic prose.

Stylistic rewrites that do not improve at least one of these six points are out of scope.

--------------------------------------------------------
# § PORTABILITY NOTES

To adapt this system for another research project:

1. Replace only `kernel-project.md` with a new project profile.
2. Keep the generic kernel files unchanged unless a workflow limitation is discovered.
3. Regenerate `docs/03_PROJECT_RULES.md`.
4. Update source-artifact paths in `docs/01_PROJECT_MAP.md`.
5. Run prompt audit for project-specific leakage.

The PR-{N} numbering is local to this file. Universal rules use A-{N}, C-{N},
P-{N}, Q-{N}, AU-{N}, and AP-{N}.
</meta_section>
