# Task 13: New Skill Opportunities — Ranked Proposal

**Status:** Proposal-only. All candidates are marked `pending Queensland curriculum reviewer`. No human signoff assumed. Do not implement.

## Scope

Seven candidate skill families derived from the gap register (04-gap-register.csv), source register (02-source-register.csv), source-and-version-policy.md, and QCAA/ACARA source records. Each candidate is scored 1–5 on seven dimensions and ranked. Top three recommended with staged implementation order.

---

## Candidate 1: F-10 Unit/Sequence Planning + Curriculum Mapping

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests a multi-lesson unit or sequence plan aligned to Australian Curriculum v9.0 content descriptions and achievement standards for a learning area and year band. |
| **Target users / year bands** | F–10 teachers; Primary (F–6) and Secondary (7–10) bands; all learning areas (Mathematics, English, Science, HASS, Technologies, The Arts, HPE, Languages). |
| **Required official sources** | ACARA Australian Curriculum v9.0 (Class 1): content descriptions, achievement standards, year-level descriptions, general capabilities continua, cross-curriculum priority organising ideas. Source IDs: SRC-ACARA-V9-MATH, SRC-ACARA-V9-ENG, SRC-ACARA-V9-SCI, SRC-ACARA-V9-HASS, etc. |
| **Proposed outputs** | Unit overview (duration, year level, learning area, curriculum codes), sequence of 5–10 lesson-level learning intentions mapped to content descriptions, assessment checkpoints mapped to achievement standards, differentiation notes per lesson, curriculum mapping table (content description → lesson → evidence). |
| **Three eval scenarios** | 1. Year 4 Mathematics unit on fractions (AC9M4N01–AC9M4N04) — mapping accuracy and coverage. 2. Year 7 HASS unit on Ancient Egypt (AC9HH7K01–AC9HH7K04) — cross-curriculum priority integration (Aboriginal and Torres Strait Islander Histories and Cultures). 3. Year 9 Science unit on ecosystems (AC9S9U01–AC9S9U03) — achievement-standard evidence alignment across lessons. |
| **Tool/data dependencies** | curriculum_lookup adapter (ACARA v9.0), offline manifest data/curriculum/source-manifest.australian.json, unit/sequence template scripts, existing lesson-plan-creation skill for lesson-level detail. |
| **Overlap with existing 4 skills** | High overlap with australian-lesson-plan-creation (lesson-level planning) and australian-lesson-preparation (internalisation). New skill operates at unit/sequence grain (weeks), not lesson grain (hours). |
| **Scores (1–5)** | Teacher value: 5 | Source stability: 5 | Curriculum specificity: 5 | Distinctness: 3 | Testability: 4 | Maintenance burden: 3 | Implementation risk: 3 |
| **Weighted composite** | 4.14 |

---

