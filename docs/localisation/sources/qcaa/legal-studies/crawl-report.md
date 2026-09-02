# Legal Studies — QCAA Source Registration

## Identification

| Field | Value |
| --- | --- |
| QSID | QSUB-0052 |
| Subject slug | `legal-studies` |
| Subject family | Humanities and Social Sciences |
| Course type | General |
| Official page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/legal-studies |
| Worktree | `.kilo/worktrees/qcaa-legal-studies-sources-v2` |
| Branch | `qcaa-legal-studies-sources-v2` |
| Base commit | `281eb8d41fe2837d911541c9bbb870b58add804c` (pinned upstream SHA) |
| Pinned upstream SHA | `281eb8d41fe2837d911541c9bbb870b58add804c` |
| Retrieval date (UTC) | `2026-09-02` |

## Authority Verification (subject-level)

| Field | Recorded value |
| --- | --- |
| Authority name | Queensland Curriculum and Assessment Authority (QCAA) |
| Authority type | statutory curriculum authority |
| Publication owner | Queensland Curriculum and Assessment Authority |
| Authority evidence URL | https://www.qcaa.qld.edu.au/about/governance/legislation |
| Authority-verification status | `verified` |
| Verification evidence | The official QCAA Legislation page states that QCAA is established under and has its functions and powers set out in the *Education (Queensland Curriculum and Assessment Authority) Act 2014* and the *Education (Queensland Curriculum and Assessment Authority) Regulation 2025*. The retrieved Legal Studies syllabus page is served from the `qcaa.qld.edu.au` domain and the syllabus document footer identifies `Queensland Curriculum & Assessment Authority` as publisher (`© State of Queensland (QCAA) 2026`). The page footer and the syllabus PDF both display the Creative Commons Attribution 4.0 International licence linked to `creativecommons.org/licenses/by/4.0`. Task 4 catalogue authority verification for QCAA (`QSUB-0052`, status `verified`) applies unchanged. |

## Current vs Superseded Classification

- **Current syllabus:** Legal Studies General senior syllabus **2025 v1.3**, published January 2026, for implementation with students who will complete their study of the course in **2026 or beyond**. Registered as two sources: the official HTML page and the syllabus PDF (`snr_legal_25_syll.pdf`, 809.7 KB).
- **Superseded syllabus:** the previous Legal Studies **2019 General Senior Syllabus** (2019 v1.x). It is not linked from the supplied current Legal Studies page and is not registered in this work order, consistent with the bounded single-work-order convention.
- **Historical external assessment papers (not superseded syllabuses):** the current page lists 2020–2025 past papers (marking guide, question and response book, stimulus book for each year). These are official historical assessment resources, retained as locators only; they are not registered as hashed source records.
- **Current official support/assessment resources (locators only):** Key senior subject changes: For external assessment in 2026; sample assessment instruments (Unit 3 IA1 Examination — combination response; Unit 3 IA2 Investigation — inquiry report; Unit 4 IA3 Investigation — analytical essay); 2026 Endorsement subject report; 2020–2025 subject reports.

## Registered Sources

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| (Task 6 assigns) | current | Legal Studies General senior syllabus (HTML page) | 2025 v1.3 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/legal-studies |
| (Task 6 assigns) | current | Legal Studies 2025 v1.3 General senior syllabus PDF | 2025 v1.3 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_legal_25_syll.pdf |

`source_id` is intentionally omitted from the per-subject shard; Task 6 assigns the final `SRC-####` identifiers when merging source registers.

## Retrieval Method, Representation Type and Hash Provenance

Direct byte retrieval from `qcaa.qld.edu.au` is blocked by the QCAA Cloudflare protection (a direct `curl` request for the official Legal Studies page returned HTTP `403` in this environment). This work order therefore applies the recorded coordinator hash policy ruling (`progress.md`, 2026-08-31): a documented retrieval/rendering representation of the official QCAA URL may be hashed when direct retrieval is blocked.

- **Retrieval method:** official QCAA URLs rendered through the Firecrawl scrape/parse path on `2026-09-02`.
- **Representation type:** rendered markdown of the official HTML subject page (534 lines) and rendered markdown of the official syllabus PDF (1903 lines, 44 numbered pages per footer, `Page 1 of 44` … `Page 44 of 44`).
- **Hash provenance:** each `content_hash` is the SHA-256 over the exact retained rendered representation of the registered official URL:
  - HTML page representation SHA-256: `be1d1a18d13e198eaa3e18a2c00a4b5f94bfbd7ebe8ff686e57fe216b10f4b23`
  - Syllabus PDF representation SHA-256: `fcb0f3023af803c1cadeb1e6efe5333b9b7312773f344bcf10c60469e7da2da8`
- **Content verification:** the representation content was cross-checked against the official QCAA page and syllabus via the web-search index on the same day. The page lists "Legal Studies 2025 v1.3 (PDF, 809.7 KB)" as current and the PDF title block reads "Legal Studies 2025 v1.3 — General senior syllabus — January 2026 — © State of Queensland (QCAA) 2026", agreeing with the retained representations.
- **Reproducibility limitation:** the hashes cover the rendered representations, not the raw `%PDF-` byte stream. A follow-up pass with an authorised QCAA-compatible client should re-fetch the PDF bytes and recompute the SHA-256 over the raw PDF to upgrade these hashes to byte-level integrity. No Wayback, challenge-page, metadata-only, or fabricated hashes are used.

## Source Schema Conformance

- CSV uses the `source-register.schema.json` columns (authority name, type, evidence URL, publication owner, verification status, jurisdiction `Queensland`, phase `Years 11-12`, subject `Legal Studies`, title, version, URL, locator, licence, retrieval date, content hash), with the addendum `status` column used by the other committed QCAA shards and a `status` value of `current`.
- `authority_name` is `QCAA`; `authority_type` is `statutory curriculum authority`; `authority_verification_status` is `verified`.
- Both `content_hash` values match the schema pattern `^sha256:[a-f0-9]{64}$`.
- Licence recorded as `CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)`.

## Minimum Extraction Notes

- The structured data in `data/curriculum/qcaa/legal-studies.json` is limited to the five syllabus objectives, four-unit structure, and four-instrument assessment model (IA1/IA2/IA3/EA at 25% each) plus official locators. No substantial syllabus text is reproduced.
- QCAA terminology is preserved (General, internal assessment, external assessment, ISMG, combination response, inquiry report, analytical essay).
- The fixture `source-fixture.json` mirrors the two registered source records and omits `source_id` per the Task 6 merge ruling.

## Gaps / Unresolved Items

1. Raw-PDF-byte SHA-256 for the syllabus PDF (and any future hashed resource PDFs) must be computed once direct QCAA download is available, per the coordinator hash-policy ruling. The current hashes are over documented rendered representations of the official URLs.
2. Historical past papers and prior-year subject reports are retained as official locators only and are not registered as hashed source records, to avoid fabricating hashes for resources that Cloudflare blocked this pass.
3. No superseded Legal Studies syllabus is linked from the supplied current page; registering the 2019 General Senior Syllabus as a historical record would require a separate QCAA/Pandora archive search outside this single-work-order scope.