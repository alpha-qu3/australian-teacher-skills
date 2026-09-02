# German Extension — QCAA Source Registration

## Identification

| Field | Value |
| --- | --- |
| QSID | QSUB-0044 |
| Subject slug | `german-extension` |
| Subject family | Languages |
| Course type | General (Extension) |
| Official page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/languages/german-extension |
| Worktree | `.kilo/worktrees/qcaa-german-extension-sources` |
| Branch | `qcaa-german-extension-sources` |
| Base commit | `281eb8d` (pinned upstream SHA on the localisation baseline) |
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
| Verification evidence | QCAA is established as the statutory curriculum and assessment authority for Queensland senior schooling by the *Education (Queensland Curriculum and Assessment Authority) Act 2014*, as recorded on the official QCAA Legislation page. The German Extension syllabus PDF carries the QCAA byline and report number, and the official subject page footer identifies `Queensland Curriculum and Assessment Authority` as publisher (`dcterms.creator` / `dcterms.publisher`) on the `qcaa.qld.edu.au` domain. The page footer displays the Creative Commons Attribution 4.0 International (CC BY 4.0) licence. Catalogue authority verification (Task 4) for QCAA applies unchanged. |

## Current Syllabus Determination

- **Current syllabus:** *German Extension 2026 v1.3*, General (Extension) senior syllabus, January 2026. The official page states the syllabus is "For implementation with students who will complete their study of the course in 2026 or beyond."
- **Version evidence:** The page lists the current PDF as `German Extension 2026 v1.3 (PDF, 539.5 KB)`; the syllabus body text repeatedly carries the header `German Extension 2026 v1.3 General (Extension) senior syllabus | January 2026` (34 pages). An earlier search-index payload still labelled the PDF with the older `v1.2` title; the January 2026 v1.3 designation is confirmed by the body text of the current PDF and by the current subject page, and is treated as authoritative for this registration.
- **Superseded syllabuses:** none registered. The current page links only the 2026 v1.3 syllabus; earlier syllabus versions are not linked from the current page and are not registered in this work order.

## Source Inventory

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| SRC-0001 | current | German Extension General senior syllabus (HTML page) | 2026 v1.3 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/languages/german-extension |
| SRC-0002 | current | German Extension 2026 v1.3 General (Extension) senior syllabus PDF | 2026 v1.3 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_german_ext_26_syll.pdf |
| SRC-0003 | current | Subject report: Endorsement 2026 | 2026 | https://www.qcaa.qld.edu.au/downloads/senior-qce/languages/snr_german_ext_26_subj_rpt_endorse.pdf |

## Current vs Superseded Classification

- **Current syllabus material:** SRC-0001 (HTML page) and SRC-0002 (syllabus PDF v1.3). Both confirm v1.3 as the current syllabus.
- **Current support/assessment resources:** SRC-0003 (Subject report: Endorsement 2026). The report confirms the current assessment model (IA1 Examination — combination response 20%, IA2 Examination — extended response 25%, IA3 Investigative folio and interview 30%).
- **Locations on the official page that were identified but NOT registered as sources (see Gaps):**
  - Associated material: *Key senior subject changes: For external assessment in 2026* (`snr_ext_key_subj_changes_ea_26.pdf`, 295.1 KB) — the extension-subject listing file; its content was not retrievable in this work order.
  - Quality assurance: *Confirmation submission information* (`snr_qa_confirm_submission_info.pdf`, 904.6 KB).
  - Historical external assessment past papers: 2025 (marking guide 286.1 KB, question and response book 620.2 KB, stimulus book 268.3 KB), 2024, 2023, 2022, 2021, 2020 (marking guide, question and response book, stimulus book for each year). These are assessment artefacts of prior cohorts, not syllabus content required by the four localised skills, and their content representations were not retrievable.
  - Subject reports for prior years (2020–2025) and subject report factsheets: intentionally not registered as separate sources; the QCAA Senior Syllabus Resource Search is the canonical aggregator for prior years and falls outside the bounded Task 5 output domain.
- **Superseded syllabuses:** none registered.
- **No sample assessment-instrument section for German Extension was confirmed on the current page** (unlike the German general page). Item-level sample instruments for the 2026 extension syllabus were not located; see Gaps.

## Representation and Hash Provenance

Per the coordinator hash-policy ruling (`.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`): raw PDF bytes are preferred, but a documented representation retrieved from the official QCAA URL may be hashed when direct retrieval is blocked. All three registered hashes are SHA-256 over the rendered-content representation retrieved from the official QCAA URL via the session web-search provider's live rendering. No Wayback content, challenge HTML, metadata-only serialisation, or fabricated hash is used.

