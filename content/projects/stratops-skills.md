---
title: "StratOps Skills — seeding an internal AI ecosystem"
date: 2026-03-01
description: "Five McKinsey-structured strategy skills published to Xero's internal Claude Enterprise marketplace — the first plugin on the platform. Three other departments followed. A proof of concept for AI adoption through capability sharing."
tags: ["Claude Enterprise", "AI adoption", "skills", "strategy", "product"]
weight: 3
ShowToc: true
cover:
  hidden: true
---

## The problem

When Xero adopted Claude Enterprise, the natural adoption pattern was individual — each person using the model as a better search engine or a faster drafting tool. That's valuable, but it's the smallest version of what was possible.

The gap: Xero's strategy team had years of structured problem-solving methodology accumulated from MBB engagements. That methodology lived in people's heads, in decks, in the way senior strategists framed problems. It wasn't accessible to a finance analyst trying to structure a business case, or a product manager trying to facilitate a prioritisation session.

Skills could change that — if anyone actually built them.

## The approach

I built five skills following McKinsey-structured problem-solving methodology and published them to Xero's internal Claude Enterprise plugin marketplace:

- **Brainstorm** — structured divergent thinking with explicit MECE framing
- **Hypothesis** — hypothesis tree construction from a problem statement
- **Research** — structured secondary research with source discipline
- **Storyline** — top-down, SCR-structured narrative from a brief
- **Slides** — slide structure from a storyline, ready for deck assembly

The design principle throughout: each skill should be usable by someone with no MBB background. The methodology is embedded in the prompts; the user just needs to know what problem they're solving.

I published the first version in early 2026 — the first plugin on Xero's internal marketplace. Then I waited.

## The outcome

Three departments — HR, Design, and Engineering — built their own skills and published them to the marketplace within weeks, using the StratOps Skills plugin as a reference. In each case, I provided light support during the build: a conversation about what the skill should do, a review of the first draft prompt, feedback on the test outputs.

The pattern that emerged is the one I had hypothesised: once one team sees that another team has built something useful, the activation energy for their own build drops significantly. The marketplace creates a visibility layer that individual Claude use does not.

<!-- DIRECTIONAL: precise adoption/usage figures available if Brad confirms public. -->

## What I learned

**Skills are shared infrastructure.** The value of a skill isn't just to the person who built it — it's to every person in the organisation who encounters the same problem type. Building skills is an act of institutional knowledge codification, which is a very different frame from "I built a useful prompt."

**The first mover sets the template.** Because StratOps was the first plugin, it implicitly defined what a skill looked like — its format, its level of instruction, its scope. The three departments that followed all used a similar structure. Template effects are real in internal AI adoption.

**Mix-and-match is where the agility comes from.** A finance analyst running a Hypothesis skill, a product manager using a Storyline skill, a designer using a Research skill — the same infrastructure producing different outputs for different functions. The StratOps Skills plugin is proof that this is achievable at a small team's effort level. The question is what has to be true to make it the default.

---

*Tech: Claude Enterprise · custom skill prompts · internal plugin marketplace*
