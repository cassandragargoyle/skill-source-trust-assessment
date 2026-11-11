# Domain profile `bim` – Building Information Modelling

Profile for the [methodology](../../methodology.md) version 0.1.1. Status: **draft** – the institution lists below must be reviewed by domain experts before release.

Use together with a region profile: `"context": { "region": "cz", "domain": "bim" }`.

## Typical document types

| Document type | `legalAuthority` | Note |
| ------------- | ---------------- | ---- |
| law or regulation requiring BIM (e.g. in public procurement) | per region profile (`statutory`, `secondary`) | official version per region profile |
| international BIM standards – ISO 19650 series (information management), ISO 16739-1 (IFC) | `guidance` | binding only when referenced by law or contract |
| national adoptions (e.g. ČSN EN ISO 19650) | `guidance` | check the current edition in the national standards catalogue |
| government BIM strategies and concepts | `guidance` | policy documents, not binding on private parties |
| employer's information requirements, BIM execution plans (BEP) | `none` | binding only through the contract |
| buildingSMART specifications (IFC, IDS, BCF, bSDD) | `guidance` | check the released version, not drafts on GitHub |
| vendor documentation and marketing | `none` | rate independence carefully (D or lower for marketing) |

## Source reliability – typical BIM sources

| Code | Typically |
| ---- | --------- |
| **A** | ISO, CEN, national standards bodies, government agencies responsible for the national BIM strategy |
| **B** | buildingSMART International and national chapters, professional chambers, universities, recognised BIM expert councils |
| **C** | BIM consultancies' blogs, community wikis, conference slides without peer review |
| **D** | software vendors' marketing material about their own products |

## Region notes: `cz`

To be verified by Czech BIM experts:

- Ministry of Industry and Trade (MPO) – Koncepce zavádění metody BIM v ČR (state policy)
- Česká agentura pro standardizaci (ČAS) – implementation of the BIM concept, national standards and methodologies
- ČKAIT – professional practice of authorised engineers
- Odborná rada pro BIM (czBIM) – professional recommendations
- buildingSMART International – openBIM standards

A recognised institution does not automatically yield the highest rating; assess the specific document and claim.

## Domain rules

1. **Version matters.** IFC, IDS and ISO 19650 parts exist in several versions; record the exact version in the subject and rate an outdated version with `legalStatus: "repealed"` (or `currency` finding) when a newer one applies.
2. **Contractual bindingness.** For BIM requirements, record whether bindingness comes from law, a standard referenced by law, or only the contract.
