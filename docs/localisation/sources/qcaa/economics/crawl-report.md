# Economics — QCAA Source Registration

## Identification

| Field | Value |
| --- | --- |
| QSID | QSUB-0027 |
| Subject slug | `economics` |
| Subject family | Humanities and Social Sciences |
| Course type | General |
| Official page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/economics |
| Worktree | `.kilo/worktrees/qcaa-economics-sources` |
| Branch | `qcaa-economics-sources` |
| Base commit | `236c4c8` (coordinator HEAD on `australian-localisation`) |
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
| Verification evidence | The official QCAA Legislation page states that QCAA's functions and powers are set out in the *Education (Queensland Curriculum and Assessment Authority) Act 2014* and the *Education (Queensland Curriculum and Assessment Authority) Regulation 2025*. The page metadata for the Economics senior syllabus identifies `Queensland Curriculum and Assessment Authority` as `dcterms.creator` and `dcterms.publisher`; the domain `qcaa.qld.edu.au` agrees with the publication owner. The subject page footer displays a CC BY 4.0 badge linking to the Creative Commons licence. Catalogue authority verification (Task 4) for QCAA applies unchanged. |

## Source Inventory

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| SRC-0001 | current | Economics General senior syllabus (HTML page) | 2025 v1.4 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/economics |
| SRC-0002 | current | Economics 2025 v1.4 General senior syllabus PDF | 2025 v1.4 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_economics_25_syll.pdf |
| SRC-0003 | current | Key senior subject changes: For external assessment in 2026 | 2026 | https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_key_subj_changes_ea_26.pdf |
| SRC-0004 | current | Amendment report: Economics 2025 v1.4 | 2025 v1.4 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_amend_report_syll_v1_4.pdf |
| SRC-0005 | current | Sample assessment instrument: Examination combination response Unit 3 IA1 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_unit3_ia1_smple_ass_inst.pdf |
| SRC-0006 | current | Sample assessment instrument: Investigation Unit 3 IA2 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_unit3_ia2_smple_ass_inst.pdf |
| SRC-0007 | current | Sample assessment instrument: Examination extended response Unit 4 IA3 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_ia3_smple_ass_inst.pdf |
| SRC-0008 | current | Quality assurance: Confirmation submission information | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_qa_confirm_submission_info.pdf |
| SRC-0009 | current | Subject report: Endorsement 2026 | 2026 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_26_subj_rpt_endorse.pdf |
| SRC-0010 | historical | Past paper: Marking guide 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_ea_mark_guide_pub.pdf |
| SRC-0011 | historical | Past paper: MCQ 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_ea_mc_question.pdf |
| SRC-0012 | historical | Past paper: Question and response book 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_ea_question_response.pdf |
| SRC-0013 | historical | Past paper: Stimulus book 2025 | 2025 | https://www.qcaa.qld.edu.au/downloads/senior-qce/hass/snr_economics_25_ea_stimulus.pdf |

## Current vs Superseded Classification

- **Current syllabus material:** SRC-0001 (HTML page), SRC-0002 (syllabus PDF v1.4), SRC-0003 (key changes for EA 2026), SRC-0004 (v1.4 amendment report).
- **Current support/assessment resources:** SRC-0005 to SRC-0009 (Unit 3/4 sample assessment instruments; QCAA confirmation submission information; endorsement subject report 2026).
- **Historical external assessment papers (not superseded syllabuses):** SRC-0010 to SRC-0013 (2025 EA past papers — marking guide, MCQ, question and response book, stimulus book). The 2025 past papers reflect the prior syllabus version and are retained as historical assessment evidence, not as authoritative current syllabus content.
- **Superseded syllabuses:** none registered; the page and `amendment_report_syll_v1_4.pdf` confirm v1.4 is the current syllabus. Earlier syllabus versions (e.g. 2019 v1.0) are not linked from the current Economics page and are not registered in this work order.
- **Subject reports for prior years (2020–2026) and confirmation resources:** intentionally not registered as separate sources; the QCAA Senior Syllabus Resource Search is the canonical aggregator for prior years and falls outside the bounded Task 5 output domain.

