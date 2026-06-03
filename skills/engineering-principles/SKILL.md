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
