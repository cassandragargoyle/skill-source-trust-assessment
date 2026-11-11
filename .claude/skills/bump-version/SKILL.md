---
name: bump-version
description: 'Bump the skill version and/or the methodology version of source-trust-assessment (patch/minor/major), keeping SKILL.md metadata, methodology.md header, schema $id, template, profiles, fixtures, READMEs and CHANGELOG in sync. Use when the user wants to bump, raise, release or change a version (e.g. "zvedni verzi metodiky", "bump skill version", "nová patch verze skillu"). User-invocable via /bump-version.'
disable-model-invocation: false
metadata:
  internal: true
---

# Bump Version

Navýšení verze skillu `skills/source-trust-assessment/`. Komunikace s uživatelem probíhá **česky**, kód a commit messages **anglicky**.

> **NÁVRH.** Verzování projektu zatím není rozhodnuté (chybí ADR). Tento postup vychází
> z pravidel v AGENTS.md a CONTRIBUTING.md a z běžné praxe (SemVer, git tag `vX.Y.Z`,
> Keep a Changelog). Před prvním vydáním ho uprav podle schváleného ADR. Při použití
> upozorni uživatele, že jde o návrh.

Projekt má **dvě nezávislé verze**:

- **Verze skillu** (`metadata.version` v `SKILL.md`) — vydání skillu jako celku. Mění se při každém vydání: změna workflow v `SKILL.md`, nový nebo upravený profil, oprava validátoru, změna metodiky.
- **Verze metodiky** (`metadata.methodology-version`) — mění se **jen při změně kódů nebo pravidel** (AGENTS.md: *Version the methodology*). Změna metodiky vždy znamená i navýšení verze skillu. Přidání profilu metodiku **nemění** (CONTRIBUTING.md, FORKING.md).

Kanonickým zdrojem je `skills/source-trust-assessment/SKILL.md` (frontmatter `metadata`).

## KRITICKÉ PRAVIDLO

**NIKDY nepřidávej "Co-Authored-By: Claude" do git commitů ani do kódu.** Žádná AI atribuce není vyžadována.

## KROK 1: Urči, co se navyšuje

- Pokud uživatel řekl („verze metodiky", „verze skillu"), použij to.
- Jinak se podívej, co se od posledního tagu / vydání změnilo (`git log`, `git diff --stat <tag>..HEAD -- skills/`):
  - změna v `references/methodology.md`, `assets/assessment.schema.json`, `assets/vocabulary.ttl` nebo pravidlech validátoru → **metodika + skill**,
  - jinak → **jen skill**.

Navrhni a **STOP** — zeptej se, pokud to není jednoznačné.

## KROK 2: Zjisti aktuální verze

```bash
grep -n 'version' skills/source-trust-assessment/SKILL.md
grep -rn '<aktuální-verze-metodiky>' --exclude-dir=.git --exclude-dir=research .
git tag --list 'v*' --sort=-v:refname | head -5
```

Výpis `grep` ukáže všechna místa, kde je verze metodiky zapsaná (viz KROK 4).

## KROK 3: Navrhni novou verzi

Zeptej se uživatele, kterou složku verze navýšit:

- **patch** (výchozí): `X.Y.Z` → `X.Y.(Z+1)` — opravy textu, upřesnění bez změny významu kódů
- **minor**: `X.Y.Z` → `X.(Y+1).0` — nový kód, nové pravidlo, nový profil (u verze skillu), zpětně kompatibilní
- **major**: `X.Y.Z` → `(X+1).0.0` — změna nebo odebrání kódu, nekompatibilní změna schématu

Dokud je projekt `0.x`, nekompatibilní změna smí jít do **minor**.

Zobraz aktuální a navrhovanou verzi (skill i metodiku) a seznam souborů, které se změní.

**STOP** — počkej na schválení uživatelem.

## KROK 4: Aplikuj navýšení verze

### Verze skillu

1. `skills/source-trust-assessment/SKILL.md` → `metadata.version`
2. `skills/source-trust-assessment/SKILL.cs.md` → `version` ve frontmatteru (a zkontroluj, že překlad odpovídá aktuálnímu `SKILL.md`)
3. `.claude-plugin/plugin.json` → `version`

Soulad hlídá test `test_distribution_versions_match`.

### Verze metodiky (jen pokud se mění)

1. `skills/source-trust-assessment/SKILL.md` → `metadata.methodology-version` a `SKILL.cs.md` → `methodology-version`
2. `skills/source-trust-assessment/references/methodology.md` → hlavička `Version X.Y.Z · …`
3. `skills/source-trust-assessment/assets/assessment.schema.json` → `$id` (`…/schemas/assessment-X.Y.Z.json`) a `description` (`… methodology X.Y.Z.`)
4. `skills/source-trust-assessment/assets/assessment.template.json` → `methodology.version`
5. Profily `references/profiles/regions/*.md` a `references/profiles/domains/*.md` → řádek „Profile for the methodology version …" / „Profil k metodice verze …" (u profilu ověř, že změnu metodiky stále pokrývá; jinak ho označ k revizi)
6. Fixtures `tests/fixtures/valid/*.json` a `tests/fixtures/invalid/*.json` → `methodology.version`
7. `README.md` (`Status: … (methodology X.Y.Z)`) a `README.cs.md` (`Stav: … (metodika X.Y.Z)`)
8. `FORKING.md` → příklad `methodology.version`
9. `skills/source-trust-assessment/assets/vocabulary.ttl` → pokud nese verzi (`owl:versionInfo` apod.), aktualizuj ji

Po změně ověř, že stará verze metodiky už nikde nezůstala (kromě `CHANGELOG.md` a `research/`):

```bash
grep -rn '<stará-verze>' --exclude-dir=.git --exclude-dir=research . | grep -v CHANGELOG.md
```

### CHANGELOG

V `CHANGELOG.md` přejmenuj `## [Unreleased]` na `## [X.Y.W] - <dnešní datum YYYY-MM-DD>` (formát [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)) a nad ní založ prázdnou `## [Unreleased]`. Při změně metodiky uveď v záznamu i novou verzi metodiky a odkaz na ADR. Před úpravou se zeptej, zda vydání skutečně proběhlo.

### Testy

```bash
python -m unittest discover -s tests
python skills/source-trust-assessment/scripts/validate_assessment.py tests/fixtures/valid/*.json
```

## KROK 5: Potvrzení

Zobraz:

```text
source-trust-assessment bumped: skill X.Y.Z → X.Y.W, methodology A.B.C → A.B.D (nebo: unchanged)
Updated: SKILL.md, methodology.md, assessment.schema.json, ... (dle rozsahu)
Tests: OK
```

Navrhni commit (`chore: Bump version to X.Y.W`) a případný tag `vX.Y.W` — tag vytvoř až po potvrzení uživatelem.

Push tagu `vX.Y.W` spustí workflow `.github/workflows/release.yml`: ověří, že tag odpovídá verzi v `SKILL.md`, sestaví `source-trust-assessment-X.Y.W.zip` (jen adresář skillu) a založí GitHub Release s poznámkami z odpovídající sekce `CHANGELOG.md`. Sekce `## [X.Y.W]` proto musí v CHANGELOG existovat dřív, než tag pushneš.
