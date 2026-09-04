---
name: australian-lesson-plan-creation
description: >
  Creates a teacher-ready lesson plan, student-facing materials, and observation template for
  Australian classrooms. Load this skill BEFORE asking the teacher any clarifying question about
  year level, subject, topic, curriculum alignment, or timing. Use when an F-12 teacher needs a
  Mathematics, English, Science, or HASS lesson built from scratch — even if year level, subject,
  or topic isn't yet stated. Do NOT load for grading, a rubric, assessment feedback, a quiz, or
  curriculum lookup — answer those directly. Triggers on explicit requests (lesson plan, mini-lesson,
  unit plan, daily plan) and implicit teacher intent: "I'm teaching long division to Year 5 students,"
  "need to teach photosynthesis tomorrow in Science." Core signal: teacher needs new instructional
  content created. A new lesson that asks for differentiated, tiered, or leveled materials is still
  ONE planning request — this skill produces those materials inside the lesson package; do not also
  invoke australian-lesson-differentiation. Not for differentiating an existing lesson
  (use australian-lesson-differentiation) or passage rewrites.
  Requires jurisdiction (Australia or Queensland) and year level/course, learning area/subject
  when alignment is requested. Asks a clarifying question when those are absent.
license: "Copyright 2026 Anthropic, PBC · SPDX-License-Identifier: Apache-2.0"
discovery:
  intents:
    - "lesson plan"
    - "mini-lesson"
    - "unit plan"
    - "daily plan"
    - "teaching"
    - "instructional"
    - "year level"
    - "F-12"
    - "Prep to Year 12"
    - "Australian Curriculum"
    - "QCAA syllabus"
    - "Queensland"
    - "Mathematics"
    - "English"
    - "Science"
    - "HASS"
  subject_signals:
    - "math"
    - "mathematics"
    - "eng"
    - "english"
    - "literacy"
    - "reading"
    - "writing"
    - "science"
    - "hass"
    - "history"
    - "geography"
    - "civics"
  jurisdiction_signals:
    - "Queensland"
    - "Qld"
    - "QCAA"
    - "Australia"
    - "Australian Curriculum"
---

# Australian Lesson Planning (F-12)

Produces a teacher-ready, curriculum-aligned lesson plan + student-facing materials + teacher
observation template as editable Word documents in a single output turn, rendered from one material-source JSON via
bundled scripts.

Each subject has its own pedagogy and output mapping — these live in subject-specific reference files.
This skill uses the curriculum_lookup adapter for alignment to Australian Curriculum v9.0 (F-10, ACARA)
and QCAA senior syllabuses (Years 11-12).

## Authority Selection

This skill branches based on school phase:

| Phase | Authority | Content Type |
|---|---|---|
| Prep-Year 10 | Australian Curriculum v9.0 (ACARA) | Content descriptions / Achievement standards |
| Years 11-12 (Queensland) | QCAA syllabus (by jurisdiction) | Syllabus objectives / Subject matter |

| Jurisdiction | Authority |
|---|---|
| Australia (generic) | ACARA Australian Curriculum v9.0 |
| Queensland | ACARA F-10 + QCAA senior syllabuses |

When alignment is requested, requires:
- **Year level/course** (e.g., "Year 5", "Year 11")
- **Learning area/subject** (e.g., "Mathematics", "English", "History")
- **Jurisdiction** (e.g., "Australia", "Queensland")

If any are missing, ask a concise clarifying question before proceeding.

**"The teacher"** throughout this skill is the user you are talking with — the same person, never
a third party. **"Teacher-facing"** names a document's audience: that user, as opposed to their
students.

---

## Keeping the teacher posted

Once the teacher's path is set (the draft offer answered), say in one or two sentences
what you're about to do (e.g. *"I'll look up the curriculum outcome and pull supporting ideas,
then build your lesson plan, student materials, and observation template."*).

When a task-list or to-do tool is available, also outline this skill's steps there so the
teacher can watch them check off; the only reason to skip this is that no such tool exists
in this conversation.

Teacher language only — name what the teacher is getting, never tool names, file names,
"JSON", or "rendering".

---

## Step 0 — Route (silent, before anything else)

