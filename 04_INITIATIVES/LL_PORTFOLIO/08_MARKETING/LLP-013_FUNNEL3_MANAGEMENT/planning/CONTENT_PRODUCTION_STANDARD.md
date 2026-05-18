---
title: F3 Content Production Standard
owner: ML1
status: active
version: 1.0
created_date: 2026-04-15
last_updated: 2026-04-15
tags: [funnel-03, content-standard, voice, production]
id: 04_initiatives_ll_portfolio_08_marketing_llp_013_funnel3_management_planning_content_production_standard_md
---

# F3 Content Production Standard

This document governs how F3 top-of-funnel content is written. It applies to all posts,
articles, and drafts produced for LinkedIn, blog, and external publications.

Sections 5 (Signal Anchoring) and 6 (CTA Ladder) are placeholders pending ML1 input.

---

## 1. Voice & Register

### The author position

Write as a practitioner who works on these problems weekly — not as someone explaining
them to an audience. The reader is a peer. They are experienced, opinionated, and already
dealing with the problems the post describes. Content should feel like a working note
shared between colleagues, not a primer written for people who don't know the field.

This is the single most important standard. Every other rule below is in service of it.

### What this produces

- Posts that feel like they were written from direct experience
- Titles that label a phenomenon rather than promise to reveal one
- Hooks that describe a pattern the reader already recognises
- No pedagogical framing ("here's what most teams miss", "what you need to know")

### What it rules out

- Positioning the reader as someone who doesn't yet see the full picture
- Theatrical expertise signals ("the hidden reason", "what actually happens")
- Consultant-register language ("value creation", "optimise for", "unlock")
- Legal register bleeding in ("it is important to note", "practitioners should be aware")

---

## 2. Title Construction Rules

### The standard

Titles name the topic. They do not promise a reveal, frame a puzzle, or position the
reader as missing something.

A title should read like a practitioner labeling a working document — specific enough
to signal substance, calm enough to signal seniority.

### Permitted structures

**Noun phrase**
Describes the subject directly. No implied question.
> "Stablecoin Settlement and Fiat Conversion Constraints"
> "Silent Failure Points in Payment Systems"
> "Redundancy vs. Coordination in Multi-Provider Payment Setups"

**Colon structure: [Topic]: [Specific dimension]**
The second element must be a descriptive noun phrase — not a question in disguise.
> "Launching Payment Products in Canada: Observed Friction Points"
> "Payment Flow Architecture: Common Design Patterns"
> "Increased Bank Scrutiny of Payment Flows: What Typically Drives It"

**Tradeoff structure: [X] vs. [Y] in [Context]**
Used for tradeoff-mode posts. Names both sides explicitly.
> "Speed vs. Bankability in Cross-Border Payment Expansion"
> "Flexibility vs. Stability in Payment Rail Selection"

### Prohibited patterns

**Question structures**
Titles are statements, not questions.
> ~~"Why does X happen?"~~
> ~~"What should operators know about X?"~~

**Implied reveals**
Any phrasing that signals "I'm about to show you something you don't know."
> ~~"The hidden reason X happens"~~
> ~~"What X really means"~~
> ~~"What actually breaks in X"~~
> ~~"The real problem with X"~~

**Theatrical qualifiers**
> ~~"actually", "hidden", "silently", "suddenly", "really", "truly"~~

**Colon subtitles that are questions in disguise**
The colon subtitle test: if the second element promises a reveal or could be rephrased
as a question, it fails.
> ~~"Payment Delays: What's Actually Driving Them"~~ (question in disguise)
> ~~"Cross-Border Expansion: Where It Goes Wrong"~~ (implied reveal)
> ~~"Compliance in Payments: What Teams Get Wrong"~~ (reader-as-missing-something)

**Contrast bait**
Framing that sets up an "easy vs. hard" or "works until it doesn't" structure in the title.
> ~~"Why X Works in Some Markets and Fails in Others"~~
> ~~"Payment Systems That Scale — Until They Don't"~~

---

## 3. Hook Construction Rules

### The standard

The hook is an observation, not a setup. It describes a pattern the reader already
recognises — it does not position them as someone who is about to learn something
they were previously missing.

The hook earns engagement by being precise, not by being provocative.

### Structural pattern that works

Two sentences. First sentence states the observable condition. Second sentence names
the specific mechanism, location, or implication that makes it worth reading.

> "Settlement via stablecoins can be efficient. Complexity tends to reappear at the
> point where funds re-enter fiat systems."

> "A common inflection point is when a banking partner begins asking more detailed
> questions about how funds move through a system."

> "Reliable systems don't eliminate failure points — they structure flows so that
> failures are predictable and contained."

The second sentence should be specific enough that a reader can immediately test it
against their own experience. If it applies to every industry and every product, it
is not specific enough.

### Hedge limits

Hedges ("often", "tend to", "usually", "typically", "in practice") are permitted but
limited. Maximum one hedge per sentence. No consecutive sentences that both hedge.

Failing:
> "Payment delays often tend to originate earlier in the flow than teams typically
> expect."

