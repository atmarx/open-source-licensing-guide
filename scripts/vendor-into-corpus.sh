#!/usr/bin/env bash
#
# vendor-into-corpus.sh — install this guide as a shelf inside another MkDocs site.
#
# WHY THIS EXISTS.  The guide is one body of work with several homes: its own
# site, Northwinds' governance corpus, Drexel's, and whoever forks next.  Copying
# 51 files by hand is how those homes silently drift apart — one gets the Right
# to Repair page, another still has the 2026 glossary, and nobody can tell which
# is which.  A script plus a stamp makes the copy a REF BUMP instead: the corpus
# records the commit it holds, and re-vendoring is a diff you can read.
#
# The pattern is deliberately the same one the Root Cellar overlay uses for
# upstream — the institution never edits the vendored files, and updating means
# moving a pin.
#
# USAGE
#   scripts/vendor-into-corpus.sh --docs-dir <corpus>/docs [--subpath library/licensing]
#
#   --docs-dir   the TARGET site's docs/ directory (required)
#   --subpath    where the shelf lands beneath it (default: library/licensing)
#   --dry-run    print what would happen, touch nothing
#
# It writes files and prints two things it CANNOT write for you: the nav block
# and the markdown_extensions the pages need.  Both live in the target's
# mkdocs.yml, which belongs to that institution — a script that edited it would
# be reaching into somebody else's config, and the merge is a judgement call
# (see NOTES below).
#
# NOTES / KNOWN TRADE-OFFS, all deliberate:
#
#   * `pymdownx.snippets.auto_append` is NOT carried over.  In this repo it
#     appends the abbreviation glossary to every page; in a host corpus that
#     would append it to every page of THEIRS too.  The cost is that
#     abbreviation tooltips stop rendering.  Cosmetic, and the alternative is
#     editing somebody's whole site to suit one shelf.
#
#   * The IBM Plex Mono webfont is NOT carried over.  It loads from
#     fonts.googleapis.com, and a governance corpus that phones out to Google on
#     every page view is a privacy fact its authors did not choose.  The CSS
#     falls back to Courier New.  Self-host it if you want it.
#
#   * `docs/overrides/` (theme custom_dir) is NOT carried over — the host has
#     its own theme, and a custom_dir is site-wide, not per-shelf.
#
set -euo pipefail

SRC_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SUBPATH="library/licensing"
DOCS_DIR=""
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --docs-dir) DOCS_DIR="$2"; shift 2 ;;
    --subpath)  SUBPATH="$2";  shift 2 ;;
    --dry-run)  DRY_RUN=1;     shift ;;
    -h|--help)  sed -n '2,45p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

[[ -n "$DOCS_DIR" ]] || { echo "✗ --docs-dir is required" >&2; exit 2; }
[[ -d "$DOCS_DIR"  ]] || { echo "✗ not a directory: $DOCS_DIR" >&2; exit 2; }

# The stamp records WHAT was vendored.  A dirty tree means the stamp would name
# a commit that does not contain what was copied — refuse rather than lie.
cd "$SRC_ROOT"
if [[ -n "$(git status --porcelain -- docs mkdocs.yml LICENSE)" ]]; then
  echo "✗ the guide has uncommitted changes under docs/ — commit first, so the" >&2
  echo "  vendor stamp names a commit that actually holds what it copies." >&2
  exit 1
fi
REF="$(git rev-parse HEAD)"
SHORT="$(git rev-parse --short HEAD)"
TITLE="$(sed -n 's/^site_name: *//p' mkdocs.yml | head -1)"
# The canonical home, read from the remote rather than hardcoded — a stamp
# pointing at the wrong repository is worse than one pointing nowhere.
ORIGIN="$(git remote get-url origin 2>/dev/null || git remote get-url github 2>/dev/null || echo "")"
ORIGIN="$(printf '%s' "$ORIGIN" | sed -E 's|^git@([^:]+):|https://\1/|; s|\.git$||')"
DEST="$DOCS_DIR/$SUBPATH"

echo "  guide   : $SRC_ROOT @ $SHORT"
echo "  into    : $DEST"
echo "  license : CC BY-SA 4.0 (see LICENSE)"
echo

