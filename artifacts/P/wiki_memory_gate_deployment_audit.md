# Wiki Memory Gate Deployment Audit

created_at_utc: 2026-05-05T07:27:28Z
status: VALIDATED
owner: ResearchArchitect
branch: codex/researcharchitect-presentation-agent
worktree: /private/tmp/research-backup-presentation-agent

## Scope

Strengthened the meta-prompt system so wiki memory is used proactively instead
of passively. The change adds two global gates:

- WIKI-RETRIEVAL-GATE: search `docs/wiki/` or dispatch Librarian before
  difficult, investigative, ambiguous, or precedent-likely work.
- WIKI-COMPILE-GATE: before HAND-02 SUCCESS, classify whether important
  validated findings, reusable lessons, hard-failure resolutions, or significant
  negative results should be compiled to wiki memory.

## Produced

- `prompts/meta/kernel-workflow.md`
- `prompts/meta/kernel-ops.md`
- `prompts/meta/kernel-domains.md`
- `prompts/meta/kernel-roles.md`
- `prompts/agents-codex/_base.yaml`
- `prompts/agents-claude/_base.yaml`
- updated ResearchArchitect, TaskPlanner, Librarian, KnowledgeArchitect, and
  WikiAuditor prompts
- `artifacts/K/.gitkeep`

## Validation Intent

The design keeps canonical wiki entries restricted to VALIDATED artifacts while
allowing unvalidated but important findings to be captured as K-candidates under
`artifacts/K/`.

## CoVe

- Q1 logical consistency: pass; retrieval is read-only and compilation remains
  gated by validation.
- Q2 axiom compliance: pass; A11 is strengthened without weakening source
  integrity or domain sovereignty.
- Q3 scope fidelity: pass; the changes directly address proactive wiki search,
  reuse, and compilation.
