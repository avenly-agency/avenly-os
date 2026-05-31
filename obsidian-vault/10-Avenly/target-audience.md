# Target Audience — Avenly

Wypełniony na podstawie `avenly-web/PRODUCT.md` + nisz w avenly-crm + analizy istniejących klientów (`avenly-web/app/data/projects.ts`).

## Główni klienci (primary)

### Archetyp 1: Właściciel SMB usługowego — **sweet spot Avenly**

- **Branże (z CRM workflow analizy):** fizjoterapia, dentystyka, psychologia, prawo, weterynaria, salony beauty, kliniki, gabinety, kluby sportowe, szkoły jogi/tańca, restauracje, hotele
- **Wielkość firmy:** 1-10 osób, obrót szacunkowo 200k–2M PLN/rok
- **Lokalizacja:** głównie miasta wojewódzkie + powiatowe (>30k mieszkańców)
- **Wiek właściciela:** 35-55
- **Stopień techniczności:** **niska** — ocenia agencję wizualnie i przez jasność value prop (PRODUCT.md: "not deeply technical — they evaluate agencies on visual credibility and clarity of value proposition")
- **Pain points:**
  - Aktualna strona robiona "kiedyś przez znajomego" — wygląda na 2018, nie responsywna, nikt do niej nie wraca
  - Klienci dzwonią pytać o rzeczy które powinny być na stronie ("czy macie godziny w niedzielę?", "czy przyjmujecie NFZ?")
  - Konkurencja na pierwszej stronie Google, oni gdzieś niżej
  - Brak czasu/wiedzy na social media — wrzucają coś raz na kwartał
  - Strona nie konwertuje — wiedzą o tym, ale nie wiedzą czemu
- **Co działa w komunikacji:**
  - Konkretne liczby ("Mcentrum: 1. miejsce w lokalnym SEO po miesiącu", "Amazon: 100ms opóźnienia = 1% mniej sprzedaży")
  - Case study tej samej branży ("zrobiliśmy stronę dla podobnej fizjoterapii w...")
  - Krótkie wezwanie do darmowej konsultacji
  - Wizualny dowód jakości (sama strona avenly.pl jest pitch'em)
- **Czego unikamy:**
  - Żargon techniczny: SSR, hydration, Core Web Vitals, ARIA — to dla nich szum (chyba że oświetla benefit: "ARIA = dostępność dla osób z niepełnosprawnościami = większe grono klientów")
  - "Premium" i "ekskluzywne" — odbierają to jako "drogo"
  - Długie listy fee — wolą rozmowę

### Archetyp 2: Większa firma szukająca konkretnego projektu (secondary)

- **Branże:** dowolne, często firmy 20-50 osób gdzie ktoś podejmuje decyzję o konkretnym projekcie
- **Typowe zlecenia:**
  - Dedykowana strona WWW (Next.js, customowy design, brand reset)
  - Aplikacja webowa (custom CRM, panele klientów, narzędzia branżowe)
  - Chatbot AI (poważniejsze wdrożenie, integracje)
  - Automatyzacja n8n (workflow inside firmy)
- **Pain points:**
  - Mają wewnętrzny dział marketingu/IT ale potrzebują "outside hands" na konkretny sprint
  - In-house jest zajęty bieżącą operacyjką
  - Wcześniejsza agencja zawiodła (drogie, długie, słabe)
- **Co działa w komunikacji:**
  - Profesjonalna oferta (PDF, struktura `30-Templates/proposal.md`)
  - Konkretny scope + kamienie milowe + ceny
  - Case study odpowiedniej skali
  - "Państwo" w treści formalnej (mail / propozal), "Ty" w nieformalnej (chat / mail follow-up)

## Tertiary audience (przyjmiemy ale nie polujemy)

- Startupy pre-seed potrzebujące landing page'a → one-page szybki
- Inne agencje szukające white-label developera (`developer` jako buyer persona)
- Jednorazowe wydarzenia / kampanie (event landing)

## Anti-audience (KOGO NIE chcemy)

- **Klienci szukający najtaniej (Fiverr-tier):** "zrób mi stronę za 500 zł". Kierujemy gdzie indziej.
- **"Wiedzą lepiej" — wymagają mikromanagement na każdym kroku**
- **Branże których nie chcemy:** [WYPEŁNIJ — typowo: hazard, treści dla dorosłych, MLM, pożyczki chwilówki, kryptocoiny pump'n'dump]
- **"Pilność na wczoraj":** "dziś trzeba zacząć, jutro launch". Bez rozmowy = bez projektu.
- **Klienci którzy nie chcą podpisywać umowy.** Bez umowy = bez startu.
- **Klienci którzy "wyślą maila gdy będą gotowi"** — brak konkretu, brak kontaktu, brak responsywności.

## Jak to wpływa na komunikację

- **Język:** prosty, bez żargonu, "Ty" w SMB
- **Hooki:** pain-driven (zadajemy pytanie o ból klienta) — "Twoja strona nie konwertuje? Sprawdziłeś czemu?"
- **CTA:** zawsze prowadzi do realnej rozmowy (mail / formularz / telefon), nie do "zapisu na newsletter"
- **Social proof:** case study z tej samej branży > generyczna lista logo klientów
- **Visual:** szybkie ładowanie + responsywność na pierwszym kontakcie = pierwsze wrażenie agencji (avenly.pl sama jest pitch'em)

## Mapa kanałów per archetyp

| Archetyp | Najlepszy kanał | Drugorzędny | Trzeciorzędny |
|---|---|---|---|
| Archetyp 1 (SMB usługowe) | Cold mail z kontekstem + telefon | Lokalne Google + opinie | FB grupy branżowe |
| Archetyp 2 (większe firmy) | LinkedIn + cold mail formalny + referencje | Case studies na blogu | Referrale od istniejących klientów |

## Geografia

- **Główny rynek:** Polska (PL)
- **Język operacyjny:** polski
- **Akceptujemy:** klientów z Polski (B2B i B2C SMB)
- **Nie aktywnie celujemy:** UE / global — choć technicznie nic nie stoi na przeszkodzie