if [[ $DRY_RUN -eq 1 ]]; then
  echo "-- dry run: no files written --"
else
  # Replace wholesale rather than merge: a page DELETED upstream must disappear
  # here too, or the corpus quietly keeps serving a page its source retracted.
  rm -rf "$DEST"
  mkdir -p "$DEST"

  # The content tree, with its internal shape intact.  Every cross-link inside
  # the guide is relative, so moving the subtree as one piece keeps them all
  # valid without a single rewrite.
  for d in concepts creative-commons guides lessons-learned licenses reference; do
    cp -r "$SRC_ROOT/docs/$d" "$DEST/$d"
  done
  cp "$SRC_ROOT/docs/index.md" "$SRC_ROOT/docs/preface.md" \
     "$SRC_ROOT/docs/foreword.md" "$DEST/"

  # Assets ride WITH the shelf, not into the host's own assets/.  Two reasons:
  # the host may already have an `images/hero.webp`, and the guide's pages
  # reference `../assets/...` which resolves correctly only when assets sit at
  # the shelf root.
  mkdir -p "$DEST/assets/stylesheets"
  cp -r "$SRC_ROOT/docs/assets/images" "$DEST/assets/images"

  # ONLY THE SHELF-PORTABLE CSS TRAVELS, and this is the difference between a
  # shelf and a takeover.  `custom.css` styles this guide as a SITE: it sets
  # --md-primary-fg-color yellow, restyles every h2/h3, and repaints all nine
  # admonition types in a VT100 palette.  Loaded into a host corpus via
  # extra_css — which is site-wide, there is no per-section stylesheet — every
  # one of those rules would land on the host's own policy pages.  Northwinds
  # would go yellow.
  #
  # So the guide marks the rules that match only ITS markup (`.hero`,
  # `.grid.cards.two-column`, `.red-flag`) and ships those alone.  The vendored
  # pages then wear the host's skin, which is the correct outcome: a vendored
  # shelf brings its content, not its brand.  Same rule the Root Cellar overlay
  # keeps in the other direction — brand lives at the institution, never
  # upstream.
  #
  # The Bitwise webfont is not copied either: its only user is the admonition
  # theme that stays behind.
  awk '
    /^\/\* >>> SHELF-PORTABLE/ { keep = 1 }
    /^\/\* <<< SHELF-PORTABLE/ { keep = 0; next }
    keep
  ' "$SRC_ROOT/docs/assets/stylesheets/custom.css" > "$DEST/assets/stylesheets/shelf.css"

  if [[ ! -s "$DEST/assets/stylesheets/shelf.css" ]]; then
    echo "✗ shelf.css came out empty — the SHELF-PORTABLE markers are missing" >&2
    echo "  from docs/assets/stylesheets/custom.css.  Refusing to ship a shelf" >&2
    echo "  with no styling rather than shipping one that repaints its host." >&2
    exit 1
  fi

  # THE ONE PATH THAT DOES NOT SURVIVE THE MOVE.  Every other page sits one
  # level below the shelf root, so `../assets/` still lands on the shelf's
  # assets.  The shelf's own index IS the root, so `../` would climb out of it.
  # Six references exist in total; this is the only one that changes.
  sed -i 's|\.\./assets/images/|assets/images/|g' "$DEST/index.md"

  # The stamp.  Not decoration: without it, "which version of the guide is this
  # corpus serving" is answerable only by diffing 51 files against a repo you
  # may not have.
  cat > "$DEST/VENDORED.md" <<STAMP
---
title: About this shelf
---

# About this shelf

These pages are **vendored** — copied in from another repository, not written
here.  Do not edit them in place: an edit made here is lost the next time the
shelf is refreshed, and the change never reaches anyone else reading the guide.