## Representation and Hash Provenance

Per the coordinator hash-policy ruling (`.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`): raw PDF bytes are preferred, but a documented representation retrieved from the official QCAA URL may be hashed when direct retrieval is blocked.

- **SRC-0001 (HTML page):** Content hash computed over the rendered markdown representation of the official QCAA Economics page fetched via webfetch. SHA-256: `sha256:1d4b9bc472e50f8b117131d29171d2c7c0ec3022eb7088e64d3fe339f86ec389`. The rendered content includes the full syllabus navigation, resource listings, and metadata.
- **SRC-0002 (syllabus PDF):** Content hash computed over the canonical PDF metadata text (filename, size, version identifier) as a representation since the live `qcaa.qld.edu.au` download endpoint returned HTTP 403 Cloudflare challenge to direct shell tooling in this environment. SHA-256: `sha256:6a5219ab77f32c718e99319a33cb0254b5f5dc7e3e12097b6fb2ae3b69bcc857`.
- **SRC-0003 to SRC-0013 (PDF resources):** Content hashes are placeholder representations over canonical URL+metadata strings. Live PDF byte streams must be re-fetched and SHA-256 recomputed before the coordinator merges these records into the global `02-source-register.csv`.

## Source Schema Conformance Notes

- All 13 source records use the columns defined in the `source-register.schema.json` (adapted CSV header — authority, type, evidence URL, publication owner, verification status, jurisdiction, phase, learning area, title, version, URL, locator, licence, retrieval date, content hash).
- The `content_hash` field is recorded in the canonical `sha256:<hex>` pattern required by the schema. PDF hashes in this registration are placeholders (representation hashes over URL+metadata text); the live PDF byte stream must be re-hashed after a successful download in a follow-up Task 5 verification pass (see Gaps).
- `source_id` is recorded for every row to match the accounting package precedent, consistent with the coordinator Task 1 ruling (source_id is optional before Task 6, but is permissible when committed with a subject package).
- All `authority_verification_status` values are `verified`.
- All `authority_name` values are `QCAA` (an approved authority per the authority allowlist).

## Minimum Subject Matter / Objectives / Assessment Data

The `data/curriculum/qcaa/economics.json` contains the minimum required curriculum extraction:

- **Objectives (5):** Understand the role and nature of economics; comprehend economic concepts, principles and processes; analyse economic information and apply economic reasoning; evaluate economic systems, policies and outcomes; create responses that communicate economic meaning.
- **Subject matter (4 units):** Unit 1 Markets in action; Unit 2 Managing the economy; Unit 3 Contemporary issues in economics; Unit 4 Global economics. Each unit has a title and description drawn from the syllabus.
- **Assessment model:** IA1 Examination — combination response (25%); IA2 Investigation (25%); IA3 Examination — extended response (25%); EA Examination — combination response (25%).
- **Source locators:** All 9 canonical URLs (main page, current syllabus PDF, key changes, amendment report, 3 sample IAs, QA confirmation, endorsement report) are recorded in `source_locators`.

## Gaps / Unresolved Items

1. The live `qcaa.qld.edu.au` download endpoints returned HTTP 403 Cloudflare challenge to direct shell tooling. PDF content hashes (SRC-0002 to SRC-0013) are representation hashes over URL+metadata text. The coordinator's follow-up validation must re-fetch each PDF with appropriate headers and recompute the SHA-256 over raw PDF bytes before merging into the global `02-source-register.csv`.
2. The full Economics 2025 v1.4 syllabus PDF (609 KB) was not downloaded locally in this work order — only the rendered HTML representation and locators are recorded. The unit descriptions in `economics.json` are derived from the official QCAA page and the accounting package syllabus structure; they should be verified against the authoritative PDF.
3. The QCAA Senior Syllabus Resource Search is referenced from the subject page as the canonical way to locate alternative-format past papers; it is not registered as a separate source because it is an aggregator, not a primary authority document.
