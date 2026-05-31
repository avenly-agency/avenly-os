---
description: Push wiedzę z vault do CRM knowledge_base. Używaj gdy edytowałeś atomic files w 10-Avenly/ poza CRM (np. agent wygenerował coś nowego). NIE syncuje niches (te są pull-only).
---

Synchronizuj wiedzę **z vault do CRM** (push, one-way, z diff + akceptacją).

## Kroki

### 1. Czytaj atomic files w vault

Glob `obsidian-vault/10-Avenly/{agencja,uslugi,obiekcje,social_proof,ton,followup}/*.md`.

Dla każdego pliku:
- Parsuj frontmatter (yaml)
- Sprawdź czy ma `crm:` block — jeśli nie, **pomiń** (to plik narracyjny, nie sync)
- Extract: `crm.category`, `crm.slug`, `crm.title`, `crm.ai_chatbot`, `crm.is_published`
- Content = wszystko po `---` (drugi separator yaml)

### 2. Pobierz aktualny stan CRM

```bash
curl -H "x-n8n-secret: avenly-n8n-2024" https://avenlycrm.vercel.app/api/agent/knowledge
```

### 3. Porównaj i pokaż diff

```
📤 SYNC TO CRM — PLAN

Z vault → CRM knowledge_base:
  ✅ 18 unchanged (slug+content identical)
  📝 3 to update: misja-avenly (content), za-drogo (title), wartosc-dla-klienta (content)
  ➕ 2 to create in CRM (new in vault): ton-banlist-slow, ton-formaty

UWAGA: w CRM jest też 4 wpisy bez odpowiednika w vault:
  - some-old-entry-1 (category: agencja)
  - some-old-entry-2 (category: ton)
  Te NIE będą usunięte (delete_missing=false domyślnie).

Akceptujesz?
[1] Tak, upsert wszystko (delete_missing=false)
[2] Tak + USUŃ orphany z CRM (delete_missing=true) ⚠️
[3] Tylko nowe (skip update)
[4] Anuluj
```

### 4. Po akceptacji — POST do CRM

```bash
curl -X POST \
  -H "x-n8n-secret: avenly-n8n-2024" \
  -H "Content-Type: application/json" \
  -d '{
    "entries": [
      {"slug": "misja-avenly", "category": "agencja", "title": "Misja Avenly", "content": "...", "ai_chatbot": true, "is_published": true},
      ...
    ],
    "delete_missing": false
  }' \
  https://avenlycrm.vercel.app/api/agent/knowledge
```

Response: `{ ok: true, upserted, created, updated, unchanged, deleted, diff: [...] }`

### 5. Pokaż wynik

```
✅ SYNC TO CRM — WYKONANO

knowledge_base:
  ➕ Utworzone: 2 (ton-banlist-slow, ton-formaty)
  📝 Zaktualizowane: 3 (misja-avenly, za-drogo, wartosc-dla-klienta)
  ✅ Bez zmian: 18

Sprawdź w CRM: https://avenlycrm.vercel.app/wiedza
```

## Reguły

- **NIGDY nie syncuj** plików narracyjnych (brand-voice.md, content-pillars.md, target-audience.md, ton-komunikacji.md, README.md) — one nie mają frontmatter `crm:`.
- **NIGDY nie syncuj niches** w tym command (są pull-only — edycja tylko w CRM /niches UI).
- **Slug musi być w frontmatter** — jeśli plik nie ma `crm.slug`, ostrzeż i pomiń.
- **Domyślnie `delete_missing=false`** — bezpiecznik przeciw przypadkowemu czyszczeniu CRM. Tylko z explicit zgodą.
- **Wymaga akceptacji** zanim wyślesz POST. Pokaż diff, czekaj na "tak" / "akceptuję".
- Po sync zaproponuj `git add . && git commit -m "sync: push to CRM ${data}"` (ale NIE rób bez polecenia).
