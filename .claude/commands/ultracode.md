---
description: Włącz tryb ULTRACODE dla całej sesji — maksymalna głębokość rozumowania w master + propagacja do każdego subagenta.
---

ULTRACODE MODE: **ON** dla pozostałej części tej sesji.

## Co to znaczy

Od teraz w tej sesji:

1. **Master agent (Ty)** — używasz extended thinking dla każdego zadania, niezależnie od pozornej prostoty. Rozważaj alternatywy, second-order effects, edge cases. Take unlimited reasoning time.

2. **Każdy delegowany subagent** — w prompcie do niego DODAJ instrukcję:

   > _"ULTRACODE: Use extended thinking. Take unlimited reasoning time. Consider all alternatives. Surface trade-offs explicitly. Think deeply before responding."_

3. **Output szczegółowy** — pokazuj swoje rozumowanie w odpowiedziach (nie ukrywaj logiki za "tak po prostu to widzę").

## Jak długo działa

Do końca tej sesji (lub do `/normal` jeśli zostanie kiedyś dorobiony).

## Kiedy NIE używać

- Trivial lookup ("ile mamy leadów") — to waste Opus
- Quick reformat / rewrite — nie potrzeba deep thinking
- Generic questions ("co to jest X") — Sonnet/Haiku wystarczy

Jeśli zlecenie jest trivialne — powiedz to user'owi i zaproponuj że robisz "normally" zamiast ultracode (oszczędzasz pulę).

## Dla pułapki — uważaj na

- **Limity Max 5x** (45-60h Opus/tydzień). Ultracode + 28 Opus-agentów = możesz wyczerpać limit w 3-5 dni.
- **Diminishing returns** — niektóre zadania nie wymagają deep thinking, nawet jeśli wyglądają złożone.

## Status after /ultracode

Potwierdź userowi: "Ultracode ON. Każdy następny task — extended thinking + propagacja do subagentów."