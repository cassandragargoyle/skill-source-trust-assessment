# Source Trust Assessment

<img src="docs/icon/icon.svg" alt="ikona source-trust-assessment" width="128" height="128">

*English: [README.md](README.md).*

## Přehled

- **Repozitář**: `skill-source-trust-assessment`
- **Název skillu**: `source-trust-assessment`
- **Formát**: [Agent Skill](https://agentskills.io/specification) (`SKILL.md`) – Claude Code, Codex a další agenti
- **Stav**: počáteční (metodika 0.1.1)

Open-source Agent Skill pro posouzení důvěryhodnosti informačních zdrojů na základě důkazů, napříč regiony, obory a typy zdrojů.

Skill říká AI agentovi, jak posoudit vydavatele, dokument nebo jednotlivé tvrzení a vrátit strukturovaný, reprodukovatelný výsledek s důkazy. Důvěryhodnost neslučuje do jednoho čísla. Používá:

- **Admiralty Code** (NATO STANAG 2511): spolehlivost zdroje A–F a věrohodnost informace 1–6, zapsané jako `A1`, `B2`, `F6`;
- **právní autoritu** a **stav předpisu**: zda jde o závazný předpis, návrh, nebo vůbec o předpis;
- **původ**: kdo hodnotil, kdy a z čeho informace vznikla (W3C PROV-O).

Jak se kódy použijí v určité zemi nebo oboru, určují **profily**: regionální (`cz`, `eu`) a oborové (`bim`). Profil ČR je v češtině, základ metodiky v angličtině.

## Instalace

V produkci používej konkrétní vydanou verzi, aby se metodika neměnila bez tvého vědomí. Vydání jsou na stránce [Releases](https://github.com/CassandraGargoyle/skill-source-trust-assessment/releases).

### Libovolný agent (Claude Code, Codex, Cursor, …)

```bash
npx skills add CassandraGargoyle/skill-source-trust-assessment
```

### Plugin pro Claude Code

```text
/plugin install source-trust-assessment --marketplace cassandragargoyle/skill-source-trust-assessment
```

Ve starších verzích Claude Code nejdřív přidej marketplace:

```text
/plugin marketplace add CassandraGargoyle/skill-source-trust-assessment
/plugin install source-trust-assessment@cassandragargoyle
```

### Claude.ai a Claude Desktop

Stáhni `source-trust-assessment-<verze>.zip` z [posledního vydání](https://github.com/CassandraGargoyle/skill-source-trust-assessment/releases/latest) a nahraj ho v *Settings → Capabilities → Skills*.

### Ruční kopie

Zkopíruj `skills/source-trust-assessment/` do `.claude/skills/` (Claude Code) nebo `.agents/skills/` (Codex) svého projektu. Český překlad pokynů pro agenta je v [SKILL.cs.md](skills/source-trust-assessment/SKILL.cs.md) (informativní, platí anglická verze).

## Použití

```text
/source-trust-assessment
Posuď https://e-sbirka.gov.cz/eli/cz/sb/2000/406 pro region cz,
účel: povinnost energetického auditu obchodního centra.
```

Agent vrátí JSON podle [assessment.schema.json](skills/source-trust-assessment/assets/assessment.schema.json) a krátké shrnutí. Ověření:

```bash
python skills/source-trust-assessment/scripts/validate_assessment.py result.json
```

## Omezení

- **Nejde o právní radu.** Výsledek je strukturovaný, důkazy podložený názor na to, nakolik se lze na zdroj spolehnout, ne právní stanovisko. Než podle zjištěné povinnosti začneš jednat, přečti si oficiální znění předpisu nebo se obrať na odborníka.
- **Hodnocení od AI je neověřené.** Hodnocení, které provedl jen AI agent, má vždy `verificationStatus: "unverified"`. Stav `verified` získá až po kontrole odborníkem (metodika § 5).
- **Agenti chybují.** Zkontroluj citace a URL v `evidence`; zdroje, které nešlo získat, jsou uvedené v `unresolved`.

### Stav profilů

| Profil | Typ | Jazyk | Stav |
| ------ | --- | ----- | ---- |
| `cz` | regionální | čeština | použitelný |
| `eu` | regionální | angličtina | použitelný |
| `bim` | oborový | angličtina | **návrh** – seznamy institucí čekají na kontrolu odborníky z oboru |

## Struktura

Do projektů uživatelů se instaluje jen `skills/source-trust-assessment/`. Výzkum, testy a rozhodnutí zůstávají v repozitáři. Podrobně v [README.md](README.md#repository-structure).

## Úpravy

Místo změny metodiky přidej profil, viz [CONTRIBUTING.md](CONTRIBUTING.md). Změny kódů nebo pravidel patří do forku, viz [FORKING.md](FORKING.md). Fork, který mění metodiku, musí výsledky označit `methodology.modified: true`.

## Licence

[MIT](LICENSE)
