# Template: Oferta / Proposal

Struktura standardowej oferty dla klientów Avenly.

## Format

- **Plik:** PDF (nie e-mail) dla projektów >5k PLN netto
- **Dla mniejszych projektów (<5k):** może być w treści maila albo Notion link
- **Język:** polski (z opcji EN tylko gdy klient sam mówi że EN)
- **Branding:** szablon z avenly.pl — ciemne tło, biel + niebieski akcent
- **Długość:** 4-7 stron (nie więcej — klient nie czyta dłuższych)

## Struktura

### 1. Kontekst klienta (1 strona)

- 2-3 zdania: kim jest klient, co robi, w jakim momencie biznesowym
- 2-3 zdania: jaki problem chcemy rozwiązać (jego słowami)
- Cel projektu (1 zdanie, mierzalnie jeśli możliwe)

**Pokazujesz że rozumiesz. NIE generyczne "Avenly to agencja która…"**

### 2. Co proponujemy — scope (1-2 strony)

- Konkretne deliverables (lista 5-10 punktów)
- Co JEST w zakresie / co NIE jest (klarowne granice)
- Kamienie milowe z datami (przykład: "Tydzień 1-2: Design / Tydzień 3-4: Development / Tydzień 5: Launch")

**Bullet points, NIE prose. Klient skanuje, nie czyta.**

### 3. Timeline (1 strona)

- Realne daty (uwzględnij weekendy, urlopy)
- Kamienie milowe z deliverables per faza
- Czego oczekujemy od klienta i kiedy (content, materiały, feedback)

### 4. Inwestycja (1 strona)

- Kwota w PLN **netto** + VAT
- Warunki płatności (standardowo: 50% z góry, 50% po launchu)
- Co jest wliczone / co kosztuje dodatkowo
- Termin ważności oferty (zwykle 14 dni)

### 5. Co dalej (0.5 strony)

- Najbliższy krok (np. "Akceptujesz tę ofertę → wysyłamy umowę → 50% przedpłaty → kickoff w [data]")
- Mail/telefon do podejmowania decyzji
- (opcjonalnie) 1 referencja klienta z tej samej branży

## Zasady absolutne

- **Bez** "value-add", "synergy", "leverage", "best-in-class"
- **Wszystko po polsku** (chyba że klient pisze do nas po angielsku)
- **Konkretne liczby** (nie "do uzgodnienia" jeśli można konkretnie)
- **Bez** rozbudowanego "About us" — klient już wie kim jesteśmy, jest na ostatnim etapie
- **Bez** opcji A/B/C "do wyboru" w pierwszej ofercie — proponujemy konkretny scope. Wariacje to follow-up.
- **Bez** legalese pełnych zdań — warunki w 2-3 punktach max, umowa to osobny dokument

## Pricing — jak myśleć

Patrz `10-Avenly/services-pricing.md`. Reguły dla `sales-strategist` przy ustalaniu ceny:
- Minimum 3000 PLN netto — niżej kierujemy do innych
- Discount tylko w wyjątkowych przypadkach (lojalność klienta, scope ograniczony)
- "Po znajomości" — uważnie. Lepiej standardowa cena + bonus deliverable.

## Po wysłaniu

- Follow-up po 5-7 dniach jeśli brak odpowiedzi
- Po 14 dniach (termin ważności) → automatyczny "oferta wygasła, mogę wysłać świeżą?"
- Status w avenly-crm: `mail_gotowy` → `wyslany` → `odpowiedz` (manualnie)

## Output `copywriter`

Dla oferty zwraca:
1. **Pełny tekst markdown** w strukturze wyżej (do późniejszego eksportu PDF)
2. **Skrótowa wersja "w treści maila"** — jak klient prosi o "wyślij coś w mailu" — 1 strona max
3. **Variables które trzeba podmienić** (lista) — np. {{kwota}}, {{timeline_start}}, {{kontekst_specific}}
