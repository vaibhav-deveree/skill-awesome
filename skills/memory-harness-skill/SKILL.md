---
name: memory-harness-skill
description: Implements a highly token-efficient, zero-hallucination memory harness system for tracking project state, context, and history across agent sessions.
---

# Memory Harness

The Memory Harness is an extremely token-efficient state-tracking system designed to maintain zero hallucination and massive context retention across sessions. It avoids blowing up the token window by organizing memory as an indexed network of linked pages rather than one massive file.

## Rule 1: Always Initialize the Harness
When starting work in a new project, you MUST verify if the `.memory/` directory exists in the project root. If it does not, you must initialize it with the following structure:
- `.memory/INDEX.md`
- `.memory/USER_INTENT.md`
- `.memory/CURRENT_STATE.md`
- `.memory/HISTORY.md`
- `.memory/CHANGELOG.md`

## Rule 2: Token-Efficient Compression (Caveman Style)
To maximize token efficiency, **all files MUST use terse, compressed language.**
- NO pleasantries. NO fluff.
- Use raw data formats: `[STATUS] task_name`, `[TODO] task_name`.
- Omit unnecessary filler words (e.g., instead of "The user wants us to build a login page", write `USER: Build login page`).

## Rule 3: The Index File (`INDEX.md`)
The `INDEX.md` is the only file agents read initially. It MUST contain only ultra-compressed state summaries and markdown links to the other files.
Example `INDEX.md`:
```markdown
# STATE
- [CURRENT] auth layer integration (See [CURRENT_STATE.md](file:///.memory/CURRENT_STATE.md))
- [NEXT] setup routing
- [USER] wants fast, secure login (See [USER_INTENT.md](file:///.memory/USER_INTENT.md))

# HISTORY
- [DONE] database schema (See [HISTORY.md](file:///.memory/HISTORY.md))
- [LOG] schema changes (See [CHANGELOG.md](file:///.memory/CHANGELOG.md))
```

## Rule 4: Team-Based Reading (Subagent Delegation)
The orchestrator agent (Master Architect) reads `INDEX.md`. If specialized work is required (e.g., backend logic), the Master Architect MUST spawn a specialized subagent (e.g., backend agent) and pass *only* the specific memory pointers (e.g., `file:///.memory/CURRENT_STATE.md`) to that subagent.
This bypasses massive token usage by ensuring agents only read the exact memory page they need.

## Rule 5: Zero Hallucination Updates
When work is done:
1. Update `CHANGELOG.md` with technical diffs.
2. Move the task from `CURRENT_STATE.md` to `HISTORY.md`.
3. Update `INDEX.md` to reflect the new state.
Always verify previous memory before overwriting to ensure no context is lost.
