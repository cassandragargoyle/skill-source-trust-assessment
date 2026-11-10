---
name: implement-issue
description: 'Guide for implementing an issue — from reading the assignment through creating a branch, implementing the change (skill, methodology, profiles, schema, validator), up to committing. Use when the user wants to implement an issue, work on an issue from docs/issues/, or process an issue according to the project methodology. Examples: "implement issue 12", "/implement-issue 012", "let''s do the sk region profile issue".'
argument-hint: [issue name or ID]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
user-invocable: true
metadata:
  internal: true
---

# Implement an issue

@.claude/prompts/assistant-programming.md

<!-- The file above defines the base context (language, role). This file adds the workflow. -->

Argument: **$ARGUMENTS**

**IMPORTANT: NEVER add a "Generated with Claude Code" or "Co-Authored-By: Claude"
signature to code files or git commits.**

## STEP 0: Role check

Check the current role in `CLAUDE.local.md`. If the role is not **Developer**:

1. Inform the user that implementation requires the Developer role
2. Offer to switch the role with `/role developer`
3. **STOP** — Do not continue until the Developer role is active

## STEP 1: Get the issue

If the argument contains an issue name or ID, use it. Otherwise ask me for the
issue name or ID and wait for my answer.

## STEP 2: Claim the issue (status + assignee check)

Before doing any work, verify the issue is free to work on. **GitHub is the single
source of truth for status and assignee** (see `docs/issues/README.md`).

The local file `docs/issues/NNN-*.md` is named after its **GitHub issue
number** `NNN`. Use that number for all `gh` calls below.

Run the checks in order:

1. **Locate the file.** If the file lives in `docs/issues/done/`, the
   issue is already **done** → **STOP**. Tell me the issue is archived as done and
   refuse to start work on it.

2. **Get the current GitHub user:**

   ```bash
   gh api user --jq .login
   ```

   If `gh` is not installed or not authenticated, **STOP** and tell me: the claim
   check cannot run without `gh`; ask me to install/authenticate `gh` or to
   explicitly confirm I want to skip the claim check.

3. **Read the issue state and assignees:**

   ```bash
   gh issue view NNN --repo cassandragargoyle/skill-source-trust-assessment \
     --json number,title,state,assignees
   ```

4. **Status check.** If `state` is `CLOSED` → the issue is **done** → **STOP**.
   Tell me the issue is already closed on GitHub and refuse to start work on it.

5. **Assignee check:**
   - If it is assigned to **someone other than the current user** → **STOP**.
     Report who it is assigned to and refuse to continue. Tell me to ask that
     person to **release the issue** (unassign themselves) before I can pick it up.
   - If it is assigned to **the current user already** → it is mine, continue.
   - If it is **unassigned** → claim it for me:

     ```bash
     gh issue edit NNN --repo cassandragargoyle/skill-source-trust-assessment --add-assignee @me
     ```

     Confirm the assignment succeeded before continuing.

Only once the issue is not done and is assigned to the current user, continue to
STEP 3.

## STEP 3: Confirm understanding

Once the issue is claimed:

1. Read the issue file from `docs/issues/`
2. Restate the issue in your own words
3. Classify the change and list the files it touches:
   - **Methodology change** (codes or general rules) → needs an ADR in `docs/adr/` and a
     methodology version bump (see STEP 5)
   - **Profile** (new or changed region/domain profile) → CONTRIBUTING.md procedure
   - **Skill workflow** (`SKILL.md`), **schema/vocabulary**, **validator**, **docs**
4. Ask me for confirmation

**STOP** — Wait for my explicit confirmation before continuing.

## STEP 4: Create a branch

Create a git branch: `feature/<issue-id>-<short-description>` or `fix/<issue-id>-<short-description>`

- Use lowercase letters and hyphens for the description
- Example: `feature/012-region-profile-sk`

Show the git command before running it.

## STEP 5: Implementation

- Make all changes in a single continuous phase
- Do NOT ask questions unless it is genuinely ambiguous
- Modify only the relevant files, prefer minimal diffs
- Code and identifiers in English; region profiles in the language of the region

### Project rules (AGENTS.md, CONTRIBUTING.md)

- **Distributed directory stays clean.** Only `skills/source-trust-assessment/` is installed
  into user projects. Never put research notes, tests, CI files or architecture notes there.
- **Codes are defined once.** A new or changed code goes into `references/methodology.md`,
  `assets/assessment.schema.json`, `assets/vocabulary.ttl` and
  `scripts/validate_assessment.py` in the same change.
- **Profiles may only specify, never redefine or add codes** (methodology § 8). Cite sources
  for institution lists and legal statements; mark unverified items.
- **Version the methodology** on every change of codes or rules (`SKILL.md`
  `metadata.methodology-version`, header of `methodology.md`, schema `$id`) and record it in
  `CHANGELOG.md`. Use `/bump-version`.
- **Methodology changes need an ADR** in `docs/adr/` (format of the existing ADRs:
  Status, Metadata, Context, Decision, Consequences).
- **No external dependencies in the skill.** The validator runs on plain Python 3.11+
  standard library.
- Every user-visible change gets an entry under `## [Unreleased]` in `CHANGELOG.md`.

### New profile checklist

1. `references/profiles/regions/<code>.md` (language of the region) or
   `references/profiles/domains/<code>.md` (English), using an existing profile as the template
2. Register it in `assets/vocabulary.ttl` (`sta:profileScheme`) with English and local labels
3. At least one valid fixture in `tests/fixtures/valid/` using the profile
4. Mention it in `README.md` and `README.cs.md` (profile list, repository structure)

### Tests

- Add tests for new validator behaviour in `tests/test_validate_assessment.py`
- Add fixtures: `tests/fixtures/valid/` for accepted results, `tests/fixtures/invalid/` for
  results the validator must reject
- Run:

  ```bash
  python -m unittest discover -s tests
  python skills/source-trust-assessment/scripts/validate_assessment.py tests/fixtures/valid/*.json
  ```

### Architecture documentation

The validator (`scripts/validate_assessment.py`) is the only program code. Its architecture
document lives **outside the distributed directory** in
`docs/architecture/validate_assessment.md`, so it is not installed into user projects.

- The document MUST start with a frontmatter block warning that only the code is the
  source of truth and that this file is meant for humans, e.g.:

  ```markdown
  ---
  warning: Only the code is the source of truth. This document is for humans and may lag behind the code.
  source: skills/source-trust-assessment/scripts/validate_assessment.py
  ---
  ```

- The document MUST contain Mermaid diagrams describing the structure and flow
  (e.g. the checks performed and the flow of a validation run)
- Whenever you change the validator, update its document in the SAME commit
- If the document does not exist yet, create it as part of the change
- Do NOT create architecture docs for tests or fixtures

At the end, provide a summary:

- Modified files
- Added or changed codes / rules / profiles / validator checks
- Methodology version change (if any) and ADR
- Key decisions

Ask me what I want:

- a) Accept as is
- b) Adjust specific parts
- c) Redo completely

**STOP** — Wait for my approval before continuing.

## STEP 6: Commit

Prepare the commit message:

```text
<type>(<issue-id>): <short summary>

- key change 1
- key change 2

Closes #<NNN>
```

Allowed types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

Do not add a "Generated with Claude Code" or "Co-Authored-By: Claude" signature to the commit.

**STOP** — Ask me to confirm the commit message before committing.

---

## Next steps

After the implementation is committed, use `/finish-branch` to:

- Run the tests and the consistency check
- Merge the branch into the main branch
- Delete the feature branch
- Update the issue status to ✅ Implemented and archive it into `docs/issues/done/`
