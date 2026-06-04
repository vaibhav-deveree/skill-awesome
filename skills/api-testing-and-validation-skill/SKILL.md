---
name: api-testing-and-validation-skill
description: Comprehensive API testing skill focusing on deep flow validation, edge cases, response structures, and simulating production readiness via a total mockup report.
---

# API Testing and Validation Skill

## Purpose
This skill ensures an API or feature is fundamentally indestructible before going to production. It mandates an ultra-deep understanding of the feature's logic, complete mapping of success and failure flows, and a rigorous simulation of every conceivable edge case, culminating in a "Total Mockup Report."

---

## PHASE 0: Deep Knowledge Acquisition
Before testing or executing any API calls, you MUST acquire an ultra-deep understanding of how the feature works.
1. **Read the Source Code**: Trace the exact logic from Controller -> Service -> Repository/DB.
2. **Understand the Contracts**: Analyze request DTOs, response DTOs, Headers, and Authentication requirements.
3. **Map the Dependencies**: What third-party APIs, queues, or caches does this feature rely on?

---

## PHASE 1: Flow Mapping & Test Case Generation
You must map out EVERY possible scenario. Do not stick to the "happy path."

### 1. Success Flows (Happy Path)
- Standard execution with typical payloads.
- Responses must match exact expected schema.
- Status codes must be strictly compliant (e.g., 200 OK, 201 Created).

### 2. Failure Flows (Unhappy Path)
- Invalid payloads (missing fields, wrong types).
- Unauthorized / Unauthenticated requests (401, 403).
- Not Found scenarios (404).
- Dependency failures (Database timeout, third-party API 5xx errors).

### 3. Edge Cases & Malicious Input (Deep Down Check)
- **Boundary Testing**: Maximum length strings, extremely large integers, negative numbers where positive is expected.
- **Null & Empty Values**: Empty arrays, null objects, whitespace-only strings.
- **Concurrency & Rate Limits**: Race conditions, duplicate requests (idempotency check), throttling limits.
- **Injection & Payload Attacks**: Malformed JSON, unexpected extra fields in payload (mass assignment).

---

## PHASE 2: Execution & Response Validation
When executing tests (whether statically reviewing the code paths or dynamically querying a live dev server via Bash/cURL), you must check:
1. **Response Structure**: Does the JSON payload perfectly match the documented contract? Are there missing fields?
2. **Error Formatting**: Are error messages safe? (They must NOT expose stack traces or internal database column names).
3. **Headers**: Are security headers present? Are pagination headers accurate?
4. **State Mutations**: Did the database actually update correctly? Were side effects (like sending emails) triggered appropriately?

---

## PHASE 3: Total Mockup Report (Production Readiness)
Before signing off on the feature and allowing it to go live, you MUST generate a `Test_Mockup_Report.md`. This report simulates the entire testing lifecycle.

### Report Structure:
1. **Feature Deep Dive**: A 2-paragraph summary of how the feature actually works under the hood.
2. **Success Flow Scenarios**: Detailed logs of inputs and simulated expected outputs.
3. **Failure Flow Scenarios**: Detailed logs of inputs and expected error responses.
4. **Edge Case Matrix**: A table showing the exact edge cases tested and how the system defended against them.
5. **Vulnerability Assessment**: Any potential loopholes discovered during testing.
6. **Go/No-Go Decision**: Explicit approval or rejection of the feature based on the findings.
