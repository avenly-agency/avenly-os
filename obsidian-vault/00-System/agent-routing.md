# Agent Routing

Mapa wszystkich agentów: kiedy każdy jest wołany, który model używa, co potrafi.

## Aktywne (faza 0)

| Agent | Model | Domena | Wołasz gdy |
|---|---|---|---|
| `avenly-master` | Opus | Orkiestracja | Domyślny entry point. Zlecenie złożone, niejasne, lub wieloetapowe. |
| `social-media-strategist` | Sonnet | Strategia social | "plan na miesiąc", "kalendarz IG", "strategia FB", "mix contentowy", "kampania social" |
| `copywriter` | Sonnet | Konkretne teksty | "napisz post", "draft maila", "headline", "caption", "landing copy", "treść reklamy", "oferta" |

## Planowane (faza 1+)

| Agent | Model | Domena | Status |
|---|---|---|---|
| `sales-strategist` | Opus | Strategia sprzedaży, scoring leadów, value prop, positioning | TBD faza 1 |
| `cold-outreach` | Sonnet | Cold maile i follow-upy | TBD faza 1 |
| `seo-specialist` | Sonnet | Keywords, audyty on-page, content brief | TBD faza 2 |
| `business-advisor` | Opus | Strategiczne decyzje agencji (pricing, kierunek, pivoty) | TBD faza 2 |
| `crm-analyst` | Sonnet | Analizy z Supabase (leady, klienci, wyniki) read-only | TBD faza 1 |
| `researcher` | Haiku | Web research, fast lookups, fact-check | TBD faza 1 |
| `developer` | Sonnet | Kod projektów klienckich (NIE avenly-web/-crm — to robisz Ty bezpośrednio) | TBD faza 2 |
| `ui-ux-reviewer` | Opus | Audyty designu, kierunek wizualny | TBD faza 2 |
| `content-strategist` | Sonnet | Strategia content marketingu (blog, video, lead magnets) | TBD faza 2 |
| `ad-creative` | Sonnet | Creatives reklamowe, ad copy, hook'i video | TBD faza 2 |
| `client-{slug}` | Sonnet | Per-klient agent z full kontekstem | TBD na każdego klienta |

## Wybór modelu — reguła kciuka

- **Opus** — strategia, decyzje wieloetapowe, audyt jakości, orkiestracja. Drogi → używaj świadomie.
- **Sonnet** — większość pracy: copy, plany, analizy, kod, review. Domyślny wybór.
- **Haiku** — ekstrakcja, formatowanie, lookup, klasyfikacja. Tani → spamuj.

## Zasada delegowania

`avenly-master` zawsze deleguje do specjalisty zamiast robić sam. Wyjątek: prosty merge wyników od 2+ subagentów. Sam Opus piszący posty = strata puli + gorszy efekt niż wyspecjalizowany Sonnet.

## Jak dodać nowego agenta

1. Stwórz `.claude/agents/{nazwa}.md` z YAML frontmatter (`name`, `description`, `tools`, `model`) + system prompt
2. Dodaj wpis do tej tabeli wyżej
3. Zaktualizuj `avenly-master.md` w sekcji "Routing" żeby wiedział że istnieje
4. Git commit + push → Bartek pull → obaj mają
5. Test: napisz do mastera prośbę pasującą do nowego agenta — czy go wywoła
