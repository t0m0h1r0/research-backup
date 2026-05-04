# AGENTS Instruction Optimization Audit

| Field | Value |
|-------|-------|
| Branch | `codex/researcharchitect-codex-config` |
| Worktree | `/private/tmp/research-backup-codex-config` |
| Date UTC | 2026-05-04T13:03:07Z |
| Verdict | PASS |

## PLAN

Refine `AGENTS.md` from a compact rule list into a practical first-read
operational contract while keeping project-specific and workflow source of truth
in `prompts/meta/`.

## EXECUTE

- Added a Fast Start read order for active brief, ledger, project rules, project
  map, environment base prompt, role prompt, and git state.
- Added a `Where Work Goes` table for common research, code, evidence, paper,
  workflow, and prompt/configuration artifacts.
- Consolidated Codex workflow rules for task worktrees, coherent commits,
  explicit-user/no-ff `main` merges, user-change preservation, and verification.
- Added anomaly-detection research gates and prompt-maintenance instructions.
- Updated `prompts/README.md` and `prompts/meta/kernel-deploy.md` so the AGENTS
  profile is visible from the prompt-system docs and regeneration spec.

## VERIFY

Commands:

```sh
git diff --check
ruby -e 'require "json"; require "yaml"; YAML.load_file("prompts/agents-codex/_base.yaml"); JSON.parse(File.read("token_telemetry_report.json")); a=File.read("AGENTS.md"); k=File.read("prompts/meta/kernel-deploy.md"); raise "missing Fast Start" unless a.include?("## Fast Start"); raise "missing work map" unless a.include?("## Where Work Goes"); raise "missing prompt maintenance" unless a.include?("## Prompt Maintenance"); raise "missing deploy profile" unless k.include?("content profile"); puts "PASS agents_instruction_profile"'
```

Observed output:

```text
PASS agents_instruction_profile
```

## AUDIT

No source papers, raw datasets, experiment outputs, model code, or manuscript
claims were modified. No `main` merge was performed.
