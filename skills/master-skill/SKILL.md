---
name: master-skill
description: master skill
---

# Master Skill Orchestrator

## Purpose

This is the entry point for all engineering skills.

Every user request must first pass through this orchestrator before any specialized skill is executed.

The orchestrator is responsible for:

* Understanding user intent
* Identifying required skills
* Loading appropriate skills
* Coordinating multiple skills
* Resolving conflicts between skills
* Producing a validated final response

---

# Workflow

```text
User Request
      │
      ▼
Intent Analysis
      │
      ▼
Skill Selection
      │
      ▼
Skill Execution
      │
      ▼
Cross Skill Validation
      │
      ▼
Final Review
      │
      ▼
Response
```

---

# Step 1 – Intent Analysis

Analyze the request.

Determine:

* What is the user trying to achieve?
* What artifacts are involved?
* What technologies are involved?
* Is the request development related?
* Is the request architecture related?
* Is the request deployment related?
* Is the request review related?

---

# Step 2 – Skill Discovery

Select required skills.

Examples:

---

## Backend Development

Load:

* Backend Architecture Skill
* Security Skill
* Performance Skill

---

## Frontend Development

Load:

* Frontend Architecture Skill
* Accessibility Skill
* Performance Skill

---

## Full Stack Feature

Load:

* Backend Architecture Skill
* Frontend Architecture Skill
* Security Skill
* Testing Skill

---

## Code Review

Load:

* Multi-Agent Code Review Skill

---

## Deployment

Load:

* Deployment Skill
* Security Skill
* Reliability Skill

---

## Database Work

Load:

* Backend Skill
* Database Review Skill
* Performance Skill

---

## Authentication

Load:

* Backend Skill
* Security Skill

Additional Review:

* Session vs Token Analysis

---

## Multi-Tenant Systems

Load:

* Backend Skill
* Security Skill
* Database Skill

Additional Review:

* Tenant Isolation
* Authorization
* Data Segregation

---

# Step 3 – Skill Priority

Priority Order:

```text
Security
      ↓
Reliability
      ↓
Architecture
      ↓
Performance
      ↓
Maintainability
      ↓
Developer Experience
```

Security and reliability always override convenience.

---

# Step 4 – Mandatory Global Rules

Apply these rules regardless of project type.

---

## Rule 1

Prefer reusable solutions.

Do not create duplicate functionality.

---

## Rule 2

Prefer extending existing APIs over creating new APIs.

---

## Rule 3

Controllers must not contain business logic.

---

## Rule 4

Business logic belongs in services.

---

## Rule 5

Always review:

* Null safety
* Exception handling
* Edge cases

---

## Rule 6

Always review:

* N+1 queries
* Index usage
* Query performance

---

## Rule 7

Always review:

* Authentication
* Authorization
* OWASP

---

## Rule 8

Always review:

* Responsive design
* Accessibility
* Mobile usability

---

## Rule 9

Prefer side panels over modals.

Use modals only when necessary.

---

## Rule 10

Always reuse existing components before creating new ones.

---

## Rule 11

Always reuse existing APIs before creating new APIs.

---

## Rule 12

Every implementation must consider:

* Monitoring
* Logging
* Error handling

---

## Rule 13

Mandatory Implementation Plan: Whenever a user requests a new feature, you MUST create a comprehensive implementation plan that explicitly covers:
- Backend Architecture
- Frontend Architecture
- System Architecture
- Security Architecture

---

## Rule 14

Centralized Plans Directory: You MUST create and store all implementation plans in a dedicated directory located at `.memory/plans/` to integrate with the memory harness.

---

## Rule 15

Mandatory Task Tracking: You MUST create a `task.md` artifact when beginning execution. You must use this file to track all task progress and codebase changes systematically while implementing the task.

---

# Step 5 – Agent Assignment

Deploy specialized agents based on request type.

Examples:

Backend Request:

* Architecture Agent
* Security Agent
* Database Agent
* Reliability Agent

Frontend Request:

* UI Agent
* UX Agent
* Accessibility Agent
* Performance Agent

Deployment Request:

* Infrastructure Agent
* Security Agent
* Monitoring Agent

Review Request:

* Multi-Agent Review Framework

---

# Step 6 – Cross Skill Validation

When multiple skills are used:

Verify:

* No conflicting recommendations
* No duplicated work
* No security violations
* No performance regressions

---

# Step 7 – Final Review Board

Before producing output:

Deploy:

### Principal Architect

### Principal Security Engineer

### Principal Reliability Engineer

### Engineering Manager

Verify:

* Technical correctness
* Security compliance
* Reliability compliance
* Business practicality

---

# Final Response Requirements

Every response should be:

* Actionable
* Structured
* Maintainable
* Secure
* Performant
* Production-ready

---

# Golden Rule

Never immediately solve a problem.

First determine which skills are required.

Then execute the relevant skills.

Then validate the combined result before responding.