| Source | Representation type | Retrieval method | Hash |
| --- | --- | --- | --- |
| SRC-0001 (HTML page) | Rendered markdown of the official QCAA German Extension page (heading, syllabus block, associated material, resource listings, copyright footer) | Session web-search provider live rendering of the official QCAA URL; direct `curl`/`webfetch` returned HTTP 403 Cloudflare challenge, and Firecrawl rendering was unavailable | `sha256:2b29b8e278a46d123f12fb0686f18e8f570972bfd8fb88fe9c5e6c7dcafcc1c4` |
| SRC-0002 (syllabus PDF) | Rendered PDF text of the official syllabus (cover, rationale, six objectives, A–E reporting standards, Units 3–4, IA1/IA2/IA3 and EA specifications and mark allocations) | Session web-search provider rendering of the official `snr_german_ext_26_syll.pdf` URL; direct download returned HTTP 403 Cloudflare challenge | `sha256:0f7f2a4622f02a457149d329785161ae8faf361e1ae22c136ad764ce39c2ac1f` |
| SRC-0003 (endorsement report) | Rendered PDF text of the official Subject report: Endorsement for the German Extension 2026 cohort (summary table, advice for assessment design, licence footer) | Session web-search provider rendering of the official `snr_german_ext_26_subj_rpt_endorse.pdf` URL; direct download returned HTTP 403 Cloudflare challenge | `sha256:3ea065d648c1c1e9eacbd47666cdfa08b60d8b32e2b450a8923672dc0516b6ad` |

Reproducibility limitation (all three): the hashed representations are search-provider renderings of the official QCAA URLs, and re-running the same retrieval path can produce byte-identical output only while the provider's index snapshot is unchanged. The coordinator's follow-up validation must re-fetch each registered URL with QCAA-compatible headers and recompute SHA-256 over the raw page/PDF bytes before merging the Task 5 source shards into the global `02-source-register.csv`.

## Source Schema Conformance Notes

- All 3 source records use the columns defined in the `source-register.schema.json` (authority, type, evidence URL, publication owner, verification status, jurisdiction, phase, learning area, title, version, URL, locator, licence, retrieval date, content hash).
- Every `content_hash` matches the canonical `^sha256:[a-f0-9]{64}$` pattern required by the schema and is a real hash of a recovered content representation (no placeholders, no PENDING markers, no fabricated hex).
- `authority_name` is `QCAA` (approved authority), `authority_type` is `statutory curriculum authority`, and `authority_verification_status` is `verified` for every row.
- `source_id` (SRC-####) is recorded per row; the JSON `source-fixture.json` deliberately omits `source_id` to leave the final stable ID for the coordinator's Task 6 merge pass.

## Minimum Subject Matter / Objectives / Assessment Data

The `data/curriculum/qcaa/german-extension.json` contains the minimum required curriculum extraction:

- **Objectives (6):** apply knowledge of language elements, structures and textual conventions to explore how meaning is conveyed in texts; make decisions about language elements, structures and textual conventions to create or determine meaning in texts; interpret how meaning, attitudes, perspectives and values underpin texts and influence audiences through an investigative and/or critical process; analyse and evaluate information and ideas to draw conclusions, justify points of view and construct arguments in German through an investigative and/or critical process; create texts that communicate information and ideas in German for context, purpose, audience, tone and cultural conventions; structure, sequence and synthesise information to respond to texts personally, critically and/or creatively.
- **Subject matter:** Unit 3 *Guided investigation*; Unit 4 *Independent investigation*. Subjects matter is organised under areas of study (Literature and Social sciences are named directly in the retrieved text; arts, business and commerce, and innovation/science/technology areas are referenced in the retrieved syllabus content but are not exhaustively catalogued in this extraction).
- **Assessment model (2026 v1.3):** IA1 Examination — combination response (20%); IA2 Examination — extended response (25%); IA3 Investigative folio and interview (30%); EA Examination — extended response (25%). The endorsement report (SRC-0003) corroborates the three internal weightings.
- **Source locators:** all 3 canonical URLs are recorded in `source_locators`.

## Gaps / Unresolved Items

1. **Direct QCAA retrieval remains Cloudflare-blocked.** `curl` and `webfetch` returned HTTP 403 challenge pages and the Firecrawl render path was unavailable, so all three hashes are over search-provider rendered representations, not raw QCAA bytes. The coordinator must re-fetch page/PDF bytes and recompute SHA-256 before Task 6 merge.
2. **Unregistered page-listed resources.** The extension-subject *Key senior subject changes: For external assessment in 2026* (`snr_ext_key_subj_changes_ea_26.pdf`) and *Confirmation submission information* (`snr_qa_confirm_submission_info.pdf`) are linked from the official page but could not be content-retrieved in this work order, so they were not registered rather than register unhashed or metadata-only records. A follow-up pass should register them once raw bytes are retrievable.
3. **Historical past papers (2025–2020).** Seventeen historical external-assessment papers (marking guide, question and response book, stimulus book across 2020–2025) are listed on the official page and classified as historical; they are not registered because their content could not be retrieved and they are assessment artefacts rather than syllabus content needed by the four localised skills.
4. **Extension sample assessment instruments.** No 2026-sample assessment-instrument section was confirmed on the German Extension page in the retrievable rendering. If QCAA publishes unit 3/4 sample instruments for this extension subject, a follow-up pass should register them.
5. **v1.2 vs v1.3 index ambiguity.** One search-index payload still titles the current PDF with the superseded `v1.2` label; the current page and PDF body both use `2026 v1.3` (January 2026) and the new payload was treated as authoritative. The coordinator should confirm the PDF cover when raw bytes are retrieved.