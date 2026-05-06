# SKILL-PAPER-WRITING

id: SKILL-PAPER-WRITING
purpose: Write or revise manuscript sections with author-perspective planning, claim grounding, focused feedback, bounded revision, and AI-use transparency.
trigger:
- PaperWriter receives a manuscript drafting, expansion, related-work, abstract, or substantive revision task
- PaperReviewer audits manuscript feedback quality or source fidelity
minimal_instruction: Build a ManuscriptSectionPlan with source scope, author perspective, claim register, section outline, revision actions, and transparency record before drafting or revising.
full_ref: prompts/meta/kernel-ops.md §PAPER-WRITE-01
input_contract:
- target manuscript section path
- source artifacts and evidence paths
- author key points, intended contribution, and exclusions when available
forbidden_context:
- source-free prose claims
- broadening a claim beyond its recorded scope limit
- style-only feedback when content support is the task
success_metric:
- every material claim has source refs, scope limit, and allowed strength
- revision actions are bounded to the dispatched section
- transparency record lists source materials and verification actions
token_target: 190
