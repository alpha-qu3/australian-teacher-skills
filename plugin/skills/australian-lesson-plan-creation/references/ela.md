# English — lesson pedagogy

Loaded by `australian-lesson-plan-creation` when the subject is **English**.

## Clarify

Before asking anything, assess the following from all available conversation signals:

**1. Year band.** Determine from year level which band applies:
- **Prep-Year 2**: foundational literacy — phonics/decoding OR read-aloud/comprehension (infer from
  content description; phonics content descriptions for decoding, comprehension content descriptions for read-aloud)
- **Years 3-6**: transitional comprehension
- **Years 7-10**: literary and rhetorical analysis
- **Years 11-12**: sophisticated analysis and argument

**2. Anchor text.** Note whether the teacher has specified a text. If not, select one from
training knowledge appropriate to the year level and content description — or draw from the
curriculum lookup results. Flag any selections in Section 1 as [suggested].

**3. Jurisdiction.** Ask when the year level/course is senior (Years 11-12). The QCAA publishes
specific English syllabuses (English, English Extensions, Literature, etc.). For F-10, the
Australian Curriculum v9.0 applies across Australia with EAL-D provisions.

When key information is missing, ask. Priority: (1) year level if missing, (2) topic or text
if missing, (3) lesson type for Prep-Year 2 if standard doesn't clarify, (4) jurisdiction if
senior years. Infer everything else. Defaults applied silently: 45-60 min (F-2: allow 45 min),
universal access design, Australian Curriculum v9.0 with EAL-D provisions.

---

## Standards grounding

Follow **Step 2 — Ground in Australian content descriptions / QCAA syllabus** in SKILL.md:
use the curriculum_lookup adapter for authority-verified alignment. For F-10 English, look
up the relevant Australian Curriculum content description by year level and strand. For Years
11-12 (Queensland), look up the QCAA English syllabus objective. If not found, proceed from best
knowledge and add the disclaimer footer.

**For F-10:** The Australian Curriculum v9.0 English includes:
- **Interacting with Text** (understanding, interpreting)
- **Expressing and Creating Ideas** (writing, speaking, viewing, reading)
- **Positioning and Personalising Knowledge** (critical, creative thinking)
- **Engaging with Ideas and Texts in Different Media**

Use the proficiency strands (Understanding, Fluency, Problem-solving, Reasoning) across all.

**For QCAA Years 11-12:** Use the appropriate syllabus:
- **English** — general pathway
- **English Extensions** — advanced study
- **Literature** — text analysis focus
- **EAL-D** — support for English learners

---

## Build the lesson

**For all lessons**
Include at least one visual scaffold that appears concretely on the student page — a
`fill_table` organizer or an annotation key — registered in `shared`
and pulled via `from_shared` so the same scaffold
appears in the lesson plan with the teacher-facing rationale beside it.

Be sure that overall timing and timing for each section is realistic — do not overload the lesson.

---

### Year band — apply before drafting

Year band is the primary structural branch. Determine from year level and apply the matching
structure.

---

#### Prep-Year 2: Foundational Literacy

Determine lesson type from the target content description:
- **Phonemes/Blending** — **Lesson Type A: Phonics/Decoding**
- **Reading/Listening** — **Lesson Type B: Comprehension via Read-Aloud**

Both types share a brief phonics review warm-up; they differ in primary focus.

**Lesson Type A — Phonics/Decoding (Phonemes)**

Student-page word work renders as `display: "large"` table grids — big type a child points to
and reads — never as paragraph runs of words. Word lists for a pattern contain only that
pattern plus graphemes already taught; read each word aloud to confirm every letter behaves
as taught. The exit ticket has the child read 3-4 target-pattern words aloud to the teacher
(include one contrast word, e.g. short-a among a_e); dictation words are spoken by the
teacher and never printed on the child's ticket.

Match the lesson's scope to the request: a single-pattern introduction ("a lesson on
magic-e") is a focused 30-40 minute lesson — warm-up on the prerequisite sound, teach the
pattern, guided practice, independent practice, exit ticket — covering ONE pattern (a_e
alone, with the others as later lessons). When the teacher names a whole category
("r-controlled vowels"), the lesson covers the category's distinct sounds — ar, or, and
er/ir/ur treated as one sound, since they are. The full block below is for when the teacher asks
for their complete literacy block.

