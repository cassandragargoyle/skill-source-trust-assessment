# Methodology References

Standards and methods the methodology builds on, with their origin and how they are used. Not distributed with the skill.

| Reference | Origin | Version / date | Used for | Status |
| --------- | ------ | -------------- | -------- | ------ |
| Admiralty Code – source reliability and information credibility | NATO STANAG 2511, AJP-2.1 | – | `sourceReliability` A–F, `informationCredibility` 1–6 | adopted (ADR-001) |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation | 2013 | `derivedFrom` → `prov:wasDerivedFrom`, assessor → `prov:wasAttributedTo` | adopted |
| [W3C DQV](https://www.w3.org/TR/vocab-dqv/) | W3C Group Note | 2016 | dimensions as `dqv:Dimension`, assessments as `dqv:QualityMeasurement` | adopted (vocabulary) |
| [W3C SKOS](https://www.w3.org/TR/skos-reference/) | W3C Recommendation | 2009 | code lists and multilingual labels (`assets/vocabulary.ttl`) | adopted |
| [ISO/IEC 25012](https://www.iso.org/standard/35736.html) | ISO/IEC | 2008 | data quality characteristics (currency, traceability, …) as background for evidence criteria | reference |
| CRAAP test (Currency, Relevance, Authority, Accuracy, Purpose) | California State University, Chico | – | evidence criteria (§ 4) | reference |
| SIFT (Stop, Investigate the source, Find better coverage, Trace claims) | Mike Caulfield | – | tracing to the original, `derivedFrom` | reference |
| RADAR | – | – | further structured evaluation approach | to review |
| [University of Alberta – Evaluating Information](https://guides.library.ualberta.ca/research-writing/evaluating-information) | university library guide | – | overview of SIFT, CRAAP and RADAR | reference |
| [Agent Skills specification](https://agentskills.io/specification) | agentskills.io | – | `SKILL.md` format, directory layout | adopted |

## Origin of the methodology

The methodology was first written for the BIM legal knowledge model project (assessment of sources of an AI chat about the EPBD and a Czech shopping centre, November 2026) and split there into an English core and the `cz` and `eu` profiles. This repository takes it over as version 0.1.0.

## Open questions

- Verify the institution lists of the `bim` domain profile with Czech BIM experts.
- Decide whether to publish a machine-readable profile format (JSON) in addition to Markdown (ADR-002).
- Map `criteria` findings to ISO/IEC 25012 characteristics explicitly.
