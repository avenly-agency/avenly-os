# Template: Blog Post (avenly.pl/blog)

Pattern używany dla bloga avenly.pl. Identyczny z istniejącymi 3 postami (`avenly-web/app/data/posts.ts`).

## Struktura

- **Długość:** 400-600 słów (5-6 min czytania) — NIE pillar 2000+ słów
- **Nagłówki:**
  - 2× `<h2>` (drugi zawsze brzmi `Podsumowanie: ...`)
  - 2-3× `<h3>` (sub-pytania, podtematy)
- **Lista:** 1× `<ul>` lub `<ol>` z pattern `<li><strong>Etykieta:</strong> Wyjaśnienie</li>`
- **CTA:** zawsze końcowy `<blockquote>` z linkiem do `/kontakt` (NIGDY `/audyt` — to nie istnieje)
- **`<strong>` w każdym akapicie** — 1-2× na akapit (kluczowe słowa)
- **"W Avenly..."** użyte 1-2 razy w tekście (nie więcej)

## Wykluczenia

- Bez FAQ
- Bez tabel
- Bez intro przed pierwszym h2 (od razu pierwszy nagłówek)
- Bez emoji
- Bez wykrzykników w nagłówkach
- Bez listy dłuższej niż 5 elementów (lepiej dwie krótsze)

## Output format (do `avenly-web/app/data/posts.ts`)

```typescript
{
  id: <next-id>,
  slug: "kebab-case-tytul",
  title: "Tytuł — 50-70 znaków",
  excerpt: "Krótki opis, 130-160 znaków. Powtarza co jest w meta description.",
  category: "Strony WWW" | "AI i Automatyzacja" | "Marketing" | "Design",
  date: "YYYY-MM-DD",
  readTime: "5 min" | "6 min",
  mainImage: "/blog/<slug>.webp",   // 1200x630
  content: `
      <h2>Pierwszy nagłówek</h2>
      <p>Pierwszy akapit z <strong>kluczowymi</strong> słowami...</p>
      ...
      <h2>Podsumowanie: ...</h2>
      ...
      <blockquote>
        Chcesz omówić jak [konkret z tematu] może wyglądać u Ciebie? <a href="/kontakt">Napisz do nas</a>.
      </blockquote>
  `,
  tags: ["tag1", "tag2", "tag3"]
}
```

**Indentacja:** TAB w `app/data/posts.ts`, 6-space indent wewnątrz template literal `content`.

## Sekcje obowiązkowe (kolejność)

1. **Pierwszy `<h2>`** — postawienie problemu (pytanie / sytuacja klienta)
2. **2-3 akapity** rozwijające
3. **`<h3>`** — pierwszy sub-temat (np. "Dlaczego to ważne", "Jak działa")
4. **2-3 akapity**
5. **`<h3>`** — drugi sub-temat
6. **Lista** z `<strong>:</strong>` pattern (3-5 elementów)
7. **(opcjonalnie) `<h3>`** — trzeci sub-temat
8. **`<h2>Podsumowanie: ...</h2>`**
9. **1-2 akapity podsumowujące**
10. **`<blockquote>` z CTA do `/kontakt`**

## Tone i styl

- Patrz `10-Avenly/ton-komunikacji.md` (banlist słów)
- Pierwsza linijka musi działać — NIE "W dzisiejszych czasach..."
- Pisz dla SMB owner'a, nie dla developera
- Konkretne przykłady > teorie

## Po napisaniu

`copywriter` zwraca:
1. Gotowy obiekt do wklejenia w `posts.ts`
2. Sugestię nazwy pliku obrazka (`/blog/<slug>.webp`)
3. Notatkę co dalej (deploy: `npm run build` + upload, lub czeka na obraz)
