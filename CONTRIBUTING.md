# Contributing

Contributions of new profiles are the most valuable: they bring local knowledge the core cannot have.

## Add a region profile

1. Create `skills/source-trust-assessment/references/profiles/regions/<code>.md` in the language of the region. Use [cz.md](skills/source-trust-assessment/references/profiles/regions/cz.md) as the template.
2. Cover: what each `legalAuthority` code means in the region and the order of precedence, where the official versions are published, typical institutions for reliability A–F, recognised authorizations for `certified-expert` and how to check them, examples, local rules.
3. For EU member states, refer to the `eu` profile instead of repeating EU law.
4. Add the profile to `assets/vocabulary.ttl` (`sta:profileScheme`) with labels in English and the local language.
5. Add at least one valid fixture in `tests/fixtures/valid/` using the profile.

## Add a domain profile

Same as above in `references/profiles/domains/<code>.md`, written in English. Cover typical document types and their legal authority, typical institutions, and domain rules. Region-specific notes go into a "Region notes" section.

## Change the methodology

Changes of codes or general rules are rare and need an ADR in `docs/adr/`. Update in the same pull request:

- `references/methodology.md` and its version,
- `assets/assessment.schema.json` (`$id` version),
- `assets/vocabulary.ttl`,
- `scripts/validate_assessment.py` and tests,
- `SKILL.md` `metadata.methodology-version`,
- `CHANGELOG.md`.

## Rules

- A profile may specify, never redefine or add codes.
- Never put research notes, tests or CI files inside `skills/source-trust-assessment/` – that directory is installed into user projects.
- Cite sources for institution lists and legal statements in profiles; mark unverified items.
- Run `python -m unittest discover -s tests` before opening a pull request.
