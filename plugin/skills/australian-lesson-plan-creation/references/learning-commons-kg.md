# Knowledge Graph — call sequences

Used by `australian-lesson-plan-creation` Step 2 **only when the Knowledge Graph tools are available**.
If they are not, skip this file entirely (SKILL.md Step 2 has the fallback).
Each section below is the call sequence for one subject. Calling the KG when connected is
mandatory; not calling it is a critical failure.

## Resolving the standard (all subjects)

Resolve the standard with `find_standard_statement`, passing `academicSubject` and `jurisdiction` (the Australian state/territory) when they're known:

- **A code is provided** (named in the source lesson or by the teacher): search by code — `find_standard_statement(code=<code>, academicSubject="<subject>")`. A code search matches both the code itself and everything beneath it (prefix match): a leaf like `3.NF.A.1` returns just that standard, while a parent like `2.OA` returns `2.OA` plus all `2.OA.*`. **If it returns nothing**, the code's format probably doesn't match the graph's — fall back to keyword search (below); its results come back with real `code` values that reveal the correct format, which you can use to retry the code search.
- **No code provided**: start with keyword search — `find_standard_statement(keywords=["<word or phrase>", "<word or phrase>", …], academicSubject="<subject>")`. `keywords` is a **list** of topic words/phrases; a standard matches if ANY of them appears in its description. Pick the best-matching standard from the returned `standards` array — its `code` can seed a follow-up code search for related standards (e.g. its parent prefix to pull the whole family).

When a returned standard has children, they come back in its `subStandards` array — use whichever is most relevant to the user's request, the standard itself or one of its sub-standards.

**Cap at 3 search attempts total.** Results from the wrong year level or course count as
a miss — a senior secondary request answered with primary codes means the search
terms missed, so spend the remaining attempts with different keywords (the course name,
the topic, the standard family) rather than falling back early. If no usable standard after
3 calls to `find_standard_statement`, stop searching — proceed with the best-matching
standard from training knowledge for the year level and topic, and add the partial-coverage
footer to the lesson plan. Never call `find_curriculum_lessons` to locate a standard.

From the chosen standard, extract: the verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls). When the statement has lettered sub-parts, the verbatim quote is the sub-part(s) this lesson targets, with the parent named by code.

## Mathematics

Call BEFORE drafting. Not calling when connected is a critical failure. Make all calls, extract only what is specified below, then proceed directly to Step 3 — KG findings surface in chat only through the draft's one-line standard read-back, never as a results summary.

The only cross-call data dependencies are the standard's `caseIdentifierUUID` (used by steps 2–5) and the `lessonIdentifier` that `find_curriculum_lessons` returns (used by `find_materials_for_lesson`). So: resolve the standard, then issue the step 2–4 calls and `find_curriculum_lessons` — each with its full parameters as specified below — as one parallel batch, then fetch materials.

**Available tools:** `find_standard_statement`, `find_standards_progression_from_standard`, `find_misconceptions_for_standard`, `find_learning_components_from_standard`, `list_standards_for_mathematical_practice`, `find_curriculum_lessons`, `find_materials_for_lesson`.

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Mathematics"`. Use the verbatim statement text exactly as written in the lesson plan's standard callout.

2. **Prerequisite**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract: the single primary prerequisite standard, verbatim. Use in the LEARNING GOAL section. Non-negotiable — not naming the prior standard is a critical failure.

3. **Learning components**: Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill descriptions (unknown positions, problem types). Use directly as SWBAT bullets and as look-for row labels in the observation template. Discard the rest.

4. **Misconceptions**: Call `find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` → extract: the 3 most relevant misconceptions. For each keep only the student behavior and the teacher move, rewritten in your own words. If no results, draft 3 from training knowledge.

5. **Lesson materials**: Call `find_curriculum_lessons(caseIdentifierUUID=<uuid from step 1>, author="Illustrative Mathematics")` → select the single most relevant lesson (grade-level match first). Call `find_materials_for_lesson(lessonIdentifier, materialSource=["lesson", "activity"])` for the lesson overview and activity materials in one call → extract: (a) activity names and sequence, (b) problem types and unknown positions addressed, (c) any explicit discourse moves. Discard full activity narratives and student-facing text — these must not be reproduced verbatim.

