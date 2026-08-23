#!/usr/bin/env python3
"""build-card-catalog.py — one card per licence, joined from the people who already did this.

WHAT THIS IS FOR.  A reader flips through every licence we know about and lands
on that licence's own card: identifier, what it permits, what it obliges, where
the long version lives — and eventually, which datasets on our own system carry
it.

WE ARE NOT THE FIRST TO MAKE A LICENCE LIBRARY, so this fetches rather than
remembers.  Three public sources, each authoritative for a different column:

  * SPDX License List — the IDENTIFIER authority.  733 entries with
    `isOsiApproved` / `isFsfLibre` / `isDeprecatedLicenseId`.  This is the
    interchange format; everything else keys to it.
  * choosealicense.com (GitHub) — the CARD SHAPE, already.  Its per-licence YAML
    carries `permissions` / `conditions` / `limitations`, which is exactly
    allows / requires / prohibits, plus a one-line description and real projects
    using it.  47 licences, and that set is a good working definition of "major".
  * ScanCode LicenseDB (nexB) — the CATEGORY axis (Permissive, Copyleft,
    Source-available, Public Domain), plus the steward.

## Why this is fetched and not written

Because licence facts are the last thing on earth to reconstruct from memory.
A card that says AGPL's network clause triggers on internal use, or that
BSD-3-Clause carries a patent grant, is not a typo — it is a wrong answer to a
legal question, sitting inside a governance corpus, wearing the same typeface as
the right ones.  Every factual field here has a URL behind it.

What the guide adds is the part no database has: **why you would pick it**, and
the story of what went wrong for the people who picked badly.  That is the
`explained_in` link, and it is the only field on this card that is ours.

## Attribution

The sources are themselves licensed, which is not a detail we of all people get
to skip.  Their terms ride in the output under `_sources`.

Usage:
    scripts/build-card-catalog.py --out licenses.yaml [--base-url URL] [--offline]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CACHE = Path("/tmp/licence-catalog-cache")

SPDX_URL = "https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json"
CAL_INDEX = "https://api.github.com/repos/github/choosealicense.com/contents/_licenses?ref=gh-pages"
CAL_RAW = "https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/{}.txt"
SCANCODE = "https://scancode-licensedb.aboutcode.org/{}.json"
SCANCODE_INDEX = "https://scancode-licensedb.aboutcode.org/index.json"

SOURCES = [
    {"name": "SPDX License List", "url": "https://spdx.org/licenses/",
     "data": "https://github.com/spdx/license-list-data",
     "license": "CC-BY-3.0",
     "gives": "identifiers, names, OSI/FSF approval, deprecation, reference URLs"},
    {"name": "choosealicense.com", "url": "https://choosealicense.com/",
     "data": "https://github.com/github/choosealicense.com",
     "license": "CC-BY-3.0",
     "gives": "permissions, conditions, limitations, description, notable projects"},
    {"name": "ScanCode LicenseDB", "url": "https://scancode-licensedb.aboutcode.org/",
     "data": "https://github.com/nexB/scancode-toolkit",
     "license": "CC-BY-4.0 (data)",
     "gives": "licence category, steward, homepage"},
]

# The guide's own pages, and which licences each explains.  Listed rather than
# globbed: concept pages mention identifiers in passing, and a card linking to a
# page that merely name-drops it is a link that wastes somebody's click.
LICENCE_PAGES = [
    "licenses/permissive/mit.md", "licenses/permissive/apache-2.md",
    "licenses/permissive/bsd.md", "licenses/copyleft/gpl.md",
    "licenses/copyleft/lgpl.md", "licenses/copyleft/mpl.md",
    "licenses/copyleft/epl.md", "licenses/other/agpl.md",
    "licenses/other/public-domain.md", "licenses/other/source-available.md",
    "creative-commons/cc0.md", "creative-commons/cc-by.md",
    "creative-commons/cc-by-sa.md", "creative-commons/cc-by-nc.md",
    "creative-commons/cc-by-nd.md",
]

# Headings that are page furniture, never a licence name.  Without this, a page
# using `## At a Glance` (rather than `###`) produces a card titled "At a
# Glance", which is how the AGPL card was born wrong on the first pass.
NOT_A_LICENCE_HEADING = {
    "at a glance", "what it allows", "what it requires", "what it prohibits",
    "the full text", "key terms", "when to use", "notable projects",
    "the license", "full text", "summary",
}


def fetch(url: str, name: str, *, offline: bool) -> str:
    CACHE.mkdir(parents=True, exist_ok=True)
    hit = CACHE / name
    if hit.exists():
        return hit.read_text(encoding="utf-8")
    if offline:
        raise RuntimeError(f"--offline and no cached copy of {name}")
    req = urllib.request.Request(url, headers={"User-Agent": "licence-card-catalog"})
    with urllib.request.urlopen(req, timeout=45) as r:          # noqa: S310 — pinned https
        text = r.read().decode("utf-8")
    hit.write_text(text, encoding="utf-8")
    return text


def slugify(text: str) -> str:
    """The anchor MkDocs generates for a heading — python-markdown's default."""
    s = re.sub(r"[^\w\s-]", "", text.strip().lower())
    return re.sub(r"[-\s]+", "-", s).strip("-")


