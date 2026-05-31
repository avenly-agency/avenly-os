# Tech Stack Avenly — używane technologie

Stos technologiczny używany przez Avenly w projektach klienckich i wewnętrznych.

## Strony statyczne / one-page

**Stack:** HTML, SCSS, JavaScript, Cloudflare
**Kiedy:** najmniejsze projekty (one-page wizytówka, event landing, MVP marki)
**Argumentacja:** ekstremalnie szybkie, minimum kosztów hostingu, łatwe utrzymanie

## Strony WordPress (większość projektów SMB)

**Stack:** WordPress + motyw **IMPREZA** + plugin **All in One SEO** + Cloudflare
**Czemu IMPREZA:** flexibility (page builder dla klienta po wdrożeniu) + dobra wydajność + duża społeczność
**Kiedy:** profesjonalne strony firmowe + sklepy e-commerce
**Argumentacja:**
- Klient samodzielnie zarządza treścią po wdrożeniu
- Bez kosztu rozwoju customowego CMS
- Sprawdzony stack — łatwo znaleźć developerów do utrzymania jeśli zmienicie agencję
- All in One SEO daje 90% tego co premium SEO pluginy (Yoast/Rank Math) za $0

## Strony dedykowane (custom)

**Stack:** **React + Next.js + Tailwind CSS** + Headless CMS (Strapi / Sanity / Decap CMS — w zależności od projektu) + Cloudflare CDN
**Kiedy:** największe / najbardziej widoczne projekty, gdzie performance i unikalny design są kluczowe
**Argumentacja:**
- Static export → 99/100 PageSpeed desktop (jak avenly.pl)
- Płynne animacje (Framer Motion, GSAP)
- Pełna kontrola design system + skalowalność
- Bez bagażu WordPress (no plugin bloat, no security maintenance)

**Avenly.pl jest własnym proof of craft** — strona pokazuje co potrafimy w Next.js. Klienci często widzą stronę → pytają "chcę taką samą".

## E-commerce

**Stack:** **WordPress + WooCommerce + IMPREZA** + Cloudflare
**Integracje:**
- **Płatności:** Przelewy24 / Stripe (BLIK, karty)
- **Kurierzy:** InPost, DPD
- **SEO:** All in One SEO
**Kiedy:** sklepy małej i średniej skali (do ~1000 produktów, do ~100k PLN miesięcznej sprzedaży)
**Argumentacja:**
- Stabilność + przewidywalność (WooCommerce to standard)
- Klient sam dodaje produkty bez wiedzy IT
- Integracje z polskimi standardami płatności i kurierów out-of-the-box

> **Dla większych sklepów:** rozważamy Shopify (jeśli klient ma międzynarodowo) lub custom (Next.js + Medusa / Saleor) — ale to rzadkie i quote-only.

## Aplikacje webowe (custom)

**Stack:** **Next.js + TypeScript + Tailwind + Supabase**
**Czasem:** Convex (jako alternatywa dla Supabase), Drizzle ORM, tRPC
**Kiedy:** customowe systemy — CRM lite, panele klientów, narzędzia branżowe
**Argumentacja:**
- TypeScript = mniej bugów + łatwiejsze utrzymanie
- Supabase = full backend (Auth + Postgres + Storage + Realtime) bez własnego serwera
- Next.js = static + SSR + API routes w jednym

**Przykład żywy:** avenly-crm jest własnym CRM-em z dokładnie tym stackem.

## AI / Chatboty / Automatyzacje

### Chatboty (Voiceflow — dla SMB)
**Stack:** **Voiceflow** (no-code drag&drop) + integracja z bazą wiedzy klienta + frontend widget
**Kiedy:** klient SMB chce chatbota szybko (1-2 tygodnie wdrożenie) bez customizacji deep
**Cennik Voiceflow:** plan Pro ~$50/mo per workspace

### Chatboty (Claude AI — custom, dla większych)
**Stack:** **Anthropic Claude API** (direct fetch, NIE SDK) + **n8n** (orchestration) + **Supabase** (storage) + **Next.js widget**
**Modele:** Haiku (większość zadań), Sonnet (deeper context), Opus (rzadko)
**Kiedy:** klient potrzebuje głębokiej integracji z systemami, custom personality, specyficzne workflow
**Argumentacja:** koszt zmienny per użycie + maksymalna jakość + integracje z czymkolwiek

**Live example:** chatbot na avenly.pl jest custom Claude AI + n8n + Supabase, NIE Voiceflow.

### Workflow automation (n8n)
**Stack:** **n8n self-hosted** (n8n.avenly.pl)
**Use cases:**
- Lead enrichment (scraping + AI analysis)
- Cross-system sync (CRM ↔ social media ↔ email)
- Cron jobs (follow-up, scrape, daily reports)
- Webhook orchestration

