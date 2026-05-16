# SKILL-PROMPT-AUDIT

id: SKILL-PROMPT-AUDIT
purpose: Audit generated prompts for Q3-AUDIT compliance, rule bloat, JIT discipline, support-artifact coverage, wiki-packet discipline, and token ROI.
trigger:
- PromptAuditor receives generated prompt artifacts
- EnvMetaBootstrapper Stage 4
- AP-13 suspicion
- AP-17 suspicion
minimal_instruction: Verify all Q3-AUDIT items, reject duplicated operation bodies, reject broad preloading, reject stale/full wiki prose, and require role-relevant SkillID/RULE_MANIFEST/wiki-packet references where full text has weak ROI.
full_ref: prompts/meta/kernel-deploy.md §Stage 4
input_contract:
- generated agent prompt paths
- prompts/skills paths
- wiki_knowledge_injection_report.json when docs/wiki/ exists
- token_telemetry_report.json
forbidden_context:
- PromptArchitect reasoning
- previous generated prompt transcripts
- unlisted draft prompts
success_metric:
- Q3-AUDIT 15-item verdict
- duplicate-rule scan recorded
- WikiKnowledgePacket/AP-17 verdict recorded
- prompt-load ROI verdict recorded
- token telemetry gate result recorded
token_target: 150
