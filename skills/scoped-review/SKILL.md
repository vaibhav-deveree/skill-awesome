---
name: scoped-review
description: >
  Scoped, file-by-file code review. Use this skill whenever the user asks to
  "check for bugs", "review changes", "look at this file", "verify the fix",
  or any variation of reviewing code — even if the request sounds broad.
  The skill PREVENTS the agent from expanding scope beyond what the user
  explicitly asked about. It reviews only the file(s) or diff mentioned,
  goes one file at a time, and stops when done. Do NOT invoke a broad
  codebase scan. Do NOT surface findings from files the user didn't mention.
---

# Scoped Code Review

## The core rule

Review **only what the user pointed at**. Nothing more.

- If they said "check this file" → review that file only
- If they said "check my changes" → review only the git diff of the current branch
- If they said "verify the fix" → look only at the files that were just changed

Do not open adjacent files looking for related issues. Do not scan other controllers, services, or configs because they "might be relevant." The user will ask about those separately if they want them reviewed.

## Why this matters

Every time the scope expands, the user gets a longer list of findings from files they didn't ask about. This creates the feeling that bugs are never fixed — because every review finds new ones in new places. Staying scoped means findings are predictable and actionable.

## How to run the review

**Step 1 — Identify scope**

Determine what to review:
- File(s) explicitly named by the user → review those
- "My changes" / "the diff" / "what I just changed" → run `git diff main...HEAD --name-only` and review only those files
- "This PR" or a specific branch → same as above scoped to that branch
- A specific feature or bug fix just completed → ask "which files did you change?" if not obvious

**Step 2 — Review one file at a time**

For each file in scope:
1. Read the file
2. Check for issues **within that file only** — logic bugs, unhandled exceptions, security problems, missing null checks
3. Report findings for that file before moving to the next

Do not read files outside the scope list even if a method call leads you to want to "just check" something else.

**Step 3 — Report findings**

For each file, report in this format:

```
### [filename]
- [line N] Issue description — why it matters, what to fix
- [line N] ...
✅ Nothing else found in this file.
```

If no issues found in a file: `### [filename] — ✅ No issues found.`

End with a one-line summary: `Review complete. X files checked, Y issues found.`

**Do not** append a list of "other things you noticed elsewhere." Do not add a "Recommended next steps" section that lists unrelated files to review. Stop after the scoped files are done.

## What counts as in-scope

✅ The exact file(s) the user named  
✅ Files shown in `git diff` when the user says "check my changes"  
✅ A single controller/service/config the user is asking about  

❌ Other files that import or are imported by the target  
❌ Files you "noticed" while reading the target  
❌ The whole API surface because one endpoint was mentioned  
❌ Security config, DB migrations, or test files unless explicitly asked  

## Edge cases

**"Check for bugs in the billing flow"** — this sounds broad but still has a scope. Ask: "Which files make up the billing flow? I'll go through them one by one." Then review only those files.

**"Is everything working?"** — this is too vague to scope. Ask: "Which files or changes do you want me to check specifically?"

**"Review this PR"** — scope = files changed in the PR diff. Get the list with `gh pr diff --name-only` or `git diff`, review each one, stop.
