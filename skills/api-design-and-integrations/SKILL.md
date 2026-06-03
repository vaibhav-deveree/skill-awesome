---
name: api-design-and-integrations
description: api design and integrations
---


# Universal API Design & Integration Skill

## API Design Principles

APIs should be:

* Predictable
* Versionable
* Observable
* Secure

---

# Before Creating A New API

Mandatory Questions:

1. Does an API already exist?
2. Can an existing API be extended?
3. Can frontend reuse existing response?

Do not create duplicate APIs.

---

# REST Standards

Use:

```text
GET
POST
PUT
PATCH
DELETE
```

according to intent.

---

# API Response Standards

Success:

```json
{
  "data": {},
  "meta": {}
}
```

Failure:

```json
{
  "errorCode": "",
  "message": "",
  "correlationId": ""
}
```

---

# Pagination Standards

Mandatory for list APIs.

Support:

* page
* size
* sort

---

# Integration Standards

External integrations must have:

* Timeout
* Retry policy
* Circuit breaker
* Monitoring

Never call third-party APIs directly from business logic.

---

# Integration Review Agents

1. API Architect
2. Backend Engineer
3. Security Engineer
4. Integration Engineer

---

# Final Checklist

✓ Request validation

✓ Response validation

✓ Authentication

✓ Authorization

✓ Pagination

✓ Monitoring

✓ Retry handling
