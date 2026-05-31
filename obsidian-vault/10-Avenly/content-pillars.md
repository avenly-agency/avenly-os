# Content Pillars — Avenly

Wypełniony na podstawie `avenly-web/docs/blog-style-guide.md` i istniejących 3 postów blogowych. Dostosuj proporcje jak ewoluuje strategia.

## Pillars (% mix dla wszystkiego co publikujemy)

| Pillar | % | Cel | Przykładowe tematy |
|---|---|---|---|
| **Edukacja** | 50% | Buduje autorytet | "Czym jest nowoczesny konsultant AI?", "Szybkość strony a SEO", "Core Web Vitals w praktyce", tutoriale branżowe |
| **Case study** | 25% | Pokazuje wyniki | Wyniki klientów (Mcentrum: nr 1 lokalnie w miesiąc, <1s ładowania), before/after, konkretne liczby |
| **Strategia / Biznes** | 15% | Pozycjonuje jako partnera | "Dlaczego własna strona to konieczność", "Niezależność od social media", argumenty inwestycyjne |
| **Behind-the-scenes / Promo** | 10% | Buduje markę i sprzedaje | Zespół, proces, oferty sezonowe, dostępność |

> **Uwaga:** istniejące 3 posty na avenly.pl/blog mają kategorie `AI & Automatyzacja`, `Biznes`, `Performance`, `Strategia`. Mix jest mocno przesunięty w stronę Edukacja+Strategia — Case studies dopiero dochodzą.

## Per platform

### Instagram (`@avenly.pl`)

- **Mix:** głównie Case study + Edukacja (60-70%)
- **Format:** głównie carousel (slajdy 5-10) + reels (15-30s), pojedyncze grafiki tylko dla quote'ów / hooków
- **Visual:** ciemne tło `#050505`, biel + niebieski `#2f5beb`, screen-pierwsze dla case'ów (mockup laptop/telefon)
- **Emoji w caption:** max 2-3 per post, nie spamujemy
- **CTA:** miękkie — pytanie, "save for later", "tag someone"

### Facebook (https://www.facebook.com/profile.php?id=61581862509345)

- **Mix:** więcej Promo + Behind-the-scenes (FB lepiej konwertuje na bezpośredni kontakt)
- **Format:** dłuższy storytelling OK (do 300 słów)
- **Hashtagi:** zero (FB nie indeksuje)
- **CTA:** pytanie wymuszające engagement (FB nagradza komentarze)

### LinkedIn (opcjonalnie — jeśli ruszamy)

- **Mix:** Edukacja + Behind-the-scenes (B2B-friendly)
- **Format:** long-form (1000-1500 znaków), line breaks dużo
- **Ton:** odrobinę bardziej formalny, ale wciąż bez korpo-mowy

### Blog avenly.pl/blog

- **Mix:** 100% Edukacja + Case study + Strategia (typowo wszystkie 3 razem)
- **Format:** 400-600 słów (5-6 min czytania), struktura w `30-Templates/blog-post.md`
- **Częstotliwość:** cel **2-4 posty / miesiąc** (konsystencja > velocity wg blog-style-guide)
- **Kategorie istniejące** (NIE wymyślaj nowych):
  - `AI & Automatyzacja`
  - `Biznes`
  - `Performance`
  - `Strategia`
  - `Development` (filtra obecny, brak postów)
  - `Design & UX` (filtra obecny, brak postów)
  - `Marketing` (filtra obecny, brak postów)
  - `News` (filtra obecny, brak postów)
  - `Tech` (filtra obecny, brak postów)

## Hashtagi (sygnatura)

### Brand (zawsze — IG)
- `#avenly` `#avenlypl`

### Industry (większość postów — IG)
- `#agencjareklamowa` `#stronywww` `#agencjamarketingowa` `#marketinginternetowy`

### Per pillar (IG)

| Pillar | Hashtagi |
|---|---|
| Edukacja | `#porady` `#wiedzao[temat]` `#tutoriale` `#seoporady` `#performance` |
| Case study | `#klient[branża]` `#wyniki` `#beforeafter` `#realizacja` |
| Strategia | `#strategia` `#marketingbiznesowy` `#smb` `#biznes` |
| Behind-the-scenes | `#zespol` `#kulisy` `#kultura` `#proces` |

> Maksymalnie 8-15 hashtagów na post IG. FB — bez hashtagów.

## Tematy które dobrze działają (z postów już opublikowanych)

1. **AI dla biznesu** — Voiceflow, chatboty, automatyzacje (post #1)
2. **Performance / techniczna jakość strony** — Core Web Vitals, szybkość, SEO (post #2)
3. **Strategia własnej strony vs social media** — niezależność, kontrola, długofalowe ROI (post #3)
4. **Case studies branżowe** — Mcentrum Fizjoterapia (`/realizacje/mcentrumfizjoterapia`)
5. **Tech edukacja dla SMB** — co to znaczy że strona "spełnia Core Web Vitals", po co RWD

## Tematy do dodania (sweet spot Avenly)

- Automatyzacje n8n (mamy własną instancję na `n8n.avenly.pl`)
- Lokalne SEO (mamy doświadczenie Mcentrum)
- WooCommerce optimization (z naszego stacku)
- AI w obsłudze klienta (rozszerzenie chatbotów)
- Migrations: stara strona → Next.js / WordPress IMPREZA
- Dostępność cyfrowa (WCAG — mamy doświadczenie z avenly.pl)

## Czego NIE publikujemy

- Memów politycznych, religijnych, dramy
- "Inspirujących cytatów" bez powiązania z naszym contentem
- Czystego promo bez wartości ("kup, kup, kup")
- Kopii postów konkurencji
- Materiałów klienta bez jego zgody
- Złotych myśli bez liczb ("Klienci kochają szybkie strony" — daj 100ms/Amazon zamiast)
- AI-fluff: "W dzisiejszych czasach", "W erze AI", "W świecie który się zmienia"

## Schedule recommendation (do dyskusji)

- **Blog:** 1-2× tydzień (2-4 / miesiąc — cel)
- **IG:** 3-5× tydzień (mix carousel + reel)
- **FB:** 1-2× tydzień (głównie longer-form posty z linkiem do bloga)
- **LinkedIn:** 1× tydzień (jeśli ruszamy)

Workflow generacji bloga: slash command `/new-post` w `avenly-web` (już istnieje). Workflow social: będzie agent `social-media-strategist` w tym OS.
