# Universal Backend Architecture & Engineering Standards Skill

## Purpose

This skill defines the backend engineering standards, architecture principles, review processes, and implementation guidelines that must be followed across all projects regardless of programming language, framework, or cloud provider.

Supported Technologies:

* Java
* Spring Boot
* Node.js
* Python
* Go
* .NET
* Rust
* PHP
* Ruby
* Any Backend Framework

This document focuses on:

* Maintainability
* Scalability
* Security
* Reliability
* Performance
* Readability
* Consistency

---

# Core Philosophy

Backend systems should be:

1. Easy to understand
2. Easy to maintain
3. Easy to debug
4. Easy to scale
5. Secure by default
6. Observable by default

Every engineer should be able to understand the codebase without requiring tribal knowledge.

---

# Architecture Principles

## Single Responsibility Principle

Each component should have one responsibility.

Bad:

```text
Controller
 ├── Validation
 ├── Business Logic
 ├── Database Access
 ├── External API Calls
 └── Response Mapping
```

Good:

```text
Controller
     ↓
Service
     ↓
Repository
     ↓
Database
```

---

# Layer Responsibilities

## Controller Layer

Responsibilities:

* Accept requests
* Validate request format
* Call services
* Return responses

Controller MUST NOT:

* Contain business logic
* Perform database operations
* Call repositories directly
* Perform calculations
* Contain complex conditionals

Controllers should remain thin.

---

## Service Layer

Responsibilities:

* Business logic
* Orchestration
* Validation of business rules
* Workflow management

Service Layer SHOULD:

* Be reusable
* Be testable
* Be framework independent

---

## Repository/Data Access Layer

Responsibilities:

* Database interaction
* Query execution
* Data retrieval
* Persistence

Repository MUST NOT:

* Contain business rules
* Contain workflow logic

---

## Integration Layer

Responsibilities:

* External APIs
* Webhooks
* Third-party systems

Every external integration should have its own abstraction layer.

Never mix external API logic inside business services.

---

# Naming Standards

## General Rules

Names should explain intent.

Avoid:

```text
doStuff()
process()
data()
temp()
manager()
```

Prefer:

```text
createInterviewSession()
validateCandidateAccess()
generateFraudReport()
syncCandidateFromATS()
```

---

## Service Naming

Pattern:

```text
<Entity><Action>Service
```

Examples:

```text
InterviewService
CandidateService
ReportGenerationService
BillingService
```

---

## Repository Naming

Pattern:

```text
<Entity>Repository
```

Examples:

```text
CandidateRepository
SessionRepository
ReportRepository
```

---

## Controller Naming

Pattern:

```text
<Entity>Controller
```

Examples:

```text
SessionController
ReportController
IntegrationController
```

---

# API Design Standards

## Reuse Existing APIs

Before creating a new API:

Mandatory Review:

1. Does an existing endpoint provide this data?
2. Can existing response be extended?
3. Can response fields be reused?

Never create duplicate APIs for the same data.

---

## API Versioning

Version APIs when breaking changes are introduced.

Avoid unnecessary versions.

---

## Response Consistency

All APIs should return:

```text
Success Response

Data
Metadata
Pagination (if applicable)
```

```text
Failure Response

Error Code
Error Message
Correlation Id
```

---

# Authentication Standards

## Authentication Review

Before implementation evaluate:

### Session-Based Authentication

Pros:

* Easy invalidation
* Centralized control

Cons:

* Requires session storage
* Horizontal scaling complexity

---

### Token-Based Authentication

Pros:

* Better scalability
* Stateless
* Microservice friendly

Cons:

* Revocation complexity

---

## Recommendation

Default recommendation:

### Token-Based Authentication

Use when:

* APIs
* Mobile Apps
* SaaS Platforms
* Microservices

### Session-Based Authentication

Use when:

* Internal systems
* Traditional web applications

Document decision with reasoning.

---

# Authorization Standards

Every protected resource must validate:

* User identity
* Role
* Permission
* Resource ownership

Never trust client-side authorization.

---

# Multi-Tenancy Standards

