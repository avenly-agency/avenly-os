# Ton komunikacji — granice

Wypełniony na podstawie `avenly-web/docs/blog-style-guide.md` (anti-references) + obserwacji istniejących materiałów Avenly. **NAJWAŻNIEJSZY plik** dla `copywriter`.

## Słowa których NIE używamy (banlista)

### AI-buzzwords (top wykluczenie)
- `synergia`, `synergiczne`, `synergicznie`
- `rewolucyjny`, `rewolucja`
- `przełomowy`, `przełom`
- `innowacyjny`, `innowacja` (chyba że to dosłownie nowa innowacja — rzadko)
- `gamechanger`, `game-changer`
- `w erze AI`, `w czasach AI`
- `wykorzystaj potencjał AI`, `pełen potencjał`
- `na nowo definiuje`, `redefiniuje`
- `transformacja cyfrowa` (chyba że klient sam tak mówi)

### Agency-speak (korpomowa)
- `kompleksowo`, `kompleksowe podejście`, `kompleksowa obsługa`
- `rozwiązanie szyte na miarę`
- `value-add`, `value-driven`
- `leverage`, `leveragujemy`
- `best-in-class`
- `in-house` (po polsku: "wewnętrznie" — jeśli musimy używać)
- `premium` (chyba że to dosłownie premium tier — np. Avenly Premium support)
- `dedykowane rozwiązanie` (zastąp: "zrobione pod Twój przypadek")
- `partnerstwo strategiczne` (zastąp: "współpraca")

### Generyczne otwarcia (kasuj od razu)
- `W dzisiejszych czasach...`
- `W obecnej erze...`
- `Coraz więcej firm...`
- `Wraz z rosnącym znaczeniem...`
- `Czy zastanawiałeś się kiedyś...`
- `W świecie, który się ciągle zmienia...`
- `Niezależnie od tego, czy...`

