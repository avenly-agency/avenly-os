# Template: Social Post

Patterns per platform dla postów social media Avenly i klientów.

## Instagram

### Caption

- **Długość:** 80-150 słów (max 220 dla deep dive carousel)
- **Hook (pierwsza linijka):** musi działać sam, bez kontekstu. To często jedyne co user widzi w feedzie zanim klikne "więcej".
- **Struktura:**
  ```
  [HOOK — 15-25 słów, działający sam]
  ━━━
  [Body — 2-4 akapity, każdy 1-3 linijek]
  ━━━
  [CTA miękkie: pytanie, "save for later", "tag someone who…"]

  [Hashtagi — 8-15, w sygnaturze]
  ```
- **CTA:** miękkie. NIE "kup teraz", NIE "kliknij link w bio" jako jedyne.
  - "Czy robicie podobnie?"
  - "Daj znać w komentarzu które byś wybrał"
  - "Zapisz, przyda się"
  - "Otaguj kogoś kto akurat planuje stronę"

### Carousel (slajdy 5-10)

- **Slajd 1 (cover):** big hook, 5-10 słów, brand color tło
- **Slajdy 2-N:** jeden punkt per slajd
- **Slajd ostatni:** CTA + recap
- **Caption:** krótszy (60-100 słów), prowadzi do otwarcia carousela

### Reels (15-30s)

- **Hook w 0-3s:** widzialne na thumbnail
- **Skrypt:** zawsze pisany przed nagraniem (template w `30-Templates/reel-script.md` — TBD)
- **Caption:** krótkie 30-50 słów + CTA

### Hashtagi (sygnatura)

Patrz `10-Avenly/content-pillars.md` sekcja "Hashtagi".

### Wizualnie

- **Brand color:** niebieski `#2f5beb`
- **Tło:** ciemne (#050505–#0a0a0a), biel tekstu, niebieski akcent
- **Font:** Inter (zgodne z brand)
- **Mockupy/screeny:** centrowane, drop shadow, padding 60-80px od krawędzi

## Facebook

- **Długość:** dłuższy storytelling OK (do 300 słów)
- **Hook:** też ważny, ale FB tolernuje "wstęp" bardziej niż IG
- **Bez hashtagów** (FB nie indeksuje sensownie)
- **CTA:** pytanie wymuszające engagement (FB nagradza komentarze > like'i)
- **Link do strony:** OK w treści (FB lepiej niż IG)

## LinkedIn

- **Długość:** 1000-1500 znaków
- **Line breaks często** (LinkedIn premiuje "scannable" content)
- **Hook:** pierwsza linia, druga jest cut-offem w feedzie
- **Ton:** trochę bardziej formalny, ale wciąż bez korpo-mowy
- **CTA:** zazwyczaj do bloga albo case study
- **Hashtagi:** 3-5 strategicznych na końcu (NIE 15 jak na IG)
- **Emoji:** max 2-3, raczej tylko w bullet pointach

## Co działa we wszystkich

- **Konkretne liczby** ("3 z 10 odwiedzin dzwoni" zamiast "wiele odwiedzin konwertuje")
- **Personal stories** (Michał lub Bartek w pierwszej osobie) > generyczny "my w Avenly"
- **Before/after** w case studies
- **Pytanie zaczepne** w hooku — ale nie generyczne ("Czy wiedziałeś że…")
- **Specific > general** zawsze

## Co NIE działa

- "Inspirujące cytaty" oderwane od contentu
- Memy polityczne / drama
- Czyste promo bez wartości
- Naciągane statystyki ("AI zmieni 87.3% biznesów do 2027")
- Hashtag spam
- Recycle posta sprzed 3 miesięcy 1:1

## Output `copywriter`

Per post zwraca:
1. **Hook** (pierwsza linijka)
2. **Full caption** (gotowy do wklejenia)
3. **Sugerowany visual** (1 zdanie opisu — co na grafice / first frame reela)
4. **Hashtagi** (kopiowalne osobno, żeby łatwo było zarządzać)