If application is multi-tenant:

Review:

* Tenant isolation
* Data access boundaries
* Query filtering
* Caching isolation
* Storage isolation

Every database query must be validated for tenant safety.

---

# Database Standards

## Query Review

Review every query for:

* N+1 issues
* Missing indexes
* Full table scans
* Large joins
* Unbounded queries

---

## N+1 Query Detection

Mandatory review:

```text
Parent Query
     ↓
Loop
     ↓
Additional Query
```

N+1 patterns must be eliminated.

---

## Pagination

All list endpoints must support pagination.

Never return unbounded datasets.

---

## Index Review

Verify indexes exist for:

* Search fields
* Foreign keys
* Filtering fields
* Sorting fields

---

# Performance Standards

## Performance Review Required For

* New APIs
* Query changes
* Integration changes
* Batch jobs

Review:

* CPU usage
* Memory usage
* Database load
* Network calls

---

## API Performance

Review:

* Duplicate queries
* Redundant calculations
* Unnecessary transformations

---

## Caching

Use caching when:

* Data changes infrequently
* Data is expensive to compute

Never cache sensitive tenant data incorrectly.

---

# Reliability Standards

Every implementation must consider:

## Failure Handling

What happens when:

* Database is unavailable
* API fails
* Queue fails
* Cache fails

---

## Retry Policies

Retries should be:

* Controlled
* Limited
* Idempotent

Avoid infinite retries.

---

# Exception Handling Standards

Every implementation must include:

## Exception Review

Verify:

* No unhandled exceptions
* No silent failures
* No swallowed exceptions

Review:

* Null references
* Missing values
* Invalid states

---

## Null Safety Review

Mandatory after every implementation.

Review:

* Null references
* Missing dependencies
* Optional values
* Empty collections

Every code review must include a dedicated Null Safety pass.

---

# Security Standards

Follow:

## OWASP Top 10

Mandatory review:

* Broken Access Control
* Cryptographic Failures
* Injection
* Insecure Design
* Security Misconfiguration
* Vulnerable Components
* Authentication Failures
* Integrity Failures
* Logging Failures
* SSRF

---

# Logging Standards

Log:

* Errors
* Security events
* Integration failures

Never log:

* Passwords
* Tokens
* Secrets
* Sensitive user information

---

# Backend Review Workflow

Every implementation must go through:

---

## Agent 1 - Architecture Reviewer

Checks:

* Layer separation
* Service boundaries
* Reusability

---

## Agent 2 - Business Logic Reviewer

Checks:

* Correctness
* Edge cases
* Rule validation

---

## Agent 3 - Database Reviewer

Checks:

* Query efficiency
* N+1
* Index usage

---

## Agent 4 - Security Reviewer

Checks:

* OWASP
* Authorization
* Authentication

---

## Agent 5 - Performance Reviewer

Checks:

* Scalability
* Resource usage

---

## Agent 6 - Reliability Reviewer

Checks:

* Failure handling
* Recovery logic

---

## Agent 7 - Null Safety Reviewer

Checks:

* Null pointers
* Optional handling
* Invalid states

---

## Agent 8 - Integration Reviewer

Checks:

* External APIs
* Retry logic
* Error handling

---

# Final Review Board

Every implementation must be reviewed by:

### Principal Architect

### Principal Backend Engineer

### Principal Security Engineer

### Principal Reliability Engineer

Each provides:

* Approve
* Reject
* Changes Required

Minimum 3 approvals required.

---

# Final Checklist

Before merging:

✓ No business logic in controllers

✓ Proper service separation

✓ Proper repository separation

✓ Authentication reviewed

✓ Authorization reviewed

✓ Multi-tenancy reviewed

✓ OWASP reviewed

✓ N+1 reviewed

✓ Index review completed

✓ Performance review completed

✓ Null safety review completed

✓ Exception handling reviewed

✓ Integration review completed

✓ Final board approval completed

---

# Golden Rule

Every implementation should be understandable by a new engineer within minutes.

If a solution is difficult to understand, difficult to debug, or difficult to maintain, it should be simplified before being merged.
