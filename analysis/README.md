# Numerical Evaluation Workspace

Use this directory for Python numerical checks that support paper critique or edits.

Each promoted study should use:

```text
analysis/{study}/
  run.py
  README.md
  results/
    manifest.json
    run.log
    metrics.csv or metrics.json
    figures/*.pdf
```

`manifest.json` is required before a numerical result can support a manuscript
change. It should record the exact command, parameters, source references, Python
and package versions, output files, random seed or `null`, timestamp, and verdict.

Exploratory notebooks may live in `notebooks/`, but notebook-only output is not
accepted as evidence.
