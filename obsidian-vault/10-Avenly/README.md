# 10-Avenly — Wiedza o firmie

Single source of truth dla **Avenly OS agents** i (po sync) dla **CRM `knowledge_base`**.

## Struktura

```
10-Avenly/
├── README.md                    ← ten plik (NIE sync)
│
├── agencja/                     ← CRM category=agencja (6 wpisów)
│   ├── kim-jestesmy.md
│   ├── misja.md
│   ├── wartosc-dla-klienta.md
│   ├── wyrozniki.md
│   ├── podejscie-do-pracy.md
│   └── portfolio-skrot.md
│
├── uslugi/                      ← CRM category=uslugi (7 wpisów)
│   ├── strony-szyte-na-miare.md
│   ├── strona-wizytowka-one-page.md
│   ├── profesjonalna-strona-firmowa.md
│   ├── sklepy-ecommerce.md
│   ├── design-stron-internetowych.md
│   ├── chatboty-ai.md
│   └── audyt-wydajnosci-seo.md
│
├── obiekcje/                    ← CRM category=obiekcje (8 wpisów)
│   ├── za-drogo.md
│   ├── mam-juz-strone.md
│   ├── pomysle-odezwe-sie.md
│   ├── nie-mam-czasu.md
│   ├── robimy-sami.md
│   ├── wyslijcie-oferte.md
│   ├── dlaczego-avenly.md
│   └── co-jesli-nie-zadziala.md
│
├── social_proof/                ← CRM category=social_proof (1 wpis)
│   └── mcentrum-fizjoterapia.md
│
├── ton/                         ← CRM category=ton (TBD razem w fazie 1.13)
├── followup/                    ← CRM category=followup (TBD)
│
└── (duże narracyjne pliki — NIE syncowane do CRM)
    ├── brand-voice.md           ← długa narracja stylistyczna
    ├── content-pillars.md       ← mix pillarów social, CRM tego nie ma
    ├── target-audience.md       ← archetypy klientów, CRM tego nie ma
    └── ton-komunikacji.md       ← rozszerzona narracja tonu (vault-only)
```

## Reguły

### Atomiczne pliki w podfolderach kategorii CRM

**1 plik = 1 wpis w `knowledge_base`.** Każdy taki plik MUSI mieć frontmatter:

```yaml
---
crm:
  table: knowledge_base
  category: agencja              # albo: uslugi | obiekcje | social_proof | ton | followup
  slug: misja-avenly             # unique key (kebab-case)
  title: "Misja Avenly"          # tytuł wpisu w CRM
  ai_chatbot: true               # czy trafia do n8n chatbot (avenly.pl)
  is_published: true             # czy aktywny
---

[treść — markdown, dowolnie złożona]
```

### Pliki narracyjne (root `10-Avenly/`)

**Nie mają frontmatter `crm:`** — bo nie mapują 1:1 do żadnej kategorii w `knowledge_base`. Są długie, narracyjne, dla agentów Avenly OS którzy potrzebują pełnego kontekstu (`brand-voice`, `content-pillars`, `target-audience`, rozszerzony `ton-komunikacji`).

## Sync z CRM

| Direction | Trigger | Co dotyka |
|---|---|---|
| **CRM → vault** (pull) | `/sync-from-crm` w Avenly OS | Aktualizuje atomiczne pliki w podfolderach kategorii |
| **vault → CRM** (push) | `/sync-to-crm` w Avenly OS | Pushuje nowe/zmienione atomiczne pliki do `knowledge_base` (z diff + akceptacją) |

**Primary source of truth:** CRM `knowledge_base` table (UI: `avenlycrm.vercel.app/wiedza`).

**Vault to synced kopia** — agenci Avenly OS czytają vault, nie CRM bezpośrednio. Aktualizacja vault = `/sync-from-crm`.

## Co czyta każdy agent

| Agent | Czyta z vault |
|---|---|
| `avenly-master` | Glob `10-Avenly/**/*.md` (overview), per task: konkretne pliki |
| `copywriter` | `agencja/*.md`, `uslugi/*.md`, `ton/*.md`, `ton-komunikacji.md`, `brand-voice.md`, `30-Templates/*.md` |
| `social-media-strategist` | `agencja/*.md`, `content-pillars.md`, `target-audience.md`, `social_proof/*.md`, `40-Projects/social-media/*` |
| `sales-strategist` (TBD) | `obiekcje/*.md`, `uslugi/*.md`, `agencja/podejscie-do-pracy.md`, `social_proof/*.md` |
| `cold-outreach` (TBD) | `obiekcje/*.md`, `followup/*.md`, `30-Niches/{slug}/*.md`, `30-Templates/cold-email.md` |