def guide_index() -> dict[str, dict]:
    """SPDX id -> where in the guide it is explained.

    A lumped page (`bsd.md` covers four BSD variants) yields one entry per
    identifier, each anchored at its own heading.  That is the whole reason the
    catalog can be per-licence while the prose stays per-reading: splitting
    those pages later is a one-field change, not a re-link.
    """
    out: dict[str, dict] = {}

    def record(spdx_raw: str, rel: str, current: str | None, h1: str) -> None:
        # One cell can name several ids ("AGPL-3.0-only / AGPL-3.0-or-later").
        # Each gets its own entry — they are separate identifiers and a dataset
        # carries exactly one of them.
        for spdx in [s.strip() for s in re.split(r"[/,]| or ", spdx_raw) if s.strip()]:
            if not re.match(r"^[A-Za-z0-9][A-Za-z0-9.+-]*$", spdx):
                continue          # prose, not an identifier
            out.setdefault(spdx, {
                "page": rel,
                "anchor": slugify(current) if current else "",
                "section": current or h1,
            })

    for rel in LICENCE_PAGES:
        lines = (DOCS / rel).read_text(encoding="utf-8").splitlines()
        h1 = next((l[2:].strip() for l in lines if l.startswith("# ")), rel)
        current: str | None = None
        # Set when a table declares SPDX Identifier as a COLUMN rather than a
        # row — `gpl.md` and `lgpl.md` list their four variants that way, which
        # is why those eight identifiers were missing on the first pass.
        col_idx: int | None = None
        for line in lines:
            if line.startswith("## ") and not line.startswith("###"):
                head = line[3:].strip()
                current = None if head.lower() in NOT_A_LICENCE_HEADING else head
                col_idx = None

            # The inline form: `**SPDX Identifier:** \`EPL-2.0\``
            m = re.match(r"^\*\*SPDX Identifiers?:?\*\*:?\s*`?([^`\n]+)`?\s*$", line.strip())
            if m:
                record(m.group(1), rel, current, h1)
                continue

            if not line.lstrip().startswith("|"):
                col_idx = None
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            first = cells[0].replace("*", "").strip().lower()

            # THE KEY/VALUE FORM, and the match must be EXACT.  `in` matched the
            # header row of a comparison table whose second column was titled
            # "SPDX Identifier", and duly emitted a licence card named "SPDX
            # Identifier" — a card with a source for nothing.
            if first == "spdx identifier":
                record(cells[1].replace("`", "").strip(), rel, current, h1)
                continue

            # The column form: remember which column, then read the rows under it.
            if any(c.replace("*", "").strip().lower() == "spdx identifier"
                   for c in cells):
                col_idx = next(i for i, c in enumerate(cells)
                               if c.replace("*", "").strip().lower() == "spdx identifier")
                continue
            if col_idx is not None and len(cells) > col_idx:
                if set(cells[col_idx]) <= {"-", ":", " "}:
                    continue      # the markdown separator row
                record(cells[col_idx].replace("`", "").strip(), rel, current, h1)
    return out


