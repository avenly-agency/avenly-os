"""
Bootstrap CRM → vault sync (jednorazowy script).
Czyta /tmp/knowledge.json + /tmp/niches.json i generuje pliki w obsidian-vault/.

Skrypt jednorazowy do pierwszego pull'a. Późniejsze sync zrobi /sync-from-crm slash command.
"""
from pathlib import Path
import json
import re
import sys

VAULT = Path(r"c:/Users/Start/Desktop/avenly-os/obsidian-vault")
VALID_CATEGORIES = {"agencja", "uslugi", "social_proof", "ton", "obiekcje", "followup"}

def clean_slug(s):
    """Usuń trailing timestamp (-13+digits) z CRM slug."""
    return re.sub(r"-\d{10,}$", "", s)

def polish_slug(name):
    """Polish-aware slug dla niches (Studio Detailingowe → studio-detailingowe)."""
    name = name.lower()
    pl_map = str.maketrans("ąćęłńóśźż", "acelnoszz")
    name = name.translate(pl_map)
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")

def write_md(path, frontmatter, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["---"]
    def emit(d, indent=0):
        for k, v in d.items():
            if isinstance(v, dict):
                lines.append("  " * indent + f"{k}:")
                emit(v, indent + 1)
            elif isinstance(v, bool):
                lines.append("  " * indent + f"{k}: {str(v).lower()}")
            elif v is None:
                lines.append("  " * indent + f"{k}: null")
            else:
                # Quote strings with special chars
                s = str(v)
                if any(c in s for c in [':', '#', '"', '\n']):
                    s = '"' + s.replace('"', '\\"') + '"'
                lines.append("  " * indent + f"{k}: {s}")
    emit(frontmatter)
    lines.append("---")
    lines.append("")
    lines.append(body)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path

# ============= KNOWLEDGE_BASE =============
with open("/tmp/knowledge.json", encoding="utf-8") as f:
    kb = json.load(f)

kb_created = []
kb_skipped = []

for e in kb["entries"]:
    if not e.get("is_published"):
        kb_skipped.append((e["title"], "unpublished"))
        continue
    if e["category"] not in VALID_CATEGORIES:
        kb_skipped.append((e["title"], f"category={e['category']} not in vault categories"))
        continue

    clean = clean_slug(e["slug"])
    target = VAULT / "10-Avenly" / e["category"] / f"{clean}.md"

    frontmatter = {
        "crm": {
            "table": "knowledge_base",
            "id": e["id"],
            "category": e["category"],
            "slug": e["slug"],          # pełny CRM slug z timestampem
            "title": e["title"],
            "ai_chatbot": e.get("ai_chatbot", False),
            "is_published": e.get("is_published", True),
        }
    }
    body = f"# {e['title']}\n\n{e['content']}"

    write_md(target, frontmatter, body)
    kb_created.append(str(target.relative_to(VAULT)))

print(f"=== KNOWLEDGE_BASE: {len(kb_created)} created, {len(kb_skipped)} skipped ===")
for p in kb_created:
    print(f"  + {p}")
for title, reason in kb_skipped:
    print(f"  - SKIP: {title!r} ({reason})")
print()

# ============= NICHES =============
with open("/tmp/niches.json", encoding="utf-8") as f:
    nm = json.load(f)

niche_files = []

NICHE_FIELDS = {
    "opis_branzy":     ("opis-branzy.md",       "Opis branży"),
    "persona":         ("persona.md",            "Persona klienta"),
    "problemy_2026":   ("problemy.md",           "Problemy branży"),
    "hook_points":     ("hooks.md",              "Punkty zaczepienia (hooks)"),
    "sales_arguments": ("sales-arguments.md",    "Argumenty sprzedażowe"),
    "objekcje":        ("obiekcje.md",           "Obiekcje per nisza"),
    "email_templates": ("email-templates.md",    "Szablony maili"),
    "cold_mailing_tips":("cold-mailing-tips.md", "Wskazówki cold mailingu"),
    "ai_prompts":      ("ai-prompts.md",         "Dodatkowe instrukcje AI"),
}

for n in nm["niches"]:
    name = n.get("name") or "unnamed"
    slug = polish_slug(name)
    niche_dir = VAULT / "30-Niches" / slug

    # _meta.md
    meta_frontmatter = {
        "crm": {
            "table": "niches",
            "id": n["id"],
            "name": name,
            "slug": slug,
            "sync_direction": "pull-only",
        }
    }
    write_md(niche_dir / "_meta.md", meta_frontmatter, f"# {name}\n\n*Per-nisza wiedza. Pull-only z CRM `/niches`. Edycja w CRM UI.*")
    niche_files.append(str((niche_dir / "_meta.md").relative_to(VAULT)))

    # Pliki per pole (tylko gdy content niepusty)
    for field, (fname, heading) in NICHE_FIELDS.items():
        val = n.get(field)
        if not val:
            continue
        s = str(val).strip()
        if not s or s == "[]":
            continue

        # Special: obiekcje to JSON array
        if field == "objekcje":
            try:
                obj_list = json.loads(s)
                if not obj_list:
                    continue
                body_parts = [f"# {heading} — {name}", ""]
                for item in obj_list:
                    o = item.get("objekcja", "")
                    a = item.get("odpowiedz", "")
                    if o or a:
                        body_parts.append(f"## {o}")
                        body_parts.append("")
                        body_parts.append(a)
                        body_parts.append("")
                        body_parts.append("---")
                        body_parts.append("")
                body = "\n".join(body_parts)
            except (json.JSONDecodeError, AttributeError):
                body = f"# {heading} — {name}\n\n{s}"
        else:
            body = f"# {heading} — {name}\n\n{s}"

        fm = {
            "niche": {
                "id": n["id"],
                "name": name,
                "slug": slug,
                "field": field,
            }
        }
        write_md(niche_dir / fname, fm, body)
        niche_files.append(str((niche_dir / fname).relative_to(VAULT)))

print(f"=== NICHES: {len(niche_files)} files in {len(nm['niches'])} folders ===")
for p in niche_files:
    print(f"  + {p}")
