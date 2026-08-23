# Putting this guide inside somebody else's site

Two different things can be installed from this repository, and they answer
different questions. Pick the one you actually want — or both.

| | **The licence shelf** | **The whole guide** |
|---|---|---|
| What it is | 61 cards, one per SPDX identifier | 51 pages of prose |
| Answers | *"What does BSD-3-Clause oblige me to do?"* | *"Why did HashiCorp relicense, and what did it cost?"* |
| Built by | `scripts/build-card-catalog.py` + `scripts/render-shelf.py` | `scripts/vendor-into-corpus.sh` |
| Facts from | SPDX · choosealicense · ScanCode | this repository |
| Size in the host | ~62 generated pages, no assets | 61 files including images |
| Regenerate | yes, it is output | no, it is a copy with a pin |

**Most institutions want the shelf.** It is the thing a researcher flips
through, it carries no house style, and it is where the platform will eventually
show *which datasets here carry this licence*. The full guide is a reading
experience — link out to the hosted copy unless the corpus is meant to be read
offline.

---

## A. The licence shelf

### 1. Build the catalog

```bash
scripts/build-card-catalog.py \
  --out /path/to/<institution>/seed/licenses.yaml \
  --base-url https://<where-the-guide-is-hosted>
```

Fetches SPDX's licence list, choosealicense.com's per-licence YAML, and ScanCode
LicenseDB, joins them per identifier, and adds `explained_in` links wherever this
guide covers that licence. Downloads cache in `/tmp/licence-catalog-cache`;
`--offline` reuses the cache and fails rather than reaching out.

`--base-url` is the **public URL of the guide**, not of the host corpus — the
`explained_in` links point at the long-form pages wherever they live. Omit it and
the cards simply carry no "long version" link.

Read the summary it prints. `_gaps` in the output names any identifier this
guide discusses but no source could confirm; those are for fixing upstream, not
for filling in by hand.

### 2. Render the shelf

```bash
scripts/render-shelf.py \
  --catalog /path/to/<institution>/seed/licenses.yaml \
  --out    /path/to/<corpus>/docs/library/licenses \
  --subpath library/licenses
```

Writes one page per licence plus an index, and prints a nav block.

### 3. Wire it into the host's `mkdocs.yml`

Three edits, all in the host's file, none of them ours to make automatically:

- **`markdown_extensions`** — add `abbr`, `def_list`, `footnotes`, `md_in_html`
  if absent.
- **`nav`** — paste the printed block, adjusting indentation to the host's
  nesting depth.
- **`extra_css`** — nothing. The shelf uses no custom styling on purpose.

**Do not add `pymdownx.smartsymbols`.** It rewrites `(c)`, `!=` and `+/-` across
every page of the host corpus, which is a site-wide change made to suit one
shelf.

### 4. Build strictly

```bash
mkdocs build --strict
```

Must be clean. `--strict` is what catches a nav entry pointing at a page the
renderer did not write.

---

## B. The whole guide

```bash
scripts/vendor-into-corpus.sh --docs-dir /path/to/<corpus>/docs \
                              [--subpath library/licensing]
```

Copies the content tree, the hero images, and only the **shelf-portable** slice
of the stylesheet, then writes a `VENDORED.md` stamp naming the exact commit it
copied. Prints the nav block and the `markdown_extensions` list.

`pymdownx.emoji` is required here — the comparison tables are built from
`:material-check:` icons, and without it every cell renders as literal text.

### What deliberately does not travel

- **The brand.** `custom.css` styles this guide as a *site*: yellow primary,
  restyled headings, all nine admonition types repainted VT100. MkDocs loads
  `extra_css` site-wide, so every one of those rules would land on the host's own
  policy pages. Only rules matching markup these pages emit (`.hero`,
  `.grid.cards.two-column`, `.red-flag`) are marked `SHELF-PORTABLE` and shipped.
  Vendored pages wear the host's skin. **A shelf brings its content, not its
  livery.**
- **`pymdownx.snippets.auto_append`.** Here it appends the abbreviation glossary
  to every page; in a host it would append it to every page of *theirs*.
  Abbreviation tooltips stop rendering. Cosmetic.
- **The IBM Plex Mono webfont.** It loads from `fonts.googleapis.com`, and a
  governance corpus phoning out to Google on every page view is a privacy fact
  its authors did not choose. Falls back to Courier New.
- **`docs/overrides/`.** A theme `custom_dir` is site-wide, not per-shelf.

### Refreshing

Re-run the script. It replaces the shelf wholesale, so a page retracted upstream
disappears from the host too, and the diff is the changelog. The stamp moves;
that is your ref bump.

---

## Rules that apply to both

**Never edit vendored or generated pages in place.** An edit there is lost on the
next refresh and never reaches anyone else running a copy. Corrections go
upstream — to this repository for prose, to SPDX/choosealicense/ScanCode for
facts.

**Carry the licences.** This guide is CC BY-SA 4.0; the catalog's sources are
CC-BY-3.0 and CC-BY-4.0 and ride in the output under `_sources`. A licence
library that ignores the licences of its own inputs is not a good look, and
ShareAlike means the host's corpus must be compatibly licensed. Northwinds' is
CC BY-SA 4.0, which is why the guide was relicensed from CC BY-NC in the first
place — NC forbade commercial use inside a corpus that promised forkability, and
both statements could not be true about the same page.

**Name the constructed voice.** If you vendor the full guide, the Preface travels
with it. The narrator is a composite character, built with AI assistance, who
says so himself. A corpus that ships the guide and drops that page is publishing
a fiction it has not labelled.

---

## Doing this for another institution

The reference implementation is Northwinds
(`northwinds/governance/`, shelf at `docs/library/licenses/`, catalog at
`seed/licenses.yaml`). To repeat it:

1. Pick the shelf, the guide, or both — the table at the top.
2. Run the commands above against that corpus's `docs/` and `seed/`.
3. Make the three `mkdocs.yml` edits by hand. They are judgement calls about
   somebody else's site, which is exactly why no script makes them.
4. `mkdocs build --strict` must be clean before you commit.
5. Commit the generated pages. They are checked in on purpose: the site has to
   build without network access, and a diff on a regenerated shelf is how you
   see that SPDX deprecated an identifier last month.

**Each institution's catalog is its own.** Northwinds' sample data is
Northwinds'; Drexel's is Drexel's. They are generated from the same public
sources and will mostly agree — but `holdings`, the count of datasets on *that*
system carrying *that* licence, is the field that will not, and it is the field
the shelf exists to grow into.
