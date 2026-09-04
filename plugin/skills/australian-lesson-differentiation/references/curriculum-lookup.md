# Curriculum Lookup Adapter — call sequences (differentiation)

Used by `australian-lesson-differentiation` Step 2 **only when the curriculum lookup adapter is
available**. If it is not connected, skip this file entirely (SKILL.md Step 2 has the fallback).
Each section below is the call sequence for one subject. Calling the adapter when connected is
mandatory; not calling it is a critical failure.

## Resolving the standard (all subjects)

Resolve the standard with `find_standard_statement`, passing `academicSubject` and `jurisdiction` (the state/territory) when they're known:

- **A code is provided** (named in the source lesson or by the teacher): search by code — `find_standard_statement(code=<code>, academicSubject="<subject>")`. A code search matches both the code itself and everything beneath it (prefix match): a leaf like `ACARA.V9.7.English.3.1.1` returns just that standard, while a parent like `ACARA.V9.7.English.3` returns `ACARA.V9.7.English.3` plus all `ACARA.V9.7.English.3.*`. **If it returns nothing**, the code's format probably doesn't match the graph's — fall back to keyword search (below); its results come back with real `code` values that reveal the correct format, which you can use to retry the code search.

- **No code provided**: start with keyword search — `find_standard_statement(keywords=["<word or phrase>", "<word or phrase>", …], academicSubject="<subject>")`. `keywords` is a **list** of topic words/phrases; a standard matches if ANY of them appears in its description. Pick the best-matching standard from the returned `standards` array — its `code` can seed a follow-up code search for related standards (e.g. its parent prefix to pull the whole family).

When a returned standard has children, they come back in its `subStandards` array — use whichever is most relevant to the user's request, the standard itself or one of its sub-standards.

From the chosen standard, extract: the verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls).

## Mathematics

**Call these tools before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

**Available tools:** `find_standard_statement`, `find_standards_progression_from_standard`, `find_misconceptions_for_standard`, `find_learning_components_from_standard`, `find_curriculum_lessons`, `find_materials_for_lesson`.

1. **Standard**: Resolve the standard per *Resolving the standard* above with
   `academicSubject="Mathematics"` and, when state is known from Step 0 jurisdiction detection,
   `jurisdiction="<state/territory>"` → verbatim statement text and `caseIdentifierUUID`.

   When jurisdiction is passed and the adapter returns a jurisdiction-specific standard, use that
   standard's code and text verbatim.

