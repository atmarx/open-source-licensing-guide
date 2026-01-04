# Using Licensed Code

This guide explains how to comply with open source licenses when using code you didn't write. Getting this right protects you legally and respects the work of open source contributors.

## The Basic Rule

Every open source license grants you rights in exchange for complying with conditions. If you don't comply, you don't have permission to use the code—which means copyright infringement.

## Step 1: Identify the License

Before using any code:

1. **Look for LICENSE or COPYING files** in the repository root
2. **Check package metadata** (package.json, Cargo.toml, pom.xml, etc.)
3. **Look for SPDX identifiers** in source file headers
4. **Check the README** for license information

!!! warning "No license = no permission"
    If you can't find a license, you cannot legally use the code. GitHub visibility is not a license. Ask the author to add one.

## Step 2: Understand the License Type

| License Type | What You Must Do | Can Use in Proprietary Software? |
|--------------|-----------------|----------------------------------|
| Permissive (MIT, BSD, Apache) | Include copyright/license notice | Yes |
| Weak copyleft (LGPL, MPL) | Share modifications to the library | Yes, with care |
| Strong copyleft (GPL) | Share source for derivative work | No (unless open sourcing) |
| Public domain (CC0, Unlicense) | Nothing | Yes |

## Step 3: Comply with Requirements

### For MIT, BSD, Apache-licensed code:

1. **Preserve copyright notices** in source files
2. **Include the LICENSE file** in your distribution
3. **For Apache 2.0:** Also preserve NOTICE files
4. **For Apache 2.0:** Document changes you made

**Where to put notices:**

- In your repository's `LICENSE` or `THIRD-PARTY-NOTICES` file
- In an "About" or "Legal" section of your application
- In documentation for libraries

### For GPL/LGPL/AGPL code:

1. All of the above, plus:
2. **Make source available** to recipients of binaries
3. **License your derivative work** under the same terms (GPL)
4. **LGPL special:** Ensure users can replace the library

### For MPL code:

1. Preserve notices
2. **Share source for modified MPL files only**
3. Your other files can use any license

---

## Common Scenarios

### Using npm/pip/cargo packages

Package managers make this easy:

- Dependencies are installed, not distributed
- Your users install dependencies themselves
- You typically don't need to include all license files

But if you **bundle** dependencies (webpack, etc.):

- Include a notices file with license information
- Tools like `license-checker` (npm) or `pip-licenses` can generate these

### Using code snippets from Stack Overflow

Stack Overflow content is CC BY-SA 4.0:

- Requires attribution
- ShareAlike means derivatives should be similarly licensed
- For substantial code, this may conflict with your project's license

For small snippets, the practical risk is low, but technically you should:

- Credit the source
- Consider the license compatibility

### Vendoring dependencies

If you copy library source into your repository:

- Include the original LICENSE file
- Preserve copyright notices
- Treat it like any other included code

### Forking a project

When you fork:

- You must comply with the original license
- You inherit its license for the existing code
- You can choose your license for new files (if permissive original)
- You cannot relicense copyleft code

---

## License Compatibility

Can you combine code under different licenses? This matters when building on multiple projects.

### Generally Safe Combinations

```
                   Can flow into
                   ─────────────►
    ┌─────────────────────────────────────────┐
    │  CC0 ──► MIT ──► Apache 2.0 ──► GPL v3  │
    │   │       │          │            │     │
    │   └───────┴──────────┴────────────┘     │
    │         Less restrictive to more        │
    └─────────────────────────────────────────┘
```

Permissive licenses can generally be combined with anything.

### Problematic Combinations

| Combination | Problem |
|-------------|---------|
| GPL v2 + Apache 2.0 | Incompatible (use GPL v3) |
| GPL v2 + GPL v3 | Incompatible (use "v2 or later") |
| GPL + proprietary | Not allowed |
| Different copyleft licenses | Usually incompatible |

### When in Doubt

1. Check the FSF's license compatibility chart
2. Check SPDX's license exceptions
3. Consult legal counsel for complex situations

---

## Creating a THIRD-PARTY-NOTICES File

For projects with multiple dependencies, maintain a notices file:

```
THIRD-PARTY SOFTWARE NOTICES

This project includes software from the following third parties:

---

Library: express
Version: 4.18.2
License: MIT
Copyright (c) 2009-2014 TJ Holowaychuk <tj@vision-media.ca>
Copyright (c) 2013-2014 Roman Shtylman <shtylman+expressjs@gmail.com>
Copyright (c) 2014-2015 Douglas Christopher Wilson <doug@somethingdoug.com>

[Include full MIT license text]

---

Library: lodash
...
```

### Automating Notice Generation

- **npm:** `license-checker`, `legally`
- **Python:** `pip-licenses`
- **Rust:** `cargo-license`
- **Java:** `license-maven-plugin`
- **Go:** `go-licenses`

---

## Red Flags

Watch out for:

| Situation | Concern |
|-----------|---------|
| Missing LICENSE file | No permission to use |
| "All rights reserved" | Not open source |
| Unknown license text | May not be OSI-approved |
| SSPL, BSL, Commons Clause | Source-available, not open source |
| Multiple conflicting licenses | Needs careful analysis |
| No clear copyright owner | Hard to verify permissions |

---

## Best Practices

1. **Keep a record** of dependencies and their licenses
2. **Audit regularly** as dependencies change
3. **Automate checking** with license scanning tools
4. **When adding code manually,** include the license info immediately
5. **Document your license decisions** for future reference
6. **When in doubt, ask** the copyright holder or legal counsel
