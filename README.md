# Source Trust Assessment

![source-trust-assessment icon](docs/icon/icon.svg)

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

Pin a released version for production use, so the methodology does not change underneath you. Releases are listed on the [Releases page](https://github.com/CassandraGargoyle/skill-source-trust-assessment/releases).

### Any agent (Claude Code, Codex, Cursor, …)

```bash
npx skills add CassandraGargoyle/skill-source-trust-assessment
```

### Claude Code plugin

```text
/plugin install source-trust-assessment --marketplace cassandragargoyle/skill-source-trust-assessment
```

On older Claude Code versions add the marketplace first:

```text
/plugin marketplace add CassandraGargoyle/skill-source-trust-assessment
/plugin install source-trust-assessment@cassandragargoyle
```

### Claude.ai and Claude Desktop

Download `source-trust-assessment-<version>.zip` from the [latest release](https://github.com/CassandraGargoyle/skill-source-trust-assessment/releases/latest) and upload it under *Settings → Capabilities → Skills*.

### Manual copy

Copy `skills/source-trust-assessment/` into `.claude/skills/` (Claude Code) or `.agents/skills/` (Codex) of your project.

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

## Limitations

- **Not legal advice.** The result is a structured, evidence-based opinion on how far a source can be relied on, not a legal opinion. Before acting on an obligation, read the official version of the legal act or ask a qualified professional.
- **AI assessments are unverified.** An assessment made by an AI agent alone always has `verificationStatus: "unverified"`. It becomes `verified` only after review by an expert (methodology § 5).
- **Agents make mistakes.** Check the quotes and URLs in `evidence`; sources that could not be retrieved are listed in `unresolved`.

### Profile status

| Profile | Type | Language | Status |
| ------- | ---- | -------- | ------ |
| `cz` | region | Czech | usable |
| `eu` | region | English | usable |
| `bim` | domain | English | **draft** – institution lists await review by domain experts |

## Data and privacy

- **The skill sends no data anywhere by itself.** It consists of instructions, reference files and one local script. It has no hooks, no MCP servers and no background processes, and it does not install packages.
- **Sources are fetched by the agent.** To assess a source, the agent opens the URLs you give it, or finds them with web search, using its own tools and under its own permission settings. The skill tells the agent not to bypass login walls or bot protection.
- **The validator runs locally.** `scripts/validate_assessment.py` uses only the Python standard library, reads the JSON file you pass to it and makes no network requests.
- **Nothing is stored by the skill.** The assessment stays in the conversation, or in a file if you or the agent save one. The skill does not ask for personal data.

## Agent Skills standard

This skill follows the open [Agent Skills](https://agentskills.io/) standard and its [specification](https://agentskills.io/specification). We aim to stay compliant with it and respect its conventions: the skill is a directory with a `SKILL.md` whose frontmatter `name` matches the directory name, extra data goes into `metadata`, and longer material lives in `references/`, `assets/` and `scripts/`, loaded only when needed. Anything that goes beyond the standard, such as the Claude Code plugin manifest in `.claude-plugin/`, is optional and kept outside the skill directory. If you find a deviation from the specification, please [open an issue](https://github.com/CassandraGargoyle/skill-source-trust-assessment/issues).

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