## Candidate 2: General Capabilities / Cross-Curriculum Priorities Integration

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests explicit integration of General Capabilities (Literacy, Numeracy, ICT Capability, Critical and Creative Thinking, Personal and Social Capability, Ethical Understanding, Intercultural Understanding) or Cross-Curriculum Priorities (Aboriginal and Torres Strait Islander Histories and Cultures, Asia and Australia’s Engagement with Asia, Sustainability) into a lesson or unit. |
| **Target users / year bands** | F–10 teachers; all year bands; all learning areas. |
| **Required official sources** | ACARA Australian Curriculum v9.0 (Class 1): General Capabilities continua (learning continua PDFs), Cross-Curriculum Priorities organising ideas and elaborations. Source IDs: SRC-ACARA-V9-GC-LIT, SRC-ACARA-V9-GC-NUM, SRC-ACARA-V9-GC-ICT, SRC-ACARA-V9-GC-CCT, SRC-ACARA-V9-GC-PSC, SRC-ACARA-V9-GC-EU, SRC-ACARA-V9-GC-IU, SRC-ACARA-V9-CCP-ATSI, SRC-ACARA-V9-CCP-ASIA, SRC-ACARA-V9-CCP-SUST. |
| **Proposed outputs** | Capability/priority audit of existing lesson/unit, tagged learning activities with capability elements and organising ideas, explicit teaching prompts for capability development, evidence-of-learning suggestions per capability/priority. |
| **Three eval scenarios** | 1. Year 6 English persuasive writing — embed Critical and Creative Thinking (analysing arguments) and Ethical Understanding (perspectives on an issue). 2. Year 8 Geography unit on water scarcity — embed Sustainability CCP and Numeracy capability (data interpretation). 3. Year 3 HASS unit on local history — embed Aboriginal and Torres Strait Islander Histories and Cultures CCP and Intercultural Understanding capability. |
| **Tool/data dependencies** | curriculum_lookup adapter (ACARA v9.0 capabilities/CCP), capability continua parsing, existing lesson-differentiation skill (tiered capability supports). |
| **Overlap with existing 4 skills** | Moderate overlap with australian-lesson-plan-creation (capability tags in lesson outputs) and australian-lesson-differentiation (capability-based scaffolds). New skill provides explicit capability/CCP design layer. |
| **Scores (1–5)** | Teacher value: 4 | Source stability: 5 | Curriculum specificity: 4 | Distinctness: 4 | Testability: 3 | Maintenance burden: 3 | Implementation risk: 3 |
| **Weighted composite** | 3.71 |

---

