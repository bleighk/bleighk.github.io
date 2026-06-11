---
title: "Xero Help — AI-native customer retention"
date: 2026-04-26
description: "A Claude + MCP agent that monitors live customer org state, surfaces churn risk to the CX team, and coaches customers in their own AI platform. Built in 48 hours for Xero's April 2026 hackathon."
tags: ["Claude API", "MCP", "Python", "AI agents", "product"]
weight: 1
ShowToc: true
cover:
  hidden: true
---

## The problem

At Xero, the majority of customer churn doesn't come from new customers in their first 90 days — the onboarding journey is well-instrumented and well-supported. It comes from established customers who quietly disengage: bank feeds stop reconciling, invoices pile up unmatched, the product becomes a burden instead of a tool.

The signal is in the data. The problem is that nobody is watching it in real time, and by the time a CX rep calls, the customer is already halfway out the door.

## The approach

I built Xero Help as a hackathon submission in April 2026. The architecture is straightforward: a Claude agent connected to Xero's MCP server, with read access to a customer's live org state — bank feeds, invoices, contacts, reconciliation status.

The agent does three things:

1. **Monitors for churn signals** — unreconciled transactions above a threshold, inactive bank feeds, overdue invoices — and surfaces them to an internal CX dashboard before the customer notices.
2. **Coaches customers directly** — when a customer asks a question in their own AI platform (Claude, Copilot, whatever they use), the agent can answer in context, pulling live data from their Xero org.
3. **Identifies upsell signals** — customers whose transaction volume has grown past the threshold where a plan upgrade would save them money. The same data that signals churn risk also signals expansion opportunity.

The key design decision was building this as an MCP integration rather than a traditional API wrapper. MCP means the agent can reason across the org state — it doesn't just look up a field, it can hold context across a multi-turn conversation about a customer's financial situation.

## The outcome

Demonstrated live with a real Xero org at the hackathon (April 2026). The demo shows the full loop: churn signal detected → CX dashboard alert → customer coaching conversation → expansion signal flagged.

<div style="position: relative; padding-bottom: 62.5%; height: 0;">
  <iframe src="https://www.loom.com/embed/be8da934766c40cb8e790b6ea5c5278b"
    frameborder="0"
    webkitallowfullscreen mozallowfullscreen allowfullscreen
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
  </iframe>
</div>

## What I learned

**MCP changes the design surface.** A traditional API integration gives you a data fetch. MCP gives you a reasoning partner that can hold customer context across turns — that's a fundamentally different product capability. The gap between "here is the invoice data" and "here is what is probably happening with this customer and what to do about it" is where the value is.

**Hackathon constraints are underrated.** 48 hours with a hard deadline forced architectural simplicity that a longer runway often loses. The agent does three things well rather than ten things adequately.

**The internal/external duality is the real opportunity.** The same agent that coaches customers can surface signals to the internal team. Building once for both surfaces is where the economics start to make sense for a product company at Xero's scale.

---

*Tech: Claude API · Xero MCP · Python · Loom for demo capture*
