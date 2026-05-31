---
description: PIN quick mode dla całej sesji. Wszystkie kolejne wiadomości będą traktowane jak `/quick` aż user wpisze `/auto-mode` lub zacznie nową sesję.
---

QUICK MODE: **PINNED dla całej sesji**.

Od teraz **każda kolejna wiadomość** od usera w tej sesji jest traktowana jak `/quick`:
- Odpowiadasz bezpośrednio
- BEZ delegacji do subagentów
- Pojedyncze wywołanie Opus per message

## Confirmation

Odpowiedz user'owi:

> `Quick mode PINNED. Wszystkie kolejne wiadomości — single shot bez delegacji. Wyłącz przez /auto-mode lub /team-mode.`

## Pamięć trybu w sesji

Trzymaj pin w head przez całą sesję. Każda kolejna wiadomość — quick. Reset:
- `/auto-mode` → wracasz do triage'u
- `/team-mode` → pinujesz team
- `/quick` per-message NIE zmienia pina (jest spójny)
- `/team` per-message **chwilowo override** quick-mode (tylko ten ONE message), potem znów quick

## Kiedy chcesz pinować quick

- Sesja "pisania" — masa drobnych captionów, mailów, poprawek
- Tryb "konwersacyjny" z Claude bez heavy delegation
- Oszczędność puli Opus (1 wywołanie zamiast 3-6 per message)

## Edge case

Jeśli user przyjdzie ze złożonym multi-domain zleceniem **w trakcie quick-mode** — zaznacz raz:

> _"Quick mode jest PINNED. To zlecenie dotyka X+Y+Z domen i quick je spłaszczy. OK z tym, czy `/team` ten one albo `/auto-mode` żeby triage decydował?"_

Brak odpowiedzi w 1 message → idź jak quick zgodnie z pinem.