The cited content description matches the skill taught: a hearing/blending lesson (oral, no print)
cites the phonological awareness content description family, a decoding/spelling lesson
cites phonics — a lesson whose scope says "oral identification only" never carries a
decode-words content description.

Full literacy block (60-80 min, when the teacher asks for their whole block): a typical arc
is Phonological Awareness (oral only, no print) → Phonics (explicit phoneme-grapheme mapping;
decode and spell together; real and nonsense words) → Decodable Practice (connected text
using only patterns already taught plus known high-frequency words) → Read-Aloud (complex,
content-rich text — nonfiction at least half the time; oral text-dependent questions) →
Vocabulary & Discussion (1-2 Tier 2 words) → Shared Writing (co-construct 1-2 sentences) →
Exit Ticket (one word-reading item + one word-spelling item on the target pattern).

**Lesson Type B — Comprehension via Read-Aloud (RL/RI)**

A typical arc: Phonics Warm-Up (5 min, brief review) → Read-Aloud (teacher reads the anchor
text aloud, stopping at planned points for oral text-dependent questions) → Text-Dependent
Discussion (oral think-pair-share; questions progress from general understanding → key
details → vocabulary → simple inference; every student responds) → Vocabulary (1-2 Tier 2
words with definition, context, examples) → Shared Writing (co-construct a written response
using the target words) → Exit Ticket (one oral or simple written comprehension question).

**Non-negotiables for Prep-Year 2:** no three-cueing (no picture, context, or first-letter guessing
to identify words); decodable text for phonics practice, not leveled or predictable text;
read-aloud is instructional — complex, content-rich text chosen deliberately.

---

#### Years 3-6: Transitional Comprehension

