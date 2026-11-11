---
translation-of: SKILL.md
language: cs
normative: false
version: "0.1.1"
methodology-version: "0.1.1"
note: >
  Informativní český překlad SKILL.md. Agent načítá pouze anglický SKILL.md.
  V případě rozporu mezi touto verzí a anglickou verzí platí anglická verze (SKILL.md).
---

# Hodnocení důvěryhodnosti zdrojů

> Toto je informativní překlad. Závazná je anglická verze [SKILL.md](SKILL.md); v případě rozporu platí ona.

Posuď zdroj, dokument nebo tvrzení a vrať strukturovaný, reprodukovatelný výsledek s důkazy. Metodika je v [references/methodology.md](references/methodology.md); přečti ji před prvním hodnocením v relaci.

**Popis skillu:** Hodnocení důvěryhodnosti informačního zdroje, dokumentu nebo jednotlivého tvrzení založené na důkazech. Používá Admiralty Code (spolehlivost zdroje A–F, věrohodnost informace 1–6) doplněný o právní autoritu a právní stav, s regionálními a doménovými profily (např. Česká republika, EU, BIM). Použij při ověřování předpisů, norem, úředních dokumentů, článků nebo tvrzení generovaných AI dříve, než se na ně spolehneš, když se uživatel ptá, jak důvěryhodný je nějaký zdroj, nebo když se tvrzení přiřazují k jejich zdrojům. Funguje v jakémkoli jazyce (např. „ověř tento zdroj“, „jak důvěryhodný je tento dokument“, „odkud pochází toto tvrzení“).

## Kdy použít

- Uživatel se ptá, jak důvěryhodný je zdroj, dokument, web nebo tvrzení.
- Tvrzení (často generované AI) je třeba ověřit proti zdrojům, na které odkazuje.
- Ze zdroje se má odvodit právní nebo technická povinnost.

## Postup

1. **Urči předmět a úroveň.** Jde o vydavatele (organizaci), dokument, nebo jednotlivé tvrzení? Zaznamenej název, URL a datum získání.
2. **Vyber profily.** Regionální (např. `cz`), sdílený profil `eu`, pokud jde o právo EU, a doménový (např. `bim`). Přečti odpovídající soubory v [references/profiles/](references/profiles/). Pokud žádný profil neodpovídá, použij jen metodiku a uveď to.
3. **Najdi originál.** Převzatý obsah dohledej k jeho původci (`derivedFrom`). U právních předpisů najdi oficiální znění uvedené v regionálním profilu.
4. **Shromáždi důkazy.** U každého zjištění ulož URL, doslovnou citaci a její vztah (`relation`) k předmětu: `confirms`, `partially-confirms`, `contradicts` nebo `context` (metodika § 4).
5. **Zkontroluj kritéria.** Autorita, pravost, aktuálnost, přesnost, nezávislost, dohledatelnost, relevance (metodika § 4). Zaznamenávej zjištění, ne body.
6. **Přiřaď kódy.** `sourceReliability` A–F a `informationCredibility` 1–6, potom `legalAuthority` a `legalStatus`. F a 6 znamenají *neznámé*, ne *nejhorší*.
7. **Zaznamenej původ.** `assessedBy` je `ai`, pokud výsledek nezkontroloval člověk; `verificationStatus` zůstává u hodnocení provedených jen AI `unverified`.
8. **Vrať výsledek** jako JSON podle [assets/assessment.schema.json](assets/assessment.schema.json) (šablona: [assets/assessment.template.json](assets/assessment.template.json)), následovaný krátkým shrnutím srozumitelným jazykem.
9. **Zvaliduj** JSON, pokud je k dispozici shell: `python scripts/validate_assessment.py <soubor.json>`.

## Pravidla

- Nikdy si nevymýšlej zdroje, citace, URL ani data. Co nelze najít, patří do `unresolved`.
- Hodnoť původce, ne web, kde byl obsah nalezen.
- Neslučuj dimenze do jednoho skóre.
- Závaznost plyne jen z oficiálního znění právního předpisu; vše ostatní má `legalAuthority: "none"`.
- Povinnost lze odvodit jen z informace s věrohodností 1.
- Neobcházej omezení přístupu (přihlášení, ochrana proti botům). Zablokovaný zdroj zapiš do `unresolved` a navrhni ruční získání.
- Shrnutí a volné textové části piš v jazyce uživatele. Kódy, názvy polí a hodnoty výčtů zůstávají anglicky, jak jsou definovány; citace zůstávají doslovně v jazyce zdroje.
- Uveď verzi metodiky a použité profily. Pokud se od metodiky odchýlíš, nastav `methodology.modified: true` a vysvětli proč.
