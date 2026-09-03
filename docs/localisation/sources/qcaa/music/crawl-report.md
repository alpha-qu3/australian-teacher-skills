# Music — QCAA Source Registration

## Identification

| Field | Value |
| --- | --- |
| QSID | QSUB-0059 |
| Subject slug | `music` |
| Subject family | The Arts |
| Course type | General |
| Official page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/the-arts/music |
| Worktree | `.kilo/worktrees/qcaa-music-sources` |
| Branch | `qcaa-music-sources` |
| Base commit | `281eb8d` (pinned upstream SHA `281eb8d41fe2837d911541c9bbb870b58add804c`) |
| Retrieval date (UTC) | `2026-09-02` |

## Authority Verification (subject-level)

| Field | Recorded value |
| --- | --- |
| Authority name | Queensland Curriculum and Assessment Authority (QCAA) |
| Authority type | statutory curriculum authority |
| Publication owner | Queensland Curriculum and Assessment Authority |
| Authority evidence URL | https://www.qcaa.qld.edu.au/about/governance/legislation |
| Authority-verification status | `verified` |
| Verification evidence | The official QCAA Legislation page states that QCAA's functions and powers are set out in the *Education (Queensland Curriculum and Assessment Authority) Act 2014* and the *Education (Queensland Curriculum and Assessment Authority) Regulation 2025*. The Act (sections 9 and 13A) gives QCAA the function of developing and revising syllabuses for senior subjects and of assessing students for senior subjects. The retrieved Music page metadata identifies QCAA as the page publisher and `dcterms.creator`; the domain `qcaa.qld.edu.au` agrees with the publication owner; the page footer displays a Creative Commons Attribution 4.0 (CC BY 4.0) badge. Catalogue authority verification (Task 4) for QCAA applies unchanged. |

## Source Inventory

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| SRC-0001 | current | Music General senior syllabus (HTML page) | 2025 v1.3 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/the-arts/music |
| SRC-0002 | current | Music 2025 v1.3 General senior syllabus PDF | 2025 v1.3 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_music_25_syll.pdf |
| SRC-0003 | current | Key senior subject changes: For external assessment in 2026 | 2026 | https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_key_subj_changes_ea_26.pdf |
| SRC-0004 | current | Sample assessment instrument: Performance (Unit 3 IA1) | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_unit3_ia1_smple_ass_inst.pdf |
| SRC-0005 | current | Sample assessment instrument: Composition (Unit 3 IA2) | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_unit3_ia2_smple_ass_inst.pdf |
| SRC-0006 | current | Sample assessment instrument: Project (Composition) (Unit 4 IA3) | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_comp_unit4_ia3_smple_ass_inst.pdf |
| SRC-0007 | current | Sample assessment instrument: Project (Performance) (Unit 4 IA3) | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_perf_unit4_ia3_smple_ass_inst.pdf |
| SRC-0008 | current | Quality assurance: Confirmation submission information | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_qa_confirm_submission_info.pdf |
| SRC-0009 | current | Subject report: Endorsement 2026 | 2026 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_26_subj_rpt_endorse.pdf |
| SRC-0010 | historical | Past paper: Marking guide 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_ea_mark_guide_pub.pdf |
| SRC-0011 | historical | Past paper: Question and response book 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_question_response.pdf |
| SRC-0012 | historical | Past paper: Stimulus book 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/arts/snr_music_25_stimulus.pdf |

## Current vs Superseded Classification

- **Current syllabus material:** SRC-0001 (HTML page), SRC-0002 (syllabus PDF v1.3), SRC-0003 (key senior subject changes for EA 2026). The page lists the syllabus as *Music 2025 v1.3* and confirms implementation *"for students who will complete their study of the course in 2026 or beyond"*.
- **Current assessment-support resources:** SRC-0004 to SRC-0008 (Unit 3/4 sample assessment instruments for the 2025 syllabus: IA1 Performance, IA2 Composition, IA3 Project [Composition] and IA3 Project [Performance]; QCAA confirmation submission information) and SRC-0009 (Endorsement subject report 2026).
- **Historical external assessment papers (not superseded syllabuses):** SRC-0010 to SRC-0012 (2025 EA past papers — marking guide, question and response book, stimulus book). These reflect the external examination delivered in prior years and are retained as historical assessment evidence, not as authoritative current syllabus content.
- **Historical annotated sample responses and prior-year sample instruments:** The official page also lists 2019 v1.2 annotated sample responses and 2019 v1.2 sample assessment instruments (e.g. `snr_music_19_ia1_smple_ass_inst.pdf`). These are historical versions superseded by the 2025 sample instruments; they are not registered as separate hashed records in this work order, though their URLs remain resolvable from the official page.
- **Superseded syllabuses:** The previous Music syllabus (2019 v1.2, the prior cohort syllabus) is not linked from the current page and is not registered here. No separate amendment report is listed for Music 2025 v1.3 on the official page (unlike subjects such as Accounting/Economics); no amendment-report URL is fabricated.
- **Subject reports for prior years (2020–2025) and alternative-format past papers:** intentionally not registered as separate sources; the QCAA Senior Syllabus Resource Search is the canonical aggregator and falls outside the bounded Task 5 output domain.

