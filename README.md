# Avenly OS

Multi-agent workspace dla agencji Avenly. Synchronizowany przez git między Michałem i Bartkiem.

## Setup nowej maszyny (~30 min)

1. Zainstaluj:
   - **VS Code** (https://code.visualstudio.com)
   - **Claude Code** — VS Code extension (Marketplace → "Claude Code")
   - **Obsidian** (https://obsidian.md)
   - **Git for Windows** (https://git-scm.com/download/win)
2. Zaloguj się do Claude Code swoim kontem Anthropic.
3. Klonuj repo:
   ```powershell
   cd C:\Users\<You>\Desktop
   git clone https://github.com/<org>/avenly-os.git
   cd avenly-os
   ```
4. VS Code → File → Open Folder → wskaż `avenly-os/`.
5. Obsidian → "Open folder as vault" → wskaż `avenly-os/obsidian-vault/`.
6. W Obsidianie: Settings → Community plugins → "Turn on" → Browse → zainstaluj **Obsidian Git** → Enable → ustaw:
   - Auto pull on startup: ON
   - Vault backup interval: 5 min
   - Auto pull interval: 5 min

## Codzienna praca

- **Zanim zaczniesz:** w terminalu VS Code (Ctrl+`) → `git pull`
- **Praca:** otwórz panel Claude Code, pisz po polsku naturalnym językiem (np. _"zaplanuj posty na czerwiec"_, _"napisz cold mail do leada 4521"_).
- **Po edycji agenta lub pliku w `.claude/`:** `git add . && git commit -m "..." && git push`
- **Edycje notatek w vault** (`obsidian-vault/`): Obsidian Git robi to automatycznie co 5 min.

## 3 zasady synchronizacji

1. Zaczynam dzień → `git pull`.
2. Zmieniłem agenta lub plik w `.claude/` → `git push` od razu po commicie.
3. Wiem że drugi pracuje nad tym samym plikiem → najpierw zapytam (Slack/SMS).

## Struktura

| Folder | Zawartość | Edytujesz w |
|---|---|---|
| `obsidian-vault/10-Avenly/` | Brand voice, ton, ceny, pillars | Obsidian |
| `obsidian-vault/20-Clients/{slug}/` | Per klient | Obsidian |
| `obsidian-vault/30-Templates/` | Szablony deliverables | Obsidian |
| `obsidian-vault/40-Projects/` | Aktywne kampanie/sprinty | Obsidian |
| `.claude/agents/*.md` | Definicje agentów | VS Code |
| `.claude/commands/*.md` | Slash commandy (TBD faza 2) | VS Code |
| `CLAUDE.md` | Master kontekst Claude'a | VS Code |

## Status

- **Faza 0 (skeleton):** ✅ Ukończona. Workspace gotowy do pierwszego użycia.
- **Faza 1 (seed wiedzy + 3 agenty + CRM bridge):** w toku.
- Następne kroki: wypełnić templaty w `obsidian-vault/10-Avenly/`, przetestować `avenly-master`, dorzucić `POST /api/agent/tasks` w avenly-crm.

## Co kiedy się rozjedzie

**Konflikt w git pull:** `git pull --no-rebase` → VS Code podświetli konflikt → wybierasz wersję → `git add . && git commit -m "Resolve conflict" && git push`.

**Obsidian Git nie pushuje:** ikona Source Control w boczku Obsidiana → "Commit-and-sync".

**Bartek nie widzi agenta którego dodałeś:** Bartek robi `git pull` + restart panelu Claude Code (Cmd+Shift+P → "Claude Code: Reload").

**Cofnięcie zepsutej zmiany:** `git log --oneline` → `git revert <hash>` → `git push`.
