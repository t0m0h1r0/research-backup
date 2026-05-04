# ResearchArchitect Plan: XeLaTeX Recast

## Classification

FULL-PIPELINE: the task produces a material paper artifact derived from
`paper/source/heavy_tail_backup_v13.pdf` and
`paper/source/heavy_tail_backup_v13.txt`.

## Source Contract

- Do not overwrite `paper/source/heavy_tail_backup_v13.pdf`.
- Treat `paper/source/heavy_tail_backup_v13.txt` as extracted evidence.
- Produce derived writing under `paper/sections/`.
- Verify with a local XeLaTeX build.

## Execution Contract

Produce a self-contained XeLaTeX source that recasts the attached paper as a
clean Japanese manuscript:

- title, abstract, table of contents;
- model definitions and assumptions;
- key lemmas, theorems, propositions, and corollaries;
- a TikZ reconstruction of the state-transition figure;
- numerical-summary tables;
- reference list retained from the source paper.

## Verification

Run `latexmk -xelatex` against the produced source and record the result in the
final response.