### Pompowane przymiotniki
- `niesamowity`, `fantastyczny`, `wyjątkowy` (chyba że uzasadnione + bardzo rzadko)
- `olbrzymi`, `ogromny` — używaj liczby zamiast (`240% wzrost` zamiast `ogromny wzrost`)
- `wszechstronny`
- `dynamiczny` (frazes startup'owy)

### Clickbait (NIGDY)
- `TY NIE UWIERZYSZ`
- `JEDNA RZECZ KTÓRA...`
- `10 SEKRETÓW...`
- `Sekret którego nikt Ci nie powie`
- `Zrób TO dziś!`

## Słowa których używamy świadomie (Avenly-specific)

### Brand-defining (warto powtarzać)
- `Avenly` (zawsze tak — NIE "AVENLY", NIE "avenly", NIE "Avenly Agency")
- `W Avenly...` (wzorzec autorytatywny — `projektujemy`, `budujemy`, `wierzymy że...`)
- `agencja interaktywna` (główne pozycjonowanie — preferowane nad "agencja marketingowa", choć synonim OK w SEO)
- `robimy` (NIE "świadczymy usługi")
- `strona` (NIE "serwis WWW" — to korpomowa)
- `rozmawiamy` (NIE "konsultacje" chyba że klient B2B B2L)

### Wyrażenia z istniejących materiałów (pattern do utrzymania)

- `"realnie sprzedają"` / `"realnie zwiększą Twoje zyski"` (zamiast "konwertują")
- `"błyskawicznie ładuje się"` / `"ładuje się w ułamku sekundy"` (zamiast "szybko")
- `"strategiczne połączenie"` (gdy uzasadniamy wybór technologii)
- `"przejmie do 80% powtarzalnych zapytań"` (konkret w argumentacji AI)
- `"zostaw konkurencję w tyle"` (CTA hook w one-page'ach)

### Słowa-które-używamy-ostrożnie

- `dedykowane` — OK gdy mowa o "dedykowanych stronach" (kategoria usługi), unikaj jako wypełniacz
- `optymalizacja` — OK w kontekście technicznym (SEO, performance), unikaj jako synonim "poprawiamy"
- `ekspert` — OK gdy konkretnie ("ekspert Voiceflow", "ekspert SEO"), unikaj gdy generyczne ("nasi eksperci")

## Reguły formatowania (zawsze)

- **Akapity:** 2-4 linie max, breakpoint przy zmianie myśli
- **Listy:** używamy zamiast ścian tekstu (pattern z bloga: `<li><strong>Etykieta:</strong> Wyjaśnienie</li>`)
- **Wykrzykniki:** ZERO w nagłówkach. Max 1 na treść jeśli faktycznie wykrzykuje.
- **Emoji:**
  - **Cold mail / propozal / blog post:** ZERO
  - **Social IG/FB:** max 2-3 per post (NIE każda linia)
  - **Chat / internal:** swobodnie
- **Liczby:** konkretne (`3x szybciej`, `240%`, `<1s`) NIE ogólne (`znacznie`, `kilkukrotnie`)
- **Daty (PL):** `DD.MM.YYYY` lub `DD MMM YYYY` (np. `12.05.2026` / `12 maj 2026`)
- **Telefon:** `+48 668 124 367` (z myślnikami lub spacjami)
- **Strong:** 1-2× per akapit (kluczowe pojęcia, NIE pełne zdania)

## Forma zwracania się (Ty / Państwo)

| Kanał | Domyślnie | Wyjątek |
|---|---|---|
| Strona avenly.pl | **Ty** | — |
| Blog | **Ty** | — |
| Cold mail do SMB | **Ty** od początku ("Cześć [Imię]") | — |
| Cold mail do większej firmy 20+ os | **Pan/Pani** w pierwszym mailu, potem "Ty" jeśli odpowie naturalnie | — |
| Propozal dla SMB | **Ty** w soft sections, **Państwo** w warunkach umownych | — |
| Propozal dla firmy 20+ os | **Państwo** wszędzie | — |
| Social IG/FB | **Ty** / 3 osoba | — |
| Follow-up | **Ty** zazwyczaj (zachowanie z poprzedniej wymiany) | — |
| Newsletter (jeśli będziemy mieli) | **Ty** | — |

## Format CTA

### Blog post (blockquote końcowy) — wzorzec z istniejących postów

```html
<blockquote>
  <strong>[Pytanie hook z tematu posta]</strong><br>
  [Krótki opis tego co user dostanie — 1-2 zdania.] <br>
  <a href="/kontakt">[CTA text]</a>
</blockquote>
```

Wzorce CTA text z istniejących postów:
- `Zarezerwuj termin konsultacji`
- `Zamów darmowy audyt szybkości` (post #2 — UWAGA: linkował do `/audyt` którego nie ma — bug)
- `Skontaktuj się z zespołem Avenly`

**ZAWSZE link do `/kontakt`. NIGDY do `/audyt` (nie istnieje), `/oferta` (nie istnieje), inny invented endpoint.**

### Cold mail (ostatnia linia)

- `Chciałbyś omówić w 15 min jak to mogłoby u Was wyglądać?`
- `Mogę pokazać liczby w 15-min rozmowie?`
- `Daj znać czy temat jest dla Ciebie aktualny.`

### Social

- `Daj znać w komentarzu które byś wybrał`
- `Zapisz, przyda się`
- `Otaguj kogoś kto akurat planuje stronę`
- `Czy robicie podobnie? Podziel się w komentarzu.`

## Co robimy z błędami klientów

- Klient pisze błąd ortograficzny w briefie → poprawiamy w deliverable bez komentarza
- Klient ma niejasny pomysł → pytamy `Rozumiem to tak: [X]. Czy o to chodzi?` NIE `Co masz na myśli?`
- Klient prosi o coś co go skrzywdzi (np. dark pattern, fake reviews) → mówimy uczciwie `Tego nie robimy bo [X], ale możemy zamiast tego [Y]`

## Kontekst — kiedy można złamać regułę

- W blog poście można pozwolić sobie na 1 emoji w samej treści (rzadko, nigdy w lead) jeśli temat to dosłownie wymaga
- W carousel IG OK zacząć od pytania retorycznego (ale unikaj `Czy wiedziałeś że...` — frazes)
- W tweet / viral hook social — hook może być bardziej zaczepny niż w mailu
- W FAQ / dokumentacji technicznej — żargon OK gdy klient sam zna pojęcia

> Jeśli `copywriter` chce złamać regułę z banlisty — musi explicit przegłosować z userem w sesji (`template cold-email mówi że bez 'rewolucyjny' ale tu pasuje bo X — OK?`).
