# Agent Routing — pełna mapa 30 subagentów

Wszyscy subagenty w `.claude/agents/`. Master (`avenly-master`) wybiera kogo wywołać.

## Quick reference

| Trigger | Agent | Model |
|---|---|---|
| Default entry point | `avenly-master` | Opus |
| "napisz post / mail / blog / copy" | `copywriter` | Opus |
| "cold mail / outreach / follow-up" | `cold-outreach` | Opus |
| "plan social / kalendarz IG" | `social-media-strategist` | Opus |
| "strategia content / blog roadmap" | `content-strategist` | Opus |
| "creatives / ad copy / hooki" | `ad-creative` | Opus |
| "newsletter / sequence / email automation" | `email-marketer` | Opus |
| "reel / video / podcast script" | `video-script-writer` | Opus |
| "strategia sprzedaży / ICP / value prop" | `sales-strategist` | Opus |
| "klient ma obiekcję X" | `objection-handler` | Opus |
| "zamknięcie / negocjacja / retencja oferty" | `closer` | Opus |
| "czy ten lead jest worth" | `lead-qualifier` | Haiku |
| "SEO / keywords / audyt strony" | `seo-specialist` | Opus |
| "Meta/Google Ads strategia" | `paid-ads-specialist` | Opus |
| "raport miesięczny / analytics / anomalia" | `analytics-specialist` | Opus |
| "growth / experimenty / hipotezy" | `growth-strategist` | Opus |
| "implementacja kodu / architektura web" | `web-developer` | Opus |
| "animacja / shader / performance UI" | `frontend-specialist` | Opus |
| "endpoint API / RLS / n8n / DB schema" | `backend-specialist` | Opus |
| "wireframe / mockup / design system" | `ui-ux-designer` | Opus |
| "audyt design / kierunek wizualny" | `ui-ux-reviewer` | Opus |
| "deploy / hosting / Cloudflare / .htaccess" | `devops-engineer` | Opus |
| "strategia agencji / pivots / partnerships" | `business-advisor` | Opus |
| "cash flow / runway / budget" | `financial-advisor` | Opus |
| "podatki / VAT / JDG vs sp. z o.o." | `tax-advisor` | Opus |
| "umowa / RODO / NDA / prawa autorskie" | `legal-advisor` | Opus |
| "zatrudnienie / B2B vs UoP / rekrutacja" | `hr-advisor` | Opus |
| "ile policzyć / packagi / discount" | `pricing-strategist` | Opus |
| "research / fact-check / lookup" | `researcher` | Sonnet |
| "analiza rynku / konkurencja / TAM" | `market-analyst` | Opus |
| "analiza CRM / pipeline / leady patterns" | `crm-analyst` | Opus |

## Pliki wiedzy (vault `10-Avenly/`) — co każdy agent powinien czytać

**Vault używa atomicznych plików w podfolderach kategorii CRM** (1 plik = 1 wpis `knowledge_base`). Każdy agent czyta przez Glob/Grep zamiast Read pojedynczego pliku.

| Co | Gdzie | Kto czyta |
|---|---|---|
| Kim jesteśmy, misja, wartość, wyróżniki, proces, portfolio | `10-Avenly/agencja/*.md` (6 atomic) | **Wszyscy agenci** (start kontekstu) |
| Pełna oferta (7 usług) | `10-Avenly/uslugi/*.md` (7 atomic) | `copywriter`, `sales-strategist`, `cold-outreach`, `closer`, `pricing-strategist` |
| Playbook obiekcji (8 obiekcji + skrypty) | `10-Avenly/obiekcje/*.md` (8 atomic) | `sales-strategist`, `cold-outreach`, `objection-handler`, `closer` |
| Case studies | `10-Avenly/social_proof/*.md` + `50-Reference/case-studies.md` | wszystkie agenty (do social proof) |
| Ton — atomiczne wpisy z CRM | `10-Avenly/ton/*.md` (synced) | `copywriter`, `cold-outreach`, `email-marketer`, `video-script-writer` |
| Follow-up szablony | `10-Avenly/followup/*.md` (synced) | `cold-outreach`, `email-marketer` |
| Brand voice (długa narracja) | `10-Avenly/brand-voice.md` | `copywriter`, `social-media-strategist`, `ad-creative`, `video-script-writer`, `ui-ux-designer` |
| Ton rozszerzony (narracja) | `10-Avenly/ton-komunikacji.md` | `copywriter`, wszyscy piszący |
| Content pillars (social mix + hashtagi) | `10-Avenly/content-pillars.md` | `social-media-strategist`, `content-strategist` |
| Target audience (archetypy) | `10-Avenly/target-audience.md` | `copywriter`, `sales-strategist`, `social-media-strategist`, `paid-ads-specialist`, `ui-ux-designer` |
| Per-nisza wiedza (objekcje, persona, hooks) | `30-Niches/{slug}/*.md` (synced z CRM `niches`) | `cold-outreach`, `objection-handler`, `social-media-strategist`, `ad-creative`, per-nisza agenty (TBD) |
| Per-klient wiedza | `20-Clients/{slug}/*.md` | per-klient agenty (TBD) |
| Aktywna robota | `40-Projects/*` | `social-media-strategist` (kalendarz, historia) |
| Referencje rozszerzone | `50-Reference/*` | wszystkie agenty wg potrzeb |
| Tech stack | `50-Reference/tech-stack.md` | `web-developer`, `frontend-specialist`, `backend-specialist`, `devops-engineer`, `ui-ux-designer` |
| avenly-web overview | `50-Reference/avenly-web-overview.md` | `web-developer`, `seo-specialist`, `ui-ux-reviewer`, `frontend-specialist` |

## Dynamiczne agenty (tworzone przez `/new-client` lub `/new-agent`)

- `client-{slug}` — per-klient agent z pełnym kontekstem brief'u + tone klienta + historia
- `niche-{slug}` — per-branża (czytasz `30-Niches/{slug}/*` jako kontekst branżowy)

## Dodawanie kolejnych agentów

Użyj `/new-agent` slash command. Wzorzec w `30-Templates/agent-template.md`.

## Sync vault ↔ CRM

`/sync-from-crm` (pull) i `/sync-to-crm` (push). Niches pull-only.
