---
title: Issue Management
description: Workflow for creating, assigning, tracking, and archiving issues in skill-source-trust-assessment — GitHub-first, where GitHub assigns the number and holds status and assignee, and each issue keeps a long-form write-up in docs/issues/NNN-*.md (archived to docs/issues/done/ on completion). No overview tables.
category: contributing-guide
status: active
language: en
last_updated: 2026-11-10
---

# Issue Management for skill-source-trust-assessment

## Principle: GitHub-First

**GitHub is the single source of truth for the issue list, status, and assignee.**
The issue is created on GitHub first, so **GitHub assigns the number `N`**. The
GitHub issue carries only the *basics* — a short description plus a link to the
detail file. The full write-up lives in the repo at `docs/issues/NNN-name.md`,
where `NNN` is the GitHub issue number zero-padded to three digits.

> There are **no overview tables**, no README index, and no mapping files in
> `docs/issues/` — a shared Markdown table edited by everyone causes constant
> merge conflicts. Status, assignee, labels, and milestone live on GitHub; the
> repo keeps only the long-form write-up per issue.

- Open issues: <https://github.com/cassandragargoyle/skill-source-trust-assessment/issues>
- Closed issues: <https://github.com/cassandragargoyle/skill-source-trust-assessment/issues?q=is%3Aissue+is%3Aclosed>

The skills automate this flow:

| Step | Skill |
| ---- | ----- |
| Create the GitHub issue and the detail file | [`/create-issue`](../../.claude/skills/create-issue/SKILL.md) |
| Claim the issue, branch, implement, commit | [`/implement-issue`](../../.claude/skills/implement-issue/SKILL.md) |
| Merge, close, and archive | [`/finish-branch`](../../.claude/skills/finish-branch/SKILL.md) |

## Workflow

1. **Create the GitHub issue** (GitHub assigns `N`). Keep the body minimal —
   a one-line summary plus a link placeholder:

   ```bash
   gh issue create --repo cassandragargoyle/skill-source-trust-assessment \
     --title "Short descriptive title" \
     --body "One-line summary.

   Full details: docs/issues/NNN-name.md" \
     [--label <type>,<priority>,<component>]
   ```

   `gh issue create` prints the URL — take `N` from it (`.../issues/7` → `N=7`,
   `NNN=007`). Never invent a number. GitHub issues and pull requests share one
   counter, so numbers may skip where a PR consumed one.

2. **Write the detail file** `docs/issues/NNN-name.md` (problem, acceptance
   criteria, testing, related issues). Use `NNN` in the filename and `N` in the
   `# Issue #N:` heading.

3. **Update the GitHub body** with a working link once `N` and the filename are
   known (blob URL on `main`):

   ```bash
   gh issue edit N --repo cassandragargoyle/skill-source-trust-assessment \
     --body "One-line summary.

   📄 [Full details](https://github.com/cassandragargoyle/skill-source-trust-assessment/blob/main/docs/issues/NNN-name.md)"
   ```

   The link starts working once the file reaches `main`.

