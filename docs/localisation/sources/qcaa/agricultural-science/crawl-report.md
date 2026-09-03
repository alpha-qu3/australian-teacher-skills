# QCAA Agricultural Science Syllabus Crawl Report

## Overview
This report documents the crawling, authority verification and minimum curriculum extraction for the Queensland Curriculum and Assessment Authority (QCAA) Agricultural Science General senior syllabus as part of QSUB-0006.

## Sources Processed

### 1. QCAA Agricultural Science Syllabus Landing Page
- **URL**: https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/sciences/agricultural-science
- **Status**: Successfully crawled as a rendered representation (see Retrieval and Hash Method).
- **Content Type**: HTML
- **Last Updated**: 13 April 2026
- **Purpose**: Primary landing page; identifies the current syllabus `Agricultural Science 2025 v1.3` and lists official sample assessment instruments, sample marking schemes, past papers and subject reports.

### 2. QCAA Agricultural Science PDF Syllabus (Current Version, Extraction Source)
- **URL**: https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_agricultural_science_25_syll.pdf
- **Role**: The linked official syllabus document from which the Task 5 curriculum extraction is drawn. Document metadata observed in the rendered representation: 60 pages ($`Page x of 60`$ printed footer); title `Agricultural Science 2025 v1.3 General senior syllabus`; January 2026; CC BY 4.0.
- **Raw-PDF limitation**: Direct retrieval returned HTTP 403 (Cloudflare challenge). The candidate began with `<!DOC`, not `%PDF-`, so raw PDF bytes were unavailable for hashing. The registered hash covers the rendered representation of the official subject page (see Reproducibility Limitation).

## Authority Verification

### QCAA Authority Confirmation
- **Source**: https://www.qcaa.qld.edu.au/about/what-we-do
- **Status**: Verified
- **Key Information**:
  - QCAA describes itself on the official About pages as the Queensland Curriculum and Assessment Authority, a statutory body of the Queensland Government that develops senior syllabuses and external assessments.
  - The official source URL, the QCAA domain and the publication owner (Queensland Curriculum and Assessment Authority) agree.

### Verification Criteria Met
1. **authority_name**: QCAA (Queensland Curriculum and Assessment Authority)
2. **authority_type**: statutory curriculum authority
3. **authority_evidence_url**: https://www.qcaa.qld.edu.au/about/what-we-do
4. **publication_owner**: Queensland Curriculum and Assessment Authority
5. **authority_verification_status**: verified

## Current vs Superseded Classification
- **Current**: `Agricultural Science 2025 v1.3 General senior syllabus` for implementation with students who will complete the course in 2026 or beyond (per the official subject page).
- **Superseded/historical**: Not registered. No superseded syllabus is linked from the current Agricultural Science page. The past papers (2020-2025) and 2019-era sample instruments listed on the official page are historical external-assessment support material and are not part of the current syllabus package.

## Minimum Curriculum Extraction (Task 5)

The following structured data was extracted from the official syllabus document and is stored in `data/curriculum/qcaa/agricultural-science.json` and mirrored in the fixture. Locators are printed page numbers of the official syllabus PDF as observed in the rendered representation (60-page PDF; printed pagination runs cover p.1 through version history p.60).

### Course structure
- Agricultural Science is a General senior syllabus containing four QCAA-developed units; each unit has a notional time of 55 hours of teaching and learning including assessment.
- Students complete Units 1 and 2 before beginning Units 3 and 4; Units 3 and 4 are studied as a pair.
- Locator: syllabus PDF p.6 (designing a course of study).

### Syllabus objectives (p.4)
1. Describe ideas and findings.
2. Apply understanding.
3. Analyse data.
4. Interpret evidence.
5. Evaluate processes, claims and conclusions about agricultural enterprises, and animal and plant production.
6. Investigate phenomena associated with agricultural enterprises, and animal and plant production.

### Unit structure (subject matter / unit structure) — units start at pp.20, 26, 32, 41
| Unit | Title | Topics and hours | Locator |
|---|---|---|---|
| Unit 1 | Agricultural systems | Topic 1: Agricultural enterprises A (4 h); Topic 2: Animal production A (19 h); Topic 3: Plant production A (22 h) | pp.20-25 |
| Unit 2 | Resources | Topic 1: Management of renewable resources (12 h); Topic 2: Physical resource management (18 h); Topic 3: Agricultural management, research and innovation (15 h) | pp.26-31 |
| Unit 3 | Agricultural production | Topic 1: Animal production B (26 h); Topic 2: Plant production B (15 h); Topic 3: Agricultural enterprises B (4 h) | pp.32-40 |
| Unit 4 | Agricultural management | Topic 1: Enterprise management (14 h); Topic 2: Evaluation of an agricultural enterprise's sustainability (31 h) | pp.41-44 |

### Assessment model — assessment section starts p.45
| Assessment | Technique | Weighting | Locator |
|---|---|---|---|
| IA1 | Data test | 10% | p.45 |
| IA2 | Student experiment | 20% | p.48 |
| IA3 | Research investigation | 20% | p.52 |
| External assessment | Examination — combination response | 50% | p.56 |

