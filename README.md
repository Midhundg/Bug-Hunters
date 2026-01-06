# Bug-Hunters 🐞

Bug-Hunters is a Python-based static analysis and LLM-assisted code review tool.
It scans source code to detect potential bugs and security issues and generates
a clear, human-readable bug report.

## Features
- Static code analysis using Semgrep
- LLM-based review for deeper insights
- Generates bug reports in Markdown format
- Easy to extend and customize

## Project Structure
- `Bug hunter.py` – Main script for scanning and analysis
- `bug_report.md` – Generated bug report output

## Requirements
- Python 3.8 or higher
- semgrep
- google-generativeai

## How to Run
```bash
python Bug\ hunter.py
