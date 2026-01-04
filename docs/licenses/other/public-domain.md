# Public Domain Dedications

Public domain means no copyright restrictions—anyone can use the work for any purpose without permission or attribution. For software, this is achieved through explicit dedications since simply declaring something "public domain" has legal complexities.

## The Challenge

"I dedicate this to the public domain" seems simple, but:

- Not all legal systems recognize voluntary public domain dedication
- Some countries don't allow waiving moral rights
- "Public domain" means different things in different jurisdictions

To address this, specialized legal tools exist.

---

## The Unlicense

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `Unlicense` |
| **Type** | Public domain dedication |
| **Requirements** | None |
| **Attribution** | Not required |

### Key Terms

The Unlicense has two parts:

1. **Public domain dedication:** Waives all copyright interest
2. **Fallback license:** For jurisdictions where waiver isn't possible, grants permission equivalent to public domain

```text
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.
```

### No Attribution Required

Unlike MIT or BSD, the Unlicense requires nothing. You can:

- Use the code without credit
- Remove the license text
- Claim you wrote it (ethically questionable but legally allowed)

### When to Use Unlicense

- For code snippets and small utilities
- When you genuinely don't care about credit
- When maximum adoption with zero friction is the goal
- When compatibility with everything is essential

---

## CC0 1.0 Universal

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `CC0-1.0` |
| **Type** | Public domain dedication |
| **Requirements** | None |
| **Attribution** | Not required |

### Key Differences from Unlicense

CC0 is maintained by Creative Commons and has:

- More thorough legal drafting
- Explicit handling of international jurisdictions
- Clearer fallback license provisions
- Better known for non-software works

### The Three-Layer Approach

CC0 attempts dedication in order:

1. **Waiver:** Completely waive all copyright
2. **License:** If waiver doesn't work, grant unconditional license
3. **Public License Fallback:** If that doesn't work, provide a permissive license

### When to Use CC0

- For data, datasets, and databases
- When releasing research artifacts
- When international legal coverage matters
- When you want the Creative Commons brand recognition

---

## 0BSD (Zero-Clause BSD)

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `0BSD` |
| **Type** | Permissive (public domain equivalent) |
| **Requirements** | None |
| **Attribution** | Not required |

### Why It Exists

Some organizations are uncomfortable with "public domain dedication" language but accept traditional license formats. 0BSD provides public-domain-equivalent terms using the familiar BSD license structure.

```text
Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES...
```

---

## Comparison

| License | Legal Complexity | Fallback Provisions | Best For |
|---------|-----------------|---------------------|----------|
| Unlicense | Simple | Basic | Small projects, quick releases |
| CC0 | Thorough | Comprehensive | Data, research, international use |
| 0BSD | Minimal | None (BSD structure) | Organizations wary of PD language |

## When NOT to Use Public Domain

Consider whether you really want zero requirements:

- **No attribution:** Your contribution might be forgotten
- **No copyleft:** Companies can use and not contribute back
- **No patent protection:** Unlike Apache 2.0, no patent grant

If you want maximum freedom but still care about credit, MIT requires attribution and is nearly as permissive.

## Notable Projects

### Unlicense
- youtube-dl (originally)
- Various small utilities

### CC0
- SQLite (has its own dedication, but CC0-like)
- Many datasets and research artifacts

### 0BSD
- Used in some corporate environments
- Toybox
