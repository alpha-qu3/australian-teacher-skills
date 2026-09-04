# Australian curriculum lookup adapter — australian-check-for-understanding

Used by Step 2 **only when the lookup returns `"found"`**; otherwise follow SKILL.md's not-connected
branch. Every lookup runs **before any item is designed**, and no raw results reach chat.

---

## Resolving the curriculum focus

1. **Infer the learning area and authority** from the topic and year level:
   - Learning area: Mathematics, English, Science, HASS, etc.
   - Authority: ACARA (F–10) or QCAA (Years 11–12) based on jurisdiction and school phase.
2. **Call the curriculum lookup adapter:**
   ```python
   lookup(jurisdiction=<str>, school_phase=<str>, year_level=<str>, learning_area=<str>)
   ```
   with:
   - `jurisdiction`: `"Australia"` (F–10) or `"Queensland"` (Years 11–12)
   - `school_phase`: `"F-10"` or `"Years 11-12"`
   - `year_level`: e.g. `"Year 5"`, `"Year 11"`, `"Year 12"`
   - `learning_area`: e.g. `"Mathematics"`, `"English"`, `"Science"`, `"Humanities and Social Sciences"`
3. **Nothing returned:** if the lookup returns `status: "not-found"` — see Step 2's not-connected
   branch and gap register GAP-004. Never retry with keywords or manufacture a code.
4. **`raw_entry` present:** when `status: "found"`, the `raw_entry` field contains the authority-
  verified curriculum manifest entry. Extract:
   - **`official_identifier`** — the curriculum authority's official code or title
   - **`authority`** — `"Australian Curriculum v9.0"` or `"QCAA General Senior Syllabus"`
   - **`version_or_effective_year`** — e.g. `"9.0"`
   - **`short_text`** — the learning area and band (e.g. `"Mathematics > Year 5"`, `"Science > Year 11"`)
   - **`source_url`** — the authority URL (ACARA or QCAA)
   - **`authority_verification`** — includes evidence URL, status, publication owner, licence

Store the **verbatim statement** from `official_identifier` and `short_text` (never paraphrased),
the **`authority`** and **`version_or_effective_year`**, and the full `raw_entry`. Confirm it
matches what the teacher asked for.

---

## Find misconceptions and guidance (where available)

Where the authority-verified source returns documented student errors (ACARA misconception research
or QCAA subject reports), those **errors** drive distractor design and the **guidance** turns
"revisit prior-band content" into a named sub-skill or task type.

Prioritize the errors most relevant to the **confirmed learning component** rather than to the
curriculum focus as a whole. If fewer than three authority-verified errors are relevant for the
learning area (per gap register GAP-001), fill the remaining slots from your own knowledge;
never manufacture a documented error. Record for each whether it is a **prerequisite gap**
or an **on-band confusion**.

**Attribution:** none of these sources — ACARA, QCAA, NCCD, Queensland Education — is named in
either file or in any chat message (SKILL.md's data-use guardrail). The data informs the design
internally only.

---

## Curriculum lookup adapter complete

Proceed to Step 3's focus proposal (or Step 4 if it is confirmed).