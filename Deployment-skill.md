# Universal Deployment & Production Operations Skill

## Purpose

This skill defines the standard deployment architecture, infrastructure choices, monitoring stack, security requirements, and operational guidelines for deploying modern applications with minimal cost while maintaining production-grade reliability.

This framework is optimized for:

* Startups
* SaaS Products
* AI Applications
* Internal Tools
* Vibe-Coded Projects
* MVPs
* Small Teams
* Solo Founders

The objective is:

* Fast deployment
* Low operational overhead
* Production readiness
* Cost efficiency
* Scalability

---

# Core Philosophy

Before deploying any application:

Prioritize:

1. Reliability
2. Simplicity
3. Monitoring
4. Security
5. Cost Optimization

Avoid infrastructure complexity until necessary.

---

# Recommended Free Tier Stack

## Frontend Hosting

### Preferred

#### Vercel

Best For:

* React
* Next.js
* Static Sites

Benefits:

* Free tier
* Global CDN
* Easy deployments
* Preview deployments

---

### Alternative

#### Netlify

Best For:

* Static sites
* Small applications

---

# Backend Hosting

## Preferred

### Render

Best For:

* Node.js
* Java
* Spring Boot
* Python
* Go

Benefits:

* Simple deployment
* Managed infrastructure
* Easy scaling

---

### Alternatives

#### Railway

#### Fly.io

#### Koyeb

#### Northflank

---

# Database Layer

## Preferred

### Neon

Recommended For:

* PostgreSQL
* SaaS products
* AI products

Benefits:

* Generous free tier
* Branching support
* Serverless architecture

---

### Alternative

### Supabase

Benefits:

* PostgreSQL
* Authentication
* Storage
* Realtime

Excellent for MVPs.

---

# Object Storage

## Preferred

### Cloudflare R2

Benefits:

* Low cost
* No egress fees

---

### Alternative

### Supabase Storage

Suitable for:

* Images
* Reports
* Documents

---

# Authentication

## Preferred

### Clerk

For:

* SaaS
* AI applications

Benefits:

* Easy integration
* Social login
* Security features

---

### Alternative

### Supabase Auth

Good for:

* MVPs
* Small applications

---

# Monitoring Stack

Monitoring is mandatory.

Never deploy without monitoring.

---

## Error Monitoring

### Preferred

#### Sentry

Monitor:

* Frontend errors
* Backend exceptions
* Performance issues

Track:

* Error frequency
* Stack traces
* User impact

---

## Uptime Monitoring

### Preferred

#### Better Stack

Monitor:

* API uptime
* Website uptime
* SSL status

---

### Alternative

#### UptimeRobot

---

## Logging

### Preferred

#### Better Stack Logs

Collect:

* Application logs
* Error logs
* Request logs

---

# Analytics

## Product Analytics

### Preferred

#### PostHog

Track:

* User actions
* Conversion funnels
* Feature adoption

---

# Email Infrastructure

## Preferred

### Resend

For:

* Verification emails
* Notifications
* Reports

Benefits:

* Developer friendly
* Generous free tier

---

# Background Jobs

## Preferred

### Trigger.dev

For:

* Scheduled jobs
* Long-running tasks
* Report generation

---

# Security Standards

## Secrets Management

Never:

* Commit secrets
* Store API keys in code

Always:

* Use environment variables

---

## HTTPS

Mandatory:

* All environments
* All APIs

---

## OWASP Review

Before deployment review:

* Authentication
* Authorization
* Input validation
* Rate limiting
* Dependency vulnerabilities

---

# Database Review Before Deployment

Review:

## N+1 Queries

Mandatory review.

---

## Missing Indexes

Review:

* Search columns
* Filter columns
* Foreign keys

---

## Query Performance

Review:

* Slow queries
* Full table scans

---

# API Review Before Deployment

Review:

## Duplicate APIs

Before creating a new endpoint ask:

1. Can an existing endpoint be reused?
2. Can an existing response be extended?

Avoid API duplication.

---

## Authentication Review

Determine:

### Session-Based

or

### Token-Based

Default recommendation:

Token-based authentication for:

* SaaS
* APIs
* Mobile Apps

Document reasoning.

---

# CI/CD Standards

## Source Control

Preferred:

### GitHub

---

## Deployment Pipeline

Required:

### Pull Request

↓

### Automated Checks

↓

### Review

↓

### Merge

↓

### Deploy

---

# Required Deployment Checks

Before every deployment verify:

## Frontend

✓ Build succeeds

✓ No console errors

✓ Responsive review completed

✓ Sentry configured

---

## Backend

✓ Build succeeds

✓ Database migrations verified

✓ Environment variables configured

✓ Error handling reviewed

---

## Database

✓ Migrations tested

✓ Index review completed

✓ Backup strategy verified

---

## Security

✓ Secrets secured

✓ OWASP review completed

✓ Authentication reviewed

✓ Authorization reviewed

---

## Monitoring

✓ Sentry configured

✓ Uptime monitoring configured

✓ Logging configured

---

# Multi-Agent Deployment Review

Before production deployment deploy:

---

## Agent 1 – Infrastructure Reviewer

Checks:

* Hosting setup
* Environment configuration

---

## Agent 2 – Security Reviewer

Checks:

* Secrets
* Authentication
* OWASP compliance

---

## Agent 3 – Database Reviewer

Checks:

* Migrations
* Indexes
* Query performance

---

## Agent 4 – Reliability Reviewer

Checks:

* Failure handling
* Recovery mechanisms

---

## Agent 5 – Monitoring Reviewer

Checks:

* Sentry
* Logging
* Alerts

---

## Agent 6 – Cost Reviewer

Checks:

* Free tier usage
* Infrastructure efficiency

---

## Agent 7 – Performance Reviewer

Checks:

* API performance
* Frontend performance

---

# Final Production Review Board

Every deployment must be approved by:

### Principal Engineer

### Security Engineer

### Reliability Engineer

### Infrastructure Engineer

Minimum:

3 Approvals Required

---

# Recommended Startup Stack

For most projects:

Frontend:

* Vercel

Backend:

* Render

Database:

* Neon

Authentication:

* Clerk

Monitoring:

* Sentry

Analytics:

* PostHog

Email:

* Resend

Storage:

* Cloudflare R2

Uptime Monitoring:

* Better Stack

This stack can support a surprisingly large number of users before requiring significant infrastructure changes.

---

# Golden Rule

Do not optimize for scale you do not yet have.

Start simple.

Deploy safely.

Monitor everything.

Fix issues based on real production data.

Scale only when usage demands it.
