# Source and Version Policy

This policy governs the curriculum sources, versions, licences, and verification procedures
that back the Australian-localised skills. It is the authority for what may be cited in
shipped behaviour.

## 1. Approved source classes

Only the source classes below may be cited. Each must be registered in the source registers
under `docs/localisation/sources/` with the fields defined in
`docs/localisation/schema/source-register.schema.json`.

| Class | Authority name | What it covers | Version / year field |
|---|---|---|---|
| 1 (statutory) | Australian Curriculum, Assessment and Reporting Authority (ACARA) | Australian Curriculum V9.0, F–10 content descriptions and achievement standards | `9.0` (V9) |
| 2 (statutory) | Queensland Curriculum and Assessment Authority (QCAA) | General Senior Syllabuses, Years 11–12 | syllabus year / version string in the bundled manifest |
| 3 (reference) | State/territory curriculum authorities (e.g. NSW Education Standards, VCAA, ACT EATS) | Cross-reference only; **not** an alignment target for shipped skills | as registered |
| 4 (reference) | Published research on student misconceptions / learning progressions (CC BY or equivalent) | Distractor and error-to-stem mapping only; **not** a curriculum standard | as registered |

Classes 1 and 2 are the only **alignment targets**. A curriculum code returned to a teacher
must come from class 1 or 2 and must carry the registered `source_url`, version, and licence
fields. Class 3 and 4 material informs item design only and must **not** be cited as a
curriculum standard.

## 2. Attribution and licences