def parse_front_matter(text: str) -> dict:
    """choosealicense entries are Jekyll files: YAML front matter, then the text."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    import yaml
    return yaml.safe_load(m.group(1)) or {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="-")
    ap.add_argument("--base-url", default="",
                    help="public URL of the guide, for explained_in links")
    ap.add_argument("--offline", action="store_true",
                    help="use only the download cache; fail rather than fetch")
    args = ap.parse_args()

    try:
        import yaml
    except ImportError:
        print("PyYAML is required", file=sys.stderr)
        return 1

    spdx_all = json.loads(fetch(SPDX_URL, "spdx-licenses.json", offline=args.offline))
    spdx_by_id = {l["licenseId"]: l for l in spdx_all["licenses"]}

    cal_index = json.loads(fetch(CAL_INDEX, "cal-index.json", offline=args.offline))
    cal_keys = [e["name"][:-4] for e in cal_index if e["name"].endswith(".txt")]

    # ScanCode's spdx -> its own key map, read from its index rather than
    # guessed.  2,733 entries; one fetch instead of one wrong guess per licence.
    sc_index = json.loads(fetch(SCANCODE_INDEX, "sc-index.json", offline=args.offline))
    sc_by_spdx = {e["spdx_license_key"]: e["license_key"] for e in sc_index
                  if e.get("spdx_license_key") and e.get("license_key")}

    guide = guide_index()

    cards: list[dict] = []
    unmatched_guide: list[str] = []
    no_scancode: list[str] = []

    # THE SPINE IS choosealicense's SET, widened by whatever our guide covers.
    # SPDX's full 733 is the identifier authority but not a shelf: nobody flips
    # through Zope-1.1 and NASA-1.3.  "What GitHub considers worth offering,
    # plus what we bothered to write about" is a defensible reading of "major",
    # and it is stated here rather than left as a mystery cut-off.
    wanted: dict[str, str | None] = {}
    for key in cal_keys:
        fm = parse_front_matter(fetch(CAL_RAW.format(key), f"cal-{key}.txt",
                                      offline=args.offline))
        sid = fm.get("spdx-id")
        if sid:
            wanted[sid] = key
    for sid in guide:
        wanted.setdefault(sid, None)

    for spdx in sorted(wanted, key=str.lower):
        cal_key = wanted[spdx]
        card: dict = {"spdx": spdx}

        # ---- SPDX: the identifier authority --------------------------------
        s = spdx_by_id.get(spdx)
        if s:
            card["name"] = s["name"]
            card["osi_approved"] = bool(s.get("isOsiApproved"))
            card["fsf_libre"] = bool(s.get("isFsfLibre"))
            if s.get("isDeprecatedLicenseId"):
                # Loud, because a deprecated identifier in a dataset's metadata
                # is a real finding — it means the record predates a rename.
                card["deprecated"] = True
                # SPDX split the ambiguous ids in 2018: `GPL-3.0` became
                # `GPL-3.0-only` / `GPL-3.0-or-later`, because "GPL-3.0" never
                # said whether the "or later" clause applied — which is the
                # whole question. Asserted only when the successor actually
                # exists in the list, so this is a lookup and not a guess.
                if f"{spdx}-only" in spdx_by_id:
                    card["superseded_by"] = [f"{spdx}-only", f"{spdx}-or-later"]
            card["reference"] = s.get("reference", "")
        else:
            # An id our guide uses that SPDX does not know is either a typo or a
            # non-SPDX identifier. Either way, say so rather than emit a card
            # that looks as authoritative as the ones with a source behind them.
            card["spdx_unknown"] = True
            unmatched_guide.append(spdx)

        # ---- choosealicense: the card fields -------------------------------
        if cal_key:
            fm = parse_front_matter(fetch(CAL_RAW.format(cal_key), f"cal-{cal_key}.txt",
                                          offline=args.offline))
            card["summary"] = (fm.get("description") or "").strip()
            card["allows"] = fm.get("permissions") or []
            card["requires"] = fm.get("conditions") or []
            card["prohibits"] = fm.get("limitations") or []
            if fm.get("using"):
                card["used_by"] = list(fm["using"])[:5]
            card["how_to_apply"] = (fm.get("how") or "").strip()

        # ---- ScanCode: the category axis -----------------------------------
        # KEYED THROUGH ScanCode's OWN INDEX, not by lowercasing the SPDX id.
        # Its keys are its own vocabulary — BSD-3-Clause is `bsd-new`, 0BSD is
        # `bsd-zero`, WTFPL is `wtfpl-2.0` — so guessing the key silently lost
        # the category for eleven licences, including every BSD variant.
        sc_key = sc_by_spdx.get(spdx)
        if sc_key:
            try:
                sc = json.loads(fetch(SCANCODE.format(sc_key), f"sc-{sc_key}.json",
                                      offline=args.offline))
                card["category"] = sc.get("category", "")
                if sc.get("owner"):
                    card["steward"] = sc["owner"]
            except Exception:  # noqa: BLE001 — a missing entry is a gap, not a failure
                no_scancode.append(spdx)
        elif not card.get("deprecated"):
            no_scancode.append(spdx)

        # ---- ours: the judgement, which is the only field we author ---------
        g = guide.get(spdx)
        if g:
            url = re.sub(r"\.md$", "/", g["page"])
            url = re.sub(r"(?:^|/)index/$", "/", url)
            card["explained_in"] = {
                "page": g["page"],
                "anchor": g["anchor"],
                "section": g["section"],
                "url": (args.base_url.rstrip("/") + "/" + url.lstrip("/")
                        + (f"#{g['anchor']}" if g["anchor"] else ""))
                if args.base_url else "",
            }

        # ---- the slot the platform fills later ------------------------------
        # Declared empty rather than absent: "no datasets here carry this" and
        # "we never looked" are different answers, and a reader of the card
        # deserves to be able to tell them apart once this is wired.
        card["holdings"] = None

        cards.append(card)

    doc = {
        "_generated_by": "scripts/build-card-catalog.py (open-source-licensing-guide)",
        "_spdx_list_version": spdx_all.get("licenseListVersion", ""),
        "_note": ("One card per SPDX identifier.  Every factual field is joined "
                  "from a public source (see _sources); the only field this "
                  "project authors is `explained_in`, which points at the "
                  "guide's own prose.  `holdings` is a slot for the platform to "
                  "fill with datasets carrying this licence — null means not "
                  "yet wired, which is not the same as zero."),
        "_sources": SOURCES,
        "_gaps": {
            "not_in_spdx": unmatched_guide,
            "no_scancode_entry": no_scancode,
        },
        "licenses": cards,
    }
    text = yaml.safe_dump(doc, sort_keys=False, width=92, allow_unicode=True)
    if args.out == "-":
        print(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"✓ {len(cards)} cards → {args.out}", file=sys.stderr)
        print(f"  SPDX list {doc['_spdx_list_version']}; "
              f"{sum(1 for c in cards if c.get('explained_in'))} link into the guide",
              file=sys.stderr)
        if unmatched_guide:
            print(f"  ! not in SPDX: {', '.join(unmatched_guide)}", file=sys.stderr)
        if no_scancode:
            print(f"  ! no ScanCode entry: {', '.join(no_scancode)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