A typical arc — scale it to the request: Launch (activate prior knowledge with one focused
prompt; let students grapple with the text fresh) → Close Reading (anchor text at grade-level
complexity, no leveling; first read for gist, second read with an assigned annotation
purpose) → Discussion (all students write before speaking — Think-Write-Pair-Share; questions
progress from general understanding → key details → vocabulary/structure → author's craft) →
Vocabulary (1-2 Tier 2 words with text context; students use them in the writing task) →
Writing Task (text-dependent: "Using evidence from paragraphs ___ and ___, explain how the
author shows..."); opinion in years 3-4, argument with evidence in year 6) → Exit Ticket (one
text-dependent question requiring inference or craft analysis).

**Non-negotiables for 3-6:** complex text for all students — scaffold access through
re-reading, discussion, and vocabulary, never an easier substitute; text-dependent questions
only; write before speaking in every discussion.

---

#### Years 7-10: Literary and Rhetorical Analysis

A typical arc — scale it to the request: Launch (compelling question; brief unshared
quick-write students revisit at the end) → Close Reading (annotate with an assigned
analytical lens — claim development, craft moves, evidence for the central idea; partner
annotation comparison) → Structured Discussion (Think-Write-Pair-Share into whole-class
discussion moving from literal comprehension to analysis; fishbowl or Socratic Seminar for
year 10 or strong groups; debrief discussion quality, not just content) → Vocabulary & Craft
(1 Tier 2 words plus one craft focus — students analyze effect, not just identify) →
Writing Task (claim + evidence + reasoning; model the structure in years 7-8; counterclaim by
year 10) → Formative Check (return to the Launch quick-write: how has your thinking
changed, and what evidence would you cite now?).

**Non-negotiables for 7-10:** analysis, not summary — the task requires an arguable claim the
text must be cited to support; pair a literary text with an informational source where
possible; counterclaim in argument by year 9.

---

#### Years 11-12: Rhetorical Sophistication and Sustained Argument

A typical arc — scale it to the request: Launch (a precise, genuinely arguable question;
students write independently, no discussion yet) → Close Reading (annotate for a specific
analytical lens; multiple reads with different purposes if the passage is short; keep the
complexity — it's the point) → Academic Discussion (student-to-student; teacher probes, does
not direct; Socratic Seminar references specific passages by line; debrief content and
discussion quality) → Craft & Language (one precision craft move; students analyze effect and
intent) → Writing Task (sustained analytical or argumentative response: arguable claim +
textual evidence + analysis; counterclaim by year 11, and rhetorical analysis attends to
audience, purpose, and context) → Formative Check (students assess their own opening
argument: what evidence would you add or revise?).

**Non-negotiables for 11-12:** analysis of *how* and *why*, not just *what* — effect on a
specific audience in a specific rhetorical context; full texts at full difficulty (no
excerpting around hard passages, no summaries in place of originals, no pre-explaining);
counterclaim by year 11, rhetorical analysis attends to audience, purpose, and context.

---

### Section structure — all year bands

1. **At a glance** — content description verbatim in a `special` callout (the ONE verbatim
   quote — everywhere else content descriptions go by code + a short gist); a one-line
   lesson arc naming the phases with minutes so the period's shape is visible before any
   detail; anchor text (title + genre + reference to [suggested] if applicable); materials
   list — name each item plainly (e.g. "Picture cards, 18"), literacy resources
2. **Learning goal** — Big Idea (enduring understanding, 1 sentence tied to the text and unit);
   students will be able to list 3-5 points drawn from curriculum learning goals; prerequisite
   (prior content description by code + gist + 1 sentence on prior knowledge assumed)
3. **Vocabulary & anticipated challenges** — 2-3 Tier 2 target words with definitions and text
   context; 3 misconceptions specific to this text and task, each formatted:
   *What students do* / *Why it happens* / *Teacher move*
4. **Lesson sequence** — phases per year band above; in every phase where students work (reading,
   word work, writing, sorting): 3+ look-fors each naming the specific student behavior, why
   it matters for the content description, and what to do; in every discussion phase: specific
   text-dependent prompts (not generic)
5. **Design notes** — last section, after the exit ticket: 2-3 elements to keep intact when
   adapting, each with a brief reason grounded in the Australian Curriculum's pedagogical
   principles, including the lesson's central representation or routine and its one-sentence
   why.

→ **Section structure complete. Proceed to the draft (when the teacher chose one) or Step 5.**

## Exit ticket guidance

The exit ticket is the last phase in Lesson Sequence (`from_shared:exit_ticket` under its
phase header). One item targeting the hardest inference or application the content description
requires. Prep-Year 2 phonics: word-reading + word-spelling. Prep-Year 2 comprehension: oral
or simple written check. 3-10: text-dependent question requiring evidence; 11-12 may instead
use a return-to-the-Launch-quick-write self-assessment. Three sort buckets (Got it / Almost
there / Needs re-teaching).

---

## Writing lesson.json — English mapping

When you reach Step 5 (Output) in SKILL.md, register English content in `shared` and compose
`documents[]` like this:

- `shared.year_level`; `shared.subject`: `"English"`; `shared.jurisdiction`; `shared.phase`;
  `shared.curriculum`, `shared.curriculum_code`, `shared.curriculum_text`, etc.
- The anchor text or shared writing prompt as `shared.anchor_task`:
  `{teacher: <how to introduce/read it aloud>, student: <the task as the student reads it,
  or null when the launch is purely oral>}`.
- The anchor text itself (if reproduced) as its own key — e.g. `shared.passage`:
  `{type: "source_card", title, author, date, origin, excerpt}`. If the text is teacher-supplied or
  copyrighted, don't reproduce it — the lesson plan names it (title, author, where it lives)
  in Materials and the phase that uses it.
- Each text-dependent question / writing task as `shared.q1`..`qN`:
  `{student: <question>}`. Every question names its target — "Source A", "Source B", or "both
  sources" — a student with two sources in hand can't act on "this source".
- `shared.exit_ticket`: `{student: <prompt>, teacher?: <collection note>}`. The sort
  criteria are a `cards` block you place in the lesson plan after pulling the exit
  ticket (see `example_lesson.json`).
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors` as in the `references/output.md`
  schema.

**Which documents to emit.** A Prep-Year 2 phonemic-awareness or oral-language lesson (content
descriptions on phonemes, phonological awareness) often has **no `student_materials`
document** — students hold response cards or nothing. Say so in the lesson plan's Materials
line and in your message to the teacher. For 3-10 reading/writing lessons, emit
`student_materials`; if the anchor text is reproduced, also emit a `source_packet` document
containing just `from_shared:passage`.

**Student page layout** (when emitted) — start from this and adapt:

```
sections:
  "Before you read"        from_shared:anchor_task ; answer_box if a written prediction
  "Text"                   from_shared:passage   (omit when the text isn't reproduced)
  "Read and respond"       for each question k:
                             group[ {type: from_shared, key: qk, label: "k"},
                                    answer_box ]
                           page_break
  "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
```

**Observation template layout** matches the math layout in `references/math.md`.

---

Copyright 2026 Anthropic, PBC · SPDX-License-Identifier: Apache-2.0