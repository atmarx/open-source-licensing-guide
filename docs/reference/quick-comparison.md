# Quick Comparison

A side-by-side reference for common open source licenses.

## Software Licenses

### Permissive Licenses

| | MIT | Apache 2.0 | BSD 3-Clause |
|---|:---:|:---:|:---:|
| **Commercial use** | :material-check: | :material-check: | :material-check: |
| **Modification** | :material-check: | :material-check: | :material-check: |
| **Distribution** | :material-check: | :material-check: | :material-check: |
| **Private use** | :material-check: | :material-check: | :material-check: |
| **Patent grant** | :material-close: | :material-check: | :material-close: |
| **Copyleft** | :material-close: | :material-close: | :material-close: |
| **Must include license** | :material-check: | :material-check: | :material-check: |
| **Must include copyright** | :material-check: | :material-check: | :material-check: |
| **State changes** | :material-close: | :material-check: | :material-close: |
| **Include NOTICE** | :material-close: | :material-check: | :material-close: |

### Copyleft Licenses

| | GPL v3 | LGPL v3 | MPL 2.0 | AGPL v3 |
|---|:---:|:---:|:---:|:---:|
| **Commercial use** | :material-check: | :material-check: | :material-check: | :material-check: |
| **Modification** | :material-check: | :material-check: | :material-check: | :material-check: |
| **Distribution** | :material-check: | :material-check: | :material-check: | :material-check: |
| **Private use** | :material-check: | :material-check: | :material-check: | :material-check: |
| **Patent grant** | :material-check: | :material-check: | :material-check: | :material-check: |
| **Copyleft scope** | Whole work | Library only | Modified files | Whole work + network |
| **Disclose source** | :material-check: | Library only | Modified files | :material-check: |
| **Same license** | :material-check: | For library | For MPL files | :material-check: |
| **Network use trigger** | :material-close: | :material-close: | :material-close: | :material-check: |

### Public Domain

| | CC0 | Unlicense | 0BSD |
|---|:---:|:---:|:---:|
| **Commercial use** | :material-check: | :material-check: | :material-check: |
| **Modification** | :material-check: | :material-check: | :material-check: |
| **Distribution** | :material-check: | :material-check: | :material-check: |
| **Private use** | :material-check: | :material-check: | :material-check: |
| **Attribution required** | :material-close: | :material-close: | :material-close: |
| **Include license** | :material-close: | :material-close: | :material-close: |
| **Any conditions** | :material-close: | :material-close: | :material-close: |

---

## Creative Commons Licenses

| | CC0 | CC BY | CC BY-SA | CC BY-NC | CC BY-ND | CC BY-NC-ND |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Commercial use** | :material-check: | :material-check: | :material-check: | :material-close: | :material-check: | :material-close: |
| **Modification** | :material-check: | :material-check: | :material-check: | :material-check: | :material-close: | :material-close: |
| **Distribution** | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |
| **Private use** | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |
| **Attribution required** | :material-close: | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |
| **ShareAlike** | :material-close: | :material-close: | :material-check: | :material-close: | — | — |
| **Free Culture approved** | :material-check: | :material-check: | :material-check: | :material-close: | :material-close: | :material-close: |

---

## Compatibility Matrix

Can code under License A be combined with code under License B?

| Into ► | MIT | Apache 2.0 | GPL v2 | GPL v3 | LGPL | MPL 2.0 |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|
| **MIT** | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |
| **Apache 2.0** | :material-check: | :material-check: | :material-close: | :material-check: | :material-check: | :material-check: |
| **GPL v2** | :material-close: | :material-close: | :material-check: | :material-close: | :material-close: | :material-close: |
| **GPL v3** | :material-close: | :material-close: | :material-close: | :material-check: | :material-close: | :material-check: |
| **LGPL v3** | :material-close: | :material-close: | :material-close: | :material-check: | :material-check: | :material-check: |
| **MPL 2.0** | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: | :material-check: |

:material-check: = License A code can go into License B project

Note: "GPL v2 or later" has different compatibility than "GPL v2 only."

---

## Quick Selection Guide

| If you want... | Choose |
|---------------|--------|
| Maximum adoption | MIT |
| Patent protection | Apache 2.0 |
| Derivatives stay open (strong) | GPL v3 |
| Derivatives stay open (weak) | MPL 2.0 or LGPL |
| Network use triggers copyleft | AGPL |
| No restrictions at all | CC0 or Unlicense |
| Credit but no other requirements | CC BY |
| Data sharing | CC0 |
| Documentation | CC BY or CC BY-SA |

---

## SPDX Identifiers

| License | SPDX ID |
|---------|---------|
| MIT License | `MIT` |
| Apache 2.0 | `Apache-2.0` |
| BSD 2-Clause | `BSD-2-Clause` |
| BSD 3-Clause | `BSD-3-Clause` |
| GPL v2 only | `GPL-2.0-only` |
| GPL v2 or later | `GPL-2.0-or-later` |
| GPL v3 only | `GPL-3.0-only` |
| GPL v3 or later | `GPL-3.0-or-later` |
| LGPL v2.1 | `LGPL-2.1-only` |
| LGPL v3 | `LGPL-3.0-only` |
| MPL 2.0 | `MPL-2.0` |
| AGPL v3 | `AGPL-3.0-only` |
| CC0 1.0 | `CC0-1.0` |
| CC BY 4.0 | `CC-BY-4.0` |
| CC BY-SA 4.0 | `CC-BY-SA-4.0` |
| Unlicense | `Unlicense` |
