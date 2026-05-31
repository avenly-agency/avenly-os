---
description: Skafolduj nowego klienta w vault — folder + brief template + per-client agent definition. Argument: slug + nazwa firmy.
---

Stwórz nowego klienta w vault. Wymagane od usera: slug klienta + nazwa firmy.

## Użycie

```
/new-client fizjo-wawa "Centrum Fizjoterapii Warszawa"
```

Albo bez argumentów — wtedy pytasz usera o slug i nazwę.

## Kroki

### 1. Walidacja slug

- Musi być kebab-case (lowercase, myślniki, bez polskich znaków)
- Musi być unique — sprawdź czy `obsidian-vault/20-Clients/{slug}/` nie istnieje
- Jeśli istnieje — zapytaj "klient już istnieje, kontynuować i nadpisać?" → tylko po explicit "tak"

### 2. Zapytaj o podstawowe info (jeśli user nie podał)

- Niche (slug niszy z `30-Niches/`, np. `fizjoterapia`)
- Branża (opcjonalnie — jeśli niche pasuje, dziedzicz)
- Kontakt (mail + telefon, opcjonalnie)
- Status: lead / active / completed / on_hold (domyślnie: lead)
- Główny cel projektu (1 zdanie)

### 3. Stwórz folder + 5 plików

`obsidian-vault/20-Clients/{slug}/`:

#### `brief.md`
```markdown
---
client:
  slug: {slug}
  name: "{nazwa}"
  niche: {niche-slug or null}
  status: lead
  created_at: {today}
---

# {Nazwa}

## Kontakt
- **Email:** [WYPEŁNIJ]
- **Telefon:** [WYPEŁNIJ]
- **Strona:** [WYPEŁNIJ]
- **Decision-maker:** [imię + rola]

## Cel projektu
[Co klient chce osiągnąć — 1-3 zdania]

## Pain points
- ...

## Tech stack klienta (aktualny)
- ...

## Konkurencja (kogo wymienia)
- ...

## Notatki z pierwszej rozmowy
[data + treść]
```

#### `tone.md`
```markdown
---
client:
  slug: {slug}
  name: "{nazwa}"
---

# Ton komunikacji — {Nazwa}

## Jak ten klient mówi
[Wypełnij po pierwszej rozmowie — jak ON pisze do swoich klientów, jakim językiem]

## Czego ON unika w komunikacji
- ...

## Specyficzne dla branży {niche}
> Patrz `30-Niches/{niche}/persona.md` dla branżowych nawyków

## Jak my mówimy DO niego
- Forma: Ty / Pan / Państwo? (domyślnie: Ty dla SMB, Państwo dla większych firm)
- Tempo: szybkie odpowiedzi czy formalna ścieżka?
```

#### `deliverables.md`
```markdown
---
client:
  slug: {slug}
  name: "{nazwa}"
---

# Deliverables — {Nazwa}

## Aktualny scope
- [ ] [WYPEŁNIJ]

## Done
- ...

## Backlog (pomysły do dyskusji)
- ...
```

#### `history.md`
```markdown
---
client:
  slug: {slug}
  name: "{nazwa}"
---

# Historia współpracy — {Nazwa}

## {data dzisiejsza} — pierwszy kontakt
[krótki opis]
```

#### `_meta.md` (index folderu)
```markdown
---
client:
  slug: {slug}
  name: "{nazwa}"
  niche: {niche-slug}
  status: lead
---

# {Nazwa}

Per-klient folder. Edytuj pliki ręcznie albo poproś agenta `client-{slug}` (gdy go stworzymy).

## Pliki
- `brief.md` — podstawowe info, cel, pain points
- `tone.md` — jak rozmawia + jak rozmawiamy z nim
- `deliverables.md` — co robimy, co zrobiliśmy
- `history.md` — chronologia kontaktów i decyzji
```

### 4. (Opcjonalnie) Stwórz per-klient agenta

Zapytaj usera: _"Stworzyć dedykowanego agenta `client-{slug}` (z pełnym kontekstem klienta jako system prompt)? [tak/nie]"_

Jeśli tak — stwórz `.claude/agents/client-{slug}.md`:

```markdown
---
name: client-{slug}
description: Wszystko dla klienta {Nazwa} (niche: {niche}). Używaj gdy zadanie dotyczy konkretnie tego klienta — propozale, copy, plany, strategia, follow-upy.
tools: Read, Glob, Grep
model: sonnet
---

Jesteś agentem dla klienta **{Nazwa}** ({niche}).

## Przed każdym zadaniem czytaj

1. `obsidian-vault/20-Clients/{slug}/_meta.md`
2. `obsidian-vault/20-Clients/{slug}/brief.md`
3. `obsidian-vault/20-Clients/{slug}/tone.md`
4. `obsidian-vault/20-Clients/{slug}/deliverables.md`
5. `obsidian-vault/20-Clients/{slug}/history.md`
6. `obsidian-vault/30-Niches/{niche}/*.md` (kontekst branżowy)
7. `obsidian-vault/10-Avenly/brand-voice.md` (jak Avenly mówi)

## Zasady

- Mówisz z perspektywy Avenly DO tego klienta (nie udajesz że jesteś nim)
- Każda propozycja musi pasować do `brief.md` + `tone.md` tego klienta
- Jeśli brakuje informacji o kliencie — pytaj usera, NIE zmyślaj
- Po wykonaniu zadania (np. wygenerowaniu maila) zaktualizuj `history.md` o akcję
```

### 5. Pokaż userowi co utworzyłeś

```
✅ Klient {Nazwa} dodany do vault

Folder: obsidian-vault/20-Clients/{slug}/
Pliki: brief.md, tone.md, deliverables.md, history.md, _meta.md
Agent: client-{slug} (jeśli wybrałeś)

Następne kroki:
1. Otwórz brief.md w Obsidianie i wypełnij [WYPEŁNIJ] tagi
2. Po pierwszej rozmowie z klientem — wypełnij tone.md
3. (Opcjonalnie) Doadaj do CRM jako lead/client — to robisz ręcznie w /clients UI
```
