# ADR-001: Admiralty Code and Legal Authority Instead of a Weighted Score

## Status

**Draft** — captured 2026-11-10. Awaiting review and acceptance.

## Metadata

- **Created**: 2026-11-10
- **Author**: Zdeněk Kurc
- **Target**: `skills/source-trust-assessment/references/methodology.md`, `assets/assessment.schema.json`
- **Related**:
  - [research/methodology-references.md](../../research/methodology-references.md)
  - [ADR-002 — core methodology and profiles](ADR-002-core-methodology-and-profiles.md)

---

## Context

Two shapes of a trust assessment were considered while designing the skill:

1. **A weighted score 0–100.** Criteria (authority, authenticity, currency, traceability, relevance …) get weights per domain profile, a script computes the score. Proposed in the initial design discussion together with `extends` inheritance of weights.
2. **Independent dimensions without a score.** The Admiralty Code (NATO STANAG 2511): source reliability A–F and information credibility 1–6, plus a separate legal authority and legal status, plus provenance. Used in the BIM legal knowledge model to attribute claims of an AI chat to their sources.

The use case that drives the skill is deciding whether an **obligation** (legal, technical, contractual) may be derived from a source. For that, three questions must stay separate: *Is the originator reliable? Is this specific information confirmed? Is it binding?* A reliable ministry can publish an oversimplified press release; a confirmed fact from a newspaper is still not law; a draft bill from the government is authentic but not binding.

## Decision

Use **independent dimensions without a combined score**:

- `sourceReliability` A–F and `informationCredibility` 1–6 (Admiralty Code), written as a code such as `A1`;
- `legalAuthority` (constitutional … none) and `legalStatus` (in-force, draft, repealed, n/a);
- provenance and verification (`assessedBy`, `assessor`, `derivedFrom`, `verificationStatus`).

The criteria from option 1 are kept, but as an **evidence checklist** (`criteria[]` with findings and evidence references) that leads to the codes, not as weighted numbers.

## Consequences

- **F and 6 keep their meaning** (*unknown*, not *worst*). A sum or average would rank an unknown originator with a confirmed claim (`F1`) below a reliable source with a doubtful claim (`B4`), which is wrong for deciding use.
- **Bindingness cannot be outweighed.** No amount of credibility turns a commentary into law.
- **Domain profiles cannot change weights.** They specify institutions, document types and rules instead. Users who want weighted scoring can add it in a fork as a derived view, marked `methodology.modified: true`.
- **Results are less sortable** than a single number. Sorting is done by credibility digit first, then reliability letter.
- **Interoperable.** The Admiralty Code is an established standard; the codes map to W3C DQV dimensions and SKOS concepts (`assets/vocabulary.ttl`).
