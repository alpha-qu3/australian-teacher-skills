# Mathematics — australian-check-for-understanding

Your full instruction set for the build (SKILL.md Step 4).

---

## 1. Aspect of rigor

The curriculum focus's own achievement standards and proficiency strands settle it —
*understand, describe, explain* → **conceptual**; *use, apply, solve* → **procedural**;
*model, use mathematics in context* → **application**; spanning two → **Mixed**, saying
which item covers which. Label it in the meta block; it drives item format, representation,
and what a good distractor looks like.

These strands map to the v9 Australian Curriculum generalising the US "rigor" framework:
- **Conceptual** — understanding, fluency (conceptual), problem-solving (understanding)
- **Procedural** — fluency (procedural), low-stakes problem-solving
- **Application** — problem-solving (modelling), statistics and probability investigation

---

## 2. Map documented errors to stem features

Build this map from authority-verified Australian sources returned in Step 2, or from your own
well-grounded knowledge where no such source is available (see gap register GAP-001). For each:
*what would a student reasoning this way do here, and what must the stem contain to give them
the chance?*

| Error pattern | Prerequisite gap or on-band? | Stem feature needed |
|---|---|---|
| [pattern] | [which] | [what must appear in the stem] |

Internal working; it appears in neither file. **A distractor invented after the stem was
written comes out merely wrong rather than plausible**, and discriminates nothing.

---

## 3. Item design

Write 1–3 items; one that discriminates beats three that don't.

| Rigor | Format |
|---|---|
| **Conceptual** | MC, multiple select, or CR — whichever reveals the understanding rather than the computation |
| **Procedural** | CR is primary; at most one multiple-choice item |
| **Application** | CR, with the student's approach and reasoning visible |

- **Representation.** Conceptual F–10: at least one item includes or describes a diagram, number line,
  area model, or tape diagram — an all-symbolic conceptual item measures procedure instead.
  Procedural: at least one item shows work as a student would — a partially worked problem, a worked
  example with an error to find, or a show-your-work prompt. Any representational form the confirmed
  component names is the one to use.
- **Number values** stay in the range the curriculum focus and year level expect: above it a
  conceptual check becomes an arithmetic obstacle course, below it a student can just count.
- **Discrimination.** At least one item lets a student reach the correct answer by a faulty method,
  or exposes partial understanding in a "correct" response.
- **Every item reveals thinking, not just correctness.** MC: every distractor maps to a named error
  from the map. CR: the prompt explicitly asks for the explanation, justification, or work —
  *"How do you know?"* at Year 3, *"Explain how you decided"* at Year 6.
- **Figures state in words what they show** — "4 groups of 3 dots each", not "dice"
  (`references/output.md` has the markup). **And what a picture cannot say, the stem says:** *"Which
  expression shows the number of groups times the size of each group?"* is settled by figure plus
  stem; *"Which expression matches the picture?"* is not, because factor order is a convention the
  picture cannot carry.

### Multiple-choice items

- Each distractor corresponds to one specific error from the map; prefer authority-verified ones.
- At least one reflects a **prerequisite gap** and at least one an **on-band confusion**, so
  responses route to different next steps.
- The key is not distinguishable by format, length, or specificity.
- **A distractor is a place a student's reasoning lands** — working this stem's numbers, the
  error arrives at that choice. Checked at `references/verification.md`, on the written files.

### Student-facing language sits at the year level's reading level

Above-band wording puts a second question inside the first, and the student lands in a distractor
reporting a misconception they don't have. Applies to every string a student reads: stems, choices,
directions, figure `<title>`/`<desc>`.

- **Vocabulary.** Terms this year level's instruction teaches stay — *numerator*, *denominator*,
  *equal parts* belong in a Year 3 item. Every other word is the one the year level already has:
  *split into 4 equal parts*, not *partitioned into quarters*; *find*, not *determine*. Standard
  wording is written for adults, so the meta block quotes it verbatim for the teacher and the item
  says the same idea in the students' words.
- **Sentences.** One idea each, actor first, present tense, no idioms. **F–2** about 8 words;
  **3–6** about 12 and at most one subordinate clause; **7–10** about 15; **11–12** length comes
  from the mathematics. A sentence past its band carries something the mathematics didn't ask for —
  split it. A familiar context costs no reading; an unfamiliar one must be understood first.

**Stems and choices are student-facing**: no annotation, symbol, label, bolding, or formatting that
identifies the key, references an error pattern, or names a next step. Drafting them clean once makes
the handout safe to hand over unedited.

---

## 4. Teacher-facing notes

For each item:

1. **What each response reveals** — one row per choice for MC, the expected response types for CR,
   describing the **observable behaviour**: what the student writes, draws, or circles, not an
   inferential label. "Adds the denominators as well as the numerators" is usable; "doesn't
   understand fraction addition" is not.
2. **The next step.** Name which kind it is — **prerequisite gap** (prior-band content not yet
   secure) or **on-band confusion** (this focus's own demand) — then make it concrete from the
   retrieved guidance: the specific sub-skill, representation, or task type. A prerequisite-gap row
   routes to a **named prior curriculum code**, never "review earlier work."
3. **What to look for across responses** — two or three sentences on whether a shared pattern points
   to one prior-band gap several students can all be routed to, versus scattered on-band confusions
   each needing different handling. **If two rows route alike, the data isn't working.**

---

## 5. Meta-block content (templates: `references/output.md`)

Six rows, in this order:

- **`Curriculum source`** — ACARA (Australian Curriculum v9.0 F–10) or QCAA (Years 11–12 General
  Senior Syllabus), with version.
- **`Identifier`** — the official ACERA code (e.g. `ACARA.MA2.F-Olsen.2.1`) or QCAA subject code
  (e.g. `QSUB-0089`), never fabricated.
- **`Year level`** — the year level the items are written for, using F–10 or Years 11–12 band.
- **`Rigor`** — Conceptual / Procedural / Application / Mixed.
- **`Learning goal`** — two sentences: what a student who has this can do, scoped to the confirmed
  focus, and how that shows up in these items.
- **`Prerequisite standards`** — the 1–3 most relevant backward-progression codes, with a short gist,
  and the same codes the guide routes prerequisite-gap responses to.
- **`Leads to`** — the 1–2 most relevant forward-progression codes.
- **`Mapping strength`** — exact (curriculum code matched with authority-verified mapping),
  contextual (terminology aligned but source not formally matched), or pending-reviewer
  (partial mapping under review). Never fabricated.
- **Copyright:** never reproduce retrieved problem text, contexts, or teacher notes verbatim, and
  never name the curriculum, publisher, or research source in user-facing output. Source attribution
  appears only in the meta block for teacher reference, not in student-facing content.
