# Food & Nutrition Sources Crawl Report

## Identification

| Field | Value |
| --- | --- |
| QSUB ID | QSUB-0037 |
| Subject | Food & Nutrition |
| Subject family | Technologies |
| Course type | General senior syllabus |
| Entry URL | https://www.qcaa.qld.edu.au/senior/senior-subjects/syllabuses/technologies/food-nutrition |
| Retrieval date | 2026-08-30 |
| Current syllabus | Food & Nutrition 2025 v1.3 General senior syllabus (PDF) |

## Authority Verification

| Field | Evidence |
| --- | --- |
| Authority | Queensland Curriculum and Assessment Authority (QCAA) |
| Authority type | statutory curriculum authority |
| Authority evidence | `https://www.qcaa.qld.edu.au/about/governance/legislation` |
| Publication owner | Queensland Curriculum and Assessment Authority |
| Page evidence | The retrieved page metadata identifies QCAA as both `dcterms.creator` and `dcterms.publisher`; its QCAA domain, page identity and authority evidence agree. |
| Status | `verified` |

## Registered Sources

| Classification | Source | Locator |
| --- | --- | --- |
| Current | Food & Nutrition — subject landing page | HTML: `#content`; Syllabus; Resources |
| Current | *Food & Nutrition 2025 v1.3 General senior syllabus* PDF | PDF: cover; pp. 5 (course structure); pp. 7 (complementary skills, Aboriginal/Torres Strait perspectives); pp. 10 (problem-solving process); pp. 11 (reporting standards); pp. 13-14 (food system diagram, objectives); pp. 17-19 (Unit 1 objectives); pp. 22-23 (Unit 3 Topic content) |

The landing page identifies the syllabus as Food & Nutrition General senior syllabus 2025 for implementation with students completing the course in 2026 or beyond. The parsed syllabus supplies the retained structured data: General course type, eight syllabus objectives, four-unit structure, and the Units 1-4 assessment model.

Exact field-level locators for the extracted structured data are recorded in `data/curriculum/qcaa/food-nutrition.json` (`current_syllabus.locator` and per-field `locator` values), not reproduced here.

## Hash Method

- **Retrieval method:** On 2026-08-30, direct HTTP GET requests to each official QCAA URL returned Cloudflare HTTP 403. The same official QCAA URL was then fetched through the Firecrawl-hosted rendering route, which returns a JSON payload of canonical Markdown extracted from the rendered HTML/PDF.
- **Representation type:** The HTML `content_hash` is the SHA-256 of the complete rendered Markdown representation of the QCAA HTML landing page returned by the rendering route. The PDF `content_hash` is the SHA-256 of the complete rendered text/Markdown representation of the QCAA syllabus PDF extracted via the PDF parser path (maxPages bounded to the full document). The recorded values are SHA-256 digests of those retrieved representations, not assertions about raw QCAA HTTP response bytes.
- **Rendering procedure:** Firecrawl retrieves the official QCAA URL server-side, renders the HTML (or for PDFs, parses the PDF text), applies content extraction to produce canonical Markdown, and returns it as structured payloads. The hashes above are computed over the retrieved payload content for reproducibility.
- **Reproducibility limitation:** The Firecrawl rendering and QCAA content can change between requests. Repeating the retrieval method may therefore yield a different representation and hash. Raw-byte SHA-256 values of the original QCAA HTML and PDF byte streams remain unavailable because direct QCAA requests are Cloudflare-protected. A future refresh with approved direct access should re-hash the QCAA-served byte streams and replace the documented representation hashes.

## Licence

- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0), shown on the retained landing page and syllabus PDF.

## Unregistered Fetch Limitations

Direct QCAA fetches for the following official support and historical materials were blocked (HTTP 403 / Cloudflare). No content was accepted, hashed, included in the source register or fixture, or used as a source for the curriculum JSON or behaviour scenarios. Each URL is an official `qcaa.qld.edu.au` resource; they are retained here only as documented page-resolved official locators that failed independent hashing.

- https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_key_subj_changes_ea_26.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/common/snr_qa_confirm_submission_info.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_unit3_ia1_smple_ass_inst.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_unit3_ia2_smple_ass_inst.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_unit4_ia3_smple_ass_inst.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_25_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_24_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_24_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_24_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_23_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_23_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_23_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_22_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_22_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_22_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_21_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_21_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_21_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_20_ea_question_response.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_20_ea_stimulus.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_nutrition_20_ea_mark_guide_pub.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_26_subj_rpt_endorse.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_25_subj_rpt.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_24_subj_rpt.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_23_subj_rpt.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_22_subj_rpt.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_21_subj_rpt.pdf
- https://www.qcaa.qld.edu.au/downloads/senior-qce/technologies/snr_food_20_subj_rpt.pdf

## Classification

- **Current material:** the retained landing page and 2025 v1.3 syllabus PDF.
- **Superseded syllabuses:** none identified from the retained content.
- **Historical external assessment papers and subject reports:** listed above as unregistered fetch limitations, not accepted evidence.
