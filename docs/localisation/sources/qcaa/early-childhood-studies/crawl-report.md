# Early Childhood Studies — QCAA Source Registration

## Identification

| Field | Value |
| --- | --- |
| QSID | QSUB-0025 |
| Subject slug | `early-childhood-studies` |
| Subject family | Health and Physical Education |
| Course type | Applied |
| Official page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/health-physical-education/early-childhood-studies |
| Worktree | `.kilo/worktrees/qcaa-early-childhood-studies-sources-v2` |
| Branch | `qcaa-early-childhood-studies-sources-v2` |
| Base commit | `281eb8d` (pinned upstream SHA) |
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
| Verification evidence | The official QCAA Legislation page states that "The QCAA's functions and powers are set out in the *Education (Queensland Curriculum and Assessment Authority) Act 2014* and *Education (Queensland Curriculum and Assessment Authority) Regulation 2025*". The subject page is served on the `qcaa.qld.edu.au` domain, displays the QCAA organisational branding and footer ("© State of Queensland (Queensland Curriculum and Assessment Authority) 2026"), and the current syllabus PDF carries document metadata `author=Queensland Curriculum and Assessment Authority`. The domain, page publisher and authority evidence agree; the record is `verified`. Catalogue authority verification (Task 4) for QCAA applies unchanged. |

## Source Inventory

| Source ID | Status | Document title | Year/version | URL |
| --- | --- | --- | --- | --- |
| SRC-0001 | current | Early Childhood Studies Applied senior syllabus (HTML page) | 2024 v1.2 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/health-physical-education/early-childhood-studies |
| SRC-0002 | current | Early Childhood Studies 2024 v1.2 Applied senior syllabus PDF | 2024 v1.2 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_early_childhood_24_app_syll.pdf |

Additional page-resolved official locators (not separately hashed, per minimum-extraction rule):

| Resource | Locator |
| --- | --- |
| Sample assessment instrument: B1 — Investigation: Play-based activity (numeracy) (PDF, 153.4 KB) | https://www.qcaa.qld.edu.au/downloads/senior-qce/hpe/snr_early_childhood_24_app_smple_ass_inst_b1_invest.pdf |
| Sample assessment instrument: B2 — Project: Play-based activity (literacy) (PDF, 168.2 KB) | https://www.qcaa.qld.edu.au/downloads/senior-qce/hpe/snr_early_childhood_24_app_smple_ass_inst_b2_proj.pdf |
| Senior syllabus resource search (aggregator for other option/assessment resources) | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabus-implementation/senior-syllabus-resource-search |

## Current vs Superseded Classification

- **Current syllabus material:** SRC-0001 (subject page; "Early Childhood Studies Applied senior syllabus 2024 — for implementation with students who will complete their study of the course in 2025 or beyond") and SRC-0002 (*Early Childhood Studies 2024 v1.2* syllabus PDF, 53 pages, dated January 2026 in-document). The syllabus version history confirms v1.2 is the current edition.
- **Current support resources:** the two 2024 sample assessment instruments published on the subject page (Option B, assessments B1 and B2) are page-resolved locators only.
- **Superseded editions of the same syllabus:** v1.0 (January 2023, released for familiarisation and planning) and v1.1 (August 2023, released for implementation with minor updates) are recorded in the v1.2 syllabus version history but are not linked from the current subject page; per the subject-package precedent they are not registered as separate source records.
- **Historical external assessment papers:** not applicable and none registered — Early Childhood Studies is an Applied senior syllabus and has no external assessment.
- **Superseded syllabuses from earlier QCAA programs:** none linked from the current page and none registered in this work order.

## Representation and Hash Provenance

Per the coordinator hash-policy ruling (`.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`): raw PDF bytes are preferred, but a documented retrieval/rendering representation retrieved from the official QCAA URL may be hashed when direct retrieval is blocked. Direct `curl` and webfetch requests to `qcaa.qld.edu.au` in this environment returned HTTP 403 Cloudflare challenge pages; the webfetch tool also returned a byte-mangled PDF payload whose streams fail zlib decompression, so no raw-PDF-byte hash is claimed.

