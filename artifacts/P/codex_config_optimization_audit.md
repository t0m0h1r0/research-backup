# Codex Configuration Optimization Audit

| Field | Value |
|-------|-------|
| Branch | `codex/researcharchitect-codex-config` |
| Worktree | `/private/tmp/research-backup-codex-config` |
| Session | `073ed11d-d33c-4fde-989e-446bd7544029` |
| Date UTC | 2026-05-04T12:58:55Z |
| Verdict | PASS |

## PLAN

Optimize Codex-facing configuration without changing source papers, datasets, or
active research claims. Keep the prompt source of truth in `prompts/meta/`,
update deployed Codex prompts only where the inherited base profile would leave
ambiguous operational behavior, and verify with mechanical checks.

## EXECUTE

- Added `Codex Workflow` guardrails to `AGENTS.md`.
- Added `codex_runtime` to `prompts/agents-codex/_base.yaml`.
- Updated Codex coordinator prompts so `main` merge is explicit-user-only and
  no-ff.
- Replaced Codex DevOps `.claude/worktrees/` wording with neutral task worktree
  wording.
- Updated `prompts/meta/kernel-roles.md` and `prompts/meta/kernel-deploy.md` so
  future regeneration preserves the merge/worktree guardrails.

## VERIFY

Command:

```sh
ruby -e 'require "yaml"; require "json"; base=YAML.load_file("prompts/agents-codex/_base.yaml"); JSON.parse(File.read("token_telemetry_report.json")); JSON.parse(File.read("schema_resolution_report.json")); codex=Dir["prompts/agents-codex/*.md"].size; claude=Dir["prompts/agents-claude/*.md"].size; pr=File.read("docs/03_PROJECT_RULES.md").scan(/^## PR-/).size; raise "codex agent count #{codex}" unless codex==23; raise "claude agent count #{claude}" unless claude==23; raise "project rule count #{pr}" unless pr==6; rt=base.fetch("codex_runtime"); raise "main policy" unless rt["main_merge_policy"]=="explicit_user_instruction_only"; raise "merge method" unless rt["main_merge_method"]=="no_ff"; bad=[]; Dir["prompts/agents-codex/*.md"].each{|f| s=File.read(f); bad << "#{f}: stale PR-to-main" if s.include?("PR→main") || s.include?("PR->main") || s.include?("merge PR→main") || s.include?("merge PR->main") || s.include?(".claude/worktrees/"); s.each_line.with_index(1){|line,n| bad << "#{f}:#{n}: unsafe main merge line" if line =~ /main merge/i && line !~ /(explicit user|no-ff|unilateral)/i } }; raise bad.join("\n") unless bad.empty?; puts "PASS codex_agents=#{codex} claude_agents=#{claude} project_rules=#{pr} codex_runtime=#{rt["main_merge_policy"]}/#{rt["main_merge_method"]}"'
```

Observed output:

```text
PASS codex_agents=23 claude_agents=23 project_rules=6 codex_runtime=explicit_user_instruction_only/no_ff
```

Additional checks:

- `ruby -e 'require "yaml"; YAML.load_file("prompts/agents-codex/_base.yaml")'`
  passed.
- `git diff --check` passed before committing the configuration patch.

## AUDIT

No source papers, raw datasets, experiment outputs, or manuscript claims were
modified. No `main` merge was performed.