6. **SMPs**: Choose 2–3 from training knowledge. No KG call needed.

**Curriculum-terminology check (if not IM-confirmed):** Before proceeding, scan your working notes and verify they contain zero mentions of "Illustrative Mathematics," "IM," any MLR name (MLR 1–8), "Compare and Connect," "Stronger and Clearer Each Time," or any IM lesson/activity title. Remove any that remain — a teacher who has not confirmed IM must not receive IM-specific terminology in the lesson or in chat (the same rule as SKILL.md's Copyright guardrail).

**If KG not connected:** draft from best knowledge; add footer: *"Generated without the Knowledge Graph. Standards and misconceptions reflect general best practice."*

→ **KG phase complete. Proceed immediately to Step 3.**

---

## English

Call BEFORE drafting. Not calling when connected is a critical failure. Make all calls in sequence, extract only what is specified, then proceed directly to Step 3 — KG findings surface in chat only through the draft's one-line standard read-back, never as a results summary.

**Available tools:** `find_standard_statement`, `find_learning_components_from_standard`

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="English"` (codes are Australian Curriculum v9.0 content description codes, e.g. ACELYxxxx). Use the verbatim statement text exactly as written in Section 1.

2. **Learning components**: Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract: up to 5 sub-skill descriptions if available. Use directly as SWBAT bullets in Section 2. Discard the rest.

3. **Text complexity check**: If an anchor text is identified (from teacher or KG), note whether its complexity is appropriate for the year level. Flag if outside expected band.

**If KG not connected:** draft from best knowledge; add footer: *"Generated without the Knowledge Graph. Standards and misconceptions reflect general best practice."*

→ **KG phase complete. Proceed immediately to Step 3.**

---

## Science

Call BEFORE drafting. Not calling when connected is a critical failure. Make all calls in sequence, extract only what is specified, then proceed directly to Step 3 — KG findings surface in chat only through the draft's one-line standard read-back, never as a results summary.

**Available tools:** `find_standard_statement`, `find_curriculum_lessons`, `find_materials_for_lesson`.

Note: `find_learning_components_from_standard` and `find_standards_progression_from_standard` do **not** return data for science standards — do not call them.

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="Science"` (the code is an NGSS Performance Expectation, e.g. `MS-LS2-3`, `3-LS1-1`, `HS-PS1-1`). Use the verbatim statement text exactly as written in Section 1.

2. **OpenSciEd unit and lesson**: Call `find_curriculum_lessons(caseIdentifierUUID=<uuid from step 1>, author="OpenSciEd")` → select the single most relevant lesson (grade-level match first, then closest topic match). Call `find_materials_for_lesson(lessonIdentifier, materialSource=["activity"])` → extract: (a) unit anchoring phenomenon; (b) unit driving question; (c) this lesson's investigative phenomenon or question; (d) this lesson's position in the unit storyline; (e) which SEP(s) and CCC(s) are foregrounded; (f) any specific routines or activity structures used. **Do NOT reproduce OSE student-facing text, investigation prompts, or discussion questions verbatim — these must be rewritten as original content.**

**If KG not connected:** draft from best knowledge; add footer: *"Generated without the Learning Commons Knowledge Graph. Standards and OpenSciEd alignment reflect general best practice."*

→ **KG phase complete. Proceed immediately to Step 3.**

---

## HASS


Use the KG to find the authoritative standard statement for this topic and year level. This grounds the lesson in the actual standard rather than a paraphrase.

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="HASS"`. For F-10 lessons, look up the relevant Australian Curriculum v9.0 HASS content description by year level and sub-strand (History, Geography, Civics & Citizenship, Economics & Business). For Years 11-12 (Queensland), look up the relevant QCAA syllabus objective. Use the verbatim statement text in the lesson plan header under `**Standard:**`, and let it anchor the compelling question and formative task.

**If no standard is found:** align the lesson to the most relevant Australian Curriculum content description from training knowledge, and note briefly: *"Standard lookup not available for [jurisdiction/code]."* Do not halt generation.

→ **KG phase complete. Proceed immediately to Step 3.**

---

Copyright 2026 Anthropic, PBC · SPDX-License-Identifier: Apache-2.0
