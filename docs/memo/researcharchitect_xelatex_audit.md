# ResearchArchitect Audit: XeLaTeX Recast

## Produced Artifact

- `paper/sections/heavy_tail_backup_recast_xelatex.tex`
- `paper/sections/.latexmkrc`

## Source References

- `paper/source/heavy_tail_backup_v13.pdf`
- `paper/source/heavy_tail_backup_v13.txt`
- `/Users/tomohiro/Downloads/heavy_tail_backup_v13.pdf`

## Verification

Command:

```sh
latexmk -xelatex heavy_tail_backup_recast_xelatex.tex
```

Working directory:

```text
paper/sections
```

Result: PASS. The build produced:

```text
paper/sections/build/heavy_tail_backup_recast_xelatex.pdf
```

PDF metadata observed with `pdfinfo`:

- Pages: 12
- Page size: A4
- Producer: `xdvipdfmx`

Residual warnings:

- `geometry` over-specification warning from the `bxjsarticle` geometry setup.
- One overfull hbox near the TikZ figure area.
- Japanese font italic shape fallback warning.

These warnings do not prevent PDF generation and do not indicate unresolved
cross-references or fatal LaTeX errors.

## Audit Verdict

VALIDATED for the requested XeLaTeX recast artifact. The source PDF was not
modified.

## Split-File Verification

The monolithic TeX source was split into a parent entry file and chapter-sized
inputs under `paper/sections/tex/`. Re-running:

```sh
latexmk -xelatex heavy_tail_backup_recast_xelatex.tex
```

from `paper/sections` completed successfully after the split and regenerated the
same 12-page PDF target.

## Warning-Cleanup Verification

After removing the duplicate `geometry` setup, avoiding italic theorem bodies for
Japanese text, and tightening the TikZ state diagram, a clean rebuild completed
successfully. Searching the final log for `Warning`, `Overfull`, `Underfull`,
`undefined`, `Undefined`, and `Error` returned no matches.
