# Case Studies — Avenly portfolio

3 projekty w portfolio (z `avenly-web/app/data/projects.ts`). Używane przez `sales-strategist` (jako social proof), `copywriter` (cold maile, propozale), `social-media-strategist` (treści Case study pillar).

---

## 1. Mcentrum Fizjoterapia ⭐ (pełne case study)

> **Source:** `avenly-web/app/data/projects.ts` + `avenly-crm/knowledge_base` (kategoria `social_proof`). Zsynchronizowane 2026-05-24.

- **Slug w portfolio:** `/realizacje/mcentrumfizjoterapia`
- **Klient:** Gabinet Fizjoterapii Mcentrum (nowa marka)
- **Branża:** Fizjoterapia (lokalna usługa zdrowotna)
- **Lokalizacja:** [WYPEŁNIJ miasto]
- **Rok:** 2025
- **Kategoria:** Strona WWW + integracje
- **Live:** https://mcentrumfizjoterapia.pl
- **Tech stack:** WordPress + IMPREZA, Booksy, Cloudflare

### Challenge

**Wejście na rynek lokalny jako nowa marka.** Klient potrzebował widoczności oraz umocnienia wizerunku.

### Solution (pełen zakres prac z CRM)

- Stworzenie wydajnej strony internetowej zoptymalizowanej pod SEO
- Implementacja systemu rezerwacji **Booksy**
- Optymalizacja prędkości ładowania strony
- Struktura danych (Schema.org) dla lokalnych wyników wyszukiwania
- Wdrożenie **Cloudflare** (CDN + DNS + cache)
- Platforma: **WordPress IMPREZA**

### Wyniki (mierzone)

| Metryka | Wartość |
|---|---|
| Pozycja w wyszukiwarce (lokalne) | **Nr 1 w ciągu 1 miesiąca** |
| Czas ładowania | **<1s** |
| Wzrost rezerwacji | **Duży** (TODO: dokładna liczba, jeśli mamy w analytics klienta) |
| Status rynkowy | **Całkowita dominacja lokalnego rynku SEO** |

### Cytaty do reuse (zatwierdzone w CRM)

> _"Start nowej marki i całkowita dominacja lokalnego rynku SEO"_

> _"Dzięki błyskawicznemu ładowaniu i strukturze danych, strona zajęła 1. miejsce w lokalnych wynikach wyszukiwania już po jednym miesiącu"_

### Wzorzec do reuse w komunikacji

- **Cold mail do fizjoterapeutów / klinik:**
  > _"Robimy dla podobnych klinik strony które zajmują 1. miejsce w lokalnym Google już po miesiącu. Mcentrum Fizjoterapia ([link]) to nasz najnowszy case — strona ładuje się <1s, integracja z Booksy, rezerwacje wyraźnie wzrosły. Mogę pokazać proces na 15-min rozmowie?"_

- **Social post (case study pillar):**
  > _"Centrum Fizjoterapii **w 1 miesiąc** wskoczyło na 1. miejsce lokalnych wyników. **Strona ładuje się <1s**. Co zrobiliśmy: [3 punkty]. Carousel poniżej — slide-by-slide."_

- **Argumentacja "za drogo":** _"Mcentrum był w podobnej skali jak Wy. Zwrot pieniędzy w 6 miesięcy."_

### Materiały do social
- `/public/portfolio/mcentrumgabinet.webp` — main
- `/public/portfolio/mcentrum-full-screen.webp` — mockup full screen
- `/public/portfolio/gaelria-mcentrum-1.webp`, `galeria-mcentrum-2.webp` — galeria

---

## 2. Radzyński Klub Sportowy

- **Slug:** `klub-sportowy` (tylko external link, brak case study page)
- **Klient:** Radzyński Klub Sportowy
- **Branża:** Sport / kluby sportowe
- **Lokalizacja:** Radzyń (Podlaski / Chełmiński — [WYPEŁNIJ który])
- **Rok:** 2025
- **Live:** https://klubsportowyrks.pl
- **Tech:** WordPress, Impreza, Cloudflare
- **Status:** `hasCaseStudy: false` (nie publikujemy szczegółów, tylko external link)

### Wzorzec do reuse

- **Cold mail do klubów sportowych / fitness:**
  > _"Robimy strony dla klubów sportowych — np. Radzyński Klub Sportowy ([link]). Czytelna oferta, rejestracja zawodników, kalendarz wydarzeń. Mogę pokazać jak to mogłoby wyglądać u Was?"_

> **Uwaga:** nie publikujemy konkretnych metryk tego projektu (klient nie wyraził zgody albo nie zbieraliśmy). Komunikujemy go tylko jako _live example_ + tech stack.

---

## 3. Wirtualny Asystent AI (Avenly własny)

- **Slug:** `wirtualny-asystent-ai`
- **Klient:** Avenly (siebie samym)
- **Branża:** AI & Boty
- **Rok:** 2025
- **Tech:** Claude AI, Next.js, TypeScript
- **Live:** chatbot na avenly.pl (kliknij bubble w prawym dolnym rogu)
- **Status:** `hasCaseStudy: false` + `openChat: true` (klik karty otwiera chatbota jako demo)