| | |
|---|---|
| **Source** | [$TITLE]($ORIGIN) |
| **Commit** | \`$REF\` |
| **License** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — © 2026 Andrew Marx |
| **Vendored by** | \`scripts/vendor-into-corpus.sh\` |

## Refreshing it

Re-run the script against this site's \`docs/\` directory.  It replaces the
shelf wholesale, so a page retracted upstream disappears here too — and the
diff is the changelog.

## A note on the voice

The guide is narrated by a constructed character who says so on his own
[Preface](preface.md): a composite greybeard, built with AI assistance, named
as such rather than passed off as a person.  That page travels with the rest
for a reason — a corpus that vendors the guide and drops the disclosure is
publishing a fiction it has not labelled.

## Fixing something

Corrections go **upstream**, to the guide's own repository, where they reach
every institution running a copy.  That is the entire point of vendoring from a
source rather than forking prose.
STAMP

  echo "✓ wrote $(find "$DEST" -type f | wc -l) files to $DEST"
fi

# ---------------------------------------------------------------- what YOU merge
cat <<'BANNER'

────────────────────────────────────────────────────────────────────────
The two things this script will not edit for you — they live in your
mkdocs.yml, which is yours.
────────────────────────────────────────────────────────────────────────

1) markdown_extensions — the pages need these.  Add any you are missing:

     - abbr
     - attr_list
     - def_list
     - footnotes
     - md_in_html
     - tables
     - pymdownx.betterem
     - pymdownx.caret
     - pymdownx.details
     - pymdownx.emoji:
         emoji_index:     !!python/name:material.extensions.emoji.twemoji
         emoji_generator: !!python/name:material.extensions.emoji.to_svg
     - pymdownx.highlight
     - pymdownx.inlinehilite
     - pymdownx.keys
     - pymdownx.mark
     - pymdownx.superfences
     - pymdownx.tabbed:
         alternate_style: true
     - pymdownx.tasklist:
         custom_checkbox: true
     - pymdownx.tilde

   pymdownx.emoji is the one that matters most: the comparison tables are
   built from `:material-check:` / `:material-close:` icons, and without it
   every cell renders as literal text.

   NOT recommended: pymdownx.smartsymbols.  The guide does not need it, and
   it rewrites (c), +/- and != across YOUR existing pages.

2) extra_css — the hero banners and the terminal blocks need this:

BANNER
echo "     - $SUBPATH/assets/stylesheets/shelf.css"
cat <<'BANNER'

3) nav — paste this under whatever section you want it in:
BANNER

# Generated from the source tree, so a page added upstream appears here rather
# than being silently left out of the nav by a hand-maintained list.
python3 - "$SRC_ROOT" "$SUBPATH" <<'PY'
import re, sys, pathlib
src, sub = sys.argv[1], sys.argv[2]
docs = pathlib.Path(src) / "docs"

def title_of(rel: str) -> str:
    p = docs / rel
    text = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^title:\s*(.+)$", text, re.M)         # frontmatter first
    if m:
        return m.group(1).strip().strip("'\"")
    m = re.search(r"^#\s+(.+)$", text, re.M)              # then the H1
    if m:
        return re.sub(r"[*`]", "", m.group(1)).strip()
    return p.stem.replace("-", " ").title()


def quoted(title: str) -> str:
    """ALWAYS quoted, never conditionally.

    A dozen of these titles contain a colon ("Oracle v. Google: The API
    Copyright War"), and in YAML `- A: B: c.md` is a parse error, not a nav
    entry.  Quoting only the ones that look dangerous means the next page
    upstream with a colon in its H1 silently breaks somebody's site build.
    """
    return '"' + title.replace('\\', '\\\\').replace('"', '\\"') + '"'

SECTIONS = [
    ("Concepts",         "concepts"),
    ("Software Licenses", "licenses"),
    ("Creative Commons", "creative-commons"),
    ("Practical Guides", "guides"),
    ("Lessons Learned",  "lessons-learned"),
    ("Reference",        "reference"),
]
out = ["    - Open Source Licensing:",
       f"      - Start Here: {sub}/index.md",
       f"      - Preface: {sub}/preface.md",
       f"      - Foreword: {sub}/foreword.md"]
for label, d in SECTIONS:
    files = sorted((docs / d).rglob("*.md"))
    # index.md leads its own section; the rest follow alphabetically.
    files.sort(key=lambda p: (p.name != "index.md", p.as_posix()))
    out.append(f"      - {label}:")
    for f in files:
        rel = f.relative_to(docs).as_posix()
        out.append(f"        - {quoted(title_of(rel))}: {sub}/{rel}")
out.append(f"      - About This Shelf: {sub}/VENDORED.md")
print("\n" + "\n".join(out) + "\n")
PY
