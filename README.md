# bleighk.github.io

Personal site — Hugo + PaperMod, deployed to GitHub Pages via Actions.

**Live:** https://bleighk.github.io

## Structure

```
content/
  about.md          Bio and background
  now.md            What I'm currently building
  projects/         Case studies (Xero Help, OpenClaw, StratOps Skills, AI Accelerator)
  posts/            Writing at the intersection of strategy and applied AI
```

## Local development

```bash
hugo server -D
```

Requires Hugo extended ≥ 0.163.0 and Go ≥ 1.21 (for Hugo Modules).

## Deploy

Every push to `main` triggers the GitHub Actions workflow at `.github/workflows/hugo.yaml`,
which builds with `hugo --minify` and deploys to GitHub Pages automatically.

## Built with

[Hugo](https://gohugo.io) · [PaperMod](https://github.com/adityatelange/hugo-PaperMod) ·
[Claude Code](https://claude.ai/code)