1. **Jurisdiction.** Determine the jurisdiction from conversation signals:
   - **Australia** (generic): Australian Curriculum v9.0 across all states/territories
   - **Queensland**: ACARA F-10 + QCAA Years 11-12 syllabuses

   Ask when absent: *"Is this for Queensland or another Australian state?"*

2. **Subject.** Determine the subject from the prompt:

   - **Mathematics** — arithmetic, fractions, geometry, algebra, statistics
   - **English** — reading, writing, phonics, literature, comprehension, vocabulary, EAL-D support
   - **Science** — phenomena, biological/chemical/physical sciences, Earth and environmental science
   - **HASS** — history, geography, civics and citizenship, economics and business

   Then read the matching reference file NOW:

   - Mathematics → `references/math.md`
   - English → `references/ela.md`
   - Science → `references/science.md`
   - HASS → `references/hass.md`

   **Loading the matching reference file is mandatory.** Drafting a lesson without first
   reading the subject reference is a critical failure. The reference file carries the
   complete subject-specific instructions: clarify priorities, curriculum branching,
   grade-band structures, section structure, non-negotiables, and the lesson.json mapping.
   Treat the loaded reference as your full skill instructions for this turn. If the subject
   is genuinely ambiguous or the prompt spans multiple subjects, ask about it in Step 1.

3. **Curriculum Lookup.** Use the curriculum_lookup adapter for authority-verified alignment:

   ```python
   from curriculum_lookup.lookup import lookup
   result = lookup(
       jurisdiction="Queensland",
       school_phase="F-10",
       year_level="Year 5",
       learning_area="Mathematics",
       code_query=""
   )
   ```

   The adapter returns: official identifier, statement text, source URL, version, authority,
   and mapping confidence. It returns `status: "not-found"` when no match exists — never
   fabricates a code.

---

## Step 1 — Clarify

Read the subject file first — its clarify section defines the priorities and defaults. Ask
at most 2 clarifying questions, chosen by the subject file's priority ranking; apply the
defaults silently for everything else.

The clarify questions and the **draft offer** (*Step 4*) go out together as ONE
structured-question round — the offer is its own question and doesn't count toward the 2.
When nothing needs clarifying, the offer is asked on its own. A second round happens only
when the answers still don't say what the lesson teaches.

---

## Step 2 — Ground in Australian content descriptions / QCAA syllabus

Call `curriculum_lookup.lookup()` with jurisdiction, year level, subject, and any code known.

Extract from the result:
- **official_identifier** (Australian Curriculum content description or QCAA syllabus code)
- **short_text** (the outcome statement)
- **source_url** and **version_or_effective_year** (for citation)
- **authority_name** (ACARA or QCAA)
- **mapping_confidence** (when partial alignment)

**If not connected or not-found:** draft from best knowledge and add this footer to the lesson plan:
*"Generated without curriculum lookup. Align to the relevant Australian Curriculum content description
or QCAA syllabus outcome. Check ACARA (australian-curriculum.edu.au) for F-10 content, QCAA syllabus PDF
for Years 11-12."* Do not fabricate identifiers.

---

## Step 3 — Build the lesson

Follow the subject file's build section: curriculum branching, year-band structure, section
structure, and non-negotiables. Respect the **Copyright guardrail** below — never reproduce
curriculum student-facing text verbatim.

---

## Copyright guardrail

Always write original content. Curriculum materials inform structure, scope, text
selection, phenomenon selection, problem context, and lesson-arc design only — never
reproduce student-facing text, teacher notes, comprehension questions, investigation
prompts, discussion questions, activity narratives, or problem contexts verbatim from
curriculum materials.

If the loaded reference identifies a source curriculum and the teacher is not curriculum-confirmed
for it, never name that curriculum anywhere in the output or in any chat message — not in headers,
footnotes, rationale sections, facilitation notes, or your message presenting the artifacts. The
data informs the design without being cited.

---

## Step 4 — The draft offer

The teacher gets the choice of a fast draft before the build. The offer rides in Step 1's
round (structured question tool when available, chat otherwise), and its two sides are
always the packet and the draft. The wording below lives in the question itself — the
teacher may act on it without reading the chat text around it:

- Question: *Should I build a full classroom-ready packet (lesson plan + student
  materials, as editable Word docs), or do you want to see a quick draft first?*
- Options: **Go ahead and build it** · **Quick draft first** — the lesson at a glance,
  right here in chat

