# ADR-002: English Core Methodology, Profiles in the Language of Their Region, Skill in a Subdirectory

## Status

**Draft** — captured 2026-11-10. Awaiting review and acceptance.

## Metadata

- **Created**: 2026-11-10
- **Author**: Zdeněk Kurc
- **Target**: repository layout, `skills/source-trust-assessment/references/`
- **Related**:
  - [ADR-001 — Admiralty Code instead of a weighted score](ADR-001-admiralty-code-instead-of-weighted-score.md)

---

## Context

The skill must work for several jurisdictions (CZ first, EU law shared by all member states, later others) and fields (BIM first). Three questions had to be answered:

1. One methodology in English, or a separate methodology per country in its own language?
2. Where do region- and domain-specific rules live?
3. What gets installed into user projects, given that the repository also holds research notes, tests and CI?

Separate methodologies per language drift apart and make codes incomparable across countries. A single English text cannot hold local knowledge (legal hierarchy, official gazettes, recognised authorizations), and local assessors should read their rules in their own language. Research documents installed into every user project would waste agent context and confuse the skill.

## Decision

- **One normative core in English** (`references/methodology.md`): dimensions, codes, general rules, standards. Versioned.
- **Profiles** specify how the core applies:
  - region profiles in `references/profiles/regions/`, written in the language of the region (`cz.md` in Czech, `eu.md` in English);
  - domain profiles in `references/profiles/domains/` (`bim.md`);
  - a profile may specify, never redefine or add codes; member-state profiles refer to `eu` for EU law.
- **Codes and field names stay in English everywhere**; multilingual labels live in the SKOS vocabulary `assets/vocabulary.ttl`.
- **The distributed skill is the subdirectory `skills/source-trust-assessment/`.** Research, ADRs, tests and CI stay at the repository root and are not installed by `npx skills add`.

## Consequences

- Results from different regions are comparable; a result names the profiles it used.
- Adding a country means adding one Markdown file, not forking the methodology.
- The core and the profiles can get out of step; the version in the profile header must match the core version, and changes of codes require updating all four places (methodology, schema, vocabulary, validator).
- Profiles are Markdown for agents and humans, not JSON configuration; deterministic processing relies on the schema and the validator. A machine-readable profile format can be added later if a scoring engine needs it.
