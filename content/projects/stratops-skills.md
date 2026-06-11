---
title: "Stratops Skills"
description: ""
date: 2026-06-10
params:
  githubUrl: "https://github.com/bleighk/stratops-skills"
  stars: 0
  language: ""
tags: []
weight: 1
ShowToc: false
cover:
  hidden: true
---

[View on GitHub →](https://github.com/bleighk/stratops-skills)

---

# Xero Strategy & Ops Skills

A collection of skills used by Xero's Strategy & Ops team. Covers structured problem solving toolkit commonly used by Management Consulting firms (e.g., McKinsey, BCG, Bain etc.). Plugin suite covers: domain research, structured brainstorming, MECE hypothesis trees, and Pyramid Principle executive communications, and slide generation.

## Skills

### /brainstorm

Guides you through a structured ideation session using proven creative techniques. Helps you generate a large volume of ideas before narrowing down — useful for solving problems, exploring opportunities, or unblocking creative thinking.

**Invoke:** `/brainstorm` or "help me brainstorm [topic]"

### /research

Researches a market, industry, or competitive landscape using live web data and produces a structured report. Covers market size, competitors, regulations, and technology trends.

**Invoke:** `/research` or "research [topic] for me"

### /hypothesis

Helps you structure a strategic question into a clear, testable framework before jumping to answers. Useful when you need to frame a business problem, build an analytical plan, or prepare a recommendation.

**Invoke:** `/hypothesis` or "help me structure [question]"

### /storyline

Turns your ideas or analysis into a clear, executive-ready narrative using the Pyramid Principle — conclusion first, supported by evidence. Useful for briefing notes, board papers, and presentations.

**Invoke:** `/storyline` or "help me write a briefing on [topic]"

### /slides

Builds Xero StratOps slide decks in the official "Xero 2026 (StratOps)" theme — correct master layouts, typography, brand colours, and house style. Outputs a `.pptx` that opens natively as Google Slides when uploaded to Drive. Useful for board papers, EGM updates, XLT presentations, and any executive-facing deck.

**Invoke:** `/slides` or "create a StratOps deck on [topic]"

## Limitations

- `research` requires web search tools. Without them the skill will abort at startup.
- `hypothesis` and `storyline` widget rendering requires the `visualize` MCP server. Without it, both skills still run but will not produce the interactive output.
- `brainstorm` is optimised for long ideation sessions.
- `slides` downloads the StratOps template directly from Google Drive on each run. It requires the Google Drive MCP and access to the source file — without either, it falls back to a local copy if available.
- Glean search tools (`glean_default`) are bundled with the plugin and require OAuth authorisation on first use. You will be prompted to authenticate through your browser.

