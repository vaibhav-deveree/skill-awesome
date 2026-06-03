---
name: skill-execution-framework
description: skill execution framework
---



# Universal Skill Execution Framework

## Purpose

This document defines how all skills within the Engineering Skills Repository are executed, orchestrated, validated, and reviewed.

This file acts as the runtime execution contract for all engineering skills.

It ensures:

* Consistency
* Predictability
* Cross-skill collaboration
* Quality enforcement
* Security compliance
* Reliability validation

Every task must follow this framework.

---

# Execution Hierarchy

All requests follow the same execution hierarchy.

```text id="zntk5e"
User Request
        ↓
Master Skill
        ↓
Engineering Principles
        ↓
Skill Discovery
        ↓
Skill Execution
        ↓
Cross Skill Validation
        ↓
Agent Review
        ↓
Final Review Board
        ↓
Final Output
```

No skill should execute independently.

---

# Step 1 – Request Analysis

The Master Skill is always executed first.

Responsibilities:

* Understand intent
* Understand project type
* Understand technology stack
* Understand scope
* Determine required skills

Questions:

1. What is the user trying to achieve?
2. Is this architecture work?
3. Is this development work?
4. Is this review work?
5. Is this deployment work?
6. Is this security work?
7. Is this testing work?

---

# Step 2 – Engineering Principles Loading

Mandatory.

Before any skill executes:

Load:

```text id="m4l7cu"
engineering-principles.md
```

These principles override all other skills.

Priority:

1. Simplicity
2. Security
3. Reliability
4. Maintainability
5. Performance

---

# Step 3 – Skill Discovery

Determine required skills.

---

## Backend Development

Load:

```text id="mwuxza"
backend-achitecture skill.md

api-design-and-integrations.md

database-design-and-data-architecture.md

security-architecture.md

testing-and-quality-engineering.md
```

---

## Frontend Development

Load:

```text id="j7ewik"
Frontend arch skill.md

api-design-and-integrations.md

testing-and-quality-engineering.md
```

---

## Full Stack Feature

Load:

```text id="0e3gnh"
backend-achitecture skill.md

Frontend arch skill.md

api-design-and-integrations.md

database-design-and-data-architecture.md

security-architecture.md

testing-and-quality-engineering.md
```

---

## Architecture Design

Load:

```text id="c25zlx"
system-design-and-architecture-review.md

security-architecture.md

database-design-and-data-architecture.md
```

---

## Code Review

Load:

```text id="h4j0cn"
Universal Enterprise Multi-Agent Code Review & Production Readiness Skill.md
```

---

## Deployment

Load:

```text id="5ub9eq"
Deployment-skill.md

security-architecture.md

production-readiness-review.md
```

---

## AI Systems

Load:

```text id="p5cq5l"
ai-engineering-and-llm-systems.md

security-architecture.md

testing-and-quality-engineering.md
```

---

# Step 4 – Multi Skill Execution

Each skill executes independently.

Rules:

* Skills must not overwrite each other.
* Skills must remain within their responsibility.
* Skills may provide recommendations.
* Skills may raise conflicts.

Output:

```text id="w4k6w6"
Skill Findings
Skill Recommendations
Skill Risks
Skill Approvals
```

---

# Step 5 – Conflict Resolution

When skills disagree:

Priority Order:

```text id="r8g1n3"
engineering-principles.md

security-architecture.md

testing-and-quality-engineering.md

system-design-and-architecture-review.md

backend-achitecture skill.md

Frontend arch skill.md

api-design-and-integrations.md

database-design-and-data-architecture.md

Deployment-skill.md
```

Higher priority wins.

Example:

If Performance recommends something that weakens Security:

Security wins.

---

# Step 6 – Cross Skill Validation

Perform cross-skill review.

Review:

* Architecture consistency
* Security compliance
* Reliability compliance
* API consistency
* Database consistency
* Testing coverage

Questions:

1. Does backend align with database?
2. Does frontend align with APIs?
3. Does deployment align with security?
4. Does architecture align with scalability goals?

---

# Step 7 – Agent Assignment

Agents are dynamically assigned.

---

## Architecture Agent

Reviews:

* Design
* Maintainability
* Scalability

---

## Security Agent

Reviews:

* OWASP
* Authentication
* Authorization
* Secrets

---

## Reliability Agent

Reviews:

* Failure handling
* Recovery
* Resilience

---

## Performance Agent

Reviews:

* Database
* APIs
* Rendering
* Resource utilization

---

## QA Agent

Reviews:

* User journeys
* Edge cases
* Testability

---

## Integration Agent

Reviews:

* External systems
* Retry logic
* Contracts

---

# Step 8 – Mandatory Finding Verification

Every finding must be challenged.

Verification Questions:

1. Is it reproducible?
2. Is it realistic?
3. Is it already handled?
4. Is it framework protected?
5. Is it worth fixing?

Possible Outcomes:

```text id="7w31cl"
VALIDATED

REJECTED

MONITOR_ONLY
```

---

# Step 9 – Review Board

Every task passes through the review board.

---

## Principal Architect

Validates:

* Architecture
* Maintainability

Decision:

* Approve
* Reject

---

## Principal Security Engineer

Validates:

* Security
* Compliance

Decision:

* Approve
* Reject

---

## Principal Reliability Engineer

Validates:

* Stability
* Recovery

Decision:

* Approve
* Reject

---

## Engineering Manager

Validates:

* Business value
* Complexity
* Priority

Decision:

* Approve
* Reject

---

# Review Board Rules

Approval Requirements:

```text id="3k2yq6"
Minimum 3 of 4 approvals
```

Otherwise:

```text id="d1n2ca"
STATUS = REJECTED
```

Reason must be documented.

---

# Final Response Requirements

Every response should contain:

## Summary

## Risks

## Recommendations

## Security Review

## Reliability Review

## Testing Requirements

## Deployment Considerations

## Final Verdict

---

# Skill Categories

The framework supports:

## Architecture

* Backend
* Frontend
* Database
* System Design

---

## Development

* APIs
* Integrations
* Features

---

## Quality

* Testing
* Reviews
* Production Readiness

---

## Security

* Authentication
* Authorization
* Compliance

---

## Operations

* Deployment
* Monitoring
* Reliability

---

## AI

* Prompt Engineering
* Agents
* LLM Systems

---

# Golden Rules

Rule 1

Never execute implementation before understanding requirements.

---

Rule 2

Never create new APIs when existing APIs can be reused.

---

Rule 3

Never create duplicate components when reusable components exist.

---

Rule 4

Never bypass security reviews.

---

Rule 5

Never bypass testing reviews.

---

Rule 6

Every task must be reviewed from:

* Architecture
* Security
* Reliability
* Performance
* Quality

perspectives.

---

Rule 7

Every recommendation should be evidence based.

---

Rule 8

Every finding must be validated before it becomes an action item.

---

# Final Principle

The goal of this framework is not to generate more work.

The goal is to ensure that every engineering decision is:

* Secure
* Reliable
* Maintainable
* Scalable
* Cost Effective
* Production Ready

before it reaches implementation.
