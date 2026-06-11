---
title: "OpenClaw — autonomous multi-agent research system"
date: 2026-04-21
description: "A self-directed multi-agent system that ran autonomously for four days: parallel research sub-agents, a Karpathy self-improvement loop, and a live-built knowledge base. Demonstrated as 'Jeff', an invoice-chasing agent on a Xero org via MCP."
tags: ["Claude API", "MCP", "multi-agent", "Python", "autonomous systems"]
weight: 2
ShowToc: true
cover:
  hidden: true
---

## The problem

Most AI agent demos are polished and controlled — the happy path, no rough edges. I wanted to understand what a production multi-agent system actually feels like to build and run: where it breaks, how it recovers, what the operational overhead looks like at 3am when no one is watching.

So I built one and let it run.

## The approach

OpenClaw is a multi-agent system I deployed on a Vultr VPS in April 2026. The architecture: six parallel sub-agents coordinated by a supervisor, running autonomous research tasks over a four-day period. Each agent used the Claude API; the system used Docker for isolation, Tailscale for secure access, and Vercel for auto-deploying outputs.

Two design decisions set it apart from a typical demo:

**The Karpathy self-improvement loop.** The system was designed to evaluate its own outputs and iterate — a pattern I adapted from Andrej Karpathy's writing on self-improving systems. Agents didn't just produce research; they critiqued it and queued follow-up tasks. This is where the four days came from: the system kept finding things it hadn't answered.

**The agent built its own knowledge base.** As the system ran, it used Quartz to incrementally publish its findings as a linked knowledge graph — a live record of what it had learned and where it had gaps.

The demo shown here is "Jeff": an invoice-chasing agent running on a real Xero org via MCP. Jeff handles the full workflow autonomously — customer emails, invoice drafts, late fees, escalations, multi-language support (Arabic, Japanese). It's a narrower use case than the full research system but demonstrates the same core capability: an agent that reasons across tools and holds context across a multi-turn workflow.

## The outcome

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
  <iframe src="https://www.loom.com/embed/189e207520f848bc82631102b0f9ab34"
    frameborder="0"
    webkitallowfullscreen mozallowfullscreen allowfullscreen
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
  </iframe>
</div>

The research system ran for four days without manual intervention. 38-minute competitor research runs. Outputs published to a live knowledge base updated continuously.

Getting to this point took roughly four hours of initial troubleshooting — setting up OpenClaw requires comfort with the command line and terminal. That's not a flaw in the design; it's an honest reflection of where autonomous agent infrastructure is in 2026. The friction is real.

## What I learned

**The operational layer is where the real decisions are.** Agents are easy to demo; they are hard to operate. Error handling, retry logic, cost monitoring, graceful degradation when a sub-agent fails — none of that is interesting to talk about and all of it determines whether the thing actually runs.

**Four hours of setup is a product problem, not a user problem.** The friction I documented while building OpenClaw directly informed how I think about AI adoption at Xero. When I get colleagues building agents instead of just talking about them, the setup friction is the first thing that needs to go.

**Autonomous duration reveals things that demos hide.** The four-day run surfaced failure modes that no 20-minute demo would catch: context window pressure, API rate limits at scale, the compounding cost of hallucinated sub-task generation. This is the only honest way to benchmark an autonomous system.

---

*Tech: Claude API · Xero MCP · Python · Docker · Tailscale · Vercel · Quartz*
