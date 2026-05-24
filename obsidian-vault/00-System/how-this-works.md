# Jak działa Avenly OS

System wieloagentowy dla agencji Avenly. Wszystko żyje w tym folderze (vault) + w `.claude/` obok. Synchronizowane przez git między Michałem i Bartkiem.

## Dwie warstwy

1. **Wiedza** (ten vault) — wszystko o Avenly, klientach, szablonach. Edytujesz w **Obsidianie**.
2. **Agenty** (`.claude/agents/`) — pliki markdown opisujące "kim jest" dany agent i jak działa. Edytujesz w **VS Code**.

## Jak agent działa (w praktyce)

1. User pisze do Claude Code w naturalnym języku, np. _"zaplanuj posty na czerwiec"_
2. **`avenly-master`** (Opus) rozumie zlecenie, czyta vault, deleguje do specjalisty
3. Specjalista (np. `social-media-strategist` na Sonnecie) czyta odpowiednie pliki z vault i wykonuje zadanie
4. Master agreguje wyniki, zwraca userowi
5. User akceptuje → agent zapisuje plan do vault i (opcjonalnie) tworzy taski w CRM

## Sync między Michałem a Bartkiem

- **Vault:** Obsidian Git plugin auto-pull/push co 5 min
- **Agenty + CLAUDE.md:** ręczny `git pull` / `git push` (raz dziennie wystarczy)
- **CRM (Supabase):** real-time przez sam Supabase, osobno

## Co edytujesz, czego nie

### ✅ Edytuj swobodnie

- `10-Avenly/*` — gdy zmienia się wiedza o nas (nowa usługa, nowy ton, zmiana cen)
- `20-Clients/{slug}/*` — gdy zmienia się info o kliencie
- `30-Templates/*` — gdy chcesz lepszy szablon
- `40-Projects/*` — bieżąca robota, plany, drafty

### 🔒 Edytuj ostrożnie

- `.claude/agents/*.md` — system prompty agentów. Każda zmiana = zmiana zachowania we WSZYSTKICH sesjach (u Ciebie i u Bartka po `git pull`). Testuj na małym zleceniu przed całym projektem.
- `CLAUDE.md` — globalne zasady. Zmiana wpływa na każdą sesję.

### 🚫 NIE edytuj ręcznie

- `.claude/memory/*` — tym zarządza Claude między sesjami
- Plików w `99-Archive/` — to historia, read-only (jeśli musisz coś zmienić — wyciągnij z archive, edytuj, wrzuć na nowe miejsce)

## Co kiedy się rozjedzie

- **Git conflict:** `git pull --no-rebase` → VS Code podświetli konflikt → wybierasz wersję → commit + push
- **Obsidian Git nie pushuje:** ikona Source Control → Commit-and-sync ręcznie
- **Agent zachowuje się dziwnie:** sprawdź czy nie ma zepsutego pliku w `.claude/agents/` (`git log` na nim)
- **Cofnięcie:** `git revert <hash>` cofa konkretny commit
