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
