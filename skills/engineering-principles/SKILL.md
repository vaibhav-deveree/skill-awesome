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

### Pull Request & Review Policy (The God Review)
- **NEVER merge directly to `main`**. All changes must go through a Pull Request.
- **Proper PR Descriptions**: Every PR must include a comprehensive description of the problem, the solution, and the architectural impact.
- **The God Review**: Once a PR is created, it MUST undergo a final, exhaustive "God Review" (a multi-agent comprehensive review of security, architecture, frontend, and backend code quality) before it can be merged into `main`.

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