**The full packet is the default.** A reply that selects the draft option or asks to see
the draft gets the draft; every other reply runs Steps 2-3 and goes straight to Step 5.

**The draft (on a yes) is built on Steps 2-3, never instead of them.** Run Step 2 in
full — every lookup call, exactly as written — and Step 3 before sketching anything. A draft
sketched without the Step 2 grounding is a critical failure, the same failure as skipping
the curriculum lookup. Then present the lesson in chat — the draft is chat text only;
rendering happens at Step 5 once the teacher approves. Show:

- one line naming the year level, topic, and the curriculum outcome the lesson is anchored to (identifier plus
  a gist of ten words or fewer);
- a summary of at most 3 sentences (what students do and why it works for this class);
- the sequence as one bullet per phase (name, minutes, one line of what happens);
- the student work at a glance — the actual tasks students will do, enough for the
  teacher to skim and judge coverage;
- what the lesson assumes students already know — the prerequisite knowledge or key
  vocabulary in play — so the teacher can catch a mismatch with where their class is;
- the exit ticket

The draft borrows its names from the documents it previews — phases, tasks, tiers,
and sections are called what the plan will call them.

Afterwards, ask what's next in plain chat — a typed reply can carry the changes themselves,
which a picked option cannot: *"Want anything different? Tell me here — or tell me to go
ahead and I'll create the materials (lesson plan, student materials, and observation
template, as editable Word docs)."*

Apply change requests to the draft in chat and re-present it — changes are quick at this
stage. Step 5 runs in the turn the teacher gives the go-ahead.

---

## Step 5 — Output (one turn)

Runs immediately when the teacher chose the full packet, or in the turn the draft is
approved.

The artifacts are rendered by bundled scripts from **one material-source `lesson.json`**. The JSON
holds a `shared` block (content registered once) and a `documents[]` array (each document
authored as free-form `sections`). A section's `heading` renders as a large title directly
above its blocks; a block's `label` renders as a bold lead-in on the block itself. A label
that repeats its section's heading prints the same words twice in a row — labels carry what
the heading doesn't (the task's name belongs in one of them, not both). You
compose every page — the lesson plan, the student
materials, the observation template, and any others the lesson needs (e.g. a source packet)
— directly in `documents[]`. Anything that appears on more than one page is registered once
in `shared` under a key you choose and pulled into each document with
`{"type": "from_shared", "key": …}`, so the pages cannot drift apart.

Never write layout code, never re-type lesson content into another format, and never edit a
generated document directly — every change goes into `lesson.json` and is re-rendered
(re-rendering is instant). **Do not open, cat, head, or grep the renderer scripts** — their
behavior is fully specified by the commands and output paths in §5a-5e, and
`references/example_lesson.json` is a filled-in worked example. Reading script source tells
you nothing these instructions don't already state.

**Plain language with the teacher.** The machinery above is invisible to the teacher: never
mention JSON, HTML, schemas, scripts, rendering, file names (`lesson.json`), or code in any
teacher-facing message — and never link or name the `.html` files the render command also
writes. Say *"Here's your lesson plan — the student materials and observation template are on
their way"*, not *"I've rendered lesson.json"*. This
applies to every turn: presenting artifacts, the satisfaction ask, revision summaries, and
error messages (if generation fails, say the documents couldn't be created — not that a
script or JSON failed).

Before writing `lesson.json`, read `references/output.md` in full — it carries the hard
requirements for every document (density, consistency, reading level, integrity) and the
complete `lesson.json` schema and block guide (§5a and §5e live there).

### 5b. Render every Word document — one command, same turn

```bash
bash scripts/render_all.sh lesson.json "$OUTPUT_DIR"
```

