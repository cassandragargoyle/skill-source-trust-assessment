# Profile `eu` – European Union

Profile for the [methodology](../../methodology.md) version 0.1.1 covering EU law and EU institutions. Shared by all member-state profiles (e.g. [`cz`](cz.md)). It does not change any code.

## Legal authority (`legalAuthority`) for EU law

| Code | What belongs here | Official version |
| ---- | ----------------- | ---------------- |
| `eu` | Treaties (TEU, TFEU), Charter of Fundamental Rights, regulations, directives, decisions | EUR-Lex – the electronic Official Journal is authentic since 1 July 2013 (Regulation (EU) No 216/2013) |
| `case-law` | judgments and orders of the Court of Justice and the General Court | EUR-Lex, curia.europa.eu |
| `guidance` | Commission guidelines, recommendations, interpretative notes, FAQs; harmonised European standards (EN) | EUR-Lex, Commission websites, CEN/CENELEC |
| `none` | press releases, news, studies, consultancy reports | – |

EU law takes precedence in application over national law (CJEU case law, e.g. Costa v ENEL). How this interacts with the national constitution is described in the member-state profile.

### Directives and national obligations

A **directive** binds the member state as to the result. Obligations of private parties (e.g. a building owner) usually arise only from the **national transposing act**. Therefore:

- a claim *"the directive requires member states to …"* can be rated `eu` / `in-force` from EUR-Lex;
- a claim *"the owner must …"* based on a directive needs the national transposing act (member-state profile, e.g. `statutory` / `in-force`); while transposition is pending, the obligation is rated from the draft (`statutory` / `draft`) and the rationale states that it is not yet binding;
- after the transposition deadline, note any infringement procedure in the rationale (it does not create the obligation for private parties).

## Source reliability (`sourceReliability`) – typical EU sources

| Code | Typically |
| ---- | --------- |
| **A** | EUR-Lex, Official Journal, European Commission, European Parliament, Council, CJEU, EU agencies |
| **B** | European professional associations and think tanks (e.g. eceee, BPIE, EuroACE), specialised EU media, universities |
| **C** | expert blogs and portals without clear editorial control |
| **D–F** | as in the methodology |

## Examples

| Source | Code | Legal authority | Status |
| ------ | ---- | --------------- | ------ |
| Directive (EU) 2024/1275 (EPBD) in EUR-Lex | A1 | `eu` | `in-force` |
| Commission press release on infringement procedures | A1 | `none` | `n/a` |
| association news republishing a Commission press release (`derivedFrom`: Commission) | B1 | `none` | `n/a` |
| Commission interpretative guidance to a directive (published in EUR-Lex) | A1 | `guidance` | `in-force` |
