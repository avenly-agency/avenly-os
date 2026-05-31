---
description: Wymusza single-shot answer dla tego ONE message — żadnej delegacji do subagentów. Master odpowiada bezpośrednio. Reset do auto przy następnym message.
---

QUICK MODE: **ON dla tego message**.

Odpowiedz bezpośrednio jako master agent (Opus), bez delegacji. Wykonaj zadanie w jednym shot.

## Format odpowiedzi

Zacznij od krótkiej notki:

> `[Quick mode] Single-shot answer. Jeśli chcesz głębiej z multi-agent, użyj /team.`

Potem treść.

## Kiedy quick to good choice

- Proste pytania / klaryfikacje
- Drobny tweak istniejącego tekstu
- Lookup informacji
- Pojedyncza domena bez complexity
- Konwersacyjne flow (brainstorm)

## Kiedy quick może być za mało

Jeśli widzisz że zlecenie ma >2 domeny lub wymaga deep dive — **zaznacz** user'owi:

> _"To zlecenie dotyka X+Y+Z. Quick robi powierzchowną odpowiedź. Jeśli chcesz pełną — `/team` zamiast."_

I oddaj quick answer. User decyduje czy chce poszerzyć.

## Reset

Po tym message → tryb wraca do **auto** (domyślny triage). Następna wiadomość bez `/quick` znów uruchamia klasyfikację.