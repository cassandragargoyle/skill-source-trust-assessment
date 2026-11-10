---
name: finish-branch
description: 'Finish work on a feature branch — tests, README/CHANGELOG/version check, merge into the main branch, branch clean-up and optional issue status update. Use when the user wants to finish, merge or close a feature branch. Examples: "finish the branch", "/finish-branch", "merge the feature branch into main", "dokonči branch".'
allowed-tools: Read, Glob, Grep, Bash, AskUserQuestion, Edit
user-invocable: true
---

# Finish a feature branch

Finish work on a feature branch — tests, README/CHANGELOG/version check, merge into the main branch, branch clean-up and optional issue status update.

@.claude/prompts/assistant-programming.md

<!-- This file is authoritative. SKILL.cs.md is a Czech translation for humans. -->

**IMPORTANT: NEVER add "Co-Authored-By: Claude <noreply@anthropic.com>" to code files or git commits.**

## Instructions

### STEP 1: Establish the context

Ask me for:

1. The name of the feature branch (or use the current branch)
2. The target branch for the merge (default `main`)

Verify that the branch exists and contains commits. List the changed files:

```bash
git diff --name-only <target-branch>...HEAD
```

### STEP 2: Run the checks

Run the same checks as CI (`.github/workflows/ci.yml`):

```bash
python -m unittest discover -s tests -v
python skills/source-trust-assessment/scripts/validate_assessment.py tests/fixtures/valid/*.json
```

If `vocabulary.ttl` changed and `rdflib` is available, also parse the vocabulary
(CI does this; it is not a dependency of the skill):

```bash
python -c "import rdflib; g = rdflib.Graph(); g.parse('skills/source-trust-assessment/assets/vocabulary.ttl', format='turtle'); print(len(g), 'triples')"
```

If anything fails, **STOP** and report it. Do not merge a red branch.

### STEP 3: Check consistency of the change

Check the project rules (AGENTS.md, CONTRIBUTING.md) against the changed files:

1. **Distributed directory stays clean.** `skills/source-trust-assessment/` contains no
   research notes, tests, CI files or other repository-only files.
2. **Codes are defined once.** If the branch adds or changes a code, the same change is in
   `references/methodology.md`, `assets/assessment.schema.json`, `assets/vocabulary.ttl`
   and `scripts/validate_assessment.py` (+ tests).
3. **Methodology versioning.** If codes or rules changed, the methodology version was raised
   (`SKILL.md` `metadata.methodology-version`, header of `methodology.md`, schema `$id`) and
   there is an ADR in `docs/adr/`. If not, offer `/bump-version`.
4. **Profiles** only specify codes, never redefine or add them. A new profile is listed in
   `vocabulary.ttl` (`sta:profileScheme`) and has a valid fixture in `tests/fixtures/valid/`.
5. **CHANGELOG.md** has an entry under `## [Unreleased]` for every user-visible change.

### STEP 4: Update the READMEs

Before merging the branch, verify that the READMEs match the state after the change.
Check both `README.md` and `README.cs.md`:

- the methodology version in the overview (`Status: … (methodology X.Y.Z)` /
  `Stav: … (metodika X.Y.Z)`) equals `metadata.methodology-version` in `SKILL.md`,
- the list of profiles (`cz`, `eu`, `bim`, …) in the overview and in "Repository structure"
  matches `references/profiles/regions/` and `references/profiles/domains/`,
- install and use instructions and the repository structure are not outdated.

```bash
grep -n "methodology-version\|  version" skills/source-trust-assessment/SKILL.md
grep -n "methodology\|metodika" README.md README.cs.md
ls skills/source-trust-assessment/references/profiles/*/
```

If something does not match, fix it and commit it to the feature branch before the merge:

```text
docs(<issue-id>): Update READMEs
```

If the READMEs match, skip the step and say so in the summary.

### STEP 5: Merge and clean-up

> **What is a PR (Pull Request)?** A request to integrate changes from a feature branch into the main branch. Used for code review in teams. For solo development a direct merge is possible.

Ask the user for the preferred procedure. Changes of the methodology (codes, rules) should go
through a PR, because the maintainer must review them (GOVERNANCE.md).

#### Option A: Direct merge (default for solo development)

Find the source branch (the one the feature branch was created from) and merge:

```bash
git checkout <source-branch>    # e.g. main
git merge feature/<issue-id>-<description>
git branch -d feature/<issue-id>-<description>
```

**STOP** - Wait for confirmation before merging.

#### Option B: Pull Request (for team collaboration)

Prepare the PR description:

- **Summary**: What this PR does
- **Motivation**: Why (link to the issue, ADR if any)
- **Changes**: List of changes; methodology version change if any
- **Testing**: Steps to verify (`python -m unittest discover -s tests`, validator on fixtures)

Create the PR with `gh pr create`.

### STEP 6: Issue update (optional)

Ask the user: "Is the issue completely finished by this?"

#### If YES:

Edit the issue file in `docs/issues/`:

- Change `**Status:** 📋 Open` to `**Status:** ✅ Implemented`
- Add the closing date

Move the file to the archive and close the GitHub issue (there are no README tables — the list lives on GitHub):

```bash
git mv docs/issues/<NNN>-*.md docs/issues/done/
gh issue close <NNN> --repo cassandragargoyle/skill-source-trust-assessment
```

Commit the issue status change:

```text
docs(<issue-id>): Close issue - implementation complete
```

#### If NO:

Skip the status update. The issue stays open for further work.

### STEP 7: Summary

Show a summary:

- Tests and fixture validation: passed
- Consistency check (codes, versions, profiles, CHANGELOG): OK / fixed / issues
- READMEs updated: yes/no (not needed)
- Merge performed into branch: `<name>` (or PR URL)
- Feature branch deleted: yes/no
- Issue status updated: yes/no/skipped
- Next steps (if any, e.g. `/bump-version` before a release)
