---
description: Wymusza pełną delegację do subagentów (fan-out parallel) dla tego ONE message. Master nie próbuje odpowiedzieć sam, deleguje do wszystkich relevantnych specjalistów. Reset do auto przy następnym message.
---

TEAM MODE: **ON dla tego message**.

Wykonaj **pełną orchestrację** — niezależnie od pozornej prostoty zlecenia, deleguj do **wszystkich relevantnych** subagentów (minimum 2, optymalnie 3-5 równolegle).

## Format odpowiedzi

Zacznij od:

> `[Team mode] Pełna delegacja. Wywołuję: agent-A, agent-B, agent-C.`

Potem fan-out parallel — wszystkich subagentów w jednym message (Agent tool calls).

Po agregacji:

> `Agregacja od X agentów: ...`

Plus highlight gdzie agenci się zgadzali (consensus) i gdzie były tensions (trade-offs do decyzji).

## Kiedy team to good choice

- Strategiczne decyzje (multi-domain)
- Złożone deliverables (kampania, content batch)
- Audyty (UI/UX, SEO, code, biznes)
- Nowy klient — full intake (sales + legal + pricing + business)
- Eksperymentalne — chcesz multiple perspectives

## Kiedy team to overkill

Jeśli zlecenie jest **ewidentnie 1-domenowe i trivial** ("napisz mi caption") — zaznacz user'owi:

> _"To 1 caption, team mode wywoła 3+ Opus agentów = overkill (cost vs value). Jeśli chcesz że i tak deleguję, lecę. Jeśli OK z quick — /quick zamiast."_

Daj 2 sekundy na override. Brak odpowiedzi → deleguj zgodnie z team mode.

## Reset

Po tym message → tryb wraca do **auto**.