4. **Claim the issue** before starting work (see [Assignment](#assignment)).

5. **Reference the issue** in branches and commits: `feature/NNN-name` or
   `fix/NNN-name`, `feat(NNN): …`, and `Closes #N` in the commit body or PR.

6. **Archive on completion**:

   ```bash
   git mv docs/issues/NNN-name.md docs/issues/done/NNN-name.md
   gh issue close N --repo cassandragargoyle/skill-source-trust-assessment \
     --comment "Implemented in <version/commit>."
   ```

   Update the GitHub body link to the `done/` path when archiving. Use
   `--reason "not planned"` for issues that will not be done.

## Assignment

The **GitHub assignee** says who is working on an issue. Nobody starts work on an
issue that is assigned to someone else, and the repository never records the
assignee — the detail file has no `Assignee` field.

Before starting work:

```bash
gh api user --jq .login                       # who am I
gh issue view N --repo cassandragargoyle/skill-source-trust-assessment \
  --json number,title,state,assignees
```

| GitHub state | Action |
| ------------ | ------ |
| `CLOSED`, or the file is in `docs/issues/done/` | Done — do not start work |
| Assigned to someone else | Stop; ask them to release the issue (unassign themselves) |
| Assigned to me | Continue |
| Unassigned | Claim it: `gh issue edit N --add-assignee @me`, then continue |

- **Release** an issue you stop working on: `gh issue edit N --remove-assignee @me`,
  and leave a comment saying how far you got.
- **Maintainer assignment.** The maintainer (see [GOVERNANCE.md](../../GOVERNANCE.md))
  may assign an issue to a contributor with `--add-assignee <login>`. External
  contributors without write access cannot be assigned: they comment
  "I'd like to work on this" and the maintainer assigns them or notes it in a comment.
- **Methodology issues** (codes or general rules) are assigned only after the
  maintainer has accepted the direction, because they need an ADR
  ([CONTRIBUTING.md](../../CONTRIBUTING.md#change-the-methodology)).
- **Status labels** are optional and describe progress, not ownership:
  `in-progress`, `blocked`, `ready-for-review`.

## Publication and Sensitive Content

`docs/issues/` is **public** — it is pushed to GitHub together with the rest of
the repository. Write every issue as public content:

- No customer names, business relationships, deals, or priorities tied to a customer
- No third-party or employer project names and internal identifiers
- No local paths such as `/home/<user>/…` or `C:\Users\<user>\…` — use repository-relative paths
- No internal hostnames, IP addresses, credentials, or tokens (placeholders like
  `<token>` or `example.com` are fine)
- Legal texts and documents cited in profile issues must be public sources; give
  the official URL (e.g. e-Sbírka, EUR-Lex), never a copy of a paid standard

Content that must stay internal does not belong in this repository.

## Detail file template

```markdown
# Issue #N: <Title>

**Type**: Feature | Enhancement | Bug Fix | Methodology | Profile | Docs | Task
**Priority**: Critical | High | Medium | Low
**Status**: Open
**Created**: <YYYY-MM-DD>
**GitHub**: #N
**Component**: <skill | methodology | profile-<code> | schema | validator | docs | build-infra>
**Related**: #<...>, ADR-<...>

## Summary
<1–3 sentences>

## Problem Description / Motivation
...

## Scope
### In scope
### Out of scope (follow-up issues)

## Proposed Change
<affected files; for the methodology: codes, rules, methodology version, ADR>

## Acceptance Criteria
1. ...
2. `python -m unittest discover -s tests` passes
3. Valid fixtures pass `validate_assessment.py`

## Testing
<new fixtures in tests/fixtures/valid|invalid, new tests>
```

### Formatting rules

- **No icons or emoji** in issue files: not in headings and not in the `Status`
  field (`Open`, not `📋 Open`)
- The `Status` field mirrors GitHub at the time of writing; GitHub wins when they differ.
  Values: `Open`, `In Progress`, `On Hold`, `Implemented`, `Resolved`, `Closed`
- All issue text in **English** (project convention). Quotations from a region's
  legal texts may stay in the language of the region.

## Labels

Assign labels on the GitHub issue (create them once with `gh label create`):

- **Type**: `bug`, `enhancement`, `documentation`, `question`, `task`
- **Priority**: `critical`, `high`, `medium`, `low`
- **Component** — one per area of the repository:

  | Label | Area |
  | ----- | ---- |
  | `skill` | `SKILL.md` workflow |
  | `methodology` | `references/methodology.md` — codes and general rules (needs an ADR) |
  | `profile-<code>` | a region or domain profile, e.g. `profile-cz`, `profile-eu`, `profile-bim` |
  | `schema` | `assessment.schema.json`, template, `vocabulary.ttl` |
  | `validator` | `scripts/validate_assessment.py` and tests |
  | `docs` | README, ADR, CONTRIBUTING, FORKING |
  | `build-infra` | CI, repository tooling, `.claude/` |

  This is how issues are filtered:

  ```text
  is:issue is:open label:methodology
  is:issue is:open no:assignee
  ```

- **Status** (optional): `needs-triage`, `in-progress`, `blocked`,
  `ready-for-review`

Create a component label once:

```bash
gh label create methodology --repo cassandragargoyle/skill-source-trust-assessment \
  --color 1d76db --description "Codes and general rules of the methodology"
```

## File structure

```text
docs/issues/
├── README.md                 # Stub pointing at GitHub Issues
├── NNN-name.md               # Active issue write-up (NNN = GitHub issue number)
└── done/                     # Archived (Implemented / Resolved / Closed) issues
    └── NNN-*.md
```

## Numbering note

- Files use three-digit zero padding (`013-…`, `042-…`); GitHub references do
  not (`#13`, `#42`).
- Never invent a number — always take the one GitHub returns.
- **When GitHub is not reachable**, do not pick a number. Write the detail file as
  `docs/issues/pending-<name>.md` and rename it once GitHub assigns `N`.

## Best practices

- Search existing GitHub issues before opening a new one.
- Keep the GitHub body short; put depth in the detail file.
- Assign type + priority + component labels immediately.
- Claim before you start; release when you stop.
- Include reproduction steps (input JSON, validator output) for bugs and
  acceptance criteria for features.
- For a new profile, follow [CONTRIBUTING.md](../../CONTRIBUTING.md) and list the
  sources you will cite.

---

*Adapted from the `api` sibling project (GitHub-first variant), extended with the assignment rules.*
