# Choosing a License

Selecting a license is one of the most important decisions you'll make for your project. This guide helps you think through the considerations and arrive at the right choice.

## The Decision Framework

Start with these questions:

### 1. Is this software or creative work?

| Work Type | Consider |
|-----------|----------|
| Software (code) | MIT, Apache 2.0, GPL, MPL |
| Data or databases | CC0, CC BY, ODbL |
| Documentation | CC BY, CC BY-SA |
| Images, video, music | CC licenses |
| Mixed | Multiple licenses for different components |

!!! tip "Don't use Creative Commons for code"
    CC licenses don't address software-specific concerns like source code, compilation, and linking. Use software licenses for software.

### 2. What do you want to allow?

Be honest about what matters to you:

| Priority | Suggests |
|----------|----------|
| Maximum adoption | Permissive (MIT, Apache 2.0, CC BY) |
| Keep improvements open | Copyleft (GPL, CC BY-SA) |
| Prevent commercial exploitation | NC licenses (not open source) |
| No restrictions at all | CC0, Unlicense |

### 3. What community are you joining?

Ecosystem norms matter:

| Ecosystem | Common Licenses |
|-----------|-----------------|
| JavaScript/Node | MIT |
| Java/Enterprise | Apache 2.0 |
| Linux/GNU | GPL |
| Data science | MIT, Apache 2.0, CC0 for data |
| Academic | CC BY for papers, varied for code |
| Rust | MIT + Apache 2.0 (dual) |
| Go | BSD-3-Clause |

Matching your ecosystem reduces friction.

---

## The Flowchart

```
                    START
                      │
                      ▼
            ┌─────────────────┐
            │ Do you want     │
            │ attribution?    │
            └────────┬────────┘
                     │
           ┌─────────┴─────────┐
           │                   │
          No                  Yes
           │                   │
           ▼                   ▼
     ┌──────────┐    ┌─────────────────┐
     │ CC0 or   │    │ Should changes  │
     │ Unlicense│    │ stay open?      │
     └──────────┘    └────────┬────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   No                  Yes
                    │                   │
                    ▼                   ▼
         ┌──────────────────┐   ┌──────────────────┐
         │ Is patent        │   │ How viral        │
         │ protection       │   │ should it be?    │
         │ important?       │   └────────┬─────────┘
         └────────┬─────────┘            │
                  │              ┌───────┼───────┐
           ┌──────┴──────┐       │       │       │
           │             │       ▼       ▼       ▼
          No            Yes    Whole   Files   Library
           │             │     work    only    only
           ▼             ▼       │       │       │
        ┌─────┐    ┌──────────┐  ▼       ▼       ▼
        │ MIT │    │Apache 2.0│ GPL     MPL    LGPL
        └─────┘    └──────────┘
```

---

## Common Scenarios

### "I want people to use this without hassle"

**Choose: MIT**

MIT is simple, understood everywhere, and imposes minimal burden. It's the default choice for maximum adoption.

### "I want credit but don't care about contributions back"

**Choose: MIT or Apache 2.0**

Both require attribution. Apache 2.0 adds patent protection, which matters for larger projects or enterprise use.

### "I want improvements to come back to the community"

**Choose: GPL v3 or AGPL**

Strong copyleft ensures that public improvements must be shared. AGPL extends this to SaaS.

### "I'm building a library for wide use"

**Choose: MIT, Apache 2.0, or LGPL**

- MIT/Apache: Anyone can use without complexity
- LGPL: Proprietary use allowed, but library improvements must be shared

### "This is a web service that might be hosted by others"

**Choose: AGPL**

If you want competitors to share improvements when they host your code, AGPL closes the SaaS loophole.

### "I'm publishing research data"

**Choose: CC0**

Maximum reuse for data. Academic citation norms provide attribution even without legal requirement.

### "I'm writing documentation"

**Choose: CC BY or CC BY-SA**

- CC BY: Others can use freely, must credit
- CC BY-SA: Others must keep their adaptations open

### "I want to dual-license for business"

**Choose: GPL + commercial, or AGPL + commercial**

Open source under copyleft for community, sell commercial licenses to companies that want proprietary use.

---

## License Compatibility Considerations

If your project incorporates existing code, you must comply with its license:

| Your New Code | Can Include | Cannot Include |
|---------------|-------------|----------------|
| MIT | MIT, BSD, CC0 | GPL (without becoming GPL) |
| Apache 2.0 | MIT, BSD, CC0 | GPL v2 |
| GPL v3 | MIT, BSD, Apache 2.0, LGPL, GPL v2 | Differently-copylefted code |
| Proprietary | MIT, BSD, Apache 2.0, LGPL (carefully) | GPL, AGPL |

When in doubt, check the specific licenses involved.

---

## How to Apply a License

### For software:

1. Add a `LICENSE` or `LICENSE.txt` file with the full license text
2. Add a copyright notice to the top of source files (optional but common)
3. If using Apache 2.0, consider adding a `NOTICE` file

### For creative works:

1. Include license information with the work
2. Use CC license badges where visible
3. Include license in metadata (EXIF for images, etc.)

### Template for source files:

```
// SPDX-License-Identifier: MIT
// Copyright (c) 2026 Your Name
```

SPDX identifiers are machine-readable and increasingly standard.

---

## What If I Change My Mind?

### You can always add permissions

You can release future versions under a more permissive license. This doesn't affect existing releases.

### You can't revoke past permissions

Once you've licensed something, recipients have those rights. You can't take them back.

### Relicensing requires consent

If others have contributed, relicensing typically requires agreement from all contributors. This is why Contributor License Agreements (CLAs) exist.

---

## Final Advice

When in doubt:

1. **For software:** Start with MIT unless you have specific reasons for something else
2. **For data:** Use CC0
3. **For documentation:** Use CC BY
4. **Always include a LICENSE file**—ambiguity helps no one
