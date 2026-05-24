# Template: Cold Email

Pattern dla maili sprzedażowych — **propozycja współpracy** (nie neutralny cold mail). Używany w avenly-crm `mail_tresc` na leadach.

## Zasady absolutne

- **NIE neutralny cold mail.** To jest propozycja współpracy z konkretem czym możemy pomóc.
- **Personalizacja** w pierwszych 2 linijkach — coś specyficznego o firmie odbiorcy (nazwa, lokalizacja, branża, coś z ich strony)
- **Długość:** 80-120 słów body (max 150)
- **Bez** "miło Cię poznać", "mam nadzieję że Ci się dzień dobrze układa"
- **Bez** "moja agencja świadczy szereg usług"
- **Bez** linków w pierwszym mailu (zwiększa spam score)
- **Mail z avenly.pl** (kontakt@avenly.pl), nie z gmail

## Struktura

```
Temat: [konkretny, 30-50 znaków, NIE clickbait]

Cześć [Imię],

[Linijka 1: coś konkretnego o firmie. Pokazujesz że nie robisz spamu.]
   Przykłady:
   - "Zauważyłem że Mcentrum Fizjoterapia ma w Warszawie świetne opinie ale strona jest jeszcze sprzed kilku lat..."
   - "Patrząc na Wasze Insta — robicie super content z treningu funkcjonalnego..."

[Linijka 2-3: konkretny problem który widzisz + jak Avenly to rozwiązuje. Liczby/przykłady z branży.]
   Przykład:
   - "Robimy dla podobnych klinik nowoczesne strony które konwertują 3-4x lepiej niż średnia branżowa..."

[Linijka 4: konkretna propozycja first step.]
   - "Chciałbyś omówić w 15 min jak to mogłoby u Was wyglądać?"

Pozdrawiam,
Michał Grzejdak
Avenly · avenly.pl
```

## Co dziłą / nie działa w temacie

**Działa:**
- `[Nazwa firmy] — strona + 2 sugestie`
- `Propozycja dla [Nazwa]`
- `[Imię], krótko o [Nazwa firmy]`
- `Strona [Nazwa firmy] + krótki pomysł`

**NIE działa (spam-flag):**
- `Najlepsza oferta dla Ciebie!`
- `🚀 Zwiększ swoje wyniki o 300%`
- `Pilne — przeczytaj`
- `Re: nasza rozmowa` (jeśli nie było rozmowy — kłamstwo)

## Po napisaniu

`copywriter` zwraca:
1. Temat + body w formacie do wklejenia w avenly-crm jako `mail_tresc`
2. (opcjonalnie) follow-up plan: kiedy ponowić i z jaką nową informacją
3. Notatka: zalecane wstawienie pixela trackującego (avenly-crm robi to auto)

**Po Twojej akceptacji `avenly-master` może zapisać mail do CRM** przez `update lead.mail_tresc` — ale tylko gdy explicit potwierdzisz.

## Follow-up (jeśli nie odpowiedział)

Wyklucza tych z banlisty (`ton-komunikacji.md`). Krótszy niż original (50-70 słów). Konkretny dodatkowy insight z branży lub case study.

Pattern w avenly-crm: szablon w `knowledge_base` `category='followup'`, zmienne `{{nazwa}}`, `{{miasto}}`, `{{nisza}}`. Pierwsza linia `Temat: ...` → subject.

## Zła praktyka — czego NIE robimy

- Spam-wysyłki bez personalizacji (jeden mail do 100 firm z `{{nazwa}}` placeholder'em)
- Linki w pierwszym kontakcie
- Załączniki w pierwszym mailu
- "Ostatnia szansa" / fake urgency
- Lying about prior interaction ("Jak ustaliliśmy w rozmowie...")
