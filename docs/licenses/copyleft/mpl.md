# Mozilla Public License 2.0 (MPL)

The MPL is a weak copyleft license that operates at the file level. It requires modifications to MPL files to be shared, but allows combining with other code under different licenses—including proprietary licenses.

## At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `MPL-2.0` |
| **Type** | Weak copyleft (file-level) |
| **Patent Grant** | Yes |
| **Scope** | Modified files only |
| **Distribution Trigger** | Yes |

## What It Allows

- :material-check: Commercial use
- :material-check: Modification
- :material-check: Distribution
- :material-check: Private use
- :material-check: Combining with other licensed code

## What It Requires

- :material-alert: Disclose source for modified MPL files
- :material-alert: License modifications to MPL files under MPL
- :material-alert: Include copyright and license

## What It Prohibits

- :material-close: Holding authors liable
- :material-close: Using trademarks

## File-Level Copyleft

The MPL's defining characteristic is its scope. Unlike GPL (entire work) or LGPL (library), MPL applies only to individual files:

```
┌─────────────────────────────────────────┐
│            Your Project                 │
├─────────────────────────────────────────┤
│  your_code.js        →  Any license     │
│  modified_mpl.js     →  Must be MPL     │
│  new_mpl_file.js     →  MPL if derived  │
│  your_other_code.js  →  Any license     │
│  unmodified_mpl.js   →  MPL (unchanged) │
└─────────────────────────────────────────┘
```

**If you modify an MPL file:** That file must remain MPL and source must be provided.

**If you add new files:** They can be any license, unless they're modifications of existing MPL files.

**If you use MPL files unchanged:** Just keep the license notices.

## Comparison with Other Copyleft

| License | Copyleft Scope | Practical Effect |
|---------|---------------|------------------|
| GPL | Entire combined work | Everything becomes GPL |
| LGPL | Library boundary | Application can be proprietary |
| MPL | Individual files | New files can be proprietary |

MPL is the least viral copyleft option while still requiring some sharing.

## Patent Grant

Like Apache 2.0, MPL 2.0 includes a patent grant:

- Contributors grant patent licenses for their contributions
- Patent retaliation terminates your rights

This makes MPL attractive for enterprise use where patent concerns matter.

## Compatibility

MPL 2.0 was specifically designed for license compatibility:

### Compatible with GPL
MPL 2.0 includes a compatibility clause allowing MPL code to be combined with GPL code. The combined work can be distributed under GPL. This is a one-way valve—once combined, that copy is GPL.

### Combining with proprietary code
You can combine MPL files with proprietary code. The MPL files remain MPL; your files remain your license.

### "Larger Work" provisions
MPL explicitly addresses combining MPL code with differently-licensed code in a "Larger Work," making the boundaries clear.

## MPL in Practice

### What you must do:

1. Keep license and copyright notices in MPL files
2. If you modify MPL files, provide source for those modifications
3. If you distribute, make MPL source available

### What you may do:

1. Combine MPL files with proprietary files
2. Distribute binary-only for your own files
3. Use for any purpose including commercial

## When to Use MPL

MPL is a good choice when:

- You want copyleft for your core files but flexibility for extensions
- You want to encourage contributions while allowing commercial adoption
- You care about patent protection
- You want compatibility with both GPL and proprietary projects

### Example use case:

A company releases a library under MPL. Other companies can:

- Use the library in proprietary products
- Add proprietary files around it
- But must share any fixes or improvements to the core library files

## MPL 1.1 vs MPL 2.0

MPL 2.0 (2012) was a significant update:

- Simplified and shortened
- Added GPL compatibility clause
- Modernized patent language
- Easier to understand and apply

Use MPL 2.0 for new projects. MPL 1.1 had compatibility issues with GPL.

## Notable Projects Using MPL

- Firefox
- Thunderbird
- LibreOffice (dual-licensed with LGPL)
- Syncthing
- Terraform (before license change)
- Hashicorp Consul (before license change)
