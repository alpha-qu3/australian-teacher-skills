# Mathematics — lesson pedagogy

Loaded by `australian-lesson-plan-creation` when the subject is **Mathematics**.

## Clarify

Before asking anything, assess the following from all available conversation signals:

**1. Year level and curriculum detection.** Determine the year level (Prep, Year 1-12). For
F-10, the default curriculum is the Australian Curriculum v9.0 (Mathematics, ACARA). For Years
11-12 in Queensland, the QCAA Mathematics syllabuses apply (General Mathematics, Mathematical
Methods, Specialist Mathematics, Essential Mathematics, Numeracy). If the teacher names a
specific curriculum or syllabus, use it; otherwise apply the authority-selection branch
(SKILL.md §Authority Selection).

**2. Proficiency strands.** The Australian Curriculum v9.0 Mathematics is organised around four
proficiency strands: Understanding, Fluency, Problem-solving, and Reasoning. These are used
across all year levels and should be reflected in the lesson design.

When key information is missing, ask. Priority: (1) year level if missing, (2) topic if
missing, (3) jurisdiction if not inferable (Australia or Queensland). Infer everything else.
Defaults applied silently: 45-60 min, universal access design, Australian Curriculum v9.0.

---

## Standards grounding

Follow **Step 2 — Ground in Australian content descriptions / QCAA syllabus** in SKILL.md:
use the curriculum_lookup adapter for authority-verified alignment. For F-10 Mathematics, look
up the relevant Australian Curriculum content description by year level and strand. For Years
11-12 in Queensland, look up the QCAA syllabus objective. If not found, proceed from best
knowledge and add the disclaimer footer.

---

## Build the lesson

**For all lessons**
Include at least one visual scaffold registered in `shared` (a `data_table`, `number_line`,
or `fill_table` organizer) and pulled into the lesson plan with the
teacher-facing rationale beside it. Whether it also appears on the student page depends on
what it is: a blank `fill_table` students complete or a `number_line` they mark belongs on
the worksheet; a worked reference table that shows the operation or answer structure is
teacher-only — printing it gives away the thinking.

Be sure that overall timing and timing for each section is realistic — do not overload the lesson.

### Year-band structure — apply before drafting

The Australian Curriculum organises Mathematics by year level with content descriptions grouped
into strands (Number, Algebra, Measurement, Space, Statistics, Probability). Proficiency strands
(Understanding, Fluency, Problem-solving, Reasoning) apply across all content.

- **Prep-Year 2**: Concrete counting and additive thinking — Explore must include at least one
  start-unknown and one change-unknown problem; for add/subtract story-problem content the set
  spans all four situation types (add-to, take-from, put-together/take-apart, compare); exit
  ticket must target start-unknown or change-unknown; no strategy modeling before student
  attempt; the visual model students use (part-part-whole diagram, number bond, drawing) appears
  in the materials themselves — on the worksheet or anchor chart — not as an offer
- **Years 3-6**: Problem-based, gradual release; array/area models in Discuss
- **Years 7-8**: Problem-based; ratio tables, double number lines, coordinate graphs
- **Years 9-10**: Mathematical modelling; formalize notation in Synthesize, not Launch
- **Years 11-12 (QCAA)**: Apply the QCAA syllabus structure for the specific Mathematics subject
  (General Mathematics, Mathematical Methods, Specialist Mathematics, Essential Mathematics,
  Numeracy). Use the QCAA syllabus objectives and subject matter as the alignment basis.

### Problem set — structural variety is required, not optional

Before writing the practice problems (`shared.p1`..`pN`), ENUMERATE the content description's
structural cases — the full span from the baseline case (the one every student must clear) to
the structurally hardest case (the one students most often get wrong: start-unknown for Prep-2
story problems; a product smaller than both factors for decimal multiplication; the missing-leg
case for the Pythagorean theorem; a midpoint or just-below-boundary number for rounding; a
linear-but-not-proportional relationship for proportionality; and so on for other content
descriptions). Then write the set so EVERY enumerated case is a numbered, required problem (or
the exit ticket), with its case named in that problem's `teacher` facet.

Coverage rules:
- A structural case that appears only in prose — the SWBAT, an anticipated challenge, a
  teacher move, or the Discuss notes — does NOT count as covered. If the plan's prose names
  a case, a numbered problem must present it to students.
- Emphasizing the hardest case never licenses dropping the baseline case: a set of all-hard
  problems fails coverage exactly as a set of all-easy ones does.
- The content description's number domain is part of the variety: if the content description
  or SWBAT says rational numbers, at least one required problem uses fractions or decimals —
  whole-number-only sets do not cover it.
- Never relegate a required structural case to an optional extension or bonus — if it only
  appears as a challenge add-on, most students never meet it.
- State once which problem carries each case (exit ticket included) — a coverage gap
  should be visible at a glance, to you and to the teacher.

### Section structure — all year bands