This writes one editable `.docx` per `documents[]` entry, named by `id` (e.g.
`$OUTPUT_DIR/lesson_plan.docx`, `student_materials.docx`, `observation_template.docx`,
`source_packet.docx`), plus `.html` and `lesson.json` working files. Render straight into
`$OUTPUT_DIR` and leave everything the script writes in place — later revision turns
re-render from the working files even though the teacher only sees the Word documents. Then list `$OUTPUT_DIR`
and confirm every document has both its `.docx` and `.html`; if either is missing or tiny,
rerun the script. Present the Word documents to the teacher together — attach the lesson plan
last so it lands on top (chat surfaces stack newest-first). If there is no `student_materials`
document, say so plainly ("This lesson is oral, so there's no student handout — students will
work with …"). If the script errors, fix `lesson.json` (it is almost always malformed JSON)
and rerun. If file generation fails entirely, say so clearly — do not silently fall back to a
chat-only delivery.

### 5c. The satisfaction ask + iteration options (every output turn)

End the turn with EXACTLY ONE closing message that does three things, in this order:

1. **If Materials names equipment the classroom has that a paper version can stand in
   for** — coins, blocks, dice, a hundred chart — lead with a bolded offer to print it:
   *"**This lesson uses base-ten blocks — want me to make a printable set in case
   yours are short?**"* Anything whose content this lesson wrote — word cards, a
   source excerpt, a sorting mat with this lesson's categories — already ships with
   the package.

2. Asks whether the teacher is satisfied with **every artifact produced** or wants changes —
   e.g. *"Take a look at the lesson plan, student materials, and observation template — anything
   you'd like me to adjust?"* Do not skip the ask.

3. Offers 3–4 high-leverage, **specific** iteration options customized to the subject and
   topic. Do not write "let me know if you want changes" — that's a non-offer. For example,
   for a Year 5 English reading comprehension lesson: *"Would you like to (1) add more scaffolds for
   EAL-D learners, (2) differentiate by proficiency level, or (3) adapt to be specific to
   your state's curriculum outcomes?"*

### 5d. Revisions — one edit, every artifact stays in sync

Make **targeted edits to `lesson.json`**, then re-render every document (instant). Rules that
keep the artifacts consistent:

- If the change touches content registered in `shared` (a problem, a source, the exit ticket,
  vocabulary, look-fors, the phenomenon/context/numbers), edit it **in `shared`** — every
  document that pulls that key updates automatically.
- **Consistency sweep after any context/number/task change:** after editing `shared`, re-read
  every prose block in every `documents[]` entry and update every sentence that still mentions
  the old context, names, or numbers. When you are done, no document may reference the
  replaced content anywhere — stale prose is the most common consistency failure.
- A change aimed at one document (e.g. "more workspace on the worksheet", "add a column to the
  observation grid") goes in that document's `sections` — never by forking a `shared` key into
  two variants.
- Styling: `theme` fields (`primary`, `title_size`, `body_size`) apply to every artifact.
  Artifacts use minimal color so they print cleanly in black-and-white; do not set
  per-section or per-phase colors.

---

## Australian Curriculum Alignment

For F-10 lessons: use Australian Curriculum v9.0 content descriptions and achievement
standards. The curriculum_lookup adapter returns these with authority citation.

For Years 11-12 (Queensland): use QCAA senior syllabuses. Each subject has specific
learning objectives and assessment objectives. The curriculum_lookup adapter returns
QSUB IDs and syllabus language when available.

**Do not call lesson-plan outcomes "standards" generically.** Use:
- "Australian Curriculum content description" for F-10
- "QCAA syllabus objective" for Years 11-12
- "Achievement standard" for F-10 benchmarks
- "Assessment objective" for senior assessments

---

## Step 6 — Output schema with curriculum metadata

The lesson.json includes curriculum provenance:

```json
shared:
  year_level: "Year 5"
  subject: "Mathematics"
  jurisdiction: "Queensland"
  phase: "F-10"
  curriculum: "Australian Curriculum v9.0"
  curriculum_code: "AC9M5N02"
  curriculum_text: "Multiply and divide by one-digit numbers, recalling multiplication facts..."
  curriculum_source_url: "..."
  curriculum_version: "v9.0"
  curriculum_mapping_strength: "direct"
```

For QCAA senior subjects:
```json
shared:
  year_level: "Year 11"
  subject: "Mathematics A"
  jurisdiction: "Queensland"
  phase: "Years 11-12"
  curriculum: "QCAA Mathematics A Syllabus"
  curriculum_code: "QSUB-0052"
  curriculum_text: "Functions and other basic mathematical concepts..."
  curriculum_source_url: "..."
  curriculum_mapping_strength: "authority-verified"
```

Copyright 2026 Anthropic, PBC · SPDX-License-Identifier: Apache-2.0