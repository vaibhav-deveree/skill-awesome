# Engineering Skills Repository

A collection of production-ready engineering skills, architecture standards, review frameworks, testing methodologies, deployment playbooks, and operational workflows used to design, build, review, secure, test, and deploy modern software systems.

This repository is designed to function as an **Engineering Operating System (EOS)** that provides structured guidance for engineering decisions throughout the entire software lifecycle.

---

# Purpose

As software systems scale, engineering quality becomes dependent on repeatable processes rather than individual contributors.

This repository contains reusable engineering skills that help teams:

* Design better systems
* Build maintainable software
* Review code consistently
* Prevent production issues
* Improve security
* Increase reliability
* Standardize engineering practices

The goal is to create a reusable engineering framework that can be applied to any project regardless of technology stack.

---

# Engineering Lifecycle

This repository covers the entire engineering lifecycle.

```text
Idea
 ↓
Architecture
 ↓
Backend Development
 ↓
Frontend Development
 ↓
API Design
 ↓
Database Design
 ↓
Security Review
 ↓
Testing
 ↓
Code Review
 ↓
Deployment
 ↓
Production Readiness
 ↓
Monitoring
```

Every stage has one or more supporting skills.

---

# How To Use This Repository (As a Plugin)

This repository is structured as a **Gemini Plugin**. You can install and use it directly within your agentic environment.

## Installation

There are three ways to install this plugin:

### 1. The Easy Way (AI Prompt)
Copy and paste this exact prompt to Gemini, Claude, or your local AI agent:
> "Please install the `skill-awesome` plugin from `https://github.com/vaibhav-deveree/skill-awesome.git` into my agent environment so I can use the Master Architect agent and its skills."

### 2. Global Installation (Manual)
1. Clone this repository.
2. Copy the entire folder into your global plugins directory (e.g., `C:\Users\<your_user>\.gemini\config\plugins\skill-awesome`).

### 3. Project-Local Installation
If you want to use these skills only within a specific repository:
1. Navigate to your project's root folder.
2. Create a local plugins directory and clone this repo into it:
   ```bash
   mkdir -p .gemini/plugins
   cd .gemini/plugins
   git clone https://github.com/vaibhav-deveree/skill-awesome.git
   ```

## Usage

Once installed, the plugin exposes a **Master Architect** agent and a collection of **Skills**.

### The Master Architect Agent

You can invoke the Master Architect subagent directly. It is pre-configured with the `master-skill` and `engineering-principles` to coordinate other skills.

Example prompt to the system:
> "Invoke the master-architect to review my new API design in `backend/`."

### Direct Skill Usage

Individual skills (like `backend-achitecture-skill`, `security-architecture`, etc.) are natively available to the agents. When you ask an agent to perform a task, it will automatically search the `skills/` directory and apply the relevant methodologies.

---

### Database-Backed Memory Harness (Zero Hallucination)

The plugin includes an ultra-fast, SQLite database-backed **Memory Harness** feature designed to maximize token efficiency, eliminate hallucinations, and ensure no context is ever lost.

When you start a project, the Master Architect will inject a portable database engine (`db_engine.py`) into your `.memory/` directory and initialize an SQLite database (`memory.db`). This database tracks:
- **User Intent**: Exactly what you want to do.
- **Current State**: Tasks in progress, blocked, or upcoming.
- **History**: Past decisions and completed tasks.
- **Changelog**: Specific file changes and codebase modifications.

#### Why a Database?
Instead of consuming massive token limits by reading full project histories in Markdown, agents **run SQL queries** via the CLI wrapper (e.g., `python .memory/db_engine.py query "SELECT * FROM state WHERE status = 'TODO'"`). They fetch *only* the exact 2 or 3 rows they need at that exact moment.

The Master Architect acts as a dispatcher: it queries the database, identifies pending work, and spins up specialized subagents. It instructs the subagents to query the database themselves, completely bypassing massive token usage!

# Repository Structure

```text
plugin.json                 # Plugin configuration
README.md                   # This documentation
agents/
  master-architect.json     # Orchestrator subagent definition
skills/
  master-skill/
    SKILL.md
  engineering-principles/
    SKILL.md
  backend-achitecture-skill/
    SKILL.md
  ...
```

---

# Supported Technologies

The repository is technology agnostic.

Supported ecosystems include:

### Backend

* Java
* Spring Boot
* Node.js
* Python
* Go
* .NET
* Rust

### Frontend

* React
* Next.js
* Angular
* Vue
* Svelte

### Infrastructure

* AWS
* Azure
* GCP
* Vercel
* Render
* Railway
* Kubernetes

### Databases

* PostgreSQL
* MySQL
* SQL Server
* MongoDB
* DynamoDB

### AI Systems

* OpenAI
* Anthropic
* Gemini
* LangChain
* Agent Frameworks
* RAG Systems

---

# About Zero Assist

Many of these skills were developed, refined, and validated while building Zero Assist.

Zero Assist is an interview integrity and assessment platform focused on helping organizations maintain trust, transparency, and fairness during hiring and technical evaluations. 

As the platform evolved, reusable engineering practices emerged around:

* Multi-Agent Code Reviews
* Production Readiness Reviews
* Security Validation
* Scalability Analysis
* Architecture Reviews
* Reliability Assessments

Rather than keeping those processes internal, they are documented here as reusable engineering assets that can benefit other engineering teams.

The repository itself remains vendor-neutral and technology agnostic.

---

# Contributing

Contributions are welcome.

Examples:

* New skills
* Architecture guides
* Security frameworks
* Testing methodologies
* Reliability playbooks
* AI engineering workflows
* Review frameworks

---

# Philosophy

Every skill follows four core principles:

### Evidence Over Assumptions

Recommendations should be supported by facts.

### Practical Over Theoretical

Focus on realistic production issues.

### Reusable Over Project Specific

Skills should work across projects and technologies.

### Validation Over Opinion

Findings should be verified before becoming action items.

---

# Disclaimer

These skills are intended to support engineering teams in making better technical decisions.

They do not replace:

* Security audits
* Compliance reviews
* Professional engineering judgment
* Regulatory requirements

Use them as frameworks to improve consistency, quality, and engineering effectiveness.

---

Zero Assist - Vaibhav devere
Feel free to use, modify, extend, and adapt these skills for your own engineering workflows.