| Source ID | Official URL | Retrieval method | Representation type | Rendering procedure | Hash basis | Hash | Reproducibility limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-0001 | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/health-physical-education/early-childhood-studies | jina Reader service (`r.jina.ai`) via webfetch | renderer-markdown of the live page | jina Reader markdown rendering of the official URL; 44,184 bytes; reference snapshot preserved at `/tmp/kilo/ecs_page_rjina.md` during this work order | SHA-256 of the retained renderer-markdown | `sha256:c6b1e6e73506bcd1266451b36c3373b2ea26942fff56a75c651788e5327bc011` | Authenticates the retained rendering, not a claimed QCAA-server byte stream; direct `curl`/webfetch to `qcaa.qld.edu.au` returned HTTP 403 Cloudflare challenge pages |
| SRC-0002 | https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_early_childhood_24_app_syll.pdf | jina Reader service (`r.jina.ai`) via webfetch | renderer-markdown of the official syllabus PDF URL | jina Reader markdown rendering of the PDF URL; renders all 53 pages including title block, licence/attribution notice, objectives, unit options, assessment instruments and version history; 94,547 bytes; reference snapshot preserved at `/tmp/kilo/ecs_pdf_jinamd.md` during this work order | SHA-256 of the retained renderer-markdown | `sha256:23ea1845c06530914ff072bbeb4fbbd5d404931beee68e7af4938799ba838085` | Authenticates the retained rendering, not a claimed QCAA-server byte stream; direct `curl`/webfetch to `qcaa.qld.edu.au` returned HTTP 403 Cloudflare challenge pages; the webfetch tool also returned a byte-mangled PDF payload whose streams fail zlib decompression, so no raw-PDF-byte hash is claimed |

## Source Schema Conformance Notes

- Both records use the columns defined in `source-register.schema.json` (authority, type, evidence URL, publication owner, verification status, jurisdiction, phase, learning area, title, version, URL, locator, licence, retrieval date, content hash) plus a `status` column, mirroring the economics/accounting package precedent.
- `content_hash` values follow the canonical `sha256:<hex>` pattern.
- All `authority_name` values are `QCAA` and all `authority_verification_status` values are `verified`.
- `source_id` is not emitted in the CSV (Task 6 assigns stable `SRC-####` IDs); the report labels rows SRC-0001/SRC-0002 for traceability only.

## Minimum Subject Matter / Objectives / Assessment Data

The `data/curriculum/qcaa/early-childhood-studies.json` contains the minimum required curriculum extraction:

- **Objectives (4):** investigate the fundamentals and practices of early childhood learning; plan learning activities; implement learning activities; evaluate learning activities (syllabus objectives, p. 3).
- **Course structure / unit options (6):** Option A Play and creativity; B Literacy and numeracy; C Children's development; D Children's wellbeing; E Indoor and outdoor environments; F The early childhood education and care sector. Schools select and order four 55-hour units from the six options; Units 1 and 2 precede the Unit 3/4 pair.
- **Assessment model:** Applied syllabus — units 1 and 2 use at least two but no more than four teacher-developed assessments; units 3 and 4 use four assessment instruments defined in the syllabus, following each selected option's Investigation (X1) and Project (X2) play-based activity instruments. No external assessment.
- **Source locators:** main page, current syllabus PDF, B1 and B2 sample assessment instrument URLs, and the resource-search aggregator are recorded in `source_locators`.

## Gaps / Unresolved Items

1. Raw PDF byte SHA-256 for `snr_early_childhood_24_app_syll.pdf` is not claimed because direct QCAA retrieval is Cloudflare-blocked in this environment and the webfetch PDF payload failed zlib validation. A follow-up must re-fetch the PDF through an authorised QCAA-compatible client and replace SRC-0002 with the raw-byte hash before a byte-level integrity guarantee is required. The page catalogues the file as 690.0 KB while the retained rendering covers a 53-page document dated January 2026; the catalogue entry pre-dates the 16 December 2025 file modification and may be stale.
2. Only the two Option B sample assessment instruments are published on the current subject page. The senior syllabus resource search is the canonical aggregator for the remaining options (A, C–F) and is referenced but not registered as a source.
3. Superseded editions v1.0 and v1.1 are known only from the v1.2 version history; they were not retrieved or hashed. Register as separate historical records only if Task 6 mappings require them.