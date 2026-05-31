---
description: Po akceptacji planu (social media, content, sprint, cokolwiek) — wrzuca każdy element jako task do CRM. Uniwersalny endpoint dla zadań, nie tylko social.
---

Orkiestruj wrzucanie planu do CRM jako zadania.

## Kiedy używać

Kiedy user zaakceptował plan (social media na miesiąc, content sprint, deliverables klienta, action items po rozmowie, follow-upy ręczne) i chce żeby trafił do CRM jako taski które będą widoczne w `/tasks` UI i podzielne między Michała i Bartka.

## Kroki

### 1. Zweryfikuj że plan jest zaakceptowany

User MUSI explicit powiedzieć "akceptuję" / "tak, wrzuć" / "OK". Jeśli plan tylko zaproponowałeś — **NIE wykonuj**, poczekaj.

### 2. Zmapuj plan na strukturę task

Dla każdego elementu planu wygeneruj task:

```json
{
  "title": "string (max 100 znaków)",
  "description": "string (pełny opis + draft jeśli istnieje)",
  "client_id": "uuid albo null (gdy wewnętrzne Avenly)",
  "assigned_to": ["Michał"] | ["Bartek"] | ["Michał", "Bartek"],
  "status": "todo",
  "category": "biznes" | "strona" | "ai" | "social" | "grafika" | "inne",
  "is_long_term": false,
  "date_from": "YYYY-MM-DD",
  "date_to": "YYYY-MM-DD",
  "source": "agent:nazwa-agenta"
}
```

**Reguły mapowania:**
- `social-media-strategist` plan → `category: social`
- `copywriter` blog/landing → `category: strona` (jeśli landing) lub `biznes` (jeśli blog)
- `sales-strategist` deliverable → `category: biznes`
- `developer` task → `category: strona`
- Reszta → `category: inne`

**Assigned_to:**
- Jeśli user explicit powiedział kto → użyj
- Domyślnie: nie ustawiaj (`null`) — user zdecyduje w UI
- Reguły: social media → Bartek/Michał wg rotacji; strategia → Michał; cold outreach → Michał; design → Bartek

### 3. POST do CRM

```bash
curl -X POST \
  -H "x-n8n-secret: avenly-n8n-2024" \
  -H "Content-Type: application/json" \
  -d '{
    "tasks": [ ...lista tasków... ]
  }' \
  https://avenlycrm.vercel.app/api/agent/tasks
```

Response: `{ created: 20, ids: [uuid...], tasks: [...] }`

### 4. Spotkania (jeśli plan zawiera spotkania)

Spotkania to OSOBNY endpoint `/api/agent/meetings`:

```json
{
  "meetings": [
    {
      "title": "Review meeting — Fizjo-Wawa",
      "description": "Omówienie postępów miesięcznej kampanii",
      "client_id": "uuid",
      "assigned_to": ["Michał"],
      "start_time": "2026-06-15T14:00:00Z",
      "end_time": "2026-06-15T14:30:00Z",
      "source": "agent:sales-strategist"
    }
  ]
}
```

### 5. Pokaż wynik

```
✅ PLAN W CRM

Utworzone:
- 20 tasków (kategorie: 15 social, 3 biznes, 2 inne)
- 2 spotkania (Pn 15.06 14:00 z Fizjo-Wawa, Pt 19.06 11:00 internal review)

Sprawdź:
- Taski: https://avenlycrm.vercel.app/tasks
- Kalendarz: https://avenlycrm.vercel.app/tasks (toggle "Kalendarz")
```

## Reguły absolutne

- **Wykonuj TYLKO po explicit akceptacji** ("tak", "akceptuję", "wrzuć", "OK")
- **Limit:** max 100 tasków + 50 meetings per request (endpoint to wymusza)
- **Date format:** YYYY-MM-DD dla tasków, ISO 8601 dla meetings (z TZ)
- **Polski zawsze** w title + description
- **NIGDY nie wymyślaj `client_id`** — tylko realne UUID z CRM (możesz pull przez `GET /api/agent/tasks?client_id=...` żeby sprawdzić istnienie)
- **Domyślny status: `todo`** — agent nigdy nie ustawia od razu `in_progress` ani `done`
- **Source ZAWSZE wypełnij** — żeby było wiadomo skąd przyszedł task (np. "agent:social-media-strategist")
