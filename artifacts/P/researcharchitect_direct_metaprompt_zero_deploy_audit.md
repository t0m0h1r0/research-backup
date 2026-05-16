# ResearchArchitect Direct Metaprompt Zero Deploy Audit

created_at_utc: 2026-05-16T16:50:14Z
status: VALIDATED
owner: ResearchArchitect
branch: codex/researcharchitect-direct-metaprompt-zero-deploy
worktree: /private/tmp/research-backup-direct-metaprompt-zero-deploy

## Scope

Removed the `prompts/upstream/` metaprompt source directory, pinned
`research-agent` directly at `prompts/research-agent`, imported the latest
shared metaprompts, preserved the project-local `kernel-project.md`, and
zero-base redeployed generated prompt artifacts. No `main` merge was performed.

## Source Intake

- Remote: `git@github.com:t0m0h1r0/research-agent.git`.
- Submodule path: `prompts/research-agent`.
- Imported revision: `ed388737ed01c479df4905925f1ec6791ff0f47d`
  (`Merge pull request #2 from t0m0h1r0/codex/meta-version-provenance-20260516`).
- Deprecated path removed: `prompts/upstream/`.
- Source record: `prompts/upstream.toml`.
- Project profile guard: `prompts/meta/kernel-project.md` SHA-256
  `38823508fca2e28a5cc884081be8e4b1c954329e5ebc301d60fde2865aa8e61d`.

## Zero-Base Redeploy

- Materialized shared kernel files from `prompts/research-agent` into
  `prompts/meta/` while excluding `kernel-project.md`.
- Regenerated Codex and Claude agent prompt headers and affected role contracts
  to `v8.7.0-candidate`.
- Regenerated 9 project-local skill capsules from
  `kernel-deploy.md` `skill_capsule_specs`.
- Updated prompt telemetry, schema resolution, wiki injection, and token ROI
  reports for Q3-AUDIT 16, ARTIFACT-CONVERGENCE, and version provenance.
- Updated runtime docs and instructions to name the direct
  `prompts/research-agent` submodule.

## Verification

| Check | Verdict | Evidence |
|---|---|---|
| Direct submodule revision | PASS | `git submodule status` -> `ed388737ed01c479df4905925f1ec6791ff0f47d prompts/research-agent` |
| Deprecated directory removed | PASS | `test ! -d prompts/upstream` |
| Project profile preserved | PASS | SHA-256 stayed `38823508fca2e28a5cc884081be8e4b1c954329e5ebc301d60fde2865aa8e61d`; no diff to `prompts/meta/kernel-project.md` |
| Shared kernel overlay boundary | PASS | upstream `kernel-project.md` differs from the project profile and was not copied |
| Codex agent count | PASS | 25 prompt files |
| Claude agent count | PASS | 25 prompt files |
| Skill capsule count | PASS | 9 `SKILL-*.md` files |
| Q3-AUDIT currency | PASS | no stale 13- or 15-item Q3 wording remains in generated prompts or skills |
| Token ROI | PASS | `token_roi_report.json` records all generated prompts and skills within approximate token budgets |
| JSON reports | PASS | `python3 -m json.tool` passed for schema, telemetry, wiki injection, token ROI, and lock files |
| Source integrity | PASS | no changed paths under `paper/source/` or `data/raw/` |
| Whitespace | PASS | `git diff --check` produced no findings |

## Prompt Audit

Q3-AUDIT summary:

| Item | Verdict | Evidence |
|---|---|---|
| Q3-01 local generation boundary | PASS | only the metaprompt submodule was imported; generated agents/skills remain project-local |
| Q3-10 main merge guard | PASS | generated prompts retain explicit-user and no-ff main merge requirements |
| Q3-11 project profile preserved | PASS | `kernel-project.md` SHA guard passed |
| Q3-13 telemetry | PASS | `token_telemetry_report.json` updated with direct submodule revision and path |
| Q3-14 wiki packet source scope | PASS | wiki packet report remains source-scoped with deferred packet behavior |
| Q3-16 token ROI and version provenance | PASS | token ROI report exists and generated artifacts advertise `v8.7.0-candidate` |

## K-COMPILE

No new canonical wiki entry was created. The reusable process lesson is recorded
in the active ledger as `LES-RESEARCH-PROMPT-DIRECT-001`.
