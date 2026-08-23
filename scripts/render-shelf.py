#!/usr/bin/env python3
"""render-shelf.py — turn the card catalog into a shelf you can flip through.

One page per licence, plus an index that lists every one of them.  The reader
picks a licence and lands on its card: what it permits, what it obliges, whether
OSI and the FSF both bless it, who stewards it, where the long version lives —
and a slot for the datasets on this system that carry it.

## Why generated and not written

61 cards is past the number a person keeps consistent by hand, and the facts
underneath change: SPDX deprecates an identifier, choosealicense revises a
description, our own guide gains a page. A generated shelf re-renders; a
hand-written one drifts and nobody notices which cell went stale.

So these pages are OUTPUT.  Editing one is editing a build artifact — the fix
belongs in the catalog, or upstream in the source it came from.

## The holdings slot

`holdings: null` on every card means *not wired yet*, which is deliberately not
the same as zero.  When the platform can answer "which datasets here carry
BSD-3-Clause", that number lands on this page and the card stops being a
reference and starts being an index into our own shelves.  Until then the page
says so plainly rather than showing a confident 0.

Usage:
    scripts/render-shelf.py --catalog licenses.yaml --out <corpus>/docs/library/licenses
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# choosealicense's vocabulary is machine-shaped (`commercial-use`,
# `disclose-source`).  A shelf is read by humans, so each term gets a sentence.
# Keys not listed here fall back to the raw token rather than being dropped — a
# new term upstream should look ugly, not disappear.
TERMS = {
    "commercial-use": "Use it commercially",
    "modifications": "Modify it",
    "distribution": "Distribute it",
    "private-use": "Use it privately",
    "patent-use": "Use contributors' patents",
    "include-copyright": "Keep the copyright notice",
    "include-copyright--source": "Keep the copyright notice (source form)",
    "document-changes": "State what you changed",
    "disclose-source": "Publish your source",
    "network-use-disclose": "Publish source even for network use",
    "same-license": "License your version the same way",
    "same-license--file": "Same license, for modified files",
    "same-license--library": "Same license, for the library itself",
    "liability": "No liability",
    "warranty": "No warranty",
    "trademark-use": "No trademark rights",
    "patent-use--limited": "No patent grant",
}

CATEGORY_ORDER = ["Permissive", "Copyleft", "Copyleft Limited", "Public Domain",
                  "Source-available", "Proprietary Free", "Free Restricted",
                  "Commercial", "Unstated License", ""]


def human(term: str) -> str:
    return TERMS.get(term, term.replace("-", " ").capitalize())


def slug(spdx: str) -> str:
    """A filename for an identifier.  Lowercased with dots flattened, because
    `Apache-2.0.md` reads as a file with a `.0` extension to half the tools that
    will ever touch this directory."""
    return re.sub(r"[^a-z0-9]+", "-", spdx.lower()).strip("-")


CAL_LINK = re.compile(r'<a href="/licenses/([^"/]+)/?">(.*?)</a>', re.S)


def relink(text: str, cal_to_spdx: dict[str, str]) -> str:
    """Point choosealicense's internal links at our own cards."""
    def sub(m: re.Match) -> str:
        spdx = cal_to_spdx.get(m.group(1))
        label = m.group(2)
        return f"[{label}]({slug(spdx)}.md)" if spdx else label
    return CAL_LINK.sub(sub, text)


