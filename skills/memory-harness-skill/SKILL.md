---
name: memory-harness-skill
description: Implements a highly token-efficient, zero-hallucination SQLite database memory harness for tracking project state, context, and history across agent sessions.
---

# Database-Backed Memory Harness

The Memory Harness is an extremely token-efficient, database-backed state-tracking system designed to maintain zero hallucination and massive context retention across sessions. By using a local SQLite database instead of reading massive Markdown files, agents consume minimal tokens to fetch exactly the context they need.

## Rule 1: Always Initialize the Harness
When starting work in a new project, you MUST verify if the `.memory/memory.db` file exists. If it does not, you must initialize it using the provided DB Engine script:
1. Ensure the `db_engine.py` script from this skill is placed inside the project's `.memory/` directory.
2. Run `python .memory/db_engine.py init` to generate the database tables (`intent`, `state`, `history`, `changelog`, `architecture`).

## Rule 2: Token-Efficient Querying
To maximize token efficiency, NEVER read the entire database. Use specific SQL queries via the wrapper script to fetch only the rows you need right now.
Example:
`python .memory/db_engine.py query "SELECT * FROM state WHERE status = 'IN_PROGRESS'"`
`python .memory/db_engine.py query "SELECT * FROM intent ORDER BY timestamp DESC LIMIT 3"`

## Rule 3: Updating State (Zero Hallucination)
When you complete a task or make a decision, you MUST log it to the database immediately to ensure zero hallucination for future agents.
Use the built-in CLI commands to log changes:
- **Intent**: `python .memory/db_engine.py log_intent --category "feature" --content "User wants a login page"`
- **State**: `python .memory/db_engine.py log_state --status "TODO" --task "Setup routing" --assigned_to "frontend-agent"`
- **History**: `python .memory/db_engine.py log_history --task "Database schema" --outcome "Created user and posts tables"`
- **Architecture (Brownfield)**: `python .memory/db_engine.py log_architecture --component "frontend" --structure "React SPA in /src"`
- **Changelog**: `python .memory/db_engine.py log_changelog --file "src/App.js" --description "Added routing wrapper"`

## Rule 4: Team-Based Workflows
The orchestrator agent (Master Architect) acts as the dispatcher. It queries the database to determine the current `TODO` tasks, then spawns specialized subagents (e.g., frontend-agent, backend-agent). The Master Architect instructs the subagent to query the database themselves for context, entirely bypassing the Master Architect's own token limits.

## Rule 5: Raw SQL Power
If you need complex analysis across the project's history, you can execute raw SQL joins using the `query` command.
Example: `python .memory/db_engine.py query "SELECT h.completed_task, c.file_changed FROM history h JOIN changelog c ON date(h.timestamp) = date(c.timestamp)"`
