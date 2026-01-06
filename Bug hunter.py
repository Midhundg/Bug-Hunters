#!/usr/bin/env python3
"""
Multi-Agent Bug Hunter – Single-file edition
"""

import os
import json
import subprocess
import tempfile
import shutil
import textwrap
from pathlib import Path
import argparse

try:
    import git
except Exception:
    git = None

from google import genai

# ------------------------------------------------------------------
# 0. Constants
# ------------------------------------------------------------------
GEMINI_MODEL = "gemini-1.5-flash"
ALLOWED_EXTS = {".py", ".js", ".ts", ".java", ".go", ".c", ".cpp"}

# ------------------------------------------------------------------
# 1. Agent-1: Clone Repo
# ------------------------------------------------------------------
class RepoCloner:
    @staticmethod
    def clone(url: str) -> Path:
        tmp = Path(tempfile.mkdtemp(prefix="bug_hunter_"))

        if git:
            try:
                git.Repo.clone_from(url, tmp)
                return tmp
            except Exception:
                pass

        subprocess.run(["git", "clone", url, str(tmp)], check=True)
        return tmp

    @staticmethod
    def enumerate_code_files(root: Path):
        for p in root.rglob("*"):
            if p.is_file() and p.suffix in ALLOWED_EXTS:
                yield p

# ------------------------------------------------------------------
# 2. Agent-2: Static Analysis
# ------------------------------------------------------------------
class StaticAnalyzer:
    @staticmethod
    def _run(cmd):
        try:
            out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
            return json.loads(out)
        except Exception:
            return {}

    @staticmethod
    def bandit(root: Path):
        return StaticAnalyzer._run(
            ["bandit", "-r", str(root), "-f", "json"]
        ).get("results", [])

    @staticmethod
    def semgrep(root: Path):
        return StaticAnalyzer._run(
            ["semgrep", "--config=auto", str(root), "--json", "-q"]
        ).get("results", [])

# ------------------------------------------------------------------
# 3. Agent-3: LLM Review
# ------------------------------------------------------------------
class LLMReviewer:
    def __init__(self):
        # 🔴 PUT YOUR KEY HERE (temporary)
        api_key = "PASTE_YOUR_GOOGLE_API_KEY_HERE"

        if not api_key or "PASTE_" in api_key:
            raise RuntimeError("Google API key not set")

        self.client = genai.Client(api_key=api_key)

    def _generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text or ""

    def review_file(self, path: Path) -> dict:
        try:
            code = path.read_text(encoding="utf-8", errors="ignore")[:12000]
        except Exception:
            return {"file": str(path), "issues": []}

        prompt = textwrap.dedent(f"""
        You are an expert security reviewer.

        Return ONLY valid JSON:
        {{
          "file": "{path}",
          "issues": [
            {{
              "line": 1,
              "severity": "HIGH|MED|LOW",
              "type": "bug|smell|security",
              "msg": "description"
            }}
          ]
        }}

        Code:
        {code}
        """)

        try:
            raw = self._generate(prompt).strip()
            if raw.startswith("```"):
                raw = "\n".join(raw.split("\n")[1:-1])
            return json.loads(raw)
        except Exception:
            return {"file": str(path), "issues": []}

# ------------------------------------------------------------------
# 4. Report Writer
# ------------------------------------------------------------------
class ReportWriter:
    @staticmethod
    def build(reviews, bandit, semgrep):
        md = ["# Bug Hunter Report\n"]

        md.append("## Bandit Findings")
        md += [f"- {b['issue_text']} ({b['filename']}:{b['line_number']})" for b in bandit] or ["- None"]

        md.append("\n## Semgrep Findings")
        md += [f"- {s['extra']['message']} ({s['path']}:{s['start']['line']})" for s in semgrep] or ["- None"]

        for r in reviews:
            if r["issues"]:
                md.append(f"\n## {r['file']}")
                for i in r["issues"]:
                    md.append(f"- **{i['severity']}** line {i['line']} – {i['msg']}")

        Path("bug_report.md").write_text("\n".join(md))

# ------------------------------------------------------------------
# 5. Main
# ------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()

    llm = LLMReviewer()
    repo = RepoCloner.clone(args.repo)

    bandit = StaticAnalyzer.bandit(repo)
    semgrep = StaticAnalyzer.semgrep(repo)
    reviews = [llm.review_file(f) for f in RepoCloner.enumerate_code_files(repo)]

    ReportWriter.build(reviews, bandit, semgrep)
    print("✅ bug_report.md generated")

    shutil.rmtree(repo, ignore_errors=True)

if __name__ == "__main__":
    main()