### Description (z projects.ts)
_"Nasz własny asystent AI — odpowiada na pytania, kwalifikuje leady i pracuje za Ciebie 24/7."_

### Wzorzec do reuse

- **Cold mail dla branż z dużym ruchem zapytań (medycyna, beauty, restauracje, B2B):**
  > _"Nasz własny chatbot na avenly.pl (możesz go zobaczyć live) zbiera leady 24/7 i kwalifikuje ich przed kontaktem człowieka. Wdrażamy podobne dla klientów — Voiceflow na małą skalę, custom Claude AI na większą. Chcesz zobaczyć jak to mogłoby działać w Waszej branży?"_

- **Live demo > slajdy:** zawsze zachęcamy do interakcji z chatbotem na avenly.pl jako proof of competency. To unikalny wyróżnik — większość agencji nie ma własnego live AI demo.

- **Tech-stack argument:**
  > _"Nasz chatbot to nie szablon Voiceflow — to custom integracja Claude AI z naszym backend'em (n8n + Supabase). Możesz zobaczyć efekt na żywo."_

---

## 4. Law Chatbot (branża prawna) — wymieniony w CRM, NIE w portfolio strony

> **Status:** wpis w `knowledge_base` CRM (kategoria `agencja`, wpis "Portfolio i doświadczenie") wymienia _"Law Chatbot do automatycznej kwalifikacji klientów działający 24/7"_ jako jeden z realizowanych systemów AI. **Nie ma go w `avenly-web/app/data/projects.ts`** — czyli nie jest w portfolio na avenly.pl.

**Co o nim wiemy z CRM:**
- Branża: prawo / kancelarie prawne
- Funkcja: **automatyczna kwalifikacja klientów 24/7**
- Klasa: AI chatbot (najpewniej Voiceflow lub custom Claude)

**Czego nie wiemy (do uzupełnienia przez Michała/Bartka):**
- Klient (czy mamy nazwę do publikacji, czy NDA)
- Live URL / live demo
- Metryki (ilu leadów obsłużył, % zakwalifikowanych, oszczędność czasu prawnika)
- Tech stack (Voiceflow czy custom?)
- Rok realizacji
- Czy gotowe do publikacji w portfolio (chcemy żeby trafił do `/realizacje`?)

### Wzorzec do reuse (jeśli można mówić publicznie)

- **Cold mail do kancelarii prawnych:**
  > _"Robimy chatboty AI dla branży prawnej — np. **Law Chatbot** który kwalifikuje klientów 24/7 zanim trafią do prawnika. Oszczędza godziny tygodniowo na rozmowach z osobami które i tak nie pasują do specjalizacji. Mogę pokazać jak to mogłoby u Was wyglądać?"_

> **TODO:** zdecydować z Michałem czy Law Chatbot trafia do portfolio na avenly.pl (`projects.ts`). Jeśli tak — uzupełnić dane (klient, metryki, screenshoty) i dodać jako 4. wpis.

---

## Brakujące case studies (do dorobienia)

> **Status:** mamy tylko 3 case studies, z czego 2 z opisem. **Cel: dodawać 1 case study / kwartał** żeby `social-media-strategist` miał z czego sypać.

Sugerowane case studies do udokumentowania (jeśli istnieją projekty):
- Sklep WooCommerce (jeśli zrobiliśmy)
- Aplikacja webowa custom (jeśli zrobiliśmy)
- Chatbot dla klienta (jeśli zrobiliśmy poza Avenly own)
- Strona dedykowana Next.js (jeśli zrobiliśmy)
- Migrations: stara strona → nowa (z metrykami before/after)

## Format dla przyszłych case studies

Gdy dodajesz nowy projekt do portfolio:
1. Dodaj do `avenly-web/app/data/projects.ts` z pełnymi danymi (challenge, solution, stats, gallery)
2. Dodaj odpowiedni wpis tu w vault jako reuse-friendly summary
3. Jeśli klient pozwoli — pełne metryki (wzrost ruchu, konwersji, czasu ładowania)
4. Visual: mockup laptop + telefon + galeria (3-5 zdjęć z dashboardu / interfejsu)

## Co zbieramy do każdego case study (checklist)

- [ ] Zgoda klienta na publikację case study + jego nazwy
- [ ] Before metrics (jeśli mieliśmy access do starych analytics)
- [ ] After metrics (Google Analytics, PageSpeed, position w SERP, konwersja)
- [ ] 3-5 zdjęć: mockup laptop, mockup mobile, screen dashboardu klienta, foto klienta (opcjonalnie)
- [ ] Cytaty klienta (testimonial — można równolegle do Google Reviews)
- [ ] Tech stack uzyty
- [ ] Czas trwania projektu
- [ ] Komplikacje napotkane (storytelling — co było trudne, jak rozwiązaliśmy)
