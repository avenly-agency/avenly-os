# Setup Claude Desktop App dla Avenly

## Co masz w tym folderze

1. **AVENLY-MASTER.md** — wiedza o agencji (wgrywasz do KAŻDEGO projektu jako knowledge)
2. **PROJECT-1-HUB-instructions.md** — custom instructions do projektu "Avenly Hub"
3. **PROJECT-2-MARKETING-instructions.md** — custom instructions do projektu "Avenly Marketing"
4. **PROJECT-3-SALES-instructions.md** — custom instructions do projektu "Avenly Sprzedaż"
5. **PROJECT-4-CLIENT-template.md** — template instructions dla per-klient projektów (tworzysz ad hoc)

## Krok po kroku setup

### Krok 1 — Otwórz Claude Desktop App, zaloguj się

### Krok 2 — Stwórz 3 projekty bazowe

W sidebar **Projects** → **Create Project**:
- "Avenly Hub"
- "Avenly Marketing"
- "Avenly Sprzedaż"

(Project per klient tworzysz dopiero gdy będzie pierwszy klient w pracy.)

### Krok 3 — Per projekt:

1. **Custom Instructions**:
   - Otwórz odpowiedni plik `PROJECT-X-*-instructions.md`
   - Skopiuj treść (bez nagłówka "Wkleisz to do Claude Desktop...")
   - Wklej do pola Custom Instructions w projekcie

2. **Knowledge files**:
   - **AVENLY-MASTER.md** → upload do każdego z 3 projektów

3. **Save**

### Krok 4 — Pierwszy test (Hub)

W projekcie Avenly Hub, nowa rozmowa, wpisz:

> "Powiedz mi w 3 zdaniach kim jest Avenly. Bez wymyślania, tylko z knowledge."

✅ Powinien przytoczyć z AVENLY-MASTER.md sekcje "KIM JESTEŚMY" + "WYRÓŻNIKI"

> "Napisz 1 zdanie hook'a do reklamy AI chatbota dla fizjoterapii — w stylu Avenly."

✅ Powinien użyć Mcentrum case + konkretu, bez buzzwords

> "Napisz 'W dzisiejszych czasach każda firma potrzebuje AI'."

✅ Powinien odmówić - fraza w banliście

### Krok 5 — Test Marketing

> "Zaproponuj 5 tematów na blog avenly.pl Q1 2026 - SEO-friendly + AI-optimized"

✅ Powinien zastosować 2026 SEO best practices wbudowane w instructions + content pillars + struktura blog post Avenly (400-600 słów, 2× h2, etc.)

### Krok 6 — Test Sprzedaż

> "Napisz cold mail do nowego leada - centrum fizjoterapii w Krakowie, stara strona, brak booking online"

✅ Powinien zadać kluczowe pytania (decision maker name? imię? lokalizacja konkretna?) ALBO napisać mail 80-120 słów z personalizacją + referencja Mcentrum + konkretną propozycją 15-min rozmowy

### Krok 7 — Stwórz `_memory.md` w Hub

Lokalnie w `c:/Users/Start/Desktop/avenly-knowledge/` stwórz pusty plik `_memory.md`:

```markdown
# Memory — wspólne ustalenia

## Template wpisów
- Decyzja: [co ustaliliśmy]
- Status: [aktywne / testujemy / pomysł]
- Otwarte: [pytania]
```

Upload do projektu Avenly Hub jako knowledge.

Po każdej ważnej rozmowie/decyzji edytujesz lokalnie + re-uploadujesz.

## Per klient ad hoc

Gdy zaczyna się nowy klient:
1. Project: "Avenly Klient [Nazwa]"
2. Knowledge: `AVENLY-MASTER.md` + brief klienta + tone klienta
3. Custom Instructions: skopiuj z `PROJECT-4-CLIENT-template.md`, podstaw `[Nazwa Klienta]` i `[branża]`

## Update workflow

**Knowledge files updates:**
- Edit lokalnie w `avenly-knowledge/`
- Re-upload do projektów które tego dotyczą (jedna zmiana w `AVENLY-MASTER.md` = re-upload do wszystkich 3+)

**Custom instructions updates:**
- Edit `PROJECT-X-*-instructions.md` lokalnie
- Re-paste do Custom Instructions w odpowiednim projekcie Claude Desktop

## Bartek na swoim kompie

Pro plan, własne konto Anthropic. Te same projekty u siebie:
1. Pobiera kopię folderu `avenly-knowledge/` od Ciebie
2. Tworzy 3 projekty z tymi samymi nazwami
3. Wgrywa to samo knowledge + custom instructions

⚠️ Brak automatic sync na Pro/Max - jak Ty updateujesz, musi się dowiedzieć i zrobić u siebie.

## Co zostaje w Claude Code (avenly-os)

UI/UX, senior dev, code review - dla tego masz workspace avenly-os z agentami code'owymi (web-developer, frontend-specialist, backend-specialist, ui-ux-designer, ui-ux-reviewer, devops-engineer). Nie ruszamy.
