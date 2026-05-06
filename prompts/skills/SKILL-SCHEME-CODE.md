# SKILL-SCHEME-CODE

id: SKILL-SCHEME-CODE
purpose: Design, implement, and verify scientific schemes through decomposed contracts, executable candidate evaluation, and verifier-gated handoff.
trigger:
- CodeArchitect receives numerical method, research-code synthesis, or computational scheme design work
- CodeCorrector repairs numerical logic under an existing scheme contract
- TestRunner verifies scientific behavior, convergence, invariants, or regression cases
minimal_instruction: Produce or follow a SchemeCodePlan with equations, invariants, I/O contracts, candidate loop, executable evaluator metrics, resource budget, and verification plan.
full_ref: prompts/meta/kernel-ops.md §SCHEME-CODE-01
input_contract:
- CheckSpec or governing equations
- implementation paths and forbidden paths
- expected invariants, tolerances, and resource budget
forbidden_context:
- accepting generated code by inspection
- benchmark-only correctness claims
- unrelated infrastructure optimization while changing numerical logic
success_metric:
- bounded implementation diff matches the SchemeCodePlan
- unit tests plus at least one scientific verification case are run or explicitly blocked
- TestRunner reports command logs, tolerances, verdict, and residual risks
token_target: 200
