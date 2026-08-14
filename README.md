# 🐞 Bug-Hunters

### AI-Powered Multi-Agent Code Security & Bug Detection

**Bug-Hunters** is a Python-based security analysis tool that combines **static analysis** with **LLM-powered code review** to identify potential bugs, security vulnerabilities, and code smells in software repositories.

The tool uses **Bandit**, **Semgrep**, and **Google Gemini** to provide multiple layers of analysis and generates a consolidated, human-readable Markdown report.

---

## 🚀 Overview

Finding security vulnerabilities manually in a large codebase can be time-consuming.

Bug-Hunters automates the initial security-review process by:

1. Cloning the target Git repository
2. Identifying supported source-code files
3. Running static security analysis
4. Performing LLM-based code review
5. Combining the findings
6. Generating a Markdown security report

This creates a simple **multi-agent security-analysis pipeline** where traditional static-analysis tools and an AI reviewer complement each other.

---

## ✨ Features

* 🔍 **Static Security Analysis**

  * Bandit for Python security analysis
  * Semgrep for rule-based code analysis

* 🤖 **AI-Powered Code Review**

  * Google Gemini analyzes source code for bugs, security issues, and code smells

* 📦 **Automatic Repository Cloning**

  * Accepts a Git repository URL and creates a temporary working copy

* 🧩 **Multi-Layer Analysis**

  * Combines traditional static analysis with LLM-based reasoning

* 📄 **Automated Bug Reports**

  * Generates findings in Markdown format

* 🛠️ **Multiple Programming Languages**

  * Supports scanning files with extensions such as:

    * Python
    * JavaScript
    * TypeScript
    * Java
    * Go
    * C
    * C++

* 🧹 **Temporary Repository Cleanup**

  * Removes the cloned repository after analysis

---

## 🧠 How It Works

```text
                    Target Git Repository
                            │
                            ▼
                    Repository Cloner
                            │
                            ▼
                   Temporary Repository
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
          Bandit         Semgrep       Gemini AI
       Static Scan     Static Scan    Code Review
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                    Findings Aggregator
                            │
                            ▼
                    bug_report.md
```

---

## 🔬 Analysis Pipeline

### 1. Repository Cloning

The tool accepts a Git repository URL through the `--repo` command-line argument.

The repository is cloned into a temporary directory so that the original project is not modified.

### 2. Source-Code Enumeration

Bug-Hunters searches the cloned repository for supported source files.

Currently supported extensions include:

```text
.py
.js
.ts
.java
.go
.c
.cpp
```

### 3. Bandit Analysis

**Bandit** is used for Python security analysis.

The tool executes a recursive Bandit scan and collects the results as JSON.

```text
Repository
    │
    ▼
  Bandit
    │
    ▼
Security Findings
```

### 4. Semgrep Analysis

**Semgrep** performs rule-based static analysis across the repository.

The project uses Semgrep's automatic configuration:

```text
--config=auto
```

The results are collected in JSON format for further processing.

### 5. Gemini AI Review

The LLM reviewer sends source code to **Google Gemini** for deeper analysis.

The model is instructed to identify:

* Bugs
* Security vulnerabilities
* Code smells

Each finding is structured with:

```text
File
Line
Severity
Type
Description
```

Example:

```json
{
  "line": 42,
  "severity": "HIGH",
  "type": "security",
  "msg": "Potential security issue..."
}
```

### 6. Report Generation

Results from Bandit, Semgrep, and Gemini are combined into:

```text
bug_report.md
```

The report contains separate sections for each analysis source.

---

## 🛠️ Tech Stack

| Technology    | Purpose                    |
| ------------- | -------------------------- |
| Python        | Core application           |
| Google Gemini | AI-powered code review     |
| Bandit        | Python security analysis   |
| Semgrep       | Static code analysis       |
| GitPython     | Repository cloning         |
| Git           | Repository management      |
| JSON          | Analysis-result processing |
| Markdown      | Security report generation |

---

## 📂 Project Structure

```text
Bug-Hunters/
│
├── Bug hunter.py
├── bug_report.md
└── README.md
```

### `Bug hunter.py`

The main application containing the complete analysis pipeline.

It includes:

* Repository cloning
* Source-file enumeration
* Bandit integration
* Semgrep integration
* Gemini integration
* Report generation
* Temporary-directory cleanup

### `bug_report.md`

The generated security-analysis report.

It contains findings from:

* Bandit
* Semgrep
* Gemini

The current repository includes an example report with no Bandit or Semgrep findings.

---

## ⚙️ Requirements

Before running Bug-Hunters, install:

* Python 3.8+
* Git
* Bandit
* Semgrep
* Google GenAI SDK
* GitPython

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Midhundg/Bug-Hunters.git
cd Bug-Hunters
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install google-genai GitPython bandit
```

Install Semgrep:

```bash
pip install semgrep
```

Verify the installations:

```bash
bandit --version
semgrep --version
```

---

## 🔑 Google Gemini API Key

Bug-Hunters uses Google Gemini for AI-assisted code review.

The current implementation initializes the Gemini client using an API key. Before running the project, configure your API key securely.

### Recommended approach

Use an environment variable rather than committing an API key into source code.

For Linux/macOS:

```bash
export GEMINI_API_KEY="your_api_key"
```

For Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="your_api_key"
```

> ⚠️ Never commit a real API key to GitHub.

