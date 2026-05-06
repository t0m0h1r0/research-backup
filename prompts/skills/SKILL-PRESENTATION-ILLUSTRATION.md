# SKILL-PRESENTATION-ILLUSTRATION

id: SKILL-PRESENTATION-ILLUSTRATION
purpose: Convert a supported presentation message into a source-faithful conceptual illustration brief with reverse-readback fidelity checks.
trigger:
- A deck task needs an abstract, conceptual, or painting-like visual
- A presentation image prompt must be checked against a slide claim
- Reverse readback is needed before accepting a conceptual illustration
minimal_instruction: Build a VisualConceptBrief that maps lead_message and source_refs to abstraction, concretization, image language, excluded meanings, and reverse_readback before accepting the asset.
full_ref: prompts/meta/kernel-ops.md §VISUAL-CONCEPT-01
input_contract:
- slide lead message
- source refs and claim scope
- audience takeaway and excluded meanings
forbidden_context:
- decorative visuals with no claim map
- unsupported mechanisms, quantities, citations, dataset facts, or novelty claims
- relying on embedded text labels to make the concept work
success_metric:
- visual roles map to source elements
- reverse_readback is PASS or PARTIAL with explicit residual gaps
- repeated material FAIL triggers revise/downgrade/stop action
token_target: 180
