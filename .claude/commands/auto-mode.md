---
description: Wyłącza pin trybu (quick-mode lub team-mode) i wraca do domyślnego triage'u — master sam decyduje per message czy single shot, delegacja, czy fan-out.
---

AUTO MODE: **ON (default)**.

Anuluj wszelkie piny trybu (`/quick-mode`, `/team-mode`). Od teraz **każde zlecenie przechodzi przez triage protocol**.

## Confirmation

Odpowiedz user'owi:

> `Auto mode ON. Triage decyduje per message: quick/single/fan-out/pipeline.`

## Triage workflow

Dla każdej kolejnej wiadomości, **pierwsze co robisz**:

```
📊 KLASYFIKACJA:
- Domeny: [N]
- Złożoność: [trivial/średnia/wysoka]
- Multi-step: [tak/nie]
- Decyzja: [BEZPOŚREDNIO / DELEGACJA SINGLE / DELEGACJA FAN-OUT / DELEGACJA PIPELINE / SKILL DIRECT]

🎯 EXECUTION: [konkretny plan]
Koszt: [~N min Opus]

→ Lecę (lub `quick`/`team` żeby override).
```

Patrz `avenly-master.md` sekcja "TRIAGE PROTOCOL" dla pełnej logiki.