Passing:
> "Delays are often attributed to the last visible step in a flow. In practice,
> they originate earlier — where visibility is lower."

### Reader positioning

The reader is a peer operating in the same environment the post describes. They are
not a student discovering a new concept.

Prohibited framing:
> ~~"Most teams don't realise that..."~~
> ~~"What operators often miss is..."~~
> ~~"The thing most people don't see is..."~~

Permitted framing:
> "Teams expanding into Canada often encounter delays that aren't present in other
> markets, even with similar product structures."
> "Payment partners often reassess risk as volumes grow, even when the underlying
> product hasn't changed."

The difference: the permitted version describes a pattern the reader may have
experienced. The prohibited version tells them they were naive.

### Contrast bait in hooks

The same prohibition that applies to titles applies to hooks. Do not open with
"X looks simple / X works well — until..." as a setup structure.

Failing:
> "Expansion into Canada can appear straightforward at the outset. Delays often
> show up later."

Passing:
> "Payment market entry in Canada involves a distinct set of infrastructure and
> regulatory interactions. Teams typically encounter these at the partner onboarding
> and system integration stages."

---

## 4. Content Mode Definitions

Every post is written in one of four modes. The mode determines the structure and
argument of the post body — not just the hook. Before drafting, identify the mode.

### Mode 1 — Diagnosis

**What it does:** Describes a failure pattern, degradation mechanism, or structural
problem. Names what is happening and where.

**What it is not:** A reveal. The reader should recognise the pattern, not be surprised
by it.

**Distinguishing feature:** The post answers "what is happening and why" — not
"here is something you didn't know."

**Signal posts from the master list:** #3, #9, #13, #21, #22, #32

**Example:** *Silent Failure Points in Payment Systems* — describes the mechanism by
which payment flows degrade without generating explicit errors. The reader who has
operated a payment system at scale has experienced this. The post names and structures
what they already know.

---

### Mode 2 — Judgment

**What it does:** Discriminates between what matters and what doesn't. Takes a
position on priority, sequence, or relative importance.

**What it is not:** A balanced overview. Judgment posts have a point of view.

**Distinguishing feature:** The post answers "what should I prioritise or how should
I think about this" — it gives the reader a framework for making decisions, not just
a description of the landscape.

**Signal posts from the master list:** #1, #7, #12, #17, #20, #33

**Example:** *Settlement, Clearing, and Payout as Distinct Operational Functions* —
takes the position that collapsing these functions in product thinking creates
downstream problems. The post argues for a specific way of structuring how operators
think about their stack.

---

### Mode 3 — Tradeoffs

**What it does:** Presents two competing goods with real costs on each side. Does not
resolve the tradeoff — describes it accurately so the reader can make an informed
decision given their specific context.

**What it is not:** A false balance. The tradeoff must be real. If one option is
clearly better in most situations, this is a judgment post, not a tradeoffs post.

**Distinguishing feature:** The post ends without a winner. The reader leaves with a
clearer understanding of what they are choosing between.

**Signal posts from the master list:** #2, #10, #14, #19, #23, #27

**Example:** *Redundancy vs. Coordination in Multi-Provider Payment Setups* — adding
providers genuinely improves resilience in some configurations and genuinely increases
coordination failure risk in others. Both are true. The post describes the conditions
under which each outcome is more likely.

---

### Mode 4 — Definition of Good

**What it does:** Describes what well-functioning looks like. Names the structural
characteristics of systems, products, or practices that hold up over time.

**What it is not:** A best-practice listicle. The post describes patterns observed
across real systems — not idealised prescriptions.

**Distinguishing feature:** The post answers "what does this look like when it's
working" — giving the reader a reference point rather than a warning.

**Signal posts from the master list:** #5, #8, #15, #16, #24, #28

**Example:** *How High-Reliability Payment Systems Handle Failure* — describes the
structural characteristics that high-reliability systems share. The reader can assess
their own system against a concrete reference, not a vague standard.

---

### Mode balance across the content set

The 39-post master list is balanced across modes. Do not allow production to drift
toward Diagnosis-heavy output. If a content queue contains more than 40% Diagnosis
posts, rebalance before publishing.

Target distribution:
- Diagnosis: ~30%
- Judgment: ~30%
- Tradeoffs: ~20%
- Definition of Good: ~20%

---

## 5. Signal Anchoring Protocol

*Placeholder — pending ML1 signal agent specification.*

This section will define:
- How real-world events and signals are matched to posts in the master list
- What threshold a signal must meet to anchor a post (specificity, relevance, recency)
- How to integrate a signal without making it the subject of the post
- Signal types by category (regulatory, infrastructure, market, product)

---

## 6. CTA Ladder

*Placeholder — pending ML1 review.*

This section will define:
- What is permitted in categories 1–6 (currently: no direct CTAs)
- Passive positioning signals permitted in categories 1–6
- Soft CTA format for categories 7–8
- Hard CTA format for trigger posts
- Mid-funnel conversion step (EO1–3 entry points)
