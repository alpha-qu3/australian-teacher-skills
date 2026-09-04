# QCAA Senior Syllabus Catalogue Crawl Report

## Scope and Method

- Retrieval date (UTC): `2026-08-30`
- Catalogue root: `https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses`
- Inclusion rule: every unique subject-detail link presented on the live index in the General, Applied or Short Course navigation lists.
- Classification method: after authority verification, course type and subject family were read from the QCAA-owned index navigation labels; individual subject details and documents were not retrieved, preserving the Task 5 one-subject-per-agent boundary.
- Accepted catalogue-data domains: `www.qcaa.qld.edu.au` only.
- Rejected non-QCAA sources: none were used or accepted for catalogue data.

## Authority Verification

| Field | Recorded value |
| --- | --- |
| Authority name | Queensland Curriculum and Assessment Authority (QCAA) |
| Authority type | statutory curriculum authority |
| Publication owner | Queensland Curriculum and Assessment Authority |
| Authority evidence URL | https://www.qcaa.qld.edu.au/about/governance/legislation |
| Authority-verification status | verified |
| Verification evidence | The official QCAA Legislation page states that QCAA's functions and powers are set out in the *Education (Queensland Curriculum and Assessment Authority) Act 2014* and the *Education (Queensland Curriculum and Assessment Authority) Regulation 2025*. The authority page and the syllabus index both identify Queensland Curriculum and Assessment Authority as their publisher; their `qcaa.qld.edu.au` domain and publication owner agree. |

## Crawl Results

### Successful Pages

| URL | HTTP status | Result |
| --- | --- | --- |
| https://www.qcaa.qld.edu.au/about/governance/legislation | 200 | Verified QCAA statutory authority, functions and powers, and publication ownership. |
| https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses | 200 | Parsed 78 unique subject-detail links and their QCAA navigation course-type and subject-family labels after authority verification. |

### Skipped Pages

| Pages | Count | Reason |
| --- | ---: | --- |
| Individual QCAA subject-detail pages referenced by the live index | 78 | Intentionally not fetched. Task 5 assigns each subject page and its supporting resources to exactly one subject agent; fetching them here would start prohibited subject-level crawls. Each URL is registered in `qcaa-subject-index.csv` and its matching work order. |

### Parse Failures

| URL | Failure | Outcome |
| --- | --- | --- |
| None | No QCAA page parse failed. | Not applicable |

### Retry Results

| Target | Retry attempts | Outcome |
| --- | ---: | --- |
| None | 0 | No QCAA HTTP retrieval or parse failure required a retry. |

## Live-Index Reconciliation

| Course type | Live-index links | Registered index rows | Matching work orders |
| --- | ---: | ---: | ---: |
| General | 48 | 48 | 48 |
| Applied | 25 | 25 | 25 |
| Short Course | 5 | 5 | 5 |
| Total | 78 | 78 | 78 |

Reconciliation outcome: **pass**. Each unique current syllabus link from the supplied live QCAA index is registered exactly once with an official QCAA URL and one independently dispatchable work order. Business and Food & Nutrition are independent orders marked `deep-validation: true`.
