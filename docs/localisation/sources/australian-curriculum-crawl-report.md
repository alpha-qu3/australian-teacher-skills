# Australian Curriculum Version 9.0 Crawl Report

**Retrieved:** 2026-08-30  
**Root:** https://www.australiancurriculum.edu.au/  
**Scope:** Australian Curriculum Version 9.0, Foundation to Year 10

## Authority and Version

- **Authority:** Australian Curriculum, Assessment and Reporting Authority (ACARA), a statutory curriculum authority.
- **Authority evidence:** https://www.acara.edu.au/about-us. ACARA identifies itself as an "independent statutory authority" and says it developed the Australian Curriculum.
- **Publication owner:** Australian Curriculum, Assessment and Reporting Authority (ACARA). The curriculum site's copyright page identifies ACARA as the owner of the website material.
- **Current status:** The Version 9.0 F-10 overview says education ministers approved Version 9.0 in April 2022, replacing Version 8.4. The site title is "Home | V9 Australian Curriculum".
- **Version distinction:** Version 9.0 is served at `www.australiancurriculum.edu.au` and interactive content at `v9.australiancurriculum.edu.au`; Version 8.4 is archived at `v8.australiancurriculum.edu.au`. Work Studies remains a Version 8.4-only exception and is not registered as Version 9.0 content.

## Registered Coverage

| Coverage class | Registered records | Hierarchy captured |
|---|---:|---|
| F-10 learning areas | 8 | Learning area > name > Structure |
| General capabilities | 1 | F-10 Curriculum > General capabilities > seven capabilities |
| Cross-curriculum priorities | 1 | F-10 Curriculum > Cross-curriculum priorities > three priorities |
| Student diversity | 2 | EAL/D students; students with disability |
| Retrieval, licence and structured-data support | 2 | MRAC; copyright and terms |

The eight learning areas are English, Mathematics, Science, Health and Physical Education, Humanities and Social Sciences, The Arts, Technologies and Languages. The general-capabilities record identifies the official seven-capability hierarchy; the cross-curriculum-priorities record identifies the official three-priority hierarchy. No curriculum content descriptions or achievement-standard text has been reproduced.

## Structured Data and Runtime

- **Structured source:** ACARA's Machine-readable Australian Curriculum (MRAC) Version 9.0 page: https://www.australiancurriculum.edu.au/machine-readable-australian-curriculum.
- **Published formats:** RDF/XML, JSON-LD and SPARQL; linked downloads are hosted by Scootle. The page says files were updated 7 June 2024.
- **Access and runtime:** The MRAC landing page and its download link were public during retrieval. ACARA documents files/downloads, not an authenticated live curriculum API; a consumer should use versioned downloads or explicitly handle an unavailable remote source.
- **Licence:** Website curriculum material is CC BY 4.0 unless indicated otherwise. The copyright page excludes logos, trade marks, website design, photographs, videos and some teacher-support resources; National Literacy Learning Progressions are CC BY-NC 4.0. First Nations content remains subject to ICIP protocols.

## Crawl and Re-fetch Results

The final bounded re-fetch used `curl --location`, HTTP status 200, and SHA-256 over each retrieved response body. The result is recorded in the CSV and JSON manifest. The canonical and effective URLs matched for every registered record.

| Result | Count |
|---|---:|
| Successful registered URLs | 14 |
| Source records | 15 |
| Redirects observed | 0 |
| PDFs registered | 0 |
| Parse failures | 0 |
| Re-fetch failures | 0 |
| Retries | 1 tooling retry only; no source URL was retried |

One tooling attempt failed before requesting a URL because zsh reserves the name `status`; it was corrected to `http_code`. It is not a source failure or a retry of an ACARA URL.

## Gaps

- No authority-verified NCCD or Queensland Department of Education record is included: ACARA's EAL/D and disability pages provide the permitted ACARA guidance collected in this task. Task 6 should add an authority-verified NCCD or Queensland Department of Education source only if a proposed mapping needs guidance not available from these ACARA records.
- Version 8.4 Work Studies has no Version 9.0 equivalent and is intentionally outside this Version 9.0 register.

## Validation Summary

- All 14 source records omit `source_id`; Task 6 assigns final `SRC-####` values.
- Every row has the schema-required authority fields, jurisdiction, phase, title, version, URL, locator, licence, retrieval date and a real response-body SHA-256.
- CSV and JSON manifest have identical records and cover all eight F-10 learning areas and the three curriculum dimensions.