def card_page(c: dict, cal_to_spdx: dict[str, str]) -> str:
    spdx = c["spdx"]
    name = c.get("name") or spdx
    out = [f"# {name}", ""]

    if c.get("deprecated"):
        sup = c.get("superseded_by") or []
        out += ["!!! warning \"Deprecated identifier\"",
                f"    SPDX no longer uses `{spdx}`. It was ambiguous about whether",
                "    the \"or later\" clause applies — which is usually the exact",
                "    question somebody is asking. Use "
                + " or ".join(f"`{s}`" for s in sup) + " instead."
                if sup else "    SPDX no longer uses this identifier.", ""]

    if c.get("summary"):
        out += [relink(c["summary"], cal_to_spdx), ""]

    out += ["## At a glance", "",
            "| | |", "|---|---|",
            f"| **SPDX identifier** | `{spdx}` |"]
    if c.get("category"):
        out.append(f"| **Category** | {c['category']} |")
    out.append(f"| **OSI approved** | {'Yes' if c.get('osi_approved') else 'No'} |")
    out.append(f"| **FSF free/libre** | {'Yes' if c.get('fsf_libre') else 'No'} |")
    if c.get("steward"):
        out.append(f"| **Steward** | {c['steward']} |")
    if c.get("reference"):
        out.append(f"| **Full text** | [spdx.org]({c['reference']}) |")
    out.append("")

    for key, head in (("allows", "You may"), ("requires", "You must"),
                      ("prohibits", "Limitations")):
        if c.get(key):
            out += [f"## {head}", ""]
            out += [f"- {human(t)}" for t in c[key]]
            out.append("")

    if c.get("used_by"):
        out += ["## Used by", "",
                ", ".join(str(u) for u in c["used_by"]), ""]

    if c.get("explained_in") and c["explained_in"].get("url"):
        e = c["explained_in"]
        out += ["## The long version", "",
                f"[{e.get('section') or 'Read the guide'}]({e['url']}) — the story, "
                "the arguments, and what went wrong for people who picked badly.",
                ""]

    out += ["## Datasets here under this license", ""]
    if c.get("holdings") is None:
        out += ["*Not yet wired.* When the platform can answer this, the count "
                "lands here. It is deliberately blank rather than `0` — nobody "
                "has looked yet, and those are different answers.", ""]
    else:
        out += [f"{c['holdings']} dataset(s).", ""]

    out += ["---", "",
            "*This page is generated from a licence catalog joined from the SPDX "
            "License List, choosealicense.com and ScanCode LicenseDB. Corrections "
            "go upstream, not here.*", ""]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--out", required=True, help="directory for the shelf pages")
    ap.add_argument("--subpath", default="",
                    help="the shelf's path under docs/, for the nav block")
    args = ap.parse_args()

    import yaml
    doc = yaml.safe_load(Path(args.catalog).read_text(encoding="utf-8"))
    cards = doc["licenses"]

    out = Path(args.out)
    # Wholesale, so a licence dropped from the catalog stops being served.
    if out.exists():
        for f in out.glob("*.md"):
            f.unlink()
    out.mkdir(parents=True, exist_ok=True)

    cal_to_spdx = {c["spdx"].lower(): c["spdx"] for c in cards}
    for c in cards:
        (out / f"{slug(c['spdx'])}.md").write_text(
            card_page(c, cal_to_spdx), encoding="utf-8")

    # ---- the index: every licence, grouped, with the axes worth scanning ----
    groups: dict[str, list[dict]] = {}
    for c in cards:
        groups.setdefault(c.get("category") or "", []).append(c)

    idx = ["# The licence shelf", "",
           f"Every licence this system knows about — **{len(cards)}** of them, "
           "one card each. Pick one to see what it permits, what it obliges, and "
           "where the long version lives.", "",
           "!!! info \"Where these facts come from\"",
           "    Joined from the "
           "[SPDX License List](https://spdx.org/licenses/) (identifiers, OSI and "
           "FSF status), [choosealicense.com](https://choosealicense.com/) "
           "(permissions, conditions, limitations) and "
           "[ScanCode LicenseDB](https://scancode-licensedb.aboutcode.org/) "
           "(category, steward). Nothing here is written from memory — licence "
           "facts are the last thing to guess at.", ""]

    for cat in sorted(groups, key=lambda c: (CATEGORY_ORDER.index(c)
                                             if c in CATEGORY_ORDER else 99, c)):
        rows = sorted(groups[cat], key=lambda c: c["spdx"].lower())
        idx += [f"## {cat or 'Uncategorised'}", "",
                "| Licence | SPDX | OSI | FSF | |", "|---|---|:---:|:---:|---|"]
        for c in rows:
            mark = " ⚠️ deprecated" if c.get("deprecated") else ""
            guide = ""
            if c.get("explained_in") and c["explained_in"].get("url"):
                guide = f"[the long version]({c['explained_in']['url']})"
            idx.append(
                f"| [{c.get('name') or c['spdx']}]({slug(c['spdx'])}.md){mark} "
                f"| `{c['spdx']}` "
                f"| {'✅' if c.get('osi_approved') else '—'} "
                f"| {'✅' if c.get('fsf_libre') else '—'} | {guide} |")
        idx.append("")

    idx += ["## Sources", "", "| Source | Gives us | Licensed |", "|---|---|---|"]
    for s in doc.get("_sources", []):
        idx.append(f"| [{s['name']}]({s['url']}) | {s['gives']} | {s['license']} |")
    idx += ["", f"*SPDX License List version `{doc.get('_spdx_list_version','')}`. "
            "Generated — corrections go to the source, not to this page.*", ""]
    (out / "index.md").write_text("\n".join(idx), encoding="utf-8")

    print(f"✓ {len(cards)} cards + index → {out}")

    if args.subpath:
        print("\nnav block:\n")
        print(f"    - The Licence Shelf:")
        print(f"      - All Licences: {args.subpath}/index.md")
        for cat in sorted(groups, key=lambda c: (CATEGORY_ORDER.index(c)
                                                 if c in CATEGORY_ORDER else 99, c)):
            print(f"      - {cat or 'Uncategorised'}:")
            for c in sorted(groups[cat], key=lambda c: c["spdx"].lower()):
                title = (c.get("name") or c["spdx"]).replace('"', "'")
                print(f'        - "{title}": {args.subpath}/{slug(c["spdx"])}.md')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