- The Australian Curriculum (V9) is licensed by ACARA under **Creative Commons Attribution 4.0
  International (CC BY 4.0)**. Every ACARA-sourced row in
  `data/curriculum/source-manifest.australian.json` records this licence and the ACARA
  copyright notice. Do not reproduce ACARA student-facing text verbatim; use it only to
  inform structure, scope, and sequencing (see the copyright guardrail in each skill's SKILL.md).
- QCAA senior syllabuses are © Queensland Curriculum and Assessment Authority and are used
  under the QCAA copyright/terms of use reproduced in each
  `data/curriculum/qcaa/*.json` record. They are not open-licensed for redistribution; cite
  the official QCAA syllabus URL and do not reproduce syllabus text verbatim.
- This project's source code and skill text are © 2026 Anthropic, PBC and © 2026 Learning
  Commons, licensed Apache-2.0 (SPDX-License-Identifier: Apache-2.0). See `LICENSE` and
  `NOTICE`. The skills were co-developed by Anthropic and Learning Commons.

## 3. Authority verification procedure

Every source registered in `docs/localisation/sources/` must pass the verification gate
before it can carry `authority_verification_status: "verified"` and be used as an alignment
target:

1. **Confirm governing authority** — the source is published by the body named in the
   `authority_name` field and the `authority_evidence_url` resolves to that body.
2. **Confirm version / effective year** — the document is the current version recorded in the
   manifest. ACARA V9.0 is the only ACARA version in scope; V8.4 and earlier are out of scope.
3. **Confirm licence** — the `licence` field matches the authority's declared terms and is one
   of the approved source classes above.
4. **Record retrieval date and content hash** — `retrieval_date` and `content_hash` (SHA-256)
   are captured so any drift from the registered version is detectable.
5. **Reviewer sign-off** — class 1 and 2 sources require sign-off from a curriculum-qualified
   reviewer on the `mapping_confidence` field. The sign-off column in
   `docs/localisation/06-review-log.csv` records the reviewer and date.

A source with `authority_verification_status: "unverified"` must **not** be cited in any
curriculum alignment and its codes must not appear in teacher-facing output.

## 4. Mapping confidence and review status

Every curriculum alignment produced by a skill carries a `mapping_confidence` label that is
**never fabricated**:

- `exact` — the skill's learning component maps 1:1 to a single registered authority
  statement.
- `authority-verified` — the mapping was reviewed and approved by a curriculum-qualified
  reviewer against a registered source.
- `contextual` — the mapping is supported by default terminology rules (see §5) and is
  **pending reviewer** sign-off; it is not yet approved for shipped behaviour.
- `pending-reviewer` — the row in the replacement matrix
  (`docs/localisation/03-replacement-matrix.csv`) is marked `pending` and needs an
  authority-verified mapping before it can be cited as an alignment.
- `partial` — no exact alignment exists; the skill routes to a teacher prompt for a
  teacher-provided code or notes the gap.

**Mapping rows pending reviewer.** Several replacement-matrix rows — in particular those that
cross from a US concept to an Australian equivalent with no single direct code — are marked
`pending` in `docs/localisation/03-replacement-matrix.csv` and `pending-reviewer` in
`docs/localisation/03-mapping-summary.md`. These are **not** human-reviewed mappings and must
not be described as reviewed or approved. Where a skill uses one of these mappings, it must
surface the `pending-reviewer` status to the teacher rather than presenting the alignment as
settled.

## 5. Terminology defaults

Default terminology replacements applied by the mapping rules are only used where the context
supports them. Defaults that cannot be resolved are marked `pending` and require an
authority-verified mapping:

- `K-12` → `F-12`
- `K-5` → `F-6`
- `kindergarten` → `Prep` (Queensland)
- `ELA` → `English`
- `social studies` → `HASS` (F-10) or named QCAA senior subject
- `math` → `Mathematics`
- `grade` → `year level`
- `standards` (generic) — must be specified as "Australian Curriculum content description"
  (F-10) or "QCAA syllabus objective" (Years 11-12).

## 6. Refresh manifest and eval process

When ACARA or QCAA publish an updated version or revision, the following refresh process runs.
It is the responsibility of the tooling/maintainer agent to own timing and execution; the
output is verified by `scripts/validate_localisation.py`.

1. **Detect a change.** A new ACARA V9 point release or a revised QCAA syllabus is detected
   via the authority evidence URLs and the `retrieval_date` / `content_hash` in the manifests.
2. **Update the manifest.** Add the new version to
   `data/curriculum/source-manifest.australian.json` (ACARA) or the relevant
   `data/curriculum/qcaa/*.json` (QCAA), preserving the previous version's row for audit.
   Recompute `content_hash` from the freshly retrieved source.
3. **Re-verify.** Run the authority verification procedure (§3) against the new version,
   including a curriculum-qualified reviewer sign-off on the changed mapping rows. Re-register
   new sources under the schema in
   `docs/localisation/schema/source-register.schema.json` and record them in
   `docs/localisation/sources/`.
4. **Update the mapping matrix.** Recompute `docs/localisation/03-replacement-matrix.csv` so
   rows that depended on the updated source are re-reviewed; rows that cannot be remapped are
   marked `pending-reviewer`.
5. **Run evals.** The evaluation suite under `evals/` references curriculum codes and
   versions through the same manifests. After a manifest update, run the full eval matrix and
   confirm no eval asserts against a retracted or superseded code. Evals that reference a
   superseded ACARA version (V8.4) must be updated to V9.0.
6. **Validate.** `scripts/validate_localisation.py` asserts that:
   - every cited curriculum identifier resolves to a `verified` source of class 1 or 2;
   - the `not-found` branch returns no code or identifier ever;
   - no US code pattern (CCSS/NGSS/C3/state codes) leaks into shipped behaviour
     (Gate 3 of the supervision allowlist).
7. **Document.** Update `docs/localisation/03-mapping-summary.md` with the new row counts and
   review-log entry, and update this policy only via a PR that touches this file alone.

A subject without a bundled manifest — including QCAA subjects not yet integrated — returns
`not-found` from the adapter and the skill routes to the teacher for a teacher-provided code.
This safe no-lookup behaviour is never a failure of the skill itself.

## 7. Approved vocabulary

- Use `year level` (not `grade`, `grade level`).
- Use `F-12` (not `K-12`), `F-10` (not `K-5`), `Prep` (not `kindergarten`) for Queensland.
- Use `Mathematics`, `English`, `Science`, `HASS` (not `math`, `ELA`, `social studies`).
- Use `Australian Curriculum content description` (F-10) or `QCAA syllabus objective`
  (Years 11-12) — never `standards` generically.
- Use `learning area` or `subject` rather than `course of study` for F-10, and `subject` for
  Years 11-12.

Disapproved forms that must not appear in shipped behaviour: `K-12`, `K-5`, `kindergarten`,
`ELA`, `social studies`, `CCSS`, `NGSS`, `C3`, `504`, `IEP`, `WIDA`. Requests to use a
disapproved form require a documented exception recorded in `docs/localisation/06-review-log.csv`.