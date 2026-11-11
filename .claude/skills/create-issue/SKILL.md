---
name: create-issue
description: 'Založení nového issue metodou GitHub-first — nejdřív vznikne GitHub issue (GitHub přidělí číslo), pak se dopíše detailní zápis do docs/issues/NNN-*.md. Použij když chce uživatel vytvořit/založit issue, feature request, bug nebo návrh nového profilu. Příklady: "založ issue …", "/create-issue profil sk", "vytvoř issue na …".'
argument-hint: [krátký popis issue]
allowed-tools: Read, Glob, Grep, Bash, AskUserQuestion, Write, Edit
user-invocable: true
metadata:
  internal: true
---

# Založení issue (GitHub-first)

Založení nového issue v projektu skill-source-trust-assessment.

**Argument:** $ARGUMENTS

## Princip

**GitHub je jediný zdroj pravdy pro seznam issues.** Číslo přiděluje GitHub při
založení. Na GitHubu je jen **základ** (titulek + krátký popis + odkaz na detailní
soubor). Detaily žijí v `docs/issues/NNN-*.md`, kde `NNN` = číslo GitHub issue.
Pokud adresář `docs/issues/` ještě neexistuje, založ ho.

**Nepřidávej žádné přehledové tabulky** do README — byly odstraněny kvůli konfliktům.

## Instrukce

### KROK 1: Zjisti podklady

Z argumentu / kontextu (nebo přes `AskUserQuestion`, pokud chybí) zjisti:

- **Titulek** — krátký, výstižný, anglicky (bez čísla; GitHub ho doplní sám)
- **Slug** — kebab-case pro název souboru (odvoď z titulku, např. `region-profile-sk`)
- **Typ**: Feature | Enhancement | Bug Fix | Methodology | Profile | Docs | Task
- **Priorita**: Critical | High | Medium | Low
- **Komponenta** — podle části repozitáře:
  - `skill` — workflow v `SKILL.md`
  - `methodology` — kódy a pravidla v `references/methodology.md` (změna vyžaduje ADR a navýšení verze metodiky)
  - `profile-<kód>` — profil, např. `profile-cz`, `profile-eu`, `profile-bim` (nový profil: `profile-<nový kód>`)
  - `schema` — `assets/assessment.schema.json`, šablona, `vocabulary.ttl`
  - `validator` — `scripts/validate_assessment.py` a testy
  - `docs` — README, ADR, CONTRIBUTING, FORKING
  - `build-infra` — CI, nástroje repozitáře, `.claude/`
- **Krátký popis** (1–3 věty) — půjde do těla GitHub issue
- **Detailní obsah** — půjde do lokálního `.md` (problém, kroky, akceptační kritéria, testy)

Všechny texty **anglicky** (projektová konvence). Výjimka: citace a příklady z regionálního
profilu mohou být v jazyce regionu.

Pokud issue mění **kódy nebo pravidla metodiky**, upozorni, že bude potřeba ADR v `docs/adr/`
a změna v `methodology.md`, schématu, `vocabulary.ttl`, validátoru, `SKILL.md` a `CHANGELOG.md`
najednou (AGENTS.md, CONTRIBUTING.md). Uveď to v akceptačních kritériích.

### KROK 2: Preflight — ověř `gh`

```bash
gh --version && gh auth status
```

Pokud `gh` není v PATH, zkus `"/c/Program Files/GitHub CLI/gh.exe"`.
Pokud není přihlášeno, přeruš a vyzvi uživatele: `gh auth login` (klidně přes `!` prefix).

### KROK 3: Založ GitHub issue (GitHub přidělí číslo)

Tělo drž **minimální** — krátký popis + placeholder pro odkaz (doplní se v kroku 5):

```bash
REPO="cassandragargoyle/skill-source-trust-assessment"
gh issue create --repo "$REPO" \
  --title "<TITULEK>" \
  --body "<KRÁTKÝ POPIS>

📄 Full details: docs/issues/<NNN>-<slug>.md" \
  [--label <type>,<priority>,<component>]
```

`gh issue create` vypíše URL — z ní vytáhni **číslo `NNN`**
(`.../issues/12` → `NNN=12`, v názvu souboru doplň nuly na tři místa: `012`). Labely přidávej
jen když už na GitHubu existují (`gh label list --repo "$REPO"`), jinak vynech (nezakládej je automaticky).

### KROK 4: Napiš detailní soubor

Vytvoř `docs/issues/<NNN>-<slug>.md` s plným obsahem. Doporučená kostra:

```markdown
# Issue #<NNN>: <Titulek>

## Summary
<1–3 věty>

**Status**: Open
**Priority**: <priorita>
**Component**: <komponenta>
**Created**: <YYYY-MM-DD>
**GitHub**: #<NNN>
**Related**: #<...>, ADR-<...>

## Problem Description
...

## Proposed Change
<dotčené soubory; u metodiky: kódy, verze metodiky, ADR>

## Acceptance Criteria
1. ...
2. `python -m unittest discover -s tests` passes
3. Valid fixtures pass `validate_assessment.py`

## Testing
<nové fixtures v tests/fixtures/valid|invalid, nové testy>
```

### KROK 5: Doplň do GitHub issue přesný odkaz

Teď, když známe `NNN` a název souboru, aktualizuj tělo o funkční odkaz
(blob URL na `main`):

```bash
URL="https://github.com/$REPO/blob/main/docs/issues/<NNN>-<slug>.md"
gh issue edit <NNN> --repo "$REPO" \
  --body "<KRÁTKÝ POPIS>

📄 [Full details](${URL})"
```

> Odkaz začne fungovat, jakmile je soubor na `main`. Do té doby ukazuje na
> cílovou cestu (relativní zápis v těle zůstává čitelný i tak).

### KROK 6: Neupravuj README tabulky

Seznam issues je na GitHubu. **Žádné tabulky se needitují.**

### KROK 7: Shrnutí

Zobraz uživateli:

```text
Issue #<NNN> založeno.

GitHub:  https://github.com/cassandragargoyle/skill-source-trust-assessment/issues/<NNN>
Detail:  docs/issues/<NNN>-<slug>.md
Typ/Priorita/Komponenta: <type> / <priority> / <component>

Další kroky:
  /implement-issue <NNN>
  # branch:  feature/<NNN>-<slug>
  # commit:  feat(<NNN>): <titulek>   (uzavře přes: closes #<NNN>)
```

## Poznámky

- Číslo **nikdy nevymýšlej** — vždy ho dá GitHub. GitHub issues a PR sdílejí
  jeden čítač, takže čísla můžou přeskakovat.
- Při archivaci hotového issue: `gh issue close <NNN>` +
  `git mv docs/issues/<NNN>-*.md docs/issues/done/`.
- Kompletní metodika: `docs/contributing/ISSUE-MANAGEMENT.md`.
