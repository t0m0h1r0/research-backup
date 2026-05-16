# Presentation Refinement Practices

status: COMPILED
compiled_by: ResearchArchitect
source_scope: current presentation refinement session and validated deck-review artifacts
primary_sources:
- `paper/presentations/heavy_tail_backup_refined/README.md`
- `paper/presentations/heavy_tail_backup_refined/review_reports/round3.md`
- `paper/presentations/heavy_tail_backup_refined/review_reports/round4.md`
- `paper/presentations/heavy_tail_backup_refined/review_reports/round5.md`
- `paper/presentations/heavy_tail_backup_refined/review_reports/round6.md`
- `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`

## Boundary

This page records reusable presentation-production lessons from the heavy-tail
backup deck refinement loop. These lessons are workflow and communication
knowledge, not empirical ransomware evidence, benchmark evidence, model
performance evidence, or manuscript-level proof.

Use this page when creating or reviewing technical research decks from
source-grounded material. Do not use it to promote new claims beyond the source
paper, registered evidence, or validated analysis artifacts.

## Core Knowledge

### WIKI-PRP-001: Preserve evidence boundaries while increasing theatricality

Visual drama can strengthen a research deck through larger lead messages,
clearer contrast, staged reveals, and stronger rhythm. It must not add
unsupported benchmark claims, external rates, SOTA language, empirical
performance claims, or operational recommendations not present in the source
material.

Research use: treat "theatrical" as a delivery layer over already bounded
claims. Keep slide footers, source maps, and review reports explicit enough that
readers can separate style from evidence.

Conditions: if the stronger phrasing changes the factual scope of a claim,
downgrade the phrasing or create a new evidence task before using it.

### WIKI-PRP-002: Replace specialist jargon with audience-action words

Unexplained operational jargon increases cognitive load even when it is
technically reasonable. In this session, the term "ランブック" was less useful
for the target audience than plain action language such as "判断手順".

Research use: prefer terms that tell the listener what decision or action the
slide supports. If a domain term is essential, define it on first use or move it
into notes rather than making it a lead-line dependency.

Conditions: retain precise technical terms only where replacing them would
damage correctness.

### WIKI-PRP-003: Chart-like proof objects need explicit axes and reading direction

Audience confusion increases when an authored diagram looks like a chart but
does not label its horizontal and vertical meaning. Every quantity-encoding
visual should state what the horizontal axis means, what the vertical axis means,
and which direction represents improvement, risk, age, or loss.

Research use: add visible cues such as "横軸", "縦軸", direction arrows, and a
one-line reading statement. For example, tell the audience whether they should
watch the tail, the threshold crossing, the retained clean span, or the failure
mass.

Conditions: purely decorative visuals do not need axes, but visuals used as
reasoning objects do.

### WIKI-PRP-004: Formula slides need a reading sequence, not only highlights

Highlighting terms in a formula is not enough when the audience does not know
how to read the expression. The deck became clearer after adding a dedicated
slide that walked through the clean-recovery horizon formula as a sequence:
first the operational quantity `a*`, then the numerator as the value of avoiding
total loss, then the denominator as the load of going back too far, and finally
`Delta* = a* / n` as the conversion into backup spacing.

Research use: make the slide answer "what should I look at first?" and "what
decision changes after I read this?" before asking the audience to parse a
technical expression.

Conditions: this generalizes the domain-specific clean-recovery-horizon reading
captured in `docs/wiki/ransomware_heavy_tail_backup_design.md`, but does not
replace the mathematical source.

### WIKI-PRP-005: Separate formula interpretation from design takeaway when load is high

A single slide can fail if it tries to teach notation, derive intuition, and
deliver the decision rule at once. Expanding the theatrical deck from six to
seven slides improved clarity by separating "how to read the expression" from
"what the expression tells the designer to decide".

Research use: when review feedback says the formula is not understandable,
consider adding a bridge slide rather than compressing more explanation into the
same page.

Conditions: only add slides when they reduce cognitive load; extra slides that
repeat claims without changing the reader's task should be removed.

### WIKI-PRP-006: Dramatic style should not rely on full-slide black backgrounds by default

Black full-slide backgrounds can create stage presence, but they can also feel
heavy and reduce readability across a full technical deck. In this session, a
light editorial system with white proof panels, thin red/green rails, pale
accent words, and localized dark emphasis kept the stronger tone while making
the deck easier to read.

Research use: reserve dark fields for formulas, conclusion strips, or local
contrast moments. Use light surfaces for dense reasoning, labels, and reviewable
proof panels.

Conditions: full-dark systems may still fit short keynotes or projection-first
venues, but they should be validated through rendered review rather than chosen
as the default.

### WIKI-PRP-007: Rendered review must complement mechanical layout checks

Automated layout QA can catch overlaps and minimum-gap failures, but it cannot
fully judge reading order, visual weight, or whether a proof object is
self-explanatory. Contact sheets and full-size checks of clarity-critical slides
are needed after each substantial visual change.

Research use: keep both mechanical checks and rendered inspection in the review
loop. Mechanical PASS is necessary, but not sufficient, for presentation
readiness.

Conditions: for small text-only edits, targeted slide inspection may be enough;
for theme, chart, or formula changes, inspect the rendered deck again.

### WIKI-PRP-008: Convert user review into closed issue records and ledger entries

Iterative deck work is easier to trust when each user critique becomes a named
finding, a concrete response, a verification note, and a ledger row. This keeps
stylistic decisions auditable and prevents repeated fixes from becoming
untraceable.

Research use: for each review round, record the trigger, severity before fix,
fix response, verification checks, and stop/continue decision.

Conditions: the ledger should summarize the material result; detailed slide
findings belong in the deck review artifacts.

## Reusable Checklist

- Does each slide have one lead message that can be understood without notes?
- Are all domain terms either familiar to the target audience or immediately
  explained in plain decision language?
- If a visual encodes quantities, are the axes, direction, and reading target
  explicit?
- If a formula appears, does the slide tell the audience where to look first and
  how the terms map to a design decision?
- Are interpretation and decision takeaway separated when the formula would
  otherwise overload the slide?
- Does the visual system support readability before style, especially for dense
  reasoning slides?
- Do source maps, footers, or review notes preserve the boundary between
  evidence and presentation rhetoric?
- Did rendered inspection of contact sheets and clarity-critical slides happen
  after visual or structural changes?
- Did each user review round close with a recorded finding, fix, verification,
  and stop/continue decision?

## Do Not Promote Without More Evidence

- Do not treat a presentation design choice as empirical evidence.
- Do not convert illustrative wording into manuscript claims without a source
  check.
- Do not infer that a visual theme is generally optimal without audience,
  venue, and readability validation.
- Do not introduce new ransomware rates, dataset facts, SOTA comparisons, or
  operational recommendations through slide polish.
