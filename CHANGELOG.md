# Changelog

All notable changes to the skill and its methodology. The methodology version is stated in `SKILL.md` (`metadata.methodology-version`), in the header of `references/methodology.md` and in the schema `$id`.

## [Unreleased]

### Added

- `source-trust-assessment` skill: workflow and rules in `SKILL.md`.
- Methodology 0.1.0: Admiralty Code (A–F, 1–6), legal authority and status, assessment levels (publisher, document, claim), evidence criteria, provenance, profile rules.
- Region profiles `cz` (Czech) and `eu`; domain profile `bim` (draft).
- `assessment.schema.json`, template and SKOS vocabulary.
- `validate_assessment.py` validator (standard library only) with tests.
- ADR-001 (Admiralty Code instead of a weighted score), ADR-002 (core and profiles, repository layout).

### Changed

- `SKILL.md` description lists example trigger phrases in Czech; a new rule asks for the summary and free-text fields in the user's language (codes and quotes unchanged).