---

## ▶️ Usage

Run the tool using:

```bash
python "Bug hunter.py" --repo <repository-url>
```

Example:

```bash
python "Bug hunter.py" --repo https://github.com/example/project.git
```

The tool will:

```text
Clone repository
      ↓
Discover source files
      ↓
Run Bandit
      ↓
Run Semgrep
      ↓
Review source code with Gemini
      ↓
Generate bug_report.md
      ↓
Clean temporary files
```

After execution:

```text
bug_report.md
```

will contain the generated analysis report.

---

## 📄 Example Report

The generated report follows a structure similar to:

```markdown
# Bug Hunter Report

## Bandit Findings

- Security finding...

## Semgrep Findings

- Static-analysis finding...

## path/to/file.py

- **HIGH** line 42 – Potential security issue
- **MED** line 75 – Possible code smell
```

This makes the output easy to read and share with developers.

---

## 🎯 Why Use Multiple Analysis Techniques?

A major strength of Bug-Hunters is that it does not depend on a single detection mechanism.

### Traditional Static Analysis

Bandit and Semgrep are useful for detecting known patterns and rule-based vulnerabilities.

### LLM-Based Analysis

Gemini can reason about source code and identify potential:

* Logical bugs
* Security weaknesses
* Code smells
* Suspicious implementation patterns

### Combined Approach

```text
Static Analysis
      +
AI Code Review
      ↓
More Comprehensive Review
```

The AI layer should be treated as an additional review mechanism rather than a guarantee that every reported issue is a real vulnerability.

---

## 🔐 Security & Responsible Use

Bug-Hunters is intended for **authorized security testing and code review**.

Only analyze repositories that you own or have explicit permission to test.

Do not use the tool to scan private or third-party systems without authorization.

Always follow the security policy and responsible-disclosure requirements of the target project.

---

## ⚠️ Limitations

The current implementation has several limitations:

* LLM findings may contain false positives.
* Static-analysis coverage depends on the rules used by Bandit and Semgrep.
* The Gemini review currently analyzes only a limited portion of each source file.
* The current implementation uses a fixed Gemini model configuration.
* The tool currently generates a Markdown report rather than automatically creating GitHub issues or pull requests.
* API credentials need to be handled securely.
* Large repositories may require optimization for performance and token usage.

---

## 🔮 Future Improvements

### 🤖 AI Improvements

* Support newer Gemini models
* Add multiple specialized AI agents
* Add an AI verification agent to validate findings
* Add confidence scores
* Reduce false positives
* Add vulnerability severity classification

### 🔍 Security Improvements

* Add OWASP Top 10 mapping
* Add CWE identification
* Add CVSS scoring
* Add dependency vulnerability scanning
* Add secret detection
* Add SAST rule customization

### 📊 Reporting Improvements

* HTML security reports
* PDF reports
* Interactive dashboard
* Vulnerability charts
* Severity distribution
* Remediation recommendations

### 🔗 Developer Workflow

* GitHub Actions integration
* Pull-request security scanning
* Automatic comments on pull requests
* CI/CD integration
* Security-gate support

### 🧠 Advanced Multi-Agent Architecture

A future version could use specialized agents:

```text
                 Repository
                     │
                     ▼
               Recon Agent
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       SAST Agent  AI Agent  Dependency Agent
          │          │          │
          └──────────┼──────────┘
                     ▼
              Verification Agent
                     │
                     ▼
               Risk Classifier
                     │
                     ▼
               Report Generator
```

This would make the system more robust by allowing one agent to discover an issue and another agent to independently verify it.

---

## 📌 Project Highlights

### What makes Bug-Hunters interesting?

**1. Hybrid Security Analysis**

Combines deterministic static-analysis tools with LLM reasoning.

**2. Automated Repository Analysis**

The user only needs to provide a repository URL.

**3. Multi-Agent Architecture**

The project separates repository cloning, static analysis, AI review, and reporting into different components.

**4. Human-Readable Output**

Security findings are consolidated into a Markdown report.

**5. Extensible Design**

The architecture can be extended with additional security scanners, AI agents, languages, and reporting formats.

---

## 📈 Future Vision

Bug-Hunters can evolve into a complete **AI-powered DevSecOps security platform**:

```text
Developer
    │
    ▼
Git Push / Pull Request
    │
    ▼
Bug-Hunters
    │
    ├── SAST
    ├── Dependency Scan
    ├── Secret Detection
    ├── AI Code Review
    └── Vulnerability Verification
             │
             ▼
       Risk Classification
             │
       ┌─────┴─────┐
       ▼           ▼
    Critical      Safe
       │
       ▼
 Developer Alert
```

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

```bash
git checkout -b feature/new-feature
```

Make your changes, test them, and submit a pull request.

Ideas for contributions include:

* New static-analysis integrations
* Additional AI models
* New vulnerability detection rules
* Improved reporting
* CI/CD integrations
* Performance improvements

---

## 👨‍💻 Author

**Midhun D G**

GitHub: [Midhundg](https://github.com/Midhundg)

---

## ⭐ Project Summary

**Bug-Hunters is a Python-based AI-assisted security analysis tool that combines Bandit, Semgrep, and Google Gemini to automatically inspect source-code repositories for potential bugs, security vulnerabilities, and code smells and generate a consolidated Markdown security report.**
