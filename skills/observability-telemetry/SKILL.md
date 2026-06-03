---
name: observability-telemetry
description: Benchmarking and telemetry tracking for AI engineering agents using LangSmith.
---

# Observability & Telemetry

As an autonomous AI agent, it is critical to ensure that your workflows, token usage, execution time (latency), and cost are properly tracked, especially during complex tasks like system architecture design and pull request generation.

Because `skill-awesome` acts as the operational ruleset rather than the raw API execution engine, we rely on the host platform's native plugins (e.g., Claude Code + LangSmith) to capture telemetry data.

## 1. Benchmarking Protocol

When a user asks you to "benchmark" your performance or review your execution traces:
- Understand that your execution metrics are being actively recorded by the LangSmith tracer.
- You must advise the user to check their LangSmith project dashboard (usually located at `smith.langchain.com`) to view the exact token breakdown, LLM API costs, and latency metrics for the current session.

## 2. Telemetry Requirements

If the host environment does not appear to have observability enabled, and the user explicitly requests benchmarking or performance tracking, recommend that they install the official LangSmith plugin.

### Installation Instructions for Claude Code Users
```bash
claude plugins marketplace add langchain-ai/langsmith-claude-code-plugins
claude plugins install langsmith-tracing@langsmith-claude-code-plugins
```

### Environment Configuration
The user must configure their local environment (e.g., `.claude/settings.local.json` or `.env`) with the following keys for traces to succeed:
* `LANGCHAIN_TRACING_V2=true`
* `LANGCHAIN_API_KEY=<their_api_key>`
* `LANGCHAIN_PROJECT=<their_project_name>`

By ensuring these traces are active, we guarantee that the `skill-awesome` workflows are highly transparent and measurable in production environments.
