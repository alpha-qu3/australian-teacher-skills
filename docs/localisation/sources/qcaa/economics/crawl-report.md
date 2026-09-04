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

## Current vs Superseded Classification

- **Current syllabus material:** SRC-0001 (HTML page), SRC-0002 (syllabus PDF v1.4), SRC-0003 (key changes for EA 2026), SRC-0004 (v1.4 amendment report).
- **Current support/assessment resources:** SRC-0005 to SRC-0009 (Unit 3/4 sample assessment instruments; QCAA confirmation submission information; endorsement subject report 2026).
- **Historical external assessment papers (not superseded syllabuses):** None registered in this work order. Past paper resources were excluded because no acceptable substantive representation could be verified in this retrieval pass.
- **Superseded syllabuses:** none registered; the page and `amendment_report_syll_v1_4.pdf` confirm v1.4 is the current syllabus. Earlier syllabus versions (e.g. 2019 v1.0) are not linked from the current Economics page and are not registered in this work order.
- **Subject reports for prior years (2020–2026) and confirmation resources:** intentionally not registered as separate sources; the QCAA Senior Syllabus Resource Search is the canonical aggregator for prior years and falls outside the bounded Task 5 output domain.

## Representation and Hash Provenance

Per the coordinator hash-policy ruling (`.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`): raw PDF bytes are preferred, but a documented representation retrieved from the official QCAA URL may be hashed when direct retrieval is blocked.

- **SRC-0001 (HTML page):** Content hash computed over the substantive rendered markdown representation retrieved from the official QCAA Economics page through the Jina Reader transport at `https://r.jina.ai/https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/economics` on 2026-09-04. The response was streamed without transformation to `sha256sum`; hash: `sha256:351b50946f3010279cc184d9a3292c3b74dffcec3b9df00b8f187f4ba9f1e2e2`. The rendered content includes syllabus navigation, resource listings and metadata. Direct QCAA retrieval remained Cloudflare-blocked; this substantive rendered representation is the retained evidence.

- **Excluded PDF resources:** The live download endpoints returned HTTP 403 Cloudflare challenges to direct shell tooling, and no substantive representation could be verified for those resources in this pass. They are excluded from the source register and fixture rather than assigned unsupported hashes. This follows the safety rule to prefer fewer valid current records over invalid coverage.

Source-register schema validation: All retained records conform to the `source-register.schema.json` requirements (content_hash pattern `^sha256:[a-f0-9]{64}$`, authority_name enum `QCAA`, verified status, jurisdiction `Queensland`, school_phase `Years 11-12`).

## Retained Source Inventory

Only the independently re-fetched substantive representation is retained in the source register. The invalid PDF records are excluded rather than represented by unsupported hashes.

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| SRC-0001 | current | Economics General senior syllabus (HTML page) | 2025 v1.4 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/humanities-social-sciences/economics |
