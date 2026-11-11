---
name: source-trust-assessment
description: >
  Evidence-based assessment of how far an information source, a document or a single
  claim can be trusted, using the Admiralty Code (source reliability A–F, information
  credibility 1–6) plus legal authority and legal status, with region and domain
  profiles (e.g. Czech Republic, EU, BIM). Use when verifying regulations, standards,
  official documents, articles or AI-generated claims before relying on them, when
  asked how trustworthy a source is, or when attributing claims to their sources.
  Works in any language (e.g. "ověř tento zdroj", "jak důvěryhodný je tento dokument",
  "odkud pochází toto tvrzení").
license: MIT
metadata:
  author: CassandraGargoyle
  version: "0.1.1"
  methodology-version: "0.1.1"
---

# Source Trust Assessment

Assess a source, a document or a claim and return a structured, reproducible result with evidence. The methodology is in [references/methodology.md](references/methodology.md); read it before the first assessment in a session.

## When to use

- The user asks how trustworthy a source, document, website or claim is.
- A claim (often AI-generated) must be checked against the sources it cites.
- A legal or technical obligation is about to be derived from a source.

## Workflow

1. **Identify the subject and level.** Is it a publisher (organisation), a document, or a single claim? Record title, URL and retrieval date.
2. **Select profiles.** Region (e.g. `cz`), the shared `eu` profile when EU law is involved, and a domain (e.g. `bim`). Read the matching files in [references/profiles/](references/profiles/). If no profile fits, use the methodology alone and say so.
3. **Find the original.** Trace republished content to its originator (`derivedFrom`). For legal acts, locate the official version named in the region profile.
4. **Collect evidence.** For every finding store the URL, a verbatim quote and its `relation` to the subject: `confirms`, `partially-confirms`, `contradicts` or `context` (methodology § 4).
5. **Check the criteria.** Authority, authenticity, currency, accuracy, independence, traceability, relevance (methodology § 4). Record findings, not scores.
6. **Assign the codes.** `sourceReliability` A–F and `informationCredibility` 1–6, then `legalAuthority` and `legalStatus`. F and 6 mean *unknown*, not *worst*.
7. **Record provenance.** `assessedBy` is `ai` unless a human reviewed the result; `verificationStatus` stays `unverified` for AI-only assessments.
8. **Return the result** as JSON following [assets/assessment.schema.json](assets/assessment.schema.json) (template: [assets/assessment.template.json](assets/assessment.template.json)), followed by a short plain-language summary.
9. **Validate** the JSON when a shell is available: `python scripts/validate_assessment.py <file.json>`.

## Rules

- Never invent sources, quotes, URLs or dates. If something cannot be found, put it in `unresolved`.
- Rate the originator, not the website where the content was found.
- Do not merge the dimensions into one score.
- Bindingness comes only from the official version of a legal act; everything else has `legalAuthority: "none"`.
- An obligation may only be derived from information with credibility 1.
- Do not bypass access controls (login walls, bot protection). Record the blocked source in `unresolved` and suggest manual retrieval.
- Write the plain-language summary and free-text fields in the user's language. Codes, field names and enum values stay in English as defined; quotes stay verbatim in the language of the source.
- State the methodology version and profiles used. If you deviate from the methodology, set `methodology.modified: true` and explain it.
