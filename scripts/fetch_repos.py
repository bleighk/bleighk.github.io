#!/usr/bin/env python3
"""
Fetches public GitHub repos tagged with the 'portfolio' topic for GITHUB_USER,
generates Hugo content pages from their READMEs, and downloads the GitHub avatar.

Run before `hugo server` locally, or as a workflow step before `hugo --minify` in CI.

Usage:
    python3 scripts/fetch_repos.py

Requires: Python 3.8+, no third-party dependencies.
Respects GITHUB_TOKEN env var for higher rate limits (auto-set in GitHub Actions).
"""

import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

GITHUB_USER   = "bleighk"
PORTFOLIO_TAG = "portfolio"
CONTENT_DIR   = Path("content/projects")
STATIC_DIR    = Path("static/images")
GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")

# ── GitHub API helpers ────────────────────────────────────────────────────────

def _request(url: str) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", f"bleighk-site-builder/1.0")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} fetching {url}", file=sys.stderr)
        return {}


def fetch_portfolio_repos() -> list[dict]:
    """Return all public repos for GITHUB_USER that carry PORTFOLIO_TAG, newest-first."""
    repos, page = [], 1
    while True:
        chunk = _request(
            f"https://api.github.com/users/{GITHUB_USER}/repos"
            f"?per_page=100&page={page}&sort=pushed&direction=desc"
        )
        if not isinstance(chunk, list) or not chunk:
            break
        repos.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1

    return [
        r for r in repos
        if not r.get("private")
        and PORTFOLIO_TAG in r.get("topics", [])
    ]


def fetch_readme(repo_name: str, default_branch: str = "main") -> str | None:
    """Return decoded README text, or None if not found."""
    data = _request(f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/readme")
    if not isinstance(data, dict) or "content" not in data:
        return None
    try:
        return base64.b64decode(data["content"]).decode("utf-8")
    except Exception:
        return None


def fetch_avatar() -> None:
    """Download the user's GitHub avatar to static/images/avatar.jpg."""
    data = _request(f"https://api.github.com/users/{GITHUB_USER}")
    avatar_url = data.get("avatar_url")
    if not avatar_url:
        print("  Warning: could not retrieve avatar URL", file=sys.stderr)
        return
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    dest = STATIC_DIR / "avatar.jpg"
    req = urllib.request.Request(avatar_url, headers={"User-Agent": "bleighk-site-builder/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        dest.write_bytes(resp.read())
    print(f"  Avatar → {dest}")

# ── Content generation ────────────────────────────────────────────────────────

def _rewrite_relative_images(readme: str, repo_name: str, branch: str) -> str:
    """
    Rewrite relative image paths in README markdown/HTML to absolute GitHub raw URLs
    so images render correctly when served outside github.com.
    """
    raw_base = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/{branch}"

    def _md_replace(m: re.Match) -> str:
        alt, src = m.group(1), m.group(2)
        if src.startswith(("http://", "https://", "//", "data:")):
            return m.group(0)
        return f"![{alt}]({raw_base}/{src.lstrip('/')})"

    def _html_replace(m: re.Match) -> str:
        src = m.group(1)
        if src.startswith(("http://", "https://", "//", "data:")):
            return m.group(0)
        return f'<img src="{raw_base}/{src.lstrip("/")}"'

    readme = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", _md_replace, readme)
    readme = re.sub(r'<img\s+src="([^"]+)"', _html_replace, readme)
    return readme


def _slugify(name: str) -> str:
    return name.lower().replace("_", "-")


def _prettify(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()


def generate_page(repo: dict, readme: str | None, weight: int) -> str:
    name        = repo["name"]
    title       = _prettify(name)
    description = (repo.get("description") or "").replace('"', "'")
    stars       = repo.get("stargazers_count", 0)
    language    = repo.get("language") or ""
    topics      = [t for t in repo.get("topics", []) if t != PORTFOLIO_TAG]
    github_url  = repo["html_url"]
    branch      = repo.get("default_branch", "main")
    pushed_at   = (repo.get("pushed_at") or "")[:10]   # YYYY-MM-DD

    tags_yaml = ", ".join(f'"{t}"' for t in ([language] + topics) if t)

    # Metadata line shown above the README body
    meta_parts = []
    if language:
        meta_parts.append(f"**{language}**")
    if stars:
        meta_parts.append(f"⭐ {stars}")
    meta_parts.append(f"[View on GitHub →]({github_url})")
    meta_line = " · ".join(meta_parts)

    # Rewrite relative images in README so they render correctly off-GitHub
    if readme:
        readme = _rewrite_relative_images(readme, name, branch)

    body = readme if readme else "_No README available for this repository._"

    return f"""---
title: "{title}"
description: "{description}"
date: {pushed_at}
params:
  githubUrl: "{github_url}"
  stars: {stars}
  language: "{language}"
tags: [{tags_yaml}]
weight: {weight}
ShowToc: false
cover:
  hidden: true
---

{meta_line}

---

{body}"""

# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"Fetching repos tagged '{PORTFOLIO_TAG}' for {GITHUB_USER}…")
    repos = fetch_portfolio_repos()
    print(f"Found {len(repos)} repo(s)\n")

    print("Fetching GitHub avatar…")
    try:
        fetch_avatar()
    except Exception as e:
        print(f"  Warning: avatar fetch failed — {e}", file=sys.stderr)

    # Remove previously generated pages (keep _index.md)
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    removed = 0
    for f in CONTENT_DIR.glob("*.md"):
        if f.name != "_index.md":
            f.unlink()
            removed += 1
    if removed:
        print(f"\nRemoved {removed} stale page(s)")

    # Generate a page per repo
    print()
    for i, repo in enumerate(repos):
        slug = _slugify(repo["name"])
        print(f"  [{i+1}/{len(repos)}] {repo['name']}")
        readme = fetch_readme(repo["name"], repo.get("default_branch", "main"))
        page   = generate_page(repo, readme, weight=i + 1)
        dest   = CONTENT_DIR / f"{slug}.md"
        dest.write_text(page, encoding="utf-8")
        print(f"        → {dest}")

    print(f"\nDone — {len(repos)} project page(s) written.")
    if not repos:
        print(
            f"\nNo repos found. To include a repo, add the topic '{PORTFOLIO_TAG}' "
            f"in its GitHub Settings → Topics."
        )


if __name__ == "__main__":
    main()
