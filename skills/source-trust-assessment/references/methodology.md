# Source Trust Assessment Methodology

Version 0.1.0 · normative core · jurisdiction-neutral

This document defines the dimensions, codes and general rules of the assessment. How the codes apply in a particular region or domain (legal hierarchy, typical institutions, authorizations, local examples) is defined by **profiles** in [profiles/](profiles/). Codes and multilingual labels are also published as a SKOS vocabulary in [../assets/vocabulary.ttl](../assets/vocabulary.ttl).

## 1. Dimensions

Trust is not expressed as a single number but in **three independent dimensions**:

1. **Source reliability** (A–F) and **information credibility** (1–6) according to the **Admiralty Code** (NATO STANAG 2511, AJP-2.1), written together as a code such as `A1` or `B2`.
2. **Legal authority**: the legal force of the content. The Admiralty Code does not cover it, and a highly credible expert commentary does not become binding law.
3. **Verification and provenance**: who assessed it, when, and where the information comes from (W3C PROV-O).

The dimensions are never merged into one score. F and 6 mean *unknown*, not *worst*; a sum or weighted average would distort them.

### 1a. Source reliability (`sourceReliability`)

Rates the originator of the information (who issued it and whether they are entitled to), not the website where it was published.

| Code | Meaning | Typically |
| ---- | ------- | --------- |
| **A** | completely reliable | official law gazettes, ministries, courts, public registers |
| **B** | usually reliable | professional chambers and associations, universities, quality media, banks, an owner about their own asset |
| **C** | fairly reliable | expert websites without clear editorial control, regional directories, Wikipedia |
| **D** | not usually reliable | marketing websites, aggregators republishing content without attribution |
| **E** | unreliable | sources known for spreading false information |
| **F** | reliability cannot be judged | unknown originator, social media, AI output |

### 1b. Information credibility (`informationCredibility`)

Rates the content itself. A publisher or document carries its typical value; individual claims are rated separately, because a wrong rule can be derived even from a reliable statute.

| Code | Meaning | When |
| ---- | ------- | ---- |
| **1** | confirmed | original document (text of the law, decision) or confirmed by an independent source |
| **2** | probably true | consistent with other sources, not confirmed by the original |
| **3** | possibly true | unconfirmed, nothing contradicts it |
| **4** | doubtful | contradicts other information or is oversimplified |
| **5** | improbable | contradicts confirmed information |
| **6** | truth cannot be judged | no basis for judgement |

### 1c. Combined code

| Code | Example | Reading |
| ---- | ------- | ------- |
| `A1` | statute in the official gazette | completely reliable source, information confirmed by the original |
| `B2` | quality newspaper article on a legislative consultation | usually reliable source, information probably true |
| `A4` | ministry press release with an oversimplified claim | reliable source, but the specific claim is doubtful |
| `C3` | expert website without an author, unconfirmed figure | fairly reliable source, information possibly true |
| `F1` | AI output whose claim was verified in the statute | originator cannot be judged, but the information is independently confirmed |
| `F6` | AI answer without documented sources | neither source nor information can be judged |

- **F and 6 mean unknown, not worst.** `F1` is more usable than `B4`.
- **The digit decides use.** An obligation may only be derived from information with credibility 1. Credibility 2–3 must be verified; 4–5 must not be used.
- **The code says nothing about bindingness.** That is given by legal authority.

## 2. Legal authority and status

| `legalAuthority` | Meaning |
| ---------------- | ------- |
| `constitutional` | constitution and acts of constitutional rank |
| `international` | international treaties binding on the jurisdiction |
| `eu` | EU primary and secondary law (see the `eu` profile) |
| `statutory` | acts of parliament |
| `secondary` | government and ministerial regulations, local by-laws |
| `case-law` | decisions of the highest and constitutional courts |
| `guidance` | official guidelines and opinions, technical standards (binding only when referenced by law) |
| `none` | everything else: articles, websites, commentaries, AI output |

The order of precedence between `constitutional`, `international` and `eu` differs between jurisdictions and is defined in region profiles.

| `legalStatus` | Meaning |
| ------------- | ------- |
| `in-force` | in force (or with a fixed date of effect) |
| `draft` | bill, draft regulation, consultation version – not binding |
| `repealed` | repealed or outdated version |
| `n/a` | not a legal act |

A draft bill has `legalAuthority: "statutory"` and `legalStatus: "draft"`: it has the form of a statute but is not binding.