1. **At a glance** — content description verbatim in a `special` callout (the ONE verbatim
   quote — everywhere else content descriptions go by code plus a short gist); a one-line
   lesson arc naming the phases with minutes ("Launch 8 → Explore 15 → Discuss 12 → Synthesize
   5 → Exit 5") so the period's shape is visible before any detail; materials — name each item
   plainly (e.g. "Number cards 0-20"); proficiency strands named
2. **Learning goal** — Big Idea (enduring understanding, 1 sentence); SWBAT; Prerequisite
   (prior content description by code + one plain sentence on what students can already do
   and how today builds on it)
3. **Vocabulary & anticipated challenges** — 3-5 key terms with brief definitions; 2-3
   misconceptions each as: *What students do* / *Why it happens* / *Teacher move*
4. **Lesson sequence** — phases per year band above; **Discuss gets at least 10 minutes**
   (in a short warm-up-style request, shrink the other phases, not Discuss); in Explore:
   3+ look-fors each naming the student response, why it matters, and what to do with it —
   and if the anchor task admits more than one correct response or equation, one look-for
   must say so explicitly so the teacher accepts all of them; in Discuss: at least one named
   student-to-student talk move (Think-Pair-Share, Turn-and-Talk, partner compare,
   agree/disagree) + specific discourse prompts (not generic)
5. **Design notes** — last section, after the exit ticket: 2-3 elements to keep intact when
   adapting, with brief reasoning, including the lesson's central representation (the visual
   or model students work with) and its one-sentence why. Rationale lives here, after the
   teaching path — a teacher prepping reads the arc first, the reasoning second.

## Exit ticket guidance

The exit ticket is the last phase in Lesson Sequence (`from_shared:exit_ticket` under its phase header).

- It IS the **structurally hardest enumerated case** (from the problem-set enumeration above;
  Prep-2: start-unknown or change-unknown), never a mid-difficulty stand-in. Pick it with the
  **misconception test**: a student who holds the lesson's primary anticipated misconception
  must get the exit ticket WRONG. If that student would get it right, you picked an affirming
  instance — swap it for the discriminating one. Name the case in `shared.exit_ticket.teacher`.

- **Verify the exit ticket and every answer key by working the problem**: the stated answer is
  the one the problem actually produces, and the operation count matches the content description.

- 3 sort buckets — *Got it* / *Almost there* / *Needs re-teaching* — **each with explicit
  criteria** describing what a response in that bucket contains (e.g. "Got it: correct equation
  with the unknown where it lives in the story", not the bare label); all three criteria appear
  in the lesson plan, never truncated to labels.

---

## Writing lesson.json — Mathematics mapping

When you reach Step 5 (Output) in SKILL.md, register Mathematics content in `shared` and
compose `documents[]` like this:

- `shared.year_level`: e.g. `"Year 5"`; `shared.subject`: `"Mathematics"`; `shared.jurisdiction`:
  e.g. `"Queensland"`; `shared.phase`: e.g. `"F-10"`; `shared.curriculum`: e.g.
  `"Australian Curriculum v9.0"`; `shared.curriculum_code`: the content description code
  (e.g. `"AC9M5N02"`); `shared.curriculum_text`: the content description verbatim;
  `shared.curriculum_source_url`: the ACARA/QCAA source URL; `shared.curriculum_mapping_strength`:
  `"direct"`, `"contextual"`, or `"pending-reviewer"`.
- `shared.anchor_task`: `{teacher: <launch script + facilitation note>, student: <the task as
  the student reads it, second person>}`.
- Each practice problem as its own key — `shared.p1`..`pN`: `{student: <prompt text>}`,
  optionally `{teacher: <what to watch for on this item>}` and `stimulus: [blocks]` (a
  `data_table` the problems share, a `number_line`, etc.). A shared data set used by several
  problems can be its own key (e.g. `shared.prices_table`) and pulled once before the set.
- Register the visual scaffold as its own `shared` key (e.g. `shared.hundreds_chart`,
  `shared.prices_table`, `shared.tape_diagram`) — a `data_table`, `number_line`, or
  `fill_table` block — and pull it into the lesson plan next to the rationale. Pull it onto
  the student page only when it is something students work with (a blank organizer, a number
  line to mark, the data set the problems analyze); a worked reference table the teacher
  uses to structure the mini-lesson stays teacher-side.
- `shared.exit_ticket`: `{student: <prompt — a fresh item, never a duplicate of a practice
  problem>, teacher: <collection note>}`. The sort criteria are a `cards` block you place in
  the lesson plan after pulling the exit ticket (see `example_lesson.json`).
- `shared.vocabulary`, `shared.misconceptions`, `shared.look_fors`: register each as the
  block you want rendered (a `table` for misconceptions, a `list` for look-fors) — there is
  no special-case rendering by key name.

**Student page layout** (the `id: "student_materials"` document) — start from this skeleton
and adapt:

```
sections:
  "<warm-up heading, kid-facing>"  group[ from_shared:anchor_task, answer_box ]
  "<practice heading>"     optional callout(student-note) — a brief reminder, only when one helps
                           from_shared:<visual-scaffold key>   ← only when it is something
                             students work with (blank fill_table, number_line, the data
                             set the problems analyze) — a worked reference table is
                             teacher-only
                           for each problem k:
                             group[ {type: from_shared, key: pk, label: "k"},
                                    answer_box (bare -- it sizes to the year band;
                                    ruled: true when the answer is composed sentences) ]
                           on the ONE problem whose hard part is the writing move, its
                             group also carries the sentence support -- plain text before
                             the answer_box (see Sentence supports in `references/output.md`)
                           page_break
  "<exit heading, kid-facing>"     group[ from_shared:exit_ticket, answer_box ]
```

**Observation template layout** (the `id: "observation_template"` document):

```
sections:
  "How to use this"        one-paragraph instructions
  "Look-fors"              from_shared:look_fors
                           fill_table headers=[Student, Strategy seen, Next step] blank_rows=8
  "Anticipated challenges" from_shared:misconceptions
  "Exit-ticket sort"       from_shared:exit_ticket
```

Worked example: `references/example_lesson.json`.

---

Copyright 2026 Anthropic, PBC · SPDX-License-Identifier: Apache-2.0
