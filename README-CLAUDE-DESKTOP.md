# Setup Claude Desktop App dla Avenly

## Co masz w tym folderze

1. **AVENLY-MASTER.md** — wiedza o agencji (wgrywasz do KAŻDEGO projektu jako knowledge)
2. **PROJECT-1-HUB-instructions.md** — Custom Instructions dla "Avenly Hub" (biznes/finanse/podatki/prawo/decyzje strategiczne)
3. **PROJECT-2-COPY-instructions.md** — Custom Instructions dla "Avenly Copy" (KONKRETNE pisanie - posty/headline/landing/blog/oferty/captions)
4. **PROJECT-3-MARKETING-instructions.md** — Custom Instructions dla "Avenly Marketing" (STRATEGIA - plany social, kampanie, content roadmap, SEO, paid ads, analytics)
5. **PROJECT-4-SALES-instructions.md** — Custom Instructions dla "Avenly Sprzedaż" (cold mail, follow-upy, obiekcje, closing, pricing)
6. **PROJECT-5-CLIENT-template.md** — Template dla per-klient projektów (tworzysz ad hoc gdy startujesz klienta)

## Podział COPY vs MARKETING — uważaj

- **Copy** = pisanie konkretnego tekstu (1 post, 5 hooków, 1 blog post, landing copy, ad copy text)
- **Marketing** = strategia, planowanie, briefy, raporty, kalendarze (NIE pisze tekstu)

Workflow typowy:
1. Idziesz do **Marketing** - planujesz kampanię / kalendarz social
2. Marketing daje Ci brief'y
3. Idziesz do **Copy** z brief'em - pisze konkretne teksty
4. Wracasz do **Marketing** z gotowymi tekstami - analytics / dystrybucja / report

## Krok po kroku setup

### Krok 1 — Otwórz Claude Desktop App, zaloguj się

### Krok 2 — Stwórz 4 projekty bazowe

W sidebar **Projects** → **Create Project**:
- "Avenly Hub"
- "Avenly Copy"
- "Avenly Marketing"
- "Avenly Sprzedaż"

(Project per klient tworzysz dopiero gdy będzie pierwszy klient w pracy.)

### Krok 3 — Per projekt:

1. **Custom Instructions**:
   - Otwórz odpowiedni plik `PROJECT-X-*-instructions.md`
   - Skopiuj treść (bez nagłówka "Wkleisz to do Claude Desktop...")
   - Wklej do pola Custom Instructions w projekcie

2. **Knowledge files**:
   - **AVENLY-MASTER.md** → upload do każdego z 4 projektów

3. **Save**

### Krok 4 — Test Hub

W projekcie Avenly Hub, nowa rozmowa:

> "Powiedz mi w 3 zdaniach kim jest Avenly. Bez wymyślania, tylko z knowledge."

✅ Powinien przytoczyć z AVENLY-MASTER.md sekcje "KIM JESTEŚMY" + "WYRÓŻNIKI"

### Krok 5 — Test Copy

> "Napisz hook do landing one-page dla fizjoterapeuty w Krakowie."

✅ Powinien zadać 1-2 pytania PRZED pisaniem (target persona klienta klienta? primary cel? długość?) ALBO napisać jeden konkretny hook z konkretem (np. liczby z Mcentrum case)

> "Napisz post IG dla Avenly o speed strony."

✅ Hook 0-3s + caption 80-150 słów + max 2-3 emoji + 8-15 hashtagów + brand voice + Avenly tone bez buzzwords

### Krok 6 — Test Marketing

> "Zaplanuj kalendarz social media dla Avenly na czerwiec 2026 - mix pillarów standardowy."

✅ Powinien zwrócić plan miesięczny (4-7 Reels + 2-3 carousele tygodniowo + Stories) z pillars mix (50/25/15/10) + konkretne tematy per post + repurposing plan

### Krok 7 — Test Sprzedaż

> "Napisz cold mail do centrum fizjoterapii w Krakowie."

✅ Powinien zadać pytania (decision maker imię, lokalizacja precyzyjna, stage funnel) ALBO napisać 80-120 słów z personalizacją + Mcentrum case + konkretny CTA 15-min rozmowy

### Krok 8 — Stwórz `_memory.md`

Lokalnie w `c:/Users/Start/Desktop/avenly-knowledge/` stwórz plik `_memory.md`:

```markdown
# Memory — wspólne ustalenia

## Template wpisów
- Decyzja: [co ustaliliśmy]
- Status: [aktywne / testujemy / pomysł]
- Otwarte: [pytania]
```

Upload do projektu Avenly Hub jako knowledge.

Po każdej ważnej rozmowie edytujesz lokalnie + re-uploadujesz.

## Per klient ad hoc

Gdy zaczyna się nowy klient:
1. Project: "Avenly Klient [Nazwa]"
2. Knowledge: `AVENLY-MASTER.md` + brief klienta + tone klienta + (opcjonalnie) history
3. Custom Instructions: skopiuj z `PROJECT-5-CLIENT-template.md`, podstaw `[Nazwa Klienta]` i `[branża]`

## Update workflow

**Knowledge files updates:**
- Edit lokalnie w `avenly-knowledge/`
- Re-upload do projektów które tego dotyczą (jedna zmiana w `AVENLY-MASTER.md` = re-upload do wszystkich 4+)

**Custom instructions updates:**
- Edit `PROJECT-X-*-instructions.md` lokalnie
- Re-paste do Custom Instructions w odpowiednim projekcie Claude Desktop

## Bartek na swoim kompie

Pro plan, własne konto Anthropic. Te same projekty u siebie:
1. Pobiera kopię folderu `avenly-knowledge/` od Ciebie
2. Tworzy 4 projekty z tymi samymi nazwami
3. Wgrywa to samo knowledge + custom instructions

⚠️ Brak automatic sync na Pro/Max - jak Ty updateujesz, musi się dowiedzieć i zrobić u siebie.

## Co zostaje w Claude Code (avenly-os)

UI/UX, senior dev, code review - dla tego masz workspace avenly-os z agentami code'owymi (web-developer, frontend-specialist, backend-specialist, ui-ux-designer, ui-ux-reviewer, devops-engineer). Nie ruszamy.

## Quick reference - gdzie idziesz po co

| Pytanie | Projekt |
|---|---|
| "Co o tym sądzicie?" / strategiczna decyzja | **Hub** |
| Podatki / prawo / finanse / HR | **Hub** |
| "Napisz 1 post IG" | **Copy** |
| "Napisz blog post" | **Copy** |
| "5 wariantów hook'a" | **Copy** |
| "Napisz landing copy" | **Copy** |
| "Napisz ofertę" | **Copy** |
| "Zaplanuj social media na miesiąc" | **Marketing** |
| "Strategia paid ads" | **Marketing** |
| "SEO audyt + content brief" | **Marketing** |
| "Miesięczny raport" | **Marketing** |
| "Cold mail do leada" | **Sprzedaż** |
| "Follow-up sequence" | **Sprzedaż** |
| "Klient mówi że za drogo" | **Sprzedaż** |
| "Ile policzyć za projekt" | **Sprzedaż** |
| Per konkretny klient | **Klient [nazwa]** |
| Programowanie / UI / DevOps | Claude Code (avenly-os) |
