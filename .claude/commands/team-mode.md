---
description: PIN team mode dla całej sesji. Wszystkie kolejne wiadomości będą traktowane jak `/team` aż user wpisze `/auto-mode` lub zacznie nową sesję.
---

TEAM MODE: **PINNED dla całej sesji**.

Od teraz **każda kolejna wiadomość** od usera w tej sesji jest traktowana jak `/team`:
- Pełna delegacja do subagentów
- Fan-out parallel gdy >1 domena
- Pipeline gdy potrzeba feedback loop
- Skills + agents razem dla maksymalnej jakości

## Confirmation

Odpowiedz user'owi:

> `Team mode PINNED. Wszystkie kolejne wiadomości — pełna orchestracja. Wyłącz przez /auto-mode lub /quick-mode.`

## Cost warning

Wpisz w confirmation:

> `⚠️ Burn rate: 3-6× wyższy niż quick. Twój Max 5x ma ~45-60h Opus/tydzień. Team mode session ~6h = wyczerpiesz tygodniowy quota w 1 sesji intensywnej. Świadomie?`

User akceptuje → kontynuuj.

## Kiedy chcesz pinować team

- Sesja strategiczna (kwartalne planowanie, decision-making)
- Onboarding nowego klienta (multiple domain perspectives)
- Audit dnia (UI/UX + SEO + code + biznes w sequence)
- Eksperymentowanie z multi-agent dla porównania

## Reset

- `/auto-mode` → triage decyduje
- `/quick-mode` → pin quick
- `/quick` per-message chwilowo override team-mode (tylko ten one), potem znów team
- `/team` per-message NIE zmienia pina (jest spójny)