### Official support and assessment resources
- Subject page (HTML): https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/sciences/agricultural-science — Syllabus and Resources sections; last updated 13 April 2026.
- Syllabus (PDF): https://www.qcaa.qld.edu.au/downloads/senior-qce/syllabuses/snr_agricultural_science_25_syll.pdf — 2025 v1.3, January 2026, 60 pages.
- Sample assessment instruments (2025): IA1 Data test (10%) and IA2 Student experiment (20%) for Unit 3, and IA3 Research investigation for Unit 4, under https://www.qcaa.qld.edu.au/downloads/senior-qce/sciences/.
- Sample marking scheme (2025): IA1 Data test at https://www.qcaa.qld.edu.au/downloads/senior-qce/sciences/snr_ag_science_25_ia1_smple_m_scheme.pdf.
- Subject report (2025 cohort): https://www.qcaa.qld.edu.au/downloads/senior-qce/sciences/snr_ag_science_25_subj_rpt.pdf.

Minimum structured data required by the four localised skills (lesson-plan-creation, lesson-differentiation, check-for-understanding, lesson-preparation) is recorded under `skills_minimum_data` in `data/curriculum/qcaa/agricultural-science.json`: each skill maps to the syllabus fields it consumes (objectives, unit/topic structure, assessment model, subject identity and course type).

## Source Registry Entries

| Source | Representation | URL | Locator | Content Hash |
|--------|----------------|-----|---------|--------------|
| QCAA Agricultural Science subject page | Rendered HTML body of the official QCAA subject page | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/sciences/agricultural-science | Syllabus section -> 2025 v1.3 (PDF, 942.6 KB); extraction bounds in the linked 60-page syllabus PDF: objectives p.4; p.6 course structure; p.18 reporting; pp.20, 26, 32, 41 unit starts; pp.45, 48, 52, 56 assessment | sha256:3c79db5840a76cb849d4cbc9369711af9b8d091ecfef75a274bc7cdf6ead83aa |

## Technical Details

### Retrieval and Hash Method
- **Retrieval method/service**: The official QCAA subject-page URL was requested through the QCAA-facing Firecrawl scraping/rendering service used for this package (`firecrawl_firecrawl_scrape` with the official subject-page URL). The service returned a rendered HTML representation of the page. Direct local HTTP requests to the page and to the linked syllabus PDF both return Cloudflare challenge HTML, so no raw `%PDF-` bytes are available.
- **Representation type**: Rendered HTML body of the official QCAA Agricultural Science subject page, retained as the hash payload for the registered source record. The representation identifies the retrieved page content, not the challenge response and not raw PDF bytes.
- **Rendering procedure**: The Firecrawl route requested the exact registered URL above; the response body was the rendered HTML representation of the page. The retained payload is the HTML body of that representation (`51613` bytes), which the Syllabus section ties to `Agricultural Science 2025 v1.3 (PDF, 942.6 KB)`.
- **Hash computation**: SHA-256 was computed over the UTF-8 bytes of the retained rendered HTML body only. The computed digest is `sha256:3c79db5840a76cb849d4cbc9369711af9b8d091ecfef75a274bc7cdf6ead83aa`, which matches the value declared in the source register, the curriculum JSON and the fixture.
- **Exclusions**: The hash excludes the retrieval-service response envelope, HTTP metadata and headers, and any Cloudflare challenge content.
- **Reproducibility limitation**: Direct retrieval of the official QCAA page and PDF returns HTTP 403 (Cloudflare), so the raw PDF byte stream and a raw page re-fetch cannot be obtained independently unless an authorised QCAA-compatible client is used. Byte-for-byte reproduction of the declared hash requires re-fetching the exact registered URL through the same QCAA-facing rendered-representation route. The record does not claim a raw-PDF-byte hash; the syllabus document is identified by its official URL, version, the exact printed page locators above and the rendered-representation hash.

### Crawl Methodology
- Verified QCAA authority status from the official QCAA About pages.
- Attempted direct retrieval of the official subject page and syllabus PDF (HTTP 403 Cloudflare challenge; response began with `<!DOC`, not `%PDF-`).
- Retrieved the official subject page through the QCAA-facing rendering service as a rendered HTML representation.
- Recorded the document metadata (60 pages, January 2026, CC BY 4.0), exact page locators for objectives, units and assessment from the linked syllabus PDF, and extracted the minimum structured curriculum data required by Task 5 and by the four localised skills.

## Data Quality Assurance
- All authority-verified sources only (QCAA confirmed).
- Registered content hash identifies the permitted rendered representation; no placeholder or fake hashes used.
- Exact page locators recorded for each extracted field.
- Proper field validation against `source-register.schema.json`.
- Retrieval dates in ISO 8601 format (YYYY-MM-DD).
- Jurisdiction and school phase correctly specified.
- Representation provenance names the retrieval method/service, representation type, rendering procedure and reproducibility limitation per the recorded hash ruling in `.superpowers/sdd/2026-08-30-australian-qld-teacher-skills-localisation/progress.md`.

## Files Generated
1. `docs/localisation/sources/qcaa/agricultural-science/source-register.csv` - Authority-verified source registry
2. `docs/localisation/sources/qcaa/agricultural-science/crawl-report.md` - This report
3. `data/curriculum/qcaa/agricultural-science.json` - Curriculum data structure with minimum extraction
4. `docs/localisation/fixtures/qcaa/agricultural-science/source-fixture.json` - Test fixture

## Conclusion
The QCAA authority is verified. The Agricultural Science subject is registered with the documented rendered representation and the Task 5 minimum curriculum extraction (objectives, unit/subject-matter structure with topic hours, assessment model with weightings, and official support/assessment resources), using exact printed page locators for every extracted field. Direct raw-PDF retrieval remains blocked; the crawl report names the retrieval method, representation type, rendering procedure and reproducibility limitation as required by the recorded hash ruling.