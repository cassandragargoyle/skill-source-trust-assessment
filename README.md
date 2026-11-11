# Source Trust Assessment

*Česky: [README.cs.md](README.cs.md).*

## Overview

- **Repository**: `skill-source-trust-assessment`
- **Skill name**: `source-trust-assessment`
- **Format**: [Agent Skill](https://agentskills.io/specification) (`SKILL.md`) – Claude Code, Codex and other agents
- **Status**: Early (methodology 0.1.1)

Open-source Agent Skill for evidence-based assessment of information source trustworthiness across regions, domains, and source types.

The skill tells an AI agent how to assess a publisher, a document or a single claim and return a structured, reproducible result with evidence. It does not collapse trust into one number. It uses:

- the **Admiralty Code** (NATO STANAG 2511): source reliability A–F and information credibility 1–6, written as `A1`, `B2`, `F6`;
- **legal authority** and **legal status**: whether the content is binding law, a draft or no law at all;
- **provenance**: who assessed it, when, derived from what (W3C PROV-O).

How the codes apply in a jurisdiction or a field is defined by **profiles**: region profiles (`cz`, `eu`) and domain profiles (`bim`).

## Install

```bash
npx skills add CassandraGargoyle/skill-source-trust-assessment
```

Or copy `skills/source-trust-assessment/` into `.claude/skills/` (Claude Code) or `.agents/skills/` (Codex) of your project. Pin a released version for production use, so the methodology does not change underneath you.

## Use

```text
/source-trust-assessment
Assess https://e-sbirka.gov.cz/eli/cz/sb/2000/406 for region cz,
purpose: energy audit obligations of a shopping centre.
```

The agent returns JSON following [assessment.schema.json](skills/source-trust-assessment/assets/assessment.schema.json) and a short summary. Validate it with:

```bash
python skills/source-trust-assessment/scripts/validate_assessment.py result.json
```

## Repository structure

Only `skills/source-trust-assessment/` is installed into user projects; everything else stays in the repository.

```text
skills/source-trust-assessment/   the distributed skill
  SKILL.md                        workflow and rules for the agent
  references/methodology.md       normative methodology (EN)
  references/profiles/regions/    cz (Czech), eu (English)
  references/profiles/domains/    bim
  assets/                         JSON schema, template, SKOS vocabulary
  scripts/validate_assessment.py  validator (Python standard library only)
docs/adr/                         design decisions
research/                         existing solutions, methodology references
tests/                            validator tests and fixtures
```

## Customising

Add a profile instead of changing the methodology; see [CONTRIBUTING.md](CONTRIBUTING.md). If you need to change codes or rules, fork the repository – see [FORKING.md](FORKING.md). A fork that changes the methodology must mark its results with `methodology.modified: true`.

## Licence

[MIT](LICENSE)