## Candidate 3: QCAA Senior Assessment-Instrument Planning

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests planning support for a QCAA General Senior Syllabus internal assessment instrument (IA1, IA2, IA3) — task design, syllabus objective coverage, ISMG alignment, conditions, authentication. |
| **Target users / year bands** | Years 11–12 teachers; QCAA General subjects (e.g., Biology, Chemistry, Physics, Mathematical Methods, Specialist Mathematics, General Mathematics, English, Literature, Modern History, Ancient History, Legal Studies, Economics, Geography, Psychology, and all other General syllabuses). |
| **Required official sources** | QCAA General Senior Syllabuses (Class 2): syllabus objectives, unit subject matter, assessment specifications, instrument-specific marking guides (ISMGs), sample assessment instruments, subject reports, confirmation submission information. Source IDs: per-subject SRC-QCAA-* from 02-source-register.csv (e.g., SRC-0006 Biology, SRC-0049 Chemistry, SRC-0067 Digital Solutions, etc.). |
| **Proposed outputs** | Instrument plan: selected syllabus objectives, task type and conditions, draft task sheet, ISMG criteria mapping table, authentication strategies, timing and resource requirements, quality-assurance checklist against syllabus specifications. |
| **Three eval scenarios** | 1. Biology Unit 3 IA2 Student Experiment — design investigation task covering Unit 3 subject matter, map to ISMG criteria (Research and planning, Conducting, Analysing, Evaluating). 2. Mathematical Methods Unit 3 IA1 Problem-solving and modelling task — map to ISMG criteria (Formulate, Solve, Evaluate and communicate). 3. Modern History Unit 3 IA2 Investigation — independent source investigation, map to ISMG criteria (Devising and conducting, Analysing, Synthesising, Communicating). |
| **Tool/data dependencies** | curriculum_lookup adapter (QCAA Years 11–12), QCAA syllabus manifests (data/curriculum/qcaa/*.json), ISMG parsing, sample instrument repository, existing check-for-understanding skill (formative lead-in to summative). |
| **Overlap with existing 4 skills** | Low direct overlap. australian-check-for-understanding provides formative lead-in; australian-lesson-plan-creation covers teaching sequence. New skill targets summative instrument design (QCAA-specific). |
| **Scores (1–5)** | Teacher value: 5 | Source stability: 4 | Curriculum specificity: 5 | Distinctness: 5 | Testability: 4 | Maintenance burden: 4 | Implementation risk: 4 |
| **Weighted composite** | 4.43 |

---

## Candidate 4: ISMG-Aligned Feedback / Moderation

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests feedback on student responses to a QCAA internal assessment instrument using the instrument-specific marking guide (ISMG), or support for internal moderation/confirmation processes. |
| **Target users / year bands** | Years 11–12 teachers; QCAA General subjects; Heads of Department, moderation panels. |
| **Required official sources** | QCAA General Senior Syllabuses (Class 2): ISMGs for each instrument (IA1, IA2, IA3), sample marked responses, subject reports (endorsement/confirmation), quality assurance: Confirmation submission information. Source IDs: per-subject SRC-QCAA-* ISMG and subject report records from 02-source-register.csv. |
| **Proposed outputs** | Annotated student response with criterion-level judgements, feedback comments mapped to ISMG performance-level descriptors, moderation meeting preparation pack (evidence samples, judgement consensus protocol), confirmation submission evidence checklist. |
| **Three eval scenarios** | 1. Biology IA2 Student Experiment — annotate sample student report against ISMG criteria, produce feedback aligned to performance levels A–E. 2. English IA3 Extended response — moderate three student scripts across A–C range using ISMG, record consensus judgements. 3. Mathematical Methods IA1 — apply ISMG to student modelling report, identify evidence for each criterion at each performance level. |
| **Tool/data dependencies** | ISMG parsing (structured criteria × performance levels), sample response corpus (QCAA published), moderation protocol templates, existing skills provide no direct moderation support. |
| **Overlap with existing 4 skills** | Minimal. australian-check-for-understanding is formative; this is summative feedback/moderation against official ISMGs. |
| **Scores (1–5)** | Teacher value: 5 | Source stability: 4 | Curriculum specificity: 5 | Distinctness: 5 | Testability: 4 | Maintenance burden: 4 | Implementation risk: 4 |
| **Weighted composite** | 4.43 |

---

## Candidate 5: Reasonable-Adjustment / EAL-D Planning

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests planning for reasonable adjustments (NCCD) or EAL/D support for students accessing F–10 Australian Curriculum or QCAA senior syllabuses. |
| **Target users / year bands** | F–12 teachers; Learning Support coordinators; EAL/D specialists; all year bands. |
| **Required official sources** | ACARA Australian Curriculum v9.0 (Class 1): Student Diversity advice, EAL/D learning progression. NCCD (Class 1/3): NCCD guidelines, adjustment categories, evidence requirements. Queensland Department of Education (Class 2/3): Inclusive education policy, EAL/D band scales, reasonable adjustment resources. Source IDs: SRC-ACARA-V9-DIVERSITY, SRC-NCCD-GUIDELINES, SRC-QLD-ED-INCLUSIVE, SRC-QLD-ED-EALD. |
| **Proposed outputs** | Adjustment plan: student profile, NCCD adjustment category (QDTP, Supplementary, Substantial, Extensive), specific adjustments (presentation, response, setting, timing), EAL/D band scale alignment, curriculum access strategies maintaining standards integrity, evidence-collection template for NCCD. |
| **Three eval scenarios** | 1. Year 5 Mathematics student with working memory difficulties — QDTP adjustments for fraction lesson (visual scaffolds, chunked instructions). 2. Year 9 EAL/D student (Band B) in Science — language scaffolds for research investigation (vocabulary pre-teaching, sentence frames). 3. Year 11 General Mathematics student with dyscalculia — Substantial adjustments for IA1 (formula sheet access, extended time, alternative representation). |
| **Tool/data dependencies** | NCCD adjustment matrix, EAL/D band scales parser, ACARA Student Diversity materials, existing lesson-differentiation skill (differentiation ≠ adjustment — see skill boundary). |
| **Overlap with existing 4 skills** | Clear boundary: australian-lesson-differentiation explicitly excludes reasonable adjustments and curriculum modification (see its SKILL.md § Differentiation vs reasonable adjustments vs curriculum modification). New skill addresses NCCD/EAL-D territory. |
| **Scores (1–5)** | Teacher value: 5 | Source stability: 3 | Curriculum specificity: 4 | Distinctness: 5 | Testability: 3 | Maintenance burden: 4 | Implementation risk: 4 |
| **Weighted composite** | 4.00 |

---

## Candidate 6: Achievement-Standard Evidence / Reporting

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests support gathering, organising, and reporting evidence of student achievement against Australian Curriculum v9.0 achievement standards (F–10) or QCAA syllabus reporting standards (Years 11–12). |
| **Target users / year bands** | F–12 teachers; reporting coordinators; all learning areas/subjects. |
| **Required official sources** | ACARA Australian Curriculum v9.0 (Class 1): achievement standards (F–10), work samples (where published). QCAA General/Applied Senior Syllabuses (Class 2): reporting standards A–E, subject-specific standards elaborations, confirmation/endorsement subject reports. Source IDs: SRC-ACARA-V9-AS-* per learning area; SRC-QCAA-* reporting standards per subject. |
| **Proposed outputs** | Evidence portfolio template mapped to achievement standard/reporting standard descriptors, evidence-collection schedule across teaching period, on-balance judgement guide with annotated work samples, parent/student reporting language aligned to standard descriptors. |
| **Three eval scenarios** | 1. Year 2 English — collect evidence across reading, writing, speaking/listening for achievement standard; produce semester report comments. 2. Year 10 Science — map portfolio items to achievement standard elements; moderate on-balance judgement. 3. Year 12 Biology — align IA1/IA2/IA3 evidence to QCAA reporting standards A–E; prepare confirmation submission. |
| **Tool/data dependencies** | Achievement standard parsing, work sample repository (ACARA/QCAA), reporting timeline templates, existing lesson-preparation skill (internalisation evidence). |
| **Overlap with existing 4 skills** | Moderate overlap with australian-lesson-preparation (evidence of internalisation) and australian-lesson-plan-creation (assessment checkpoints). New skill focuses on longitudinal evidence and formal reporting. |
| **Scores (1–5)** | Teacher value: 4 | Source stability: 4 | Curriculum specificity: 5 | Distinctness: 4 | Testability: 4 | Maintenance burden: 3 | Implementation risk: 3 |
| **Weighted composite** | 3.86 |

---

## Candidate 7: Senior Revision / External-Assessment Preparation

| Field | Detail |
|---|---|
| **Trigger** | Teacher requests structured revision program or external assessment (EA) preparation for QCAA General Senior subjects with external assessment (all General syllabuses from 2026). |
| **Target users / year bands** | Years 11–12 teachers; Year 12 students (via teacher); QCAA General subjects with EA (all General syllabuses per Key senior subject changes 2026). |
| **Required official sources** | QCAA General Senior Syllabuses (Class 2): external assessment specifications, past papers (2020–2025), marking guides, subject reports, formula/data books, Key senior subject changes for EA 2026. Source IDs: per-subject SRC-QCAA-* EA records (e.g., SRC-0023 Aerospace Systems QA, SRC-0039 Chemistry past papers, SRC-0070 Earth & Environmental Science EA papers). |
| **Proposed outputs** | Revision program: topic-sequence mapped to syllabus objectives and EA specifications, practice items modelled on past paper styles, marking-guide-aligned feedback templates, cognitive-load-managed schedule (spaced retrieval, interleaving), exam-technique strategies per subject. |
| **Three eval scenarios** | 1. Mathematical Methods — 6-week EA prep program covering Units 3–4, practice combination-response and technology-free items, marking guide alignment. 2. Chemistry — revision sequence targeting Data test (IA1) and EA examination; past paper analysis for recurring concepts. 3. Modern History — EA preparation for extended response and short response; source-analysis practice using past stimulus books. |
| **Tool/data dependencies** | Past paper parsing (PDF), marking guide extraction, EA specification parser, spaced-repetition scheduler, existing check-for-understanding skill (formative checks during revision). |
| **Overlap with existing 4 skills** | Low overlap. australian-check-for-understanding provides formative items; new skill orchestrates summative EA preparation at program level. |
| **Scores (1–5)** | Teacher value: 5 | Source stability: 4 | Curriculum specificity: 5 | Distinctness: 4 | Testability: 4 | Maintenance burden: 4 | Implementation risk: 3 |
| **Weighted composite** | 4.14 |

---

## Ranking Summary

| Rank | Candidate | Composite | Teacher Value | Distinctness | Implementation Risk |
|---|---|---|---|---|---|
| 1 | QCAA Senior Assessment-Instrument Planning | 4.43 | 5 | 5 | 4 |
| 2 | ISMG-Aligned Feedback / Moderation | 4.43 | 5 | 5 | 4 |
| 3 | F-10 Unit/Sequence Planning + Curriculum Mapping | 4.14 | 5 | 3 | 3 |
| 4 | Senior Revision / External-Assessment Preparation | 4.14 | 5 | 4 | 3 |
| 5 | Reasonable-Adjustment / EAL-D Planning | 4.00 | 5 | 5 | 4 |
| 6 | Achievement-Standard Evidence / Reporting | 3.86 | 4 | 4 | 3 |
| 7 | General Capabilities / Cross-Curriculum Priorities Integration | 3.71 | 4 | 4 | 3 |

**Tie-break for #1/#2:** Assessment-Instrument Planning precedes Feedback/Moderation because instrument design precedes marking; teachers need to plan before they moderate.

**Tie-break for #3/#4:** Unit/Sequence Planning precedes Senior Revision because F–10 scope is broader (all teachers) and builds on existing lesson-plan-creation foundation.

---

## Top Three Recommendations (Staged Order)

### Stage 1: QCAA Senior Assessment-Instrument Planning
**Rationale:** Highest teacher value (5) and distinctness (5); addresses a well-defined QCAA workflow with stable official sources (syllabuses, ISMGs, sample instruments); low overlap with existing skills; directly serves Years 11–12 teachers in all General subjects. QCAA source coverage is comprehensive (78 subjects with verified packages per 06-review-log.csv).

**Dependencies to resolve first:** ISMG parsing infrastructure; per-subject assessment specification extraction from QCAA syllabus manifests; authentication strategy templates.

### Stage 2: ISMG-Aligned Feedback / Moderation
**Rationale:** Natural successor to Stage 1 — same sources, same user cohort, same syllabus cycle. Enables confirmation/endorsement readiness. Can reuse ISMG parsing from Stage 1. Moderation protocols are standardised across QCAA subjects.

**Dependencies to resolve first:** Sample response corpus access (QCAA published); moderation consensus protocol templates; confirmation submission checklist generator.

### Stage 3: F-10 Unit/Sequence Planning + Curriculum Mapping
**Rationale:** Broadest teacher cohort (F–10, all learning areas); leverages existing ACARA v9.0 manifest and lesson-plan-creation skill; extends lesson grain to unit grain. Source stability highest (ACARA v9.0 is fixed version). Lower implementation risk than senior skills due to single authority (ACARA) and stable curriculum.

**Dependencies to resolve first:** Unit/sequence template system; cross-lesson curriculum mapping table generator; achievement-standard evidence alignment across sequence.

---

## Proposal-Only Declaration

All seven candidates are **proposal-only** and marked **`pending Queensland curriculum reviewer`**. No implementation is authorised. Any future work requires:
1. Queensland curriculum-qualified reviewer sign-off on source mappings and curriculum specificity claims.
2. Authority verification of all cited sources per source-and-version-policy.md §3.
3. Evaluation fixtures authored against verified sources only.
4. Mapping confidence labels (`exact`, `authority-verified`, `contextual`, `pending-reviewer`, `partial`) applied per policy §4.
5. No US code patterns (CCSS/NGSS/C3/state codes) in any shipped behaviour per policy §6 Gate 3.

---

*Generated as Task 13 deliverable for australian-localisation branch. Candidate count: 7.*