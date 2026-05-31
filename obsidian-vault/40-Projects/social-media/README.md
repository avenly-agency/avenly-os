# Social Media — projekt ciągły

Folder zawiera planowanie i historię social media dla Avenly.

## Pliki

- **`kalendarz-2026.md`** — zaplanowane posty na 2026 (per miesiąc). Generowany przez `social-media-strategist`, aktualizowany po publikacji.
- **`historia-postow.md`** — log opublikowanych postów z notatkami co działało/co nie. Wypełniany ręcznie albo agent po publikacji.

## Workflow miesięczny

1. **Ostatni tydzień miesiąca:** user prosi agenta `social-media-strategist` o plan na kolejny miesiąc
2. Agent czyta `10-Avenly/brand-voice.md`, `content-pillars.md`, `historia-postow.md`, `kalendarz-2026.md` (zaplanowane)
3. Generuje plan kalendarzowy → pokazuje userowi
4. User akceptuje (z poprawkami albo bez)
5. Agent zapisuje plan do `kalendarz-2026.md` + tworzy taski w CRM (`POST /api/agent/tasks` — gdy będzie endpoint)
6. Bartek i Michał realizują taski w CRM jak dotąd (drag&drop w kanban)
7. Po publikacji posta: status `opublikowany` w kalendarzu + wpis w `historia-postow.md` z linkiem i wynikami

## Powiązane

- Templaty per platform: `30-Templates/social-post.md`
- Pillars i hashtagi: `10-Avenly/content-pillars.md`
- Brand voice: `10-Avenly/brand-voice.md`
- Anti-references: `10-Avenly/ton-komunikacji.md`
