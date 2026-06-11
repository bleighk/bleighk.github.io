---
title: "Why I get my colleagues to build agents instead of pitching them"
date: 2026-04-30
description: "The most effective thing I have found for cutting through AI hype — inside an organisation or anywhere else — is to get people building. Not watching demos, not reading reports. Actually building."
tags: ["AI adoption", "agents", "strategy", "enterprise"]
ShowToc: true
ShowReadingTime: true
---

There's a moment I keep watching happen in AI strategy conversations. Someone presents a genuinely impressive capability — a benchmark, a case study, a well-produced demo — and the room's reaction is a kind of suspended animation. People are neither convinced nor unconvinced. They're waiting for something.

What they're waiting for, I've come to think, is contact with the real thing.

## The hype problem is not a communications problem

The standard response to AI scepticism inside organisations is more communication: better slides, clearer ROI models, more executive sponsorship. All of that can be useful. None of it solves the underlying problem, which is that people have been told a lot about AI and have almost no direct experience of it.

In that environment, confident claims and cautious claims look identical. Both are words.

The only thing that has consistently cut through this for me — at BCG, and now at Xero — is to get people building something themselves. Small, bounded, real. Not a production system; not even a prototype, necessarily. Just: take a tool, apply it to an actual problem you have, see what happens.

The outcome is almost always the same. People who were enthusiastic become more thoughtful. People who were sceptical become more curious. The technology stops being a pitch and starts being a material with properties — things it's good at, things it isn't, edges where it fails unexpectedly.

In my global strategy team at BCG, this was the pattern I observed repeatedly: *"As soon as they started to actually just try and build something, they were like, oh, okay, now I better understand what the limitations are too."* The build was the antidote to the hype — in both directions.

## What "building" means at different levels

The mistake is to treat "building" as a binary: either you're writing production code or you're not building. That's not what I mean.

**For an executive:** Building means using a tool on a real question for 30 minutes. Not a demo, not a facilitated session — just opening the product and trying to solve something. The failure modes are instructive; the successful moments are memorable in a way that slides are not.

**For a knowledge worker:** Building means creating a custom skill or a structured prompt that addresses a specific task they actually do. The first time someone sees their own workflow reflected back to them by an agent they configured, something shifts. They start asking questions that are three levels more specific than the questions they were asking before.

**For an engineer:** Building means shipping something to production — even something small — and watching it behave under real conditions. The operational questions (error handling, cost, latency, edge cases) that don't come up in a demo come up immediately in production. That contact with reality is the fastest path to calibrated judgment.

The StratOps Skills plugin at Xero was this pattern at the organisational level. I built five skills and published them to the internal marketplace. Three departments built their own skills within weeks — not because I pitched them, but because they saw what was possible and had a concrete reference to copy. The activation energy dropped once the template existed.

## The trap in this framing

There's a version of "just build something" that is genuinely unhelpful, and it's worth naming.

Building for its own sake — agents that don't solve a real problem, prototypes that live in a demo environment and never touch production data, skills that nobody actually uses — produces the same suspended animation as the slide deck. The build needs to be in contact with a real constraint: a deadline, an accuracy threshold, a user who will be affected by the output.

At Xero, the eval harness for the AI Accelerator was built in response to a real constraint: executives needed to be confident before anything went into production. That constraint forced a level of rigour that a proof-of-concept environment would never have produced. The constraint was not an obstacle; it was the thing that made the artefact credible.

## What this means for AI adoption strategy

If I were advising an organisation trying to accelerate AI adoption — and I have been, for most of the last two years — the recommendation is not to spend more on communication. It's to lower the cost of building.

That means:
- **Internal skills and plugins** that give non-technical people a way to experience the capability without writing a line of code
- **Bounded hackathons** with real constraints and real data, not sandboxed toy problems
- **Fast feedback from production** — even limited rollouts, even read-only agents — so the operational questions surface before the full commitment

The Gong agents I'm currently prototyping for Xero's sales team started with a question from a senior GTM leader who wanted to understand what the technology could do for his function. That question came from the fact that he had already used the StratOps Skills plugin for a different problem. One build begat the next question.

That's the pattern I'm trying to accelerate. Not AI adoption as a programme — as a compounding loop.

---

*Brad Knight is strategy ops delegate on Xero's AI Transformation Programme and an independent agent builder. [Projects](/projects/) · [LinkedIn](https://www.linkedin.com/in/bradleyknight2/)*
