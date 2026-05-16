# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-*.md and regenerate.

# 00_GLOBAL_RULES - Generic Research Agent Kernel

## §A Core Axioms

- Truth before action: agents act on evidence, not belief.
- External memory first: durable state lives in files, git history, and artifacts.
- Fix at source: contradictions are resolved in the owning domain.
- Stateless agents: no result may depend on hidden conversation memory.
- Bounded autonomy: autonomy is earned through evidence and gates.
- Single source of truth: shared rules come from the pinned
  `prompts/research-agent` submodule and are materialized in
  project-local `prompts/meta/`; project rules live in
  `prompts/meta/kernel-project.md`.
- Broken symmetry: executor and auditor are separate for material outputs.
- Source integrity: source artifacts are immutable unless the user explicitly replaces them.
- Domain sovereignty: each artifact has one owning domain.
- Diff-first change control: changes should be reviewable and scoped.
- Knowledge-first retrieval: reusable findings are compiled into `docs/wiki/`.
- Wiki retrieval gate: search `docs/wiki/` before difficult, investigative, or precedent-likely work.
- Wiki compile gate: important validated findings and reusable lessons should become wiki entries.

## §C Research Implementation Rules

- C1: Keep reusable research code modular, tested, and documented.
- C2: Preserve existing behavior unless the task explicitly changes it.
- C3: Every numerical or symbolic check must record command, inputs, and outputs.
- C4: Do not substitute a model, approximation, or shortcut without a signed theory/evidence note.
- C5: Test output is evidence; interpretation must cite the output path.
- C6: Inconclusive verification is a valid result when stated precisely.

## §P Paper Rules

- P1: Claims must trace to proof, evidence, or explicit assumption.
- P2: Notation must be consistent across source, memo, and revision.
- P3: Reviewer- or audience-facing prose should be concise and defensible.
- P4: Paper and presentation edits require a revision brief unless the edit is purely typographic or presentational.

## §Q Prompt Rules

- Q1: Agent prompts contain role, scope, STOP conditions, output contract, and JIT refs.
- Q2: Prompt outputs must trace to metaprompt sources and preserve the local project profile.
- Q3-AUDIT: Prompt changes require leakage, JIT-discipline, support-artifact, wiki-packet, and token-budget checks.
- Q4: Workflow lessons can justify kernel changes only after evidence is recorded.

## §AU Audit Rules

- AU1: Audit checks artifact evidence, not hidden reasoning.
- AU2: Cross-domain consistency is required before VALIDATED state.
- AU3: Contradiction findings are useful outputs and must not be buried.

## §GIT Lifecycle

Use branch or task isolation for material work. Domain integration branches are
defined in `prompts/meta/kernel-domains.md`; `main` merges require explicit user
instruction and no-ff semantics.

## §P-E-V-A Execution Loop

PLAN -> EXECUTE -> VERIFY -> AUDIT. FAST-TRACK may collapse phases only when no
material claim, evidence, code, or paper section changes.

Before substantial PLAN/EXECUTE work, check whether prior wiki knowledge applies.
Before HAND-02 SUCCESS, state whether K-COMPILE was triggered or why it was not.
Prompt redeploys must generate project-local skills and agent prompts from the
pinned metaprompt submodule; never copy research-agent generated prompt artifacts.
