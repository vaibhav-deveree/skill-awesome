---
name: engineering-principles
description: engineering principles
---


# Universal Engineering Principles & Governance Skill

## Purpose

This document is the highest authority within the Engineering Skills Repository.

All other skills inherit and follow the principles defined here.

Hierarchy:

```text
Engineering Principles
        ↓
Master Orchestrator
        ↓
Architecture Skills
        ↓
Development Skills
        ↓
Review Skills
        ↓
Deployment Skills
```

---

# Core Engineering Values

## Simplicity First

Prefer:

* Simple solutions
* Easy debugging
* Easy onboarding

Avoid:

* Unnecessary abstractions
* Over-engineering
* Premature optimization

---

## Reuse Before Build

Before creating:

* Component
* API
* Service
* Utility
* Database table

Verify whether an existing solution already exists.

---

## Security By Default

Security is not optional.

Every implementation must consider:

* Authentication
* Authorization
* Data protection
* Secrets management

---

## Reliability By Default

Every implementation must answer:

What happens if this fails?

Review:

* API failures
* Database failures
* Queue failures
* Cache failures

---

## Observability By Default

Every critical system should provide:

* Logs
* Metrics
* Traces
* Alerts

---

## Backward Compatibility

Avoid breaking existing consumers.

When breaking changes are required:

* Document them
* Version them
* Communicate them

---

## Strict Iterative Development Workflow

To prevent bugs from piling up across multiple features, all agents MUST adhere to a strict task-by-task execution loop:

1. **One Task at a Time**: Never write code for multiple features or multiple tasks simultaneously. Complete one logical feature, component, or fix before moving to the next.
2. **Mandatory God Review per Task**: As soon as the code for a single task is written, you MUST immediately pause and trigger a God Review on that specific task.
3. **No Moving Forward Until Approved**: You are strictly forbidden from proceeding to the next task in your backlog until the current task has passed the God Review with zero anomalies and all bugs are fixed.
4. **Backend Review Requirements**: The God Review for backend tasks must explicitly check:
   - Happy and unhappy flows
   - Load testing scenarios and edge cases
   - Connection timeouts and connection-related anomalies
5. **Frontend Review Requirements**: The God Review for frontend tasks must explicitly check:
   - Routing logic
   - Correct usage of `useRef`, state management, and React hooks
   - Proper CSS and styling application
   - Data mapping accuracy (verifying that the UI shows exactly the data it should show)

---

## Version Control Standards

Every agent and engineer must strictly adhere to the following Git workflow:

### Branch Naming
Branches must be prefixed with the type of work, followed by a short, descriptive name (kebab-case):
- `feat/<task-name>`: New features
- `feature/<task-name>`: Alternate for new features
- `fix/<task-name>`: Bug fixes
- `chore/<task-name>`: Routine tasks, dependencies, setup
- `docs/<task-name>`: Documentation updates
- `refactor/<task-name>`: Code restructuring

### Commit Messages
Commits must follow the Conventional Commits standard:
`<type>(<optional scope>): <description>`

Examples:
- `feat(auth): implement JWT token rotation`
- `fix(ui): resolve button alignment issue on mobile`
- `chore: update database engine script`

---

### Context-Aware Commit & PR Policy
- **NEVER merge directly to `main`**. All changes must ultimately go through a Pull Request, but do NOT aggressively create PRs for every small prompt.
- **Context Awareness**: Understand the user's workflow. Are they iterating on a feature, or is the feature complete? Do not commit or push on every single conversational turn.
- **Interactive Commits**: When you believe a logical unit of work is done, ASK the user: "Should I commit these changes or do you want to continue working?"
- **Interactive PRs**: If the user tells you to commit, AFTER committing, ASK the user: "Should I create a Pull Request for this now?"
- **Explicit User Commands**: If the user explicitly says "commit" in their prompt, perform the commit, and then ask "Should I push this and create a PR?"
- **Autonomous God Review**: Once the user explicitly approves the creation of the PR, you MUST automatically invoke the "God Review" subagents on the PR diff.
- **DO NOT MERGE**: You are strictly forbidden from merging the Pull Request yourself. Your job ends at creating the PR and invoking the God Review. The user will manually merge the PR.
- **Merged PR Protection**: Before pushing commits to an existing branch, you MUST check if the associated PR has already been merged (e.g., using `gh pr view`). DO NOT push commits to a branch whose PR is already merged. If the PR is merged, you MUST checkout `main`, pull the latest changes, and create a brand new branch before committing.
- **Cross-Platform Path Formatting**: When invoking MCP tools, running local scripts, or interacting with the file system on Windows, you MUST format all absolute paths using standard Windows drive letters (e.g., `C:\Users\...`). NEVER use POSIX/Git Bash style paths (e.g., `/c/Users/...`) because native Windows tools (like MCP servers and Node.js) will fail to resolve them properly.
- **Execution Footer**: At the very end of every final response, you MUST append a standard footer estimating your token usage. Since you cannot view your actual telemetry natively, you must calculate a rough estimate of your input/output tokens. Format the footer EXACTLY like this:
  `---`
  `**⚡️ Execution Complete**`
  `*Estimated Token Usage: ~[Input Tokens] IN | ~[Output Tokens] OUT*`

---

# Engineering Review Agents

1. Architect Agent
2. Security Agent
3. Reliability Agent
4. Performance Agent
5. QA Agent

Minimum 3 approvals required.

---

# Golden Rule

Every solution should be understandable by a new engineer within 15 minutes.