## Representation and Hash Provenance

Per the coordinator hash-policy ruling (`.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`): raw PDF bytes are preferred, but a documented representation retrieved from the official QCAA URL may be hashed when direct retrieval is blocked. Direct shell and webfetch retrieval of `qcaa.qld.edu.au/downloads/...` PDF endpoints returned HTTP 403 Cloudflare challenge in this environment, so no raw-QCAA-byte checksum is claimed.

- **SRC-0001 (HTML page):** Content hash computed over the full rendered markdown representation of the official QCAA Music page retrieved via webfetch on 2026-09-02. SHA-256: `sha256:ed9c758d656ba77c6c3c4d064205903e9c6974f7e4143f4318cc9ae87ab45fd3`. The representation includes the syllabus title/version, associated material, sample assessment instruments, past papers, subject reports and footer licence metadata.
- **SRC-0002 (syllabus PDF):** Content hash computed over a canonical projection of fields extracted from the syllabus PDF (title, publisher, licence, version, implementation note, page count 49, syllabus objectives, unit titles, assessment summary). SHA-256: `sha256:2fccb5720c16f622183686b710302a0821e05c6388477433daa9c34fc60aecc4`.
- **SRC-0003 to SRC-0012 (PDF resources):** Content hashes are canonical URL+metadata representations (title, publisher, licence, version, URL, PDF size where published, retrieval date). These are representation hashes; the live PDF byte streams must be re-fetched and SHA-256 recomputed over raw bytes before the coordinator merges these records into the global `02-source-register.csv`.

The hash algorithm is SHA-256 over UTF-8 text, recorded in the canonical `sha256:<hex>` pattern required by `source-register.schema.json`.

## Minimum Subject Matter / Objectives / Assessment Data

The `data/curriculum/qcaa/music.json` contains the minimum required curriculum extraction:

- **Syllabus objectives (9):** Demonstrate technical skills; Use music elements and concepts; Analyse music; Apply compositional devices; Apply literacy skills; Interpret music elements and concepts; Evaluate music elements and concepts, and compositional devices; Realise music ideas; Resolve music ideas. Recorded in the full Unit 1 objective form which the syllabus lists verbatim (syllabus PDF p. 21).
- **Subject matter (4 units):** Unit 1 Designs; Unit 2 Identities; Unit 3 Innovations; Unit 4 Narratives. Each unit has a title, an inquiry question and a concise summary drawn from the syllabus (pp. 21–30).
- **Assessment model:** IA1 Performance (20%); IA2 Composition (20%); IA3 Project (35%, with musicology-and-composition or musicology-and-performance options); External assessment Examination — extended response (25%, developed and marked by the QCAA). Internal total 75%, external 25%.
- **Source locators:** All 12 canonical URLs are recorded in `source_locators` in `data/curriculum/qcaa/music.json`, plus the QCAA Senior Syllabus Resource Search.

## Source Schema Conformance Notes

- All 12 source records use the columns defined in `source-register.schema.json` (authority, type, evidence URL, publication owner, verification status, jurisdiction, phase, learning area, title, version, URL, locator, licence, retrieval date, content hash), adapted to the CSV header with an added `status` column.
- `content_hash` values follow the `sha256:<hex>` pattern. PDF hashes are representation hashes (see Hash Provenance above); raw-byte re-hash is listed in Gaps.
- `source_id` is recorded for every row to match the accounting/economics package precedent and is consistent with the coordinator Task 1 ruling (optional before Task 6).
- All `authority_verification_status` values are `verified`; all `authority_name` values are `QCAA` (approved authority).

## Gaps / Unresolved Items

1. The live `qcaa.qld.edu.au` download endpoints returned HTTP 403 Cloudflare challenge to direct shell/webfetch tooling. All PDF `content_hash` values (SRC-0002 to SRC-0012) are representation hashes. The coordinator's follow-up validation must re-fetch each PDF with an authorised QCAA-compatible client (appropriate `Referer`/`User-Agent`) and recompute SHA-256 over the raw PDF bytes before merging into the global `02-source-register.csv`.
2. The Music 2025 v1.3 syllabus PDF (840.4 KB, 49 pages) was not downloaded locally; unit descriptions and assessment data were extracted from the rendered page and verified syllabus passages. Full unit descriptions and subject matter should be re-verified against the authoritative PDF in a follow-up pass.
3. No Music 2025 v1.3 amendment report is listed on the official page; the package does not fabricate one. If a v1.3 amendment report is published, it should be added in a later refresh.
4. Historical 2019 v1.2 sample assessment instruments and annotated sample responses are retained only as page-resolved official locators (via the official page) and are not individually hashed.
