# Curriculum Lookup — Tooling Contract

**Owner:** Tooling agent (Task 8)
**Status:** Implemented; skill consumers connect in Task 9.

## Purpose

Replace the upstream assumption that the Learning Commons Knowledge Graph covers
Australian/Queensland curricula. The connector upstream was US-standards-focused
(`Learning Commons KG`: CCSS/NGSS/C3/common-core and state-standard code patterns). It
does **not** cover the Australian Curriculum Version 9.0 (Foundation/Prep–Year 10, ACARA)
or current QCAA senior syllabuses (Years 11–12). The adapter below provides a portable,
offline, no-connector curriculum lookup that degrades safely.

## Interface contract (verbatim, from plan Task 8)

Curriculum lookup **must accept**:

- `jurisdiction` — `Australia` or `Queensland`
- `school_phase` — `F-10` or `Years 11-12`
- `year_level/course`
- `learning_area_or_subject`
- `code/query`

Curriculum lookup **must return**:

- official identifier
- statement type
- short text or locator
- source URL
- version/effective year
- authority name
- authority-verification evidence
- mapping confidence

It **must return an explicit not-found result** rather than synthesising an identifier.
It must **never** present an uncited or fabricated curriculum code.

## Take no connector assumption

The upstream skills assumed the Learning Commons KG returns US standards. This adapter
contains **no** reference to the Learning Commons Graph. When no authority-verified
source matches, it returns:

```json
{ "status": "not-found",
  "message": "No curriculum found for jurisdiction='...' ..." }
```

and never guesses a code or identifier.

## Offline / no-connector behaviour

The adapter reads versioned, bundled manifests:

- `data/curriculum/source-manifest.australian.json` — ACARA F-10 authority-verified rows
- `data/curriculum/qcaa/*.json` — QCAA subject packages with authority records,
  objectives, assessment model and `source_locators`.

No network call is made. If the requested subject is not in the bundled set, the adapter
returns `not-found` and tells the consumer to supply a teacher-provided code/URL or that
no exact alignment is available.

## Authority and provenance

Every returned match carries the authority name, publication owner, authority evidence
URL and verification status from the registered source. A consumer must cite the returned
`source_url` and `version_or_effective_year` in any user-facing alignment claim and may
not present an uncited code (Gate 3).

## What the adapter does NOT do

- It does not fabricate identifiers.
- It does not map CCSS/NGSS/C3/state codes onto Australian identifiers.
- It does not query the Learning Commons Graph or assume US coverage.
- It does not invent curriculum content; it returns identifiers, statement type, short
  text/locator, version, authority and confidence.

## CLI / self-check

```sh
python3 plugin/tools/curriculum_lookup/lookup.py --test
python3 plugin/tools/curriculum_lookup/lookup.py \
  --jurisdiction Australia --phase F-10 --subject Mathematics
python3 plugin/tools/curriculum_lookup/lookup.py \
  --jurisdiction Queensland --phase "Years 11-12" --subject "Legal Studies" --code QSUB-0052
```

Expected: valid F-10 lookup → `found` with cited ACARA source; valid QCAA lookup →
`found` with cited QCAA syllabus; invalid/unknown subject → `not-found`; never a
fabricated code.

## Coverage limitation (documented)

Only the manifests shipped in `data/curriculum/` are searchable offline. The 78-subject
QCAA source packages live on isolated `qcaa-<slug>-sources` branches; their manifests are
integrated into `data/curriculum/qcaa/` progressively. Until then, a subject without a
bundled manifest returns `not-found` (safe), and the consumer must either supply the
teacher-provided code/URL or cite the official source directly.

## Contract tests

`scripts/validate_localisation.py` (Task 7) asserts that skill responses carry
curriculum source/version/identifier, and the supervision/allowlist prevents uncited US
code patterns from leaking into shipped behaviour.