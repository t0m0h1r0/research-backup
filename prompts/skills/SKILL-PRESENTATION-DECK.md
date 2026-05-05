# SKILL-PRESENTATION-DECK

id: SKILL-PRESENTATION-DECK
purpose: Create paper-grounded presentation decks with strong narrative hierarchy, traceable claims, and explanatory visuals.
trigger:
- PresentationWriter receives a slide deck, talk deck, or paper-to-presentation task
- A paper section, RevisionBrief, or EvidencePackage must become audience-facing slides
- A slide needs a concrete explanatory diagram or abstract visual explanation
minimal_instruction: Build each slide around one supported message, express it as a 1-2 line lead in the largest non-title text, and place a concrete or abstract explanatory visual directly below the lead.
full_ref: prompts/meta/kernel-roles.md §PresentationWriter
input_contract:
- paper/source or paper/sections paths
- signed RevisionBrief or EvidencePackage when claims go beyond source summary
- target audience, talk length, venue, and language if known
output_contract:
- `paper/presentations/{deck_id}/outline.md` or requested deck source
- slide-by-slide source map with paper/evidence references
- visual plan for every slide: concrete diagram, abstract diagram, chart, or figure
- speaker notes when requested
best_practices:
- one claim per slide; remove secondary claims or move them to notes
- lead text is 1-2 lines and larger than body labels, captions, legends, and notes
- visual hierarchy flows lead -> visual -> short labels -> source note
- prefer diagrams, charts, mechanisms, timelines, or comparison layouts over dense bullet lists
- use progressive disclosure for multi-step mechanisms instead of one overloaded figure
- preserve paper nuance: uncertainty, limitations, assumptions, and scope boundaries stay visible
- every quantitative value, novelty statement, dataset fact, and benchmark comparison must trace to a cited artifact
- use consistent grid, contrast, color semantics, and terminology across the deck
- mark unsupported or source-missing content as TODO rather than inventing content
forbidden_context:
- claims remembered from conversation but not present in artifacts
- unverified SOTA, novelty, benchmark, or numerical claims
- decorative visuals that obscure or contradict the paper's mechanism
success_metric:
- every slide has lead text, a visual plan below it, source references, and a single audience-facing message
token_target: 220