**Przykład żywy:** workflow `Avenly Analyze Queue` w n8n:
- 2:00 — DataForSEO Google Maps scrape → potential_leads
- 2:30 — analyze_queue (50 leadów) → Anthropic API → mail draft
- co 6h — follow-up po 48h od pierwszego maila

## Hosting / CDN / DNS

- **Hosting (statyczne strony):** Hostinger (Apache + `.htaccess`)
- **Hosting (Next.js dynamic apps):** Vercel
- **Hosting (WordPress):** Hostinger lub dedykowany serwer (zależnie od skali klienta)
- **CDN + DNS:** **Cloudflare** (dla wszystkich)
- **Email DNS:** Cloudflare (z verified Resend dla SMTP)

## Email / SMTP

- **Outbound (transactional):** **Resend** (smtp.resend.com, port 465, user=resend)
  - Domena zweryfikowana przez Cloudflare DNS
  - Hostinger SMTP blokuje połączenia z AWS (Vercel) — dlatego Resend
- **Inbound (przychodzące, dla CRM reply detection):** **Cloudflare Email Routing + Worker → n8n webhook** (planowane)

## Bazy danych

- **Backend dla SaaS / aplikacji:** Supabase (Postgres + Auth + Storage + RLS)
- **CRM agencji:** Supabase (project: `kyfsjvgixmcmafvaiyak`)
- **WordPress:** MySQL (zarządzane przez hosting)

## CMS

- **WordPress + IMPREZA** — większość projektów klienckich
- **Headless** (Strapi / Sanity / Decap CMS) — przy dedykowanych Next.js stronach gdzie klient chce edytować treść
- **No CMS (treści w kodzie)** — przy one-page'ach i avenly.pl (treści w `app/data/*.ts`)

## DevOps / CI/CD

- **Git:** GitHub (private repos)
- **Deploy statyczne:** ręczny upload przez FTP na Hostinger (avenly.pl)
- **Deploy dynamic:** Vercel auto-deploy z main branch (avenly-crm)
- **Monitoring:** [WYPEŁNIJ — Vercel Analytics, Cloudflare Analytics, brak?]
- **Error tracking:** [WYPEŁNIJ — Sentry? żadne?]

## Tools / SaaS używane wewnętrznie

| Narzędzie | Cel | Plan |
|---|---|---|
| **Cloudflare** | DNS, CDN, Email Routing (plan) | Free |
| **Hostinger** | Hosting statyczne avenly.pl | [WYPEŁNIJ — szacunkowo Business] |
| **Vercel** | Hosting avenly-crm | [WYPEŁNIJ — Hobby? Pro?] |
| **Supabase** | DB + Auth dla CRM | Free tier (do ~500k requests/mo) |
| **GitHub** | Repo + collaboration | Free private repos |
| **Resend** | SMTP outbound | Free (do 3000 maili/mo) |
| **Anthropic** | AI w CRM + agentic OS | Twoja $100 Max 5x subscription |
| **n8n** | Self-hosted automation | Free (self-hosted) |
| **Useme** | Faktury dla klientów (zamiast działalności) | Per faktura |
| **Google Workspace** | [WYPEŁNIJ — czy używamy?] | [WYPEŁNIJ] |
| **Slack/Discord** | Komunikacja team | [WYPEŁNIJ] |
| **Figma** | UI/UX design | [WYPEŁNIJ — Free? Pro?] |
| **DataForSEO** | Scraping Google Maps (CRM) | Pay per use |
| **Voiceflow** | Chatboty SMB | Pro plan per workspace |

## Tech stack — zasady wyboru

1. **Standardy branżowe > "fancy"** — WordPress + IMPREZA jest stabilnym wyborem, nawet jeśli "boring"
2. **Polski standard >> międzynarodowy** — Przelewy24, InPost, BLIK, NIP/REGON
3. **TypeScript zawsze** — w nowym kodzie. JavaScript tylko gdy projekt vintage / one-page
4. **Static-first** — Next.js static export gdy się da (avenly.pl). Dynamic SSR tylko gdy potrzebne (CRM)
5. **No vendor lock-in po naszej stronie** — klient musi móc zmienić agencję bez przepisywania od zera
6. **Cost-aware** — wybieramy bezpłatne / tanie tiery dopóki nie ma sensu skalować

## Co NIE używamy (świadoma decyzja)

- ❌ Wix / Squarespace / Webflow (nie damy klientowi solidnego SEO + customizacji + kosztów długoterminowo)
- ❌ Joomla / Drupal (dead stack)
- ❌ jQuery (przestarzałe, używamy React)
- ❌ Vue / Svelte (mamy stack na React — utrzymywalność > "który framework lepszy")
- ❌ AWS bezpośrednio (overkill dla skali SMB — Vercel/Cloudflare wystarczają)
- ❌ Generic page buildery typu Elementor jeśli możemy IMPREZA (cleaner, szybszy)
