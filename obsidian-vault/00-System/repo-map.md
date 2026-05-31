# Repo Map — gdzie żyją dane w ekosystemie Avenly

Mapa wszystkich źródeł danych które agenty mogą czytać. Ważne dla agentów żeby wiedziały **gdzie sprawdzić zanim odpiszą** na pytanie.

## 3 główne repo

### `avenly-os/` (ten workspace)
**Ścieżka:** `C:\Users\Start\Desktop\avenly-os\`
**Co:** wieloagentowy workspace + vault wiedzy
**Stack:** filesystem + git
**Kto pisze:** ludzie (Michał, Bartek) + agenty (do `40-Projects/`, `99-Output/`, `.claude/memory/`)
**Co zawiera:**
- `.claude/agents/` — definicje subagentów
- `.claude/commands/` — slash commandy (TBD)
- `obsidian-vault/` — single source of truth wiedzy
- `CLAUDE.md` — master kontekst

### `avenly-web/` (strona avenly.pl)
**Ścieżka:** `C:\Users\Start\Desktop\avenly-web\`
**Co:** statyczna strona agencji avenly.pl
**Stack:** Next.js 16, React 19, Tailwind v4, Framer Motion, GSAP, WebGL shaders
**Deploy:** Hostinger (Apache + `.htaccess`) za Cloudflare CDN
**Kto pisze:** ludzie (i agenty na zlecenie — `developer`, `copywriter`)

**Kluczowe pliki dla agentów:**
| Plik | Co tam jest | Kto może potrzebować |
|---|---|---|
| `PRODUCT.md` | Brand personality, anti-references, design principles | brand-voice, copywriter |
| `project_context.md` | Pełna mapa projektu, stan, sekcje home | wszystkie agenty |
| `docs/blog-style-guide.md` | Single source dla blog postów | copywriter (blog) |
| `docs/blog-ideas.md` | Backlog pomysłów blog | content-strategist |
| `app/data/posts.ts` | 3 istniejące posty (referencja stylu) | copywriter |
| `app/data/projects.ts` | 3 case studies (Mcentrum, Klub Sportowy, Wirtualny Asystent) | sales-strategist, social-media |
| `app/data/services.ts` | Pełna oferta z featurami i tech stackiem | wszystkie agenty |
| `app/o-nas/faq-data.ts` | FAQ (zasila też FAQPage schema) | wszystkie agenty |
| `lib/seo-data.ts` | Dane firmy (NIP, adres, social, Wizytówka Google) | wszystkie agenty |
| `lib/schemas.ts` | JSON-LD buildery (Organization, Service, FAQ itp.) | developer (gdy SEO) |
| `components/sections/Testimonials.tsx` | 2 opinie Google + AggregateRating | sales-strategist, social-media |
| `app/blog/[slug]/page.tsx` | Routing bloga | copywriter (gdy dodaje post) |
| `INSTRUKCJA-SEO.md` | SEO setup, co podmienić po rejestracji firmy | business-advisor |
| `app/sitemap.ts` | Hardcoded lista stron w sitemap | developer |
| `app/robots.ts` | Robots.txt (allow AI search, block AI training) | — |

### `avenly-crm/` (CRM agencji)
**Ścieżka:** `C:\Users\Start\Desktop\avenly-crm\`
**Co:** CRM wewnętrzny (Michał + Bartek) — leady, klienci, taski, kalendarz, chatbot, analytics
**Stack:** Next.js 16, React 19, Tailwind v4, shadcn/ui, Supabase (Auth + Postgres), Anthropic API direct fetch, Resend SMTP, web-push, n8n
**Deploy:** Vercel
**URL:** [WYPEŁNIJ — np. crm.avenly.pl] po wdrożeniu produkcyjnym
**Kto pisze:** ludzie + agenty (przez API `/api/agent/*` — gdy zrobimy, jeszcze nie istnieje)

**Kluczowe pliki dla agentów:**
| Plik | Co tam jest |
|---|---|
| `CLAUDE.md` | Stack, tabele Supabase, n8n integracje, statusy leadów |
| `PROJECT_CONTEXT.md` | Pełne TODO, zrealizowane funkcje |
| `app/(dashboard)/leady/[id]/page.tsx` | Lead detail (referencja struktury danych) |
| `app/api/analyze/route.ts` | Pipeline analizy leada (referencja prompt patterns) |

## Supabase (baza danych — wspólna dla CRM + chatbot avenly-web)

**URL:** `https://kyfsjvgixmcmafvaiyak.supabase.co`
**Anon key:** w `.env.local` obu projektów (NEXT_PUBLIC_SUPABASE_ANON_KEY)
**Service role:** w avenly-crm/.env.local (SUPABASE_SERVICE_ROLE_KEY) — NIE udostępniamy agentom

### Tabele kluczowe dla agentów Avenly OS

| Tabela | Zawartość | Dostęp dla agentów Avenly OS |
|---|---|---|
| `potential_leads` | Leady (status `nowy/w_analizie/mail_gotowy/wyslany/odpowiedz/odrzucony`) | **NIE dotykamy.** Lead management = ręcznie w CRM `/leady`. |
| `niches` | Nisze (per branża) + playbook obiekcji JSON + persona + hook_points + sales_arguments + email_templates | **Pull-only** przez `GET /api/agent/niches` → `30-Niches/{slug}/*.md`. Edycja w CRM `/niches` UI. |
| `knowledge_base` | **GLOBALNA WIEDZA AVENLY** — kategorie `agencja\|uslugi\|social_proof\|ton\|obiekcje\|followup`. Kolumny: `category`, `slug`, `title`, `content`, `is_published`, `ai_chatbot`. | **Two-way sync** vault ↔ CRM przez `/sync-from-crm` (pull) i `/sync-to-crm` (push). Primary source = CRM `/wiedza` UI. Vault to synced kopia (atomic files w `10-Avenly/{kategoria}/`). |
| `chatbot_config` | Klucz-wartość: `system_prompt`, `welcome_message`, `bot_name`, `quick_replies` (JSON) | Sterowane z CRM `/chatbot`. Anon SELECT dla widgetu. |
| `chat_messages` | Historia rozmów chatbota avenly.pl | read przez `crm-analyst` (TBD) |
| `clients` | Klienci aktywni (po podpisaniu umowy) | read przez `crm-analyst` (TBD) |
| `tasks` | Zadania kanban | **read + write** przez agenty (`POST/GET /api/agent/tasks`). Universal — nie tylko social, ale wszelkie deliverable, action items, deadline'y. |
| `meetings` | Spotkania w kalendarzu | **read + write** przez agenty (`POST /api/agent/meetings`). Review meeting, kickoff, follow-up call. |
| `goal_targets` | Cele agencji per okres | read przez `business-advisor` (TBD) |
| `ai_usage_log` | Logi użycia AI w CRM | read przez `crm-analyst` (TBD) |

## Mapping vault ↔ CRM (knowledge_base)

| Vault | CRM table+category | Sync direction |
|---|---|---|
| `10-Avenly/agencja/*.md` | `knowledge_base` where `category='agencja'` | two-way |
| `10-Avenly/uslugi/*.md` | `knowledge_base` where `category='uslugi'` | two-way |
| `10-Avenly/social_proof/*.md` | `knowledge_base` where `category='social_proof'` | two-way |
| `10-Avenly/ton/*.md` | `knowledge_base` where `category='ton'` | two-way |
| `10-Avenly/obiekcje/*.md` | `knowledge_base` where `category='obiekcje'` | two-way |
| `10-Avenly/followup/*.md` | `knowledge_base` where `category='followup'` | two-way |
| `30-Niches/{slug}/*.md` | `niches` table (z `slug` jako klucz, jeden niche = wiele plików per pole) | **pull-only** (read z CRM) |

## Mapping vault → CRM (write-only, agent inserts)

| Vault / agent action | CRM operacja |
|---|---|
| `social-media-strategist` po akceptacji planu | `POST /api/agent/tasks` (batch) |
| `sales-strategist` po planie spotkań | `POST /api/agent/meetings` (batch) |
| `crm-analyst` (TBD) — read leadów | `GET /api/agent/tasks?status=todo` (read-only) |

## n8n (orkiestracja workflow)

**URL:** `https://n8n.avenly.pl`
**Workflow ID:** `IaIg3B98AuFFSDMm` (Avenly Analyze Queue)
**Sekret:** w nagłówku `x-n8n-secret: avenly-n8n-2024` (i `x-followup-secret: avenly-crm-2026` dla follow-up)

Workflows które już działają (z avenly-crm/CLAUDE.md):
- **Cron 2:00** — DataForSEO Google Maps scrape → `potential_leads`
- **Cron 2:30** — `analyze_queue` → `POST /api/analyze` per lead (max 50)
- **Co 6h** — `POST /api/followup` (auto follow-up po 48h)
- **Chatbot** — webhook `/webhook/chatbot` → buduje prompt z `knowledge_base` + `chatbot_config` → zapisuje rozmowy do `chat_messages` + leada do `potential_leads` z tagiem `[chatbot-session:UUID]`

Agenty Avenly OS **NIE modyfikują** workflows n8n. To robi user przez UI n8n.

## Strona avenly.pl (treści publiczne)

**URL:** https://avenly.pl
**Co dostępne:**
- Pełna struktura usług (z `services.ts`)
- 3 posty bloga (`/blog/*`)
- 3 case studies (`/realizacje/*`, ale 2 z `hasCaseStudy: true` mają pełne strony)
- FAQ (`/o-nas`)
- Polityka prywatności (`/polityka-prywatnosci`)
- Sitemap (`/sitemap.xml`)
- Robots (`/robots.txt`)

**Co agenty mogą robić ze stroną:**
- `copywriter` może **czytać** existing copy jako referencję stylu
- `developer` może **modyfikować kod** (po explicit poleceniu — settings.json ma `ask` na write do avenly-web)
- `seo-specialist` (TBD) może czytać sitemap + analizować
- **NIE deployujemy automatycznie** — deploy = `npm run build` + upload `out/` na Hostinger ręcznie

## Cloudflare

- DNS i CDN dla avenly.pl
- Email Routing (planowany — do IMAP reply detection w CRM)
- Po każdym deploy strony: **Purge Everything** (manualnie w dashboard CF)

## Hostinger

- Hosting strony avenly.pl
- Apache + `.htaccess` (cache + bezpieczeństwo + force HTTPS)
- Upload przez FTP (włączyć "Pokaż ukryte pliki" — `.htaccess`)

## Vercel

- Hosting avenly-crm
- Auto-deploy z main branch (jeśli podpięte) — sprawdź konfigurację

## Useme

- Platforma pośrednicząca w wystawianiu faktur
- Z FAQ: "rozliczenie realizujemy za pośrednictwem Useme" — pełnoprawny dokument księgowy

## Resend

- SMTP dla wysyłki maili z CRM (`smtp.resend.com`, user=`resend`)
- Domena `avenly.pl` zweryfikowana przez Cloudflare DNS
- Hostinger blokuje wysyłkę z Vercel (AWS IP) — dlatego Resend
