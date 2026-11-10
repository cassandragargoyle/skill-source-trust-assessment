---
language: cs
translation-of: SKILL.md
warning: Český překlad pro lidi. Závazná je anglická verze SKILL.md; při jakémkoli rozporu má přednost anglická verze.
---

# Dokončení feature branch

Dokončení práce na feature branch — testy, kontrola README/CHANGELOG/verzí, merge do hlavní větve, úklid branch a volitelná aktualizace stavu issue.

@.claude/prompts/assistant-programming.md

**DŮLEŽITÉ: NIKDY nepřidávej "Co-Authored-By: Claude <noreply@anthropic.com>" do kódových souborů ani git commitů.**

## Instrukce

### KROK 1: Zjisti kontext

Zeptej se mě na:

1. Název feature branch (nebo použij aktuální branch)
2. Cílová větev pro merge (výchozí `main`)

Ověř, že branch existuje a obsahuje commity. Vypiš změněné soubory:

```bash
git diff --name-only <cílová-větev>...HEAD
```

### KROK 2: Spusť kontroly

Spusť stejné kontroly jako CI (`.github/workflows/ci.yml`):

```bash
python -m unittest discover -s tests -v
python skills/source-trust-assessment/scripts/validate_assessment.py tests/fixtures/valid/*.json
```

Pokud se změnil `vocabulary.ttl` a je k dispozici `rdflib`, zparsuj i slovník
(dělá to CI; skill na něm nezávisí):

```bash
python -c "import rdflib; g = rdflib.Graph(); g.parse('skills/source-trust-assessment/assets/vocabulary.ttl', format='turtle'); print(len(g), 'triples')"
```

Pokud cokoli selže, **STOP** a nahlas to. Neslučuj červenou větev.

### KROK 3: Zkontroluj konzistenci změny

Porovnej změněné soubory s pravidly projektu (AGENTS.md, CONTRIBUTING.md):

1. **Distribuovaný adresář zůstává čistý.** `skills/source-trust-assessment/` neobsahuje
   výzkumné poznámky, testy, CI ani jiné soubory určené jen pro repozitář.
2. **Kódy jsou definované jednou.** Pokud větev přidává nebo mění kód, je stejná změna v
   `references/methodology.md`, `assets/assessment.schema.json`, `assets/vocabulary.ttl`
   a `scripts/validate_assessment.py` (+ testy).
3. **Verzování metodiky.** Pokud se změnily kódy nebo pravidla, je navýšená verze metodiky
   (`SKILL.md` `metadata.methodology-version`, hlavička `methodology.md`, `$id` schématu)
   a existuje ADR v `docs/adr/`. Pokud ne, nabídni `/bump-version`.
4. **Profily** kódy jen upřesňují, nikdy je nepředefinují ani nepřidávají. Nový profil je
   uvedený ve `vocabulary.ttl` (`sta:profileScheme`) a má platnou fixture v `tests/fixtures/valid/`.
5. **CHANGELOG.md** má pod `## [Unreleased]` záznam pro každou změnu viditelnou pro uživatele.

### KROK 4: Aktualizace README

Než větev sloučíš, ověř, že README odpovídají stavu po změně. Zkontroluj `README.md` i `README.cs.md`:

- verze metodiky v přehledu (`Status: … (methodology X.Y.Z)` / `Stav: … (metodika X.Y.Z)`)
  se shoduje s `metadata.methodology-version` v `SKILL.md`,
- výčet profilů (`cz`, `eu`, `bim`, …) v přehledu a ve „Struktuře repozitáře" odpovídá
  `references/profiles/regions/` a `references/profiles/domains/`,
- návod k instalaci a použití a struktura repozitáře nejsou zastaralé.

```bash
grep -n "methodology-version\|  version" skills/source-trust-assessment/SKILL.md
grep -n "methodology\|metodika" README.md README.cs.md
ls skills/source-trust-assessment/references/profiles/*/
```

Pokud něco nesedí, uprav to a commitni do feature branch ještě před merge:

```text
docs(<issue-id>): Update READMEs
```

Pokud README odpovídají, krok přeskoč a uveď to ve shrnutí.

### KROK 5: Merge a úklid

> **Co je PR (Pull Request)?** Žádost o začlenění změn z feature branch do hlavní větve. Používá se pro code review v týmech. Pro solo vývoj lze mergovat přímo.

Zeptej se uživatele na preferovaný postup. Změny metodiky (kódy, pravidla) by měly jít přes PR,
protože je musí posoudit maintainer (GOVERNANCE.md).

#### Varianta A: Přímý merge (výchozí pro solo vývoj)

Zjisti zdrojovou větev (ze které feature branch vznikla) a proveď merge:

```bash
git checkout <zdrojová-větev>    # např. main
git merge feature/<issue-id>-<popis>
git branch -d feature/<issue-id>-<popis>
```

**STOP** - Počkej na potvrzení před provedením merge.

#### Varianta B: Pull Request (pro týmovou spolupráci)

Připrav PR popis:

- **Summary**: Co tento PR dělá
- **Motivation**: Proč (odkaz na issue, případně ADR)
- **Changes**: Seznam změn; případná změna verze metodiky
- **Testing**: Kroky pro ověření (`python -m unittest discover -s tests`, validátor na fixtures)

Vytvoř PR pomocí `gh pr create`.

### KROK 6: Aktualizace issue (volitelné)

Zeptej se uživatele: "Je tímto issue kompletně dokončeno?"

#### Pokud ANO:

Uprav soubor issue v `docs/issues/`:

- Změň `**Status:** 📋 Open` na `**Status:** ✅ Implemented`
- Přidej datum uzavření

Přesuň soubor do archivu a uzavři GitHub issue (README tabulky neexistují — seznam je na GitHubu):

```bash
git mv docs/issues/<NNN>-*.md docs/issues/done/
gh issue close <NNN> --repo cassandragargoyle/skill-source-trust-assessment
```

Commitni změnu stavu issue:

```text
docs(<issue-id>): Close issue - implementation complete
```

#### Pokud NE:

Přeskoč aktualizaci stavu. Issue zůstává otevřené pro další práci.

### KROK 7: Shrnutí

Zobraz shrnutí:

- Testy a validace fixtures: prošly
- Kontrola konzistence (kódy, verze, profily, CHANGELOG): OK / opraveno / problémy
- README aktualizována: ano/ne (nebylo potřeba)
- Merge provedený do větve: `<název>` (nebo URL PR)
- Feature branch smazána: ano/ne
- Issue status aktualizován: ano/ne/přeskočeno
- Další kroky (pokud jsou, např. `/bump-version` před vydáním)
