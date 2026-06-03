

# Universal Database Design & Data Architecture Skill

## Purpose

Define standards for:

* SQL
* NoSQL
* Multi-Tenant Systems
* SaaS Platforms

---

# Naming Standards

Use clear names.

Good:

```text
candidate_sessions
candidate_reports
user_permissions
```

Avoid:

```text
tbl1
tmp
data
```

---

# Query Standards

Review:

* N+1 queries
* Missing indexes
* Full table scans
* Large joins

---

# Pagination

Never return unlimited data.

Mandatory:

* Limit
* Offset
* Cursor

---

# Multi-Tenancy

Review:

* Tenant isolation
* Query filters
* Cache separation

Every query must be tenant-safe.

---

# Migration Standards

Migration must be:

* Rollback capable
* Backward compatible

---

# Database Review Agents

1. Database Architect
2. Performance Engineer
3. Reliability Engineer
4. Backend Engineer

---

# Final Checklist

✓ N+1 reviewed

✓ Index review completed

✓ Query review completed

✓ Migration review completed

✓ Multi-tenancy reviewed
