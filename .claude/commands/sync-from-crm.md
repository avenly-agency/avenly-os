---
description: Pull wiedzę z CRM knowledge_base + niches do vault. CRM jest primary source — vault to synced kopia.
---

Synchronizuj wiedzę **z CRM do vault** (pull, one-way).

## Kroki

### 1. Pobierz aktualny stan z CRM

```bash
curl -H "x-n8n-secret: avenly-n8n-2024" https://avenlycrm.vercel.app/api/agent/knowledge
```

Zwróci JSON: `{ entries: [{ id, slug, category, title, content, is_published, ai_chatbot, created_at }], count }`.

```bash
curl -H "x-n8n-secret: avenly-n8n-2024" https://avenlycrm.vercel.app/api/agent/niches
```

Zwróci JSON: `{ niches: [{ id, name, opis_branzy, persona, problemy_2026, hook_points, sales_arguments, objekcje, email_templates, ai_prompts, cold_mailing_tips, created_at }], count }`.

### 2. Porównaj z lokalnym stanem vault

Glob `obsidian-vault/10-Avenly/{agencja,uslugi,obiekcje,social_proof,ton,followup}/*.md` i `obsidian-vault/30-Niches/*/*.md`. Parsuj frontmatter `crm:` z każdego.

### 3. Pokaż userowi diff

Format:

```
📥 SYNC FROM CRM — PLAN

knowledge_base:
  ✅ 14 unchanged (slug match, content identical)
  📝 3 to update (content changed): misja-avenly, za-drogo, mcentrum-fizjoterapia
  ➕ 5 to create in vault (new in CRM): ton-banlist-slow, ton-formaty, ...
  ⚠️  1 orphan in vault (not in CRM): obiekcje/stary-wpis.md
     → keep in vault (manual delete if you want)

niches:
  ➕ 3 to create in vault: fizjoterapia, dentystyka, prawo
  📝 0 to update
  ✅ 0 unchanged

Akceptujesz?
[1] Tak, syncuj wszystko
[2] Tylko knowledge_base, skip niches
[3] Pokaż mi szczegóły wybranych wpisów
[4] Anuluj
```

### 4. Po akceptacji — wykonaj

Dla każdego `knowledge_base` entry:
- **create/update vault file:** `obsidian-vault/10-Avenly/{category}/{slug}.md`
- Frontmatter:
  ```yaml
  ---
  crm:
    table: knowledge_base
    category: {category}
    slug: {slug}
    title: "{title}"
    ai_chatbot: {ai_chatbot}
    is_published: {is_published}
  ---

  # {title}

  {content}
  ```

Dla każdego `niches` entry:
- **create folder:** `obsidian-vault/30-Niches/{slug-z-name}/`
- **create pliki** (po jednym per pole, jeśli pole nie jest puste):
  - `_meta.md` — frontmatter z całą niszą, content = name + opis_branzy
  - `persona.md` — niche.persona
  - `problemy.md` — niche.problemy_2026
  - `hooks.md` — niche.hook_points
  - `sales-arguments.md` — niche.sales_arguments
  - `obiekcje.md` — niche.objekcje (JSON → markdown lista pytań i odpowiedzi)
  - `email-templates.md` — niche.email_templates
  - `cold-mailing-tips.md` — niche.cold_mailing_tips (jeśli istnieje)

Frontmatter w `_meta.md`:
```yaml
---
crm:
  table: niches
  id: {id}
  name: "{name}"
  slug: {slug-from-name}
  sync_direction: pull-only
---
```

### 5. Po sync — podsumowanie

Pokaż userowi:
- Liczba zaktualizowanych/utworzonych plików
- Lista orphanów (do manualnej decyzji)
- Sugestia: `git add . && git commit -m "sync: pull from CRM ${data}"` (ale NIE wykonuj bez explicit polecenia)

## Reguły

- **NIE usuwaj** vault files które są orphan (nie ma w CRM) — chyba że user explicit poprosi. Ostrzeżenie wystarczy.
- **NIE pisz do CRM** w tym command — to jest pull-only.
- **Slug w niches**: jeśli `niches.name` to "Fizjoterapia", slug = "fizjoterapia" (lowercase, polskie znaki bez akcentów). Mapping: `name.toLowerCase().replace(/ą/g,'a').replace(/ć/g,'c').replace(/ę/g,'e').replace(/ł/g,'l').replace(/ń/g,'n').replace(/ó/g,'o').replace(/ś/g,'s').replace(/[źż]/g,'z').replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')`.
- **Format obiekcji JSON → markdown:** każda obiekcja jako `## {objekcja}\n\n{odpowiedz}\n\n---\n\n`.
- **Jeśli pole niszy puste/null** — pomiń tworzenie pliku (nie twórz pustych).
