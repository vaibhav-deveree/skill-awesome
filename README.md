# skill-awesome: The Ultimate AI Engineering Framework

![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin_Ready-7b3f00?style=for-the-badge&logo=anthropic)
![Multi-Agent](https://img.shields.io/badge/Multi--Agent-Architecture-007acc?style=for-the-badge)
![Zero Assist](https://img.shields.io/badge/Powered_by-Zero_Assist-2ea44f?style=for-the-badge)


`skill-awesome` is a collection of production-ready engineering skills, architecture standards, and autonomous AI subagents designed to turn any standard AI coding assistant (like Claude, Gemini, or ChatGPT) into a highly disciplined, zero-hallucination **Engineering Operating System (EOS)**.

---

## 🌟 What It Does

This plugin isn't just a list of guidelines; it provides **active agent behaviors** and an ultra-fast **SQLite Memory Engine** to orchestrate massive codebases without blowing up your token limits.

### 1. The Agents
When you install this plugin, you get access to specialized agents:
- **Master Architect**: A disciplined orchestrator that enforces mandatory implementation plans, centralizes architecture decisions, and delegates tasks to specialized subagents.
- **Vibe Coder**: An intuitive, aesthetics-first frontend co-pilot. It handles all boilerplate autonomously and is hardcoded to prioritize modern UI/UX design (glassmorphism, micro-animations).

### 2. The SQLite Memory Harness (Zero Hallucination)
- Rather than reading huge Markdown files that cause token limits to explode, agents inject an ultra-fast SQLite database engine (`db_engine.py`) into your project.
- It perpetually tracks **User Intent**, **Current State**, **History**, and a granular **Changelog**.
- Agents use raw SQL (`gh query "SELECT * FROM state"`) to fetch *only* the context they need, ensuring perfect memory forever.

### 3. Brownfield Project Onboarding
- Drop the agent into a 10-year-old codebase, and it won't break anything. 
- It maps the existing directory structure and architecture to the SQLite database.
- It proposes architectural and security upgrades in a dedicated `implementation_plan.md` *before* modifying your old code.

### 4. Interactive UI Mockup Workflow (Phase Zero)
- When generating a new website or feature, the **Vibe Coder** will pause and generate a standalone `mockup.html`.
- This HTML file is a visual mood board presenting color palettes, button styles, and layout variations.
- You click and choose your exact "vibe" before the heavy framework code (React/Vue/Next.js) is even written.

### 5. Context-Aware Git & PR Workflow
- **Conventional Commits**: Agents strictly enforce standard Git branching (`feat/`, `fix/`) and Conventional Commits.
- **Conversational Commits**: Agents won't spam PRs on every prompt. They explicitly ask you: *"Should I commit these changes?"*
- **Autonomous God Review**: Once approved, the agent automatically creates a Pull Request via the GitHub CLI (`gh pr create`) and triggers a multi-agent "God Review" covering security, architecture, and performance on the diff.

### 6. Native Claude Code Integration
- **Slash Commands**: Adds native `/master-architect`, `/vibe-coder`, and `/god-review` commands directly into your Claude Code terminal. No need to copy/paste long prompts.
- **Global Context Injection**: Uses a `SessionStart` hook to invisibly inject the `engineering-principles` into Claude's memory the moment the terminal opens. Claude *always* knows your PR rules.
- **Cross-Platform MCP Engine**: Built-in prompt constraints force the agent to format Windows paths correctly (`C:\`), permanently fixing the notorious Git Bash MCP crashing bug.
- **Inline Token Telemetry**: Agents automatically append an `Execution Footer` to their responses, providing an inline mathematical estimation of input/output tokens used per transaction.

---

## 🚀 How to Install

This repository is structured as a **Gemini/Claude Plugin**.

### Option 1: The AI Prompt (For Native Gemini Agents)
Copy and paste this exact prompt to your AI agent (like Gemini):
> *"Please install the `skill-awesome` plugin from `https://github.com/vaibhav-deveree/skill-awesome.git` into my agent environment so I can use the Master Architect and Vibe Coder agents."*

> [!WARNING]
> **For Claude CLI Users**: Please see Option 2 below. You must add this repository as a custom marketplace first.

### Option 2: Claude CLI Installation (Marketplace)
Because Claude Code uses a decentralized marketplace system, you must add this repository as a registry before installing the plugin:
```bash
claude plugins marketplace add vaibhav-deveree/skill-awesome
claude plugins install skill-awesome-plugin
```

### Option 3: Global Installation (Manual)
1. Clone this repository.
2. Copy the entire folder into your global plugins directory:
   ```bash
   C:\Users\<your_user>\.gemini\config\plugins\skill-awesome
   ```

### Option 4: Project-Local Installation
1. Navigate to your specific project's root folder.
2. Clone this repo into the local plugins directory:
   ```bash
   mkdir -p .gemini/plugins
   cd .gemini/plugins
   git clone https://github.com/vaibhav-deveree/skill-awesome.git
   ```

---

## 📊 Benchmarking & Observability (LangSmith)

To benchmark how the agents perform (tracking token usage, execution time, and cost of every `/master-architect` command), you should integrate LangSmith alongside this framework. 

Because `skill-awesome` acts as your prompt framework, it natively pairs with the official LangSmith tracing plugin.

To install the telemetry tracer in Claude Code:
```bash
claude plugins marketplace add langchain-ai/langsmith-claude-code-plugins
claude plugins install langsmith-tracing@langsmith-claude-code-plugins
```
Configure your `.env` or settings file with your LangSmith keys, and every action performed by the Vibe Coder or Master Architect will be fully visible and benchmarked in your dashboard!

---

## 🗣️ Commands & Skill Triggers

`skill-awesome` provides two ways to interact with the framework: **Native Slash Commands** (to invoke specific subagents) and **Natural Language Triggers** (to activate specific skills).

### Native Slash Commands
If you are using Claude Code or a compatible CLI, you can instantly switch the active agent profile using these commands:

| Command | What it does | When to use it |
|---------|--------------|----------------|
| `/master-architect` | Invokes the Master Architect agent. | For backend, system design, architectural planning, and complex multi-agent orchestration. |
| `/vibe-coder` | Invokes the Vibe Coder agent. | For frontend development, UI/UX implementation, and aesthetics-first coding. |
| `/god-review` | Invokes the God Review pipeline. | Run this autonomously on a diff to review security, architecture, and UI slop before merging a PR. |
| `/code-reviewer` | Invokes the Enterprise Code Review Orchestrator. | Use to spawn a multi-agent team (3-5 agents) for inline checks, cross-file checks, and final verification boards. |
| `/qa-tester` | Invokes the QA Tester agent. | Use to deeply analyze a feature, test all success/failure/edge case flows, and generate a total mockup report. |
| `/goal` | Invokes Claude Code's native continuous loop mode. | Use when you want agents to work autonomously until a specific condition is met (e.g., all tests pass). |

### Natural Language Skill Triggers
Agents are equipped with dozens of passive "Skills" that sit in the background. To activate them, simply include their trigger words in your prompt:

| Skill | Trigger Phrase | What it does |
|-------|----------------|--------------|
| **Web Quality Audit** | *"run lighthouse audit"*, *"check page quality"*, *"audit my site"* | Executes a massive 150+ check audit against Core Web Vitals, SEO, and Accessibility standards. |
| **Transitions.dev** | *"add a transition"*, *"make the modal open smoothly"*, *"stagger animation"* | Injects production-ready, zero-dependency CSS micro-animations into your frontend. |
| **Clean SaaS UI** | *"build a clean UI"*, *"SaaS look"*, *"professional design"* | Enforces the `frontend-design-skill` rules to build structured, high-utility, glassmorphism-free interfaces. |
| **Creative UI** | *"bold design"*, *"maximalist chaos"*, *"out of the box"* | Bypasses the SaaS rules and activates the `frontend-creative-design` skill for highly unique, experimental UI. |
| **Memory Harness** | (Automatic) | Agents automatically run SQLite commands (`log_state`, `log_history`) in the background to track project memory. |

---

## 🛠️ How to Use It

Once installed, the framework runs natively in your agent workspace.

**To invoke the Master Architect:**
Use the native slash command to instantly switch personas:
```bash
/master-architect Review my project and generate a new feature implementation plan.
```

**To do aesthetics-first frontend development:**
```bash
/vibe-coder Build a modern dashboard for this project with glassmorphism.
```

**To trigger an autonomous God Review on a PR:**
```bash
/god-review
```

**To run an autonomous loop until a condition is met (Goal Mode):**
Combine the native `/goal` command with a subagent to let the agent work completely autonomously until verifiable success is achieved:
```bash
/goal The test suite in test/api passes using the @master-architect agent
```

**To interact with the Memory Harness manually:**
You can always view your project's memory by running the python CLI the agents use:
```bash
python .memory/db_engine.py query "SELECT * FROM state"
```

---

## 💡 Copy & Paste Sample Prompts

To get the most out of the framework and its specialized agents, you can simply copy and paste these prompts directly into your AI assistant:

### For New Feature Development
> "I want to build a new feature. Use the `@master-architect` agent to analyze the current system, write an implementation plan to `.memory/plans/`, and orchestrate the backend and frontend development using the required subagents."

### For Frontend & UI Tasks
> "Use the `@vibe-coder` agent to build a new clean SaaS UI for the dashboard. Generate the interactive Phase Zero `mockup.html` first so I can select the exact vibe before we write any framework code."

### For Deep Code Reviews
> "Run the Enterprise Code Review on my recent changes using the `@code-reviewer` agent. Spawn a team of 3-5 specialized subagents to perform inline checks and cross-file validation, then present the Final Executive Report."

### For QA Testing & Edge Case Simulation
> "Use the `@qa-tester` agent to test the new authentication API. Read the source code to acquire deep knowledge, test all success and failure flows, simulate edge cases, and generate the Total Mockup Report."

### For Goal Mode (Autonomous Loops)
> "/goal All tests in `test/api/` pass and the lint step is clean using the `@master-architect` agent."

---

## 🤝 How to Contribute

Contributions are highly encouraged! We want to build the most comprehensive library of AI engineering protocols.

### Contribution Guidelines
1. **Never merge directly to `main`**. The repository is protected by strict branch protection rules.
2. **Branch Naming**: Use `feat/<name>`, `fix/<name>`, or `chore/<name>`.
3. **Commit Messages**: Use Conventional Commits (`feat(core): add new memory table`).
4. **Create a Pull Request**: Submit a PR.
5. **The God Review**: Your PR must pass an automated "God Review" and receive at least 1 approving review from a maintainer before it can be merged.

Examples of great contributions:
* New specialized skills (e.g., `cloud-native-skill`, `ai-agent-testing-skill`).
* Improvements to the SQLite Memory Harness.
* New Agent Profiles.

---

## 🏢 About Zero Assist

Many of these autonomous skills and PR workflows were developed, refined, and battle-tested while building **[Zero Assist](https://www.zeroassist.in/)**. 

Zero Assist is a next-generation engineering platform. By leveraging the advanced multi-agent architecture and rigorous engineering standards found in this repository, Zero Assist delivers an unparalleled experience for engineering teams. 

If you want to see these AI engineering protocols in action in a massive production environment, check out **[Zero Assist](https://www.zeroassist.in/)**!

---

## 📜 Philosophy

Every skill in this repository follows four core principles:
1. **Evidence Over Assumptions**: Code generation is based on the SQLite DB facts.
2. **Practical Over Theoretical**: Focus on realistic production issues.
3. **Reusable Over Project Specific**: The DB engine and skills work on ANY tech stack.
4. **Validation Over Opinion**: Code must pass the God Review before merging.

*Feel free to use, modify, extend, and adapt these skills for your own engineering workflows.*
