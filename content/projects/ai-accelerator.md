---
title: "Xero AI Accelerator — production agents at scale"
date: 2026-05-01
description: "Production AI agents across finance, HR, and IT operations — moving from manual processes to automated pipelines in weeks, not quarters. Plus an eval harness that proved the bar before anything went live."
tags: ["Claude API", "AI agents", "evals", "production", "enterprise"]
weight: 4
ShowToc: true
cover:
  hidden: true
---

## The problem

Xero's AI Accelerator was set up to move fast — identify high-value automation targets, build agents, get them into production. The challenge with moving fast is that "into production" means something different for a 2,000-person company than it does for a hackathon: there are processes that people depend on, accuracy bars that matter, and executives who need to be confident before they sign off.

Speed and rigour are usually in tension. The eval harness is how we resolved it.

## The approach

My role was the connector between the engineering squads and the executive layer — translating what the agents could and couldn't do into language that enabled a decision, and ensuring that the numbers we put in front of leadership were grounded in evidence.

The agents we shipped covered three functions:

**IT triage** — classifying and routing incoming IT support tickets. The baseline was a manual process that took the better part of an hour per ticket. The agent cut that by an order of magnitude.
<!-- DIRECTIONAL: precise figures (15%→0.6% manual rate, ~1hr→<1min) available if Brad confirms public. -->

**PX (people experience) triage** — ticket assignment for Xero's HR function. The agent produced meaningful improvements in assignment accuracy, measurable in production within weeks of deployment.
<!-- DIRECTIONAL: precise figure (14% faster assignment) available if Brad confirms public. -->

**Indirect tax (BAS) automation** — reducing the time to prepare Business Activity Statements from a multi-day manual process to a fraction of that, at production accuracy levels for the AU demo.
<!-- DIRECTIONAL: precise figures (2.5 days→0.25 days, ~85% accuracy) available if Brad confirms public. -->

## The eval harness

The piece I am most proud of is the evaluation framework — specifically the Xander intake agent, which assessed whether incoming use cases met the bar for the Accelerator programme.

The problem it solved: before Xander, the intake process relied on human judgment to decide which use cases were worth pursuing. That judgment was inconsistent and didn't scale. Xander used a two-layer evaluation design — a primary classifier plus a confidence-weighted review layer — to automate the intake decision with a verified accuracy that was roughly four times higher than the manual baseline.
<!-- DIRECTIONAL: precise figures (96% vs 24% baseline) available if Brad confirms public. -->

The design principles behind the eval harness are documented at [bleighk/custom-skills](https://github.com/bleighk/custom-skills) *(link active when repo is public)*.

## What I learned

**The eval is the product.** Getting an agent into production isn't the hard part — convincing an executive that it should go into production is. The eval harness is what makes that conversation possible. Without it, you're asking for trust; with it, you're presenting evidence.

**The connector role is underrated.** The engineers knew how to build the agents. The executives knew what outcomes they needed. The gap between those two groups — translating technical confidence into business decision-readiness — is where the programme either accelerated or stalled. That translation work is not obviously an engineering problem or a strategy problem; it sits between them.

**Production reveals what demos hide.** The IT triage agent performed differently on edge cases in production than it did in testing. Not worse overall — but differently. Building the monitoring layer that catches those differences before they compound is a capability gap most agent teams don't fill until they've been burned by it.

---

*Tech: Claude API · Python · custom eval frameworks · internal deployment infrastructure*
