# Avenly OS — Master Context

Wieloagentowy workspace dla agencji Avenly. Synchronizowany przez git między Michałem i Bartkiem.

## Struktura repo

- `obsidian-vault/` — **wiedza** (single source of truth). Edytuj w Obsidianie.
  - `00-System/` — meta: jak działa ten workspace, routing agentów
  - `10-Avenly/` — kim jesteśmy: brand voice, content pillars, target audience, ceny, ton, playbook obiekcji
  - `20-Clients/{slug}/` — per klient: brief, tone, deliverables, history
  - `30-Templates/` — szablony deliverables (blog, mail, social, oferta)
  - `40-Projects/` — aktywne sprinty/kampanie
  - `50-Reference/` — swipe files, techniki, dane rynkowe
  - `99-Archive/` — stare projekty, read-only
- `.claude/agents/` — definicje subagentów (per-agent system prompt + tools + model)
- `.claude/commands/` — slash commandy (wielokrokowe workflowy) — TBD w fazie 2
- `.claude/memory/` — persistent state Claude'a między sesjami (NIE commitować)

## Najważniejsze zasady

1. **Wiedza w vault, outputy w `.claude/memory/` lub w `40-Projects/`.** Vault to autentyczna wiedza, nie śmietnik AI.
2. **Język:** polski we wszystkim co user-facing (treści, plany, raporty, taski). Komentarze techniczne mogą być po angielsku.
3. **Plan → akceptacja → wykonanie.** Agenty NIGDY nie zapisują do CRM (avenly-crm `/api/agent/tasks`) bez explicit zatwierdzenia użytkownika ("akceptuję", "tak", "wrzuć").
4. **Master deleguje, nie wykonuje sam.** `avenly-master` rozumie zlecenie i kieruje do specjalistycznego subagenta. Sam nie pisze copy, nie planuje kampanii w detalu — od tego są specjaliści.
5. **Czyń mniej, nie więcej.** Jeśli user prosi o jeden post, daj jeden post. Nie sypaj 9 "alternatywami do wyboru".
6. **Nie zaśmiecaj CRM.** Dotykamy tylko `tasks` i `meetings` (write), reszta read-only. Leady, klienci, płatności → ręcznie w avenly-crm.

## Avenly w skrócie (startowy kontekst)

Polska agencja interaktywna, założona w 2026. Usługi: strony WWW, sklepy e-commerce, automatyzacje AI, chatboty, marketing.
Założyciele: Michał, Bartek. Klienci: SMB w Polsce, głównie branże usługowe (fizjoterapia, dentystyka, prawo, salony itd.).
Domena: avenly.pl · Mail: kontakt@avenly.pl

Pełną wiedzę agenty czytają z `obsidian-vault/10-Avenly/`. Tam edytujesz fakty, nie tutaj.

## Sąsiadujące repo

- `C:\Users\Start\Desktop\avenly-web\` — statyczna strona avenly.pl (Next.js export)
- `C:\Users\Start\Desktop\avenly-crm\` — CRM agencji (Next.js + Supabase + Anthropic API)

Agenty mogą czytać te repo gdy potrzebują kontekstu (np. copywriter sprawdza istniejące posty w `avenly-web/app/data/posts.ts` jako referencję stylu), ale **nie modyfikują ich** bez explicit polecenia.
