# SKILL-PRESENTATION-DECK

id: SKILL-PRESENTATION-DECK
purpose: Create paper-grounded presentation decks with strong narrative hierarchy, traceable claims, and explanatory visuals.
trigger:
- PresentationWriter receives a slide deck, talk deck, or paper-to-presentation task
- A paper section, RevisionBrief, or EvidencePackage must become audience-facing slides
- A slide needs a concrete explanatory diagram or abstract visual explanation
minimal_instruction: Derive a clear narrative from the paper, compress it into the available slide count, build each slide around one supported message, express it as a 1-2 line lead in the largest non-title text, and place a concrete or abstract explanatory visual directly below the lead.
full_ref: prompts/meta/kernel-roles.md §PresentationWriter
input_contract:
- paper/source or paper/sections paths
- signed RevisionBrief or EvidencePackage when claims go beyond source summary
- target audience, talk length, venue, and language if known
- slide budget or expected talk duration when known
output_contract:
- `paper/presentations/{deck_id}/outline.md` or requested deck source
- narrative spine: audience problem -> paper insight -> evidence path -> implication
- slide-by-slide source map with paper/evidence references
- visual plan for every slide: concrete diagram, abstract diagram, chart, or figure
- message budget showing which paper details were omitted, merged, or moved to notes
- speaker notes when requested
best_practices:
- start from the audience's prior knowledge and choose the shortest narrative path to the paper's core contribution
- write a narrative spine before making slides; every slide must advance that spine
- limit the deck to the requested slide count or talk duration; if no count is given, propose a concise default and state it
- preserve only the messages the audience must remember; move caveats, derivations, and secondary details to notes or backup slides
- one claim per slide; remove secondary claims or move them to notes
- lead text is 1-2 lines and larger than body labels, captions, legends, and notes
- visual hierarchy flows lead -> visual -> short labels -> source note
- prefer diagrams, charts, mechanisms, timelines, or comparison layouts over dense bullet lists
- use progressive disclosure for multi-step mechanisms instead of one overloaded figure
- preserve paper nuance: uncertainty, limitations, assumptions, and scope boundaries stay visible
- every quantitative value, novelty statement, dataset fact, and benchmark comparison must trace to a cited artifact
- use consistent grid, contrast, color semantics, and terminology across the deck
- include an audience-check pass: what will a third-party listener remember after 30 seconds, 5 minutes, and at the end?
- mark unsupported or source-missing content as TODO rather than inventing content
review_criteria:
- narrative clarity: does the deck have a single comprehensible arc?
- compression quality: does the slide budget protect the most important messages?
- audience recall: can a third-party listener state the core message without reading the paper?
- cognitive load: are slides visually and verbally light enough to follow live?
- source fidelity: did compression preserve the paper's claims, assumptions, and limits?
forbidden_context:
- claims remembered from conversation but not present in artifacts
- unverified SOTA, novelty, benchmark, or numerical claims
- decorative visuals that obscure or contradict the paper's mechanism
success_metric:
- every slide has lead text, a visual plan below it, source references, a single audience-facing message, and a role in the narrative spine
token_target: 260
