---
name: universal-enterprise-multi-agent-code-review-&-production-readiness-skill
description: Universal Enterprise Multi Agent Code Review & Production Readiness Skill
---

# Universal Enterprise Multi-Agent Code Review & Production Readiness Skill

## Purpose

This skill is designed for ANY software project:

- SaaS Platforms
- Web Applications
- Mobile Applications
- Java/Spring Boot Services
- Microservices
- APIs
- AI/LLM Products
- Internal Enterprise Systems
- FinTech Applications
- Healthcare Applications
- E-Commerce Platforms

The objective is to identify realistic production risks while minimizing false positives through multiple independent review layers and a final verification board.

---

# Guiding Principles

1. Do not suggest feature additions.
2. Do not suggest redesigns unless required to fix a validated production issue.
3. Do not report style-only issues.
4. Do not report theoretical problems.
5. Every finding must be verified.
6. Every finding must survive a final review board.
7. Findings without evidence are rejected.

---

# PHASE 0 – Project Discovery

Before reviewing code, perform discovery.

Identify:

- Architecture
- Languages
- Frameworks
- Databases
- Queues
- Caches
- Deployment model
- Authentication model
- Authorization model
- External integrations
- Monitoring stack
- Logging stack
- Build system

Produce:

## Architecture Summary

## Technology Stack Summary

## Risk Surface Map

---

# PHASE 1 – Multi-Agent Deep Review

Spawn independent review agents.

Each agent works separately.

Agents must not see findings from other agents.

---

## Agent 1 – Frontend Engineer

Review:

- Components
- State Management
- Routing
- Rendering
- Forms
- Validation
- Accessibility
- Error Handling

Checks:

- Re-render loops
- Memory leaks
- State corruption
- UI race conditions
- Loading state failures

---

## Agent 2 – Backend Engineer

Review:

- Controllers
- Services
- Business Logic
- DTOs
- Mappers
- APIs

Checks:

- Logic bugs
- Validation gaps
- Contract mismatches
- Concurrency issues

---

## Agent 3 – Database Engineer

Review:

- Queries
- Indexes
- Transactions
- Locks

Checks:

- N+1 queries
- Missing indexes
- Deadlocks
- Full table scans

---

## Agent 4 – Performance Engineer

Review:

- Latency
- Throughput
- Resource Usage

Checks:

- Hot paths
- Expensive operations
- Scaling bottlenecks

---

## Agent 5 – Security Engineer

Review:

- Authentication
- Authorization
- Secrets
- Encryption

Checks:

- Access control issues
- Token handling
- Data leakage

---

## Agent 6 – Reliability Engineer

Review:

- Failure handling
- Retry logic
- Recovery logic

Checks:

- Unhandled exceptions
- Service degradation paths
- Recovery failures

---

## Agent 7 – QA Engineer

Review:

- User journeys
- Regression risks
- Edge cases

Checks:

- Broken flows
- Data inconsistencies
- Missing validation

---

## Agent 8 – Integration Engineer

Review:

- External APIs
- Webhooks
- Third-party services

Checks:

- Retry handling
- Rate limiting
- Mapping consistency

---

# PHASE 2 – Line-by-Line Inspection

Every file must be reviewed.

Inspect:

- Methods
- Classes
- Components
- Services
- Repositories
- Utilities

Look for:

- Null pointer risks
- Undefined access
- Race conditions
- Deadlocks
- Memory leaks
- Resource leaks
- Async issues
- Validation gaps

---

# PHASE 3 – Cross File Validation

Review interactions between:

- APIs
- DTOs
- Services
- Events
- Queues
- Shared libraries

Detect:

- Contract mismatches
- Circular dependencies
- Serialization issues
- Hidden coupling

---

# PHASE 4 – Worst Case Scenario Simulation

Simulate:

## Infrastructure Failures

- Database outage
- Cache outage
- Queue outage
- API outage

## User Behavior

- Double click
- Refresh during save
- Multiple tabs
- Concurrent users

## Data Problems

- Null values
- Corrupted values
- Duplicate values
- Partial responses

## Network Problems

- Timeout
- Packet loss
- Slow connections

---

# PHASE 5 – Finding Verification Layer

For EVERY finding:

Spawn a Verification Agent.

Responsibilities:

1. Verify file location.
2. Verify line number.
3. Verify code path.
4. Verify reproducibility.
5. Verify production impact.
6. Verify issue is not already handled.

Verification Result:

- VALIDATED
- REJECTED

Rejected findings are removed.

---

# PHASE 6 – Impact Analysis Layer

For every VALIDATED finding:

Spawn:

## Business Impact Agent

Evaluates:

- Revenue impact
- Customer impact
- Operational impact

## Production Impact Agent

Evaluates:

- Crash risk
- Data corruption risk
- Availability impact

## Scalability Agent

Evaluates:

- Impact at 10 users
- Impact at 100 users
- Impact at 1000 users
- Impact at 10000 users

---

# PHASE 7 – Final 4-Agent Review Board

This is mandatory.

Every finding must be reviewed by ALL four agents.

---

## Board Agent 1 – Principal Architect

Validates:

- Technical correctness
- Root cause accuracy
- Fix feasibility

Decision:

- Approve
- Reject

---

## Board Agent 2 – Principal QA

Validates:

- Reproducibility
- User impact
- Testability

Decision:

- Approve
- Reject

---

## Board Agent 3 – Principal Reliability Engineer

Validates:

- Production risk
- Recovery implications
- Stability concerns

Decision:

- Approve
- Reject

---

## Board Agent 4 – Engineering Manager

Validates:

- Priority
- Business value
- Implementation cost

Decision:

- Approve
- Reject

---

# Final Verdict Rules

A finding is included ONLY IF:

- At least 3 of 4 board members approve.

Otherwise:

STATUS = REJECTED

Reason must be documented.

---

# Finding Classification

Every approved finding must be classified as:

## Confirmed Production Bug

Must fix.

## Production Risk

Should fix.

## Technical Debt

Can be deferred.

## Monitoring Recommendation

Track but do not change.

## False Positive

Discard.

---

# Scoring Framework

Each finding receives:

| Metric | Score |
|----------|----------|
| Technical Accuracy | 0-10 |
| Reproducibility | 0-10 |
| Production Risk | 0-10 |
| Business Impact | 0-10 |
| Confidence | 0-10 |

---

# Required Finding Format

Priority:
- P0
- P1
- P2
- P3

Status:

Classification:

File:

Line Number:

Method:

Category:

Description:

Failure Scenario:

Root Cause:

Impact:

Recommended Fix:

Verification Result:

Board Votes:

Confidence Score:

---

# Implementation Plan

Generate:

## Phase 1 – P0

Release blockers.

## Phase 2 – P1

High-risk production issues.

## Phase 3 – P2

Medium-risk issues.

## Phase 4 – P3

Low-risk issues.

For each issue:

- Effort
- Risk
- Dependencies
- Rollout Strategy

---

# Final Executive Report

Include:

## Architecture Summary

## Review Coverage

## Validated Findings

## Rejected Findings

## False Positives

## Technical Debt

## Security Risks

## Reliability Risks

## Performance Risks

## Scalability Risks

## Integration Risks

## Database Risks

## Production Readiness Score (0-100)

## Go / No-Go Recommendation

Final recommendation must be based ONLY on validated findings approved by the Final 4-Agent Review Board.
