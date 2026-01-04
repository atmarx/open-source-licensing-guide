# GNU Lesser General Public License (LGPL)

The LGPL is a "weak copyleft" license designed for libraries. It allows proprietary software to use LGPL libraries without becoming GPL, while still requiring changes to the library itself to be shared.

## Versions

| Version | SPDX Identifier | Notes |
|---------|----------------|-------|
| LGPL v2.1 | `LGPL-2.1-only` / `LGPL-2.1-or-later` | Standalone license text |
| LGPL v3 | `LGPL-3.0-only` / `LGPL-3.0-or-later` | GPL v3 + additional permissions |

LGPL v3 is structured as GPL v3 with added permissions, rather than a separate license.

## At a Glance

| Attribute | Value |
|-----------|-------|
| **Type** | Weak copyleft |
| **Patent Grant** | Yes (v3) |
| **Scope** | Library modifications only |
| **Distribution Trigger** | Yes |

## What It Allows

- :material-check: Commercial use
- :material-check: Modification
- :material-check: Distribution
- :material-check: Private use
- :material-check: Proprietary software can link to LGPL libraries

## What It Requires

- :material-alert: Disclose source for the library (when distributing)
- :material-alert: License library modifications under LGPL
- :material-alert: Allow library replacement (for dynamic linking)
- :material-alert: Include copyright and license

## What It Prohibits

- :material-close: Holding authors liable
- :material-close: Restricting library replacement

## The Core Concept

LGPL creates a boundary around the library:

```
┌────────────────────────────────────────┐
│          Your Application              │
│         (any license you want)         │
│                                        │
│    ┌────────────────────────────┐      │
│    │      LGPL Library          │      │
│    │  (modifications stay LGPL) │      │
│    └────────────────────────────┘      │
│                                        │
└────────────────────────────────────────┘
```

- Modifications to the LGPL library must be LGPL
- Your application using the library can be any license
- You must allow users to replace the library with modified versions

## Static vs Dynamic Linking

LGPL distinguishes between:

### Dynamic Linking (typical case)
Your application loads the library at runtime. Users can replace the library file with a modified version. This is the intended use case.

**Requirements:**
- Include LGPL license text
- Provide source for the library (or offer to)
- Allow library replacement

### Static Linking
The library becomes part of your binary. Users cannot easily replace it.

**Additional requirements:**
- Provide object files or source for your application, sufficient for users to relink with a modified library

!!! note "The relinking requirement"
    This is LGPL's way of ensuring users can exercise their freedom to modify the library even when statically linked. You must provide enough for someone to rebuild with a modified library.

## When LGPL Makes Sense

The LGPL was created for a specific strategic purpose: encouraging adoption of free software libraries without "giving away" the copyleft advantage entirely.

### Use LGPL when:

- You're building a library that competes with proprietary alternatives
- You want proprietary software to adopt it (growing your ecosystem)
- You still want modifications to the library itself shared back

### Examples:

- **glibc (GNU C Library):** LGPL allows any software to use it
- **GTK:** LGPL allows proprietary applications with GTK interfaces
- **FFmpeg libraries:** LGPL components can be used in proprietary video software

## LGPL vs GPL for Libraries

| Consideration | GPL | LGPL |
|--------------|-----|------|
| Proprietary software can use | No | Yes |
| All improvements come back | Yes | Only to the library |
| Adoption by commercial users | Limited | Higher |
| Competitive pressure to open | Strong | Weaker |

Some projects choose GPL even for libraries to maximize pressure toward open source. Others choose LGPL to maximize reach.

## LGPL vs Permissive

If LGPL allows proprietary software to use the library anyway, why not just use MIT or Apache?

The key difference: LGPL still requires improvements to the library to be shared. With MIT, a company could improve your library and keep those improvements proprietary. With LGPL, they must share library modifications.

## Notable Projects Using LGPL

- GNU C Library (glibc)
- GTK
- Qt (dual-licensed)
- FFmpeg (some components)
- GNU Guile
- Hibernate
