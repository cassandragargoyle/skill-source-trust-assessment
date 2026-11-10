# Development Instructions

## Project Information

- **GitHub Repository**: <https://github.com/CassandraGargoyle/skill-source-trust-assessment>
- **Project Name**: skill-source-trust-assessment
- **Primary Purpose**: An Agent Skill (`source-trust-assessment`) for evidence-based assessment of the trustworthiness of publishers, documents and claims, with region and domain profiles
- **Primary Language**: Markdown (skill, methodology, profiles), JSON (schema), Python 3.11+ standard library (validator)
- **Platforms**: any agent supporting the Agent Skills format (Claude Code, Codex, …)

The methodology originates in the BIM legal knowledge model project, where it was used to attribute claims of an AI chat to their sources (Admiralty Code + legal authority, profiles `cz` and `eu`). The design discussion is summarised in [research/](research/) and the decisions in [docs/adr/](docs/adr/).

## Security Guidelines

- Never run destructive commands without confirmation
- Always warn about potential data loss before executing risky operations
- Require explicit confirmation for operations that could lose implemented code

## Project Structure

- `/skills/source-trust-assessment/` - **The distributed skill.** Only this directory is installed into user projects; keep it free of research notes, tests and CI files
  - `SKILL.md` - frontmatter (name must equal the directory name) and the agent workflow
  - `references/methodology.md` - normative methodology, English, versioned
  - `references/profiles/regions/` - region profiles in the language of the region (`cz.md` Czech, `eu.md` English)
  - `references/profiles/domains/` - domain profiles (`bim.md`)
  - `assets/` - `assessment.schema.json`, `assessment.template.json`, `vocabulary.ttl` (SKOS code lists)
  - `scripts/validate_assessment.py` - validator, standard library only
- `/docs/adr/` - architecture decision records
- `/research/` - existing solutions and methodology references (not distributed)
- `/tests/` - validator tests (`python -m unittest`) and fixtures

## Rules for Changes

- **Codes are defined once.** A new code goes into `methodology.md`, `assessment.schema.json`, `vocabulary.ttl` and the validator in the same change.
- **Profiles may only specify, never redefine** codes (methodology § 8).
- **Version the methodology** (`SKILL.md` metadata `methodology-version`, header of `methodology.md`, schema `$id`) on every change of codes or rules, and record it in `CHANGELOG.md`.
- **No external dependencies in the skill.** The validator must run with a plain Python 3.11+.
- **Code and identifiers in English**; region profiles in the language of the region.

## Testing

```bash
python -m unittest discover -s tests
python skills/source-trust-assessment/scripts/validate_assessment.py tests/fixtures/valid/*.json
```
