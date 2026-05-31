# Avenly.pl — struktura i kluczowe strony

Snapshot mapy strony avenly.pl (z `avenly-web/`). Dla agentów: gdzie czego szukać + jak istniejące copy używać jako referencji.

## Domena: https://avenly.pl

**Stack publiczny (co user widzi):**
- Static export Next.js → Hostinger
- Cloudflare CDN
- Brand: ciemne tło `#050505`, akcent niebieski `#2f5beb`
- Animacje: Framer Motion, GSAP, Lenis smooth scroll
- 5 lokalizacji z WebGL shaderami (Hero, Portfolio, Impact, /o-nas, /one-page)

## Główne strony

### `/` (Home)

10 sekcji w kolejności:

1. **Hero** — split: nagłówek `AVENLY TWOJA FIRMA WYŻSZY POZIOM` + makieta "powiadomień firmy" (3 karty)
   - WebGL Aurora shader (desktop only, mobile = CSS gradient)
2. **TechStack** — marquee 7 metryk
3. **Portfolio** — horizontal scroll z `FocusCard`, ostatnia karta CTA z `LiquidGlassBackground` shader
4. **Process** — pionowy timeline (#proces anchor)
5. **Impact** — bento 4 karty z WebGL contour shaders + GlassEdge (iOS 26 Liquid Glass)
6. **Testimonials** — 2 opinie Google (Maciej Piekarski, Perwee NLB) + JSON-LD Review/AggregateRating (5.0★)
7. **AiConsultant** — fake-chat sekwencja + CTA otwierający globalnego chatbota
8. **Services** — desktop taby / mobile accordion (#oferta + #uslugi)
9. **BlogTeaser** — top 3 najnowsze posty
10. **CallToAction** — finalny CTA do `/kontakt`

### `/uslugi/` (Services Hub)
Filtrowanie po kategoriach (Framer Motion). Lista wszystkich usług (aktywne + "wkrótce").

### `/uslugi/strony-www/`
Kategoria + 5 podstron:
- `/one-page/` (3-5 dni, HTML/SCSS/JS/Cloudflare)
- `/profesjonalna-strona-firmowa/` (WordPress + Impreza)
- `/dedykowane-strony-www/` (Next.js, ultra-fast)
- `/sklepy-internetowe/` (WP + WooCommerce + Impreza)
- `/aplikacje-webowe/` (custom Next.js + BaaS)

### `/uslugi/design/`
- `/ui-ux/` — aktywne
- `identyfikacja-wizualna/` — wkrótce
- `materialy-marketingowe/` — wkrótce

### `/uslugi/automatyzacje-ai/`
- `/chatboty-ai/` — aktywne (Voiceflow + Claude AI)

### `/uslugi/marketing/`
- `/audyt-wydajnosci-seo/` — wkrótce (page.tsx zwraca null)

### `/realizacje/` (Portfolio)

3 projekty (`avenly-web/app/data/projects.ts`):
1. **Mcentrum Fizjoterapia** — pełne case study (`hasCaseStudy: true`)
   - Strona: https://mcentrumfizjoterapia.pl
   - Tech: WordPress, Impreza, Booksy, Cloudflare
   - Wyniki: 1. miejsce w lokalnych wynikach po 1 miesiącu, <1s ładowania
2. **Radzyński Klub Sportowy** — tylko external link
   - Strona: https://klubsportowyrks.pl
   - Tech: WordPress, Impreza, Cloudflare
3. **Wirtualny Asystent AI** — Avenly własny
   - Tech: Claude AI, Next.js, TypeScript
   - Specjalność: live demo — klik karty otwiera chatbota na avenly.pl

### `/blog/` + `/blog/[slug]`

3 posty (datowane styczeń 2026):
1. `konsultant-ai-automatyzacja-obslugi-klienta` (AI & Automatyzacja, Biznes)
2. `szybkosc-strony-internetowej-seo-konwersja` (Performance, Biznes)
3. `dlaczego-strona-www-koniecznosc-2026` (Strategia, Biznes)

Pattern stylistyczny: patrz `50-Reference/existing-blog-posts.md` + `30-Templates/blog-post.md`.

### `/o-nas/`

GSAP zoom hero + statystyki + FAQ (3 pytania w `faq-data.ts`):
1. Faktury → przez Useme
2. Wsparcie po wdrożeniu → SLA, <24h reakcja
3. Czas realizacji → 2-4 tyg strony korporacyjne, 4-8 tyg sklepy

Zasila też FAQPage JSON-LD schema (rich snippet w SERP).

### `/kontakt/`

Formularz Web3Forms (access_key zaszyte w kodzie). Walidacja React Hook Form. Honeypot przeciw spamowi.
Pola: imię, email, telefon, temat, wiadomość, zgoda RODO.

### `/polityka-prywatnosci/`

Standardowa polityka prywatności + cookies.

## SEO setup (kompletny)

- **JSON-LD:** 8 typów (Organization, ProfessionalService, WebSite, BreadcrumbList, Service, BlogPosting, CreativeWork, FAQPage, Review/AggregateRating)
- **Robots.txt:** allow AI search bots (Google-Extended, OAI-SearchBot, PerplexityBot, Claude-SearchBot), block training bots (GPTBot, CCBot, anthropic-ai, ClaudeBot)
- **Sitemap:** hardcoded `SERVICE_PAGES` (omija marketingowe placeholdery)
- **PageSpeed:** mobile 85 / desktop 99
- **AI search visibility:** Google AI Overviews aktywnie cytuje z linkiem

## Wzorce komunikacji (do utrzymania)

Wyjątki/charakterystyczne formy z aktualnych treści:

**Nagłówki sekcji (Home):**
- _"Co mówią o nas Partnerzy Biznesowi?"_ (Testimonials — duże litery jak "Partnerzy Biznesowi" — trochę szlachetnie ale to działa)
- _"Twoja firma wyższy poziom"_ (Hero h1)

**Karty usług (services.ts):**
- _"Szybki start dla Twojego biznesu"_
- _"Zarządzaj swoją ofertą bez wiedzy technicznej"_
- _"Zostaw konkurencję w tyle dzięki niesamowitej wydajności"_
- _"Zarabiaj na autopilocie 24/7"_

**Blog CTA blockquote pattern:**
- _Strong + pytanie hook → opis value → link do `/kontakt`_

## Ograniczenia / known bugs

- `services.ts` design card linkuje do `/uslugi/design/design-stron-internetowych` → 404 (powinno być `/ui-ux`)
- `services.ts` marketing card linkuje do `/uslugi/marketing/audyt-seo-wydajnosci` → 404 (folder to `audyt-wydajnosci-seo`)
- Marketing pages zwracają `return null`
- Post #2 blockquote linkuje do `/audyt` → 404 (powinno być `/kontakt`)

## Czego NIE robimy na avenly.pl

- Newsletter signup (nie mamy)
- E-commerce dla siebie (nie sprzedajemy produktów cyfrowych)
- Chatbot wystawiony jako self-service product (mamy live demo, ale produkt sprzedawany 1-to-1)
- Multi-language (tylko PL — `lang="pl"` na html)