## 3. Assessment levels and context

| `subject.level` | What is assessed | Typical use |
| --------------- | ---------------- | ----------- |
| `publisher` | an organisation or author | catalogue of trusted publishers |
| `document` | a specific document or web page | source list of a project |
| `claim` | a single statement | checking AI output or a report against its sources |

A trustworthy publisher can publish an outdated document, and a trustworthy document can contain a claim that does not fit the purpose. Assess at the level that is needed and do not copy ratings between levels without checking.

`context` records the region profile, the domain profile and the purpose of the assessment (e.g. "deriving building owner obligations").

## 4. Evidence criteria

The criteria below structure the evidence that leads to the codes. They are recorded as findings, **not** as weighted scores. They draw on CRAAP, SIFT and ISO/IEC 25012.

| Criterion | Question | Mainly informs |
| --------- | -------- | -------------- |
| `authority` | Who issued it and are they competent and entitled to? | reliability, legal authority |
| `authenticity` | Is it really from the declared issuer (official site, signature, official gazette)? | reliability |
| `currency` | Is it still valid, the current version, not superseded? | credibility, legal status |
| `accuracy` | Is it supported by evidence and consistent with other sources? | credibility |
| `independence` | Conflicts of interest, commercial influence, advocacy? | reliability, credibility |
| `traceability` | Can the origin, citations and history be traced? | credibility, provenance |
| `relevance` | Does it apply to the region, domain and purpose? | context (not trust itself) |

Each finding: `{ "criterion": "...", "finding": "...", "evidence": [<indexes into evidence>] }`.

## 5. Verification and provenance

| Field | Values | Meaning |
| ----- | ------ | ------- |
| `verificationStatus` | `verified`, `unverified`, `disputed` | whether the assessment was reviewed |
| `assessedBy` | `human`, `expert`, `certified-expert`, `ai`, `ai+human`, `ai+expert`, `ai+certified-expert` | who assessed |
| `assessor` | name, authorization number, field | required for `certified-expert`; region profiles list recognised authorizations |
| `assessedAt` | date | when |
| `derivedFrom` | URL or id | what the information was derived from (`prov:wasDerivedFrom`) |

An assessment with `verificationStatus: "verified"` needs an expert among the assessors. AI-only assessments stay `unverified`.

## 6. Rules

1. **Rate the originator, not the place of publication.** Republished text is rated by its original and linked with `derivedFrom`. If it does not match the original, rate the republishing site.
2. **Bindingness only from the official version.** Text of a legal act from a commercial database or an article has `legalAuthority: "none"`. Region profiles name the official sources.
3. **An information system is rated by the content it publishes** (an official gazette `in-force`, a consultation portal `draft`).
4. **A claim inherits the rating of the source that actually supports it.** A claim confirmed by two independent sources gets credibility 1; republications of the same text are not independent. A claim without support is `F6`.
5. **Deviations are explained** in `rationale`, e.g. an old article on a changing topic gets credibility one step worse.
6. **Never bypass access controls.** A source that cannot be retrieved goes to `unresolved`.

## 7. Methodology provenance and forks

Every result states `methodology.id`, `methodology.version`, the profiles used and, when known, the repository and commit. A fork that changes codes, rules or profiles must set `methodology.modified: true` and must not present its results as assessments under the reference methodology.

## 8. Profiles

A profile **may** specify what each `legalAuthority` code covers in its region and the order of precedence, list typical institutions for reliability levels, list authorizations recognised as `certified-expert`, name official sources, add examples and stricter local rules. A profile **must not** redefine or add codes or contradict this core. Region profiles are written in the language of the region; codes and field names stay in English. Member-state profiles refer to the `eu` profile for EU law.

## 9. Standards

| Area | Standard | Use here |
| ---- | -------- | -------- |
| source and information rating | Admiralty Code (NATO STANAG 2511, AJP-2.1) | `sourceReliability`, `informationCredibility` |
| provenance | W3C PROV-O | `derivedFrom` → `prov:wasDerivedFrom`, `assessedBy`/`assessor` → `prov:wasAttributedTo` |
| storing assessments in RDF | W3C DQV | each dimension as `dqv:Dimension`, an assessment as `dqv:QualityMeasurement` |
| code lists, multilingual labels | W3C SKOS | `assets/vocabulary.ttl` |
| evidence criteria | CRAAP, SIFT, ISO/IEC 25012 | § 4 |
