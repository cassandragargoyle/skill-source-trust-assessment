# Profil `cz` – Česká republika

Profil k [metodice](../../methodology.md) verze 0.1.0. Upřesňuje, jak se její kódy použijí v českém právním prostředí. Kódy ani jejich význam nemění. Právo EU popisuje [profil `eu`](eu.md).

Hodnocení podle tohoto profilu má `"context": { "region": "cz" }`.

## Právní autorita (`legalAuthority`) v ČR

Pořadí podle síly: ústavní pořádek (čl. 112 Ústavy) > vyhlášené mezinárodní smlouvy, které mají přednost před zákonem (čl. 10 Ústavy) > zákony > podzákonné předpisy. Právo EU má přednost v použití před českým zákonem (judikatura SDEU, čl. 10a Ústavy); podrobnosti v profilu `eu`.

| Kód | Co sem v ČR patří | Oficiální znění |
| --- | ----------------- | --------------- |
| `constitutional` | Ústava, Listina základních práv a svobod, ústavní zákony | e-Sbírka |
| `international` | vyhlášené mezinárodní smlouvy, k jejichž ratifikaci dal Parlament souhlas a jimiž je ČR vázána | e-Sbírka |
| `eu` | viz profil `eu` | EUR-Lex |
| `statutory` | zákony, zákonná opatření Senátu | e-Sbírka |
| `secondary` | nařízení vlády, vyhlášky ministerstev a jiných ústředních úřadů, obecně závazné vyhlášky obcí a krajů | e-Sbírka; Sbírka právních předpisů územních samosprávných celků |
| `case-law` | nálezy a usnesení ÚS, rozhodnutí NSS a NS (SDEU viz profil `eu`) | nalus.usoud.cz, nssoud.cz, nsoud.cz |
| `guidance` | metodiky a stanoviska ministerstev, technické normy ČSN (závazné jen při odkazu z předpisu) | weby ministerstev, Česká agentura pro standardizaci |
| `none` | ostatní obsah | – |

Oficiálním zněním předpisů ve Sbírce zákonů je od 1. 1. 2024 e-Sbírka (e-sbirka.gov.cz, zákon č. 222/2016 Sb.). Text z komerčních databází (ASPI, Beck-online, zakonyprolidi.cz) má podle pravidla 2 metodiky `legalAuthority: "none"`, dokud se neověří proti e-Sbírce.

Návrhy předpisů ve VeKLEP (odok.gov.cz/portal/veklep) mají `legalStatus: "draft"`; sněmovní tisky (psp.cz) také `draft` až do vyhlášení. Portál VeKLEP blokuje automatizované dotazy – dokumenty je nutné stáhnout ručně (pravidlo 6).

## Spolehlivost zdroje (`sourceReliability`) – typické české zdroje

| Kód | Typicky |
| --- | ------- |
| **A** | e-Sbírka, ministerstva, Úřad vlády (ODok, VeKLEP), Poslanecká sněmovna a Senát, soudy, ČÚZK, veřejné registry (ARES, seznamy ČKAIT a ČKA) |
| **B** | ČKAIT, ČKA, Svaz průmyslu a dopravy, Komora OZE, univerzity, ČTK, Ekonomický deník, Česká justice, celostátní a regionální deníky, banky, vlastník o vlastním majetku |
| **C** | odborné weby bez uvedeného autora, regionální katalogy, Wikipedie |
| **D** | marketingové weby, agregátory tiskových zpráv bez uvedení původce |
| **E** | weby známé šířením dezinformací |
| **F** | neznámý původce, sociální sítě, výstupy AI |

## Certifikovaný odborník (`certified-expert`) v ČR

| Oprávnění | Podle | Ověření |
| --------- | ----- | ------- |
| autorizovaný inženýr / technik / stavitel (ČKAIT) | zákon č. 360/1992 Sb. | seznam autorizovaných osob na ckait.cz |
| autorizovaný architekt (ČKA) | zákon č. 360/1992 Sb. | seznam ČKA |
| energetický specialista | zákon č. 406/2000 Sb. | seznam MPO |
| soudní znalec | zákon č. 254/2019 Sb. | seznam znalců Ministerstva spravedlnosti |

```json
"assessedBy": "certified-expert",
"assessor": { "name": "Jan Novák", "authorization": "ČKAIT 0000000", "field": "IP00" }
```

## Příklady

| Zdroj | Kód | Právní autorita | Stav |
| ----- | --- | --------------- | ---- |
| zákon č. 406/2000 Sb. v e-Sbírce | A1 | `statutory` | `in-force` |
| návrh novely zákona č. 406/2000 Sb. ve VeKLEP | A1 | `statutory` | `draft` |
| tisková zpráva MPO k novele | A2 | `none` | `n/a` |
| převzatá tisková zpráva MPO na zpravodajském portálu (`derivedFrom`: MPO) | A2 | `none` | `n/a` |
| článek Ekonomického deníku o připomínkovém řízení | B2 | `none` | `n/a` |
| informační leták banky shrnující zákon | B2 | `none` | `n/a` |
| odborný web bez autora shrnující směrnici EU | C3 | `none` | `n/a` |
| odpověď AI bez doložených zdrojů | F6 | `none` | `n/a` |

## Místní pravidla

1. **Povinnost se odvozuje z e-Sbírky.** Tvrzení o povinnosti podle českého předpisu musí být doloženo zněním z e-Sbírky (A1, `in-force`) k datu, ke kterému se posuzuje.
2. **Novely.** U předpisů s probíhající novelou uveď v `rationale`, ke kterému znění se hodnocení vztahuje, a odkaz na návrh (VeKLEP, sněmovní tisk).
