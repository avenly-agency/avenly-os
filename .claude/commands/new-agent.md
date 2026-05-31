---
description: Stwórz nowego subagenta według wzorca z 30-Templates/agent-template.md. Argument: nazwa agenta + krótki opis domeny.
---

Stwórz nowego subagenta dla Avenly OS.

## Użycie

```
/new-agent video-editor "Edycja video, motion graphics, color grading"
```

Albo bez argumentów — wtedy pytasz user'a o:
- Nazwę (kebab-case)
- Krótki opis domeny (1-2 zdania)
- Model (Opus / Sonnet / Haiku)
- Tools (minimum Read+Glob+Grep; dodatkowe per agent)

## Kroki

### 1. Walidacja nazwy

- kebab-case (lowercase, myślniki, no polskie znaki)
- Unikatowa — sprawdź czy `.claude/agents/{nazwa}.md` nie istnieje
- Bez sufiksu `-agent` (redundancja)

### 2. Czytaj template

`obsidian-vault/30-Templates/agent-template.md` — pełen wzorzec.

### 3. Zapytaj user'a o kluczowe decyzje (jeśli nie podane)

```
NAZWA: [proponowana]
DOMENA: [opis 1-2 zdania]

DECYZJE:
- Model: [Opus / Sonnet / Haiku]
- Tools dodatkowe (poza Read/Glob/Grep): [Bash / WebSearch / WebFetch / Edit / Write]
- Reading list (jakie pliki z vault):
  - Standard: brand-voice, agencja/*
  - Domain-specific: [...]
- Kiedy go wołać (description trigger keywords): [...]
- Kiedy go NIE wołać (delegacja gdzie indziej): [...]
- Output format: [...]

Lecę?
```

### 4. Wygeneruj plik

Wypełnij template z user-provided decisions. Wszystkie sekcje:
- YAML frontmatter (name, description, tools, model)
- Domena ekspertyzy
- Reading list
- Strategia myślenia (jeśli Opus — full block; jeśli Sonnet/Haiku — pomiń)
- Output format
- Zasady absolutne
- Kontekst dot. Avenly (skrót — copy-paste)

### 5. Update related files

- **`avenly-master.md`** — dodaj wpis w sekcji "Pełny katalog subagentów"
- **`obsidian-vault/00-System/agent-routing.md`** — dodaj wpis w tabeli routingu
- (Opcjonalnie) **`obsidian-vault/00-System/agent-catalog.md`** — jeśli istnieje

### 6. Pokaż userowi summary

```
✅ Agent {nazwa} utworzony.

Plik: .claude/agents/{nazwa}.md
Model: {model}
Tools: {tools}

Updates:
- avenly-master.md (lista subagentów + routing rules)
- agent-routing.md (mapa)

Następny krok:
1. Sprawdź czy avenly-master mainstream go wywołuje na proper trigger
2. Test: napisz w panelu "[test trigger]" — czy master wywoła nowego agenta
3. Commit + push gdy zaakceptujesz
```

### 7. NIE commituj automatycznie

Zostaw commit dla user'a — niech sprawdzi że agent działa zanim wrzucimy do git'a.

## Reguły

- **Pole `description`** w YAML frontmatter musi mieć **trigger keywords + anti-triggers** żeby master agent wiedział kiedy go wybrać
- **Reading list** musi być konkretna — generic "czytaj vault" = waste
- **Output format** explicit — bez tego agent output będzie chaotyczny
- **Zasady absolutne** krótkie, konkretne, łatwo testowalne
- **Język polski** declared w system prompt