2. **Prerequisite and forward standard**: Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="backward")` → extract the single primary prerequisite standard, verbatim — this grounds the Below tier. Call `find_standards_progression_from_standard(caseIdentifierUUID, direction="forward")` → extract the single primary forward standard, verbatim — this grounds the Above tier. Omitting either is a critical failure.

3. **Misconceptions**: Call `find_misconceptions_for_standard(caseIdentifierUUID, subject="Mathematics")` → extract the 3 most relevant misconceptions. For each, keep only the student behavior and the teacher move, rewritten in your own words. If no results, draft 3 from training knowledge.

4. **Learning components** (optional, for teacher plan): Call `find_learning_components_from_standard(caseIdentifierUUID)` → extract up to 5 sub-skill descriptions. Use to verify R2: all components must appear across all tiers.

5. **ACARA lesson materials** (only when BOTH conditions hold: ACARA is confirmed as the curriculum AND the teacher named the lesson — Scenario B3 — rather than uploading or linking it): Call `find_curriculum_lessons` with `author="ACARA"`. Use the mode that matches what the teacher provided:
   - **Teacher named by position** (e.g., "Year 7 Mathematics, Unit 2, Lesson 3"): use `ordinalName="Year N Mathematics, Unit N, Lesson N"`. Expand abbreviations first.
   - **Teacher named by title**: use `lessonName="<content words from the title>"`. No year/unit/lesson numbers.

   If multiple candidates return, echo `fullOrdinalName` and `lessonName` back to the teacher to confirm. Once confirmed, call `find_materials_for_lesson(lessonIdentifier, materialSource=["lesson", "activity"])` → extract: (a) activity names and sequence, (b) problem types and unknown positions addressed, (c) discourse moves. Use to ground tier task design in the actual lesson structure — do not reproduce student-facing text verbatim.

   If the teacher uploaded or linked the lesson (Scenarios B or B2), skip this step — lesson content is already available.

**Curriculum-terminology check (if not ACARA-confirmed):** Before proceeding, scan your working notes and verify they contain zero mentions of "ACARA," "Australian Curriculum," "v9.0," any ACARA lesson/activity title, or any Australian Curriculum terminology. Remove any that remain — a teacher who has not confirmed ACARA must not receive ACARA-specific terminology in any tier document, the teacher plan, or chat (the same rule as SKILL.md's Copyright guardrail).

**If adapter not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the curriculum lookup adapter. Standard text, prerequisite grounding, and misconceptions reflect general best practice."*

---

## English

**Call these tools before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

1. Resolve the standard per *Resolving the standard* above with
   `academicSubject="English"` and, when state is known from Step 0 jurisdiction detection,
   `jurisdiction="<state/territory>"` → verbatim standard text, its `code`, and
   `caseIdentifierUUID`.

   When jurisdiction is passed and the adapter returns a jurisdiction-specific standard, use that
   standard's code and text verbatim.

2. `find_learning_components_from_standard(caseIdentifierUUID)` → up to 5 sub-skill descriptions. **Call this for Year 7 and below standards only; for Year 8+, learning components are not yet available in the adapter — skip this call and draft sub-skills from the standard statement.** Use sub-skills to verify R2: all learning components must remain in scope across all three tiers.

**If adapter not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the curriculum lookup adapter. Standard text, prerequisite grounding, and learning components reflect general best practice."*

---

## Science

**Call all three before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

Note: `find_learning_components_from_standard` and `find_standards_progression_from_standard` do **not** return data for science standards — do not call them.

1. **Standard**: Resolve the standard per *Resolving the standard* above with
   `academicSubject="Science"` and, when state is known from Step 0 jurisdiction detection,
   `jurisdiction="<state/territory>"` → verbatim statement text and `caseIdentifierUUID`.

   When jurisdiction is passed and the adapter returns a jurisdiction-specific standard, use that
   standard's code and text verbatim.

2. **Find the source lesson in the adapter** using `find_curriculum_lessons` with `author="OpenSciEd"` (for national standards). Use exactly ONE mode per call:
   - **Curriculum position known** (teacher named the lesson by position — Scenario B3 — or unit/lesson number is visible in the uploaded/fetched lesson — e.g., "Science Year 7, Unit 2, Lesson 3"): use `ordinalName="Science Year 7, Unit 2, Lesson 3"`. Expand abbreviations before passing (Y7 U2 L3 → Science Year 7, Unit 2, Lesson 3). This is the most precise mode; prefer it when available.
   - **Title known but no position** (teacher named the lesson by title — Scenario B3 — or title is visible in the uploaded/fetched source): use `lessonName="<words from the lesson title>"`. Pass distinctive content words only — omit year/unit/lesson numbers. Results come back best-match-first.
   - **Standard UUID only** (uploaded/fetched lesson with no recoverable position or title — not applicable for Scenario B3): use `caseIdentifierUUID=<uuid from step 1>`. Note: OpenSciEd lessons align to Multi-State (NGSS) standards only — a state-specific PE UUID with no exact crosswalk returns no results.

   If multiple candidates return, echo their `fullOrdinalName` and `lessonName` back to the teacher to confirm which lesson is meant before fetching materials. Once confirmed, call **`find_materials_for_lesson(lessonIdentifier)`** → extract: (a) anchoring phenomenon; (b) unit driving question; (c) this lesson's investigative phenomenon or question; (d) lesson position in the unit storyline; (e) which SEPs and CCCs are foregrounded; (f) any routines or activity structures used.

3. **Progression.** From the lesson materials or adapter data, identify: (a) the prior-grade PE or DCI element that the below-level scaffold should route students *up from*; (b) the forward PE that the above-level extension should preview. Name both verbatim. Omitting either is a critical failure.

**If adapter not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the curriculum lookup adapter. PE grounding, OpenSciEd alignment, and progression reflect general best practice."*

---

## HASS

**Call all queries before drafting. Not calling when connected is a critical failure.**

Note any standard code the source lesson names — the resolution step searches by it when present.

1. **Standard**: Resolve the standard per *Resolving the standard* above with `academicSubject="HASS"` and `jurisdiction="<state/territory>"` (required — national adapter carries no HASS standards) → verbatim statement text, its `code`, and `caseIdentifierUUID` (store — required for all subsequent calls). Use statement text verbatim in all output.

**Note on standard progressions:** `find_standards_progression_from_standard` does not return data for HASS standards — do not call it. Source prerequisite and forward standards from state standards vertical alignment knowledge (e.g., adjacent grade standards in the same strand). Add a footer to the teacher plan: *"Standard text retrieved from the curriculum lookup adapter. Prerequisite and forward standard grounding reflects [state/territory] standards vertical alignment."*

**If adapter not connected:** proceed from best knowledge; add footer to teacher plan: *"Generated without the curriculum lookup adapter. Standard text, prerequisite grounding, and misconceptions reflect general best practice."*

---

Copyright 2026 Anthropic, PBC · Copyright 2026 Learning Commons · SPDX-License-Identifier: Apache-2.0