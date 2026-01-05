# Attribution

Attribution—giving credit to creators—is required by almost every open source license. This guide explains how to do it correctly.

## Why Attribution Matters

<div class="grid cards two-column" markdown>

-   :material-gavel:{ .lg .middle } **Legal Requirement**

    ---

    Most licenses require it. Non-compliance is infringement.

-   :material-school:{ .lg .middle } **Academic Integrity**

    ---

    Citation norms exist for a reason. Give credit where it's due.

-   :material-handshake:{ .lg .middle } **Community Respect**

    ---

    Acknowledging work maintains goodwill and trust.

-   :material-source-branch:{ .lg .middle } **Provenance**

    ---

    Helps others trace origins and find upstream projects.

</div>

## What's Required

Different licenses require different things. Here's what to include:

### Minimum (MIT, BSD, Apache, CC BY)

| Element | Required | Example |
|---------|----------|---------|
| Copyright notice | Yes | Copyright (c) 2024 Jane Doe |
| License text or link | Yes | MIT License (full text or link) |
| Original author name | Usually | Jane Doe |

### Additional for Some Licenses

| License | Additional Requirement |
|---------|----------------------|
| Apache 2.0 | Preserve NOTICE file if present |
| Apache 2.0 | Note modifications made |
| GPL | Prominent program name, copyright, links |
| CC BY | Indicate if changes were made |
| CC BY | Link to license |
| CC BY | Don't imply endorsement |

---

## How to Provide Attribution

### In Source Code

Preserve existing copyright headers:

```python
# Copyright (c) 2024 Jane Doe
# SPDX-License-Identifier: MIT
```

Don't remove these when incorporating code.

### In Your LICENSE File

Create a section for third-party notices:

```
---

This project includes code from [ProjectName]:

  Copyright (c) 2024 Jane Doe
  Licensed under the MIT License
  https://github.com/janedoe/project
```

### In a THIRD-PARTY-NOTICES File

For projects with many dependencies:

```
THIRD-PARTY SOFTWARE NOTICES AND INFORMATION

This project incorporates components from the projects
listed below. The original copyright notices and license
terms are included below.

---

1. React (https://reactjs.org/)

   Copyright (c) Meta Platforms, Inc. and affiliates.

   MIT License

   [Full license text here]

---

2. lodash (https://lodash.com/)

   Copyright JS Foundation and other contributors

   MIT License

   [Full license text here]
```

### In Application UI

If distributing a binary application, include an "About" or "Legal" screen:

```
About MyApp

MyApp v1.0
Copyright (c) 2024 My Company

This software includes open source components:
- React (MIT License)
- lodash (MIT License)
- Postgres driver (Apache 2.0)

See NOTICES.txt for full license information.
```

### In Documentation

For websites, README files, or docs:

```markdown
## Acknowledgments

This project builds on:
- [Library Name](https://link) - MIT License
- Data from [Source](https://link) - CC BY 4.0
```

---

## Creative Commons Attribution

CC licenses have specific attribution requirements. A complete attribution includes:

1. **Title** of the work (if provided)
2. **Author/creator** name
3. **Source** link to the original
4. **License** with link

### Good CC Attribution Example

```
"Storm Clouds" by Jane Smith (https://example.com/storm)
Licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
Image cropped from original.
```

### Minimal Acceptable

```
Photo by Jane Smith, CC BY 4.0
```

This omits title and source link, which is acceptable but not ideal.

### For Modified Works

You must indicate changes:

```
"Storm Clouds" by Jane Smith, CC BY 4.0
Modified: converted to grayscale, cropped
```

---

## Common Mistakes

### Mistake 1: Removing copyright notices

Wrong:
```python
# I deleted the original header because I rewrote this
```

Right:
```python
# Original: Copyright (c) 2024 Original Author
# Modifications: Copyright (c) 2024 You
# SPDX-License-Identifier: MIT
```

### Mistake 2: Only crediting in one place

If you include attribution in source files, also include it in distributed binaries. Users of your binary may never see source files.

### Mistake 3: Vague attribution

Wrong:
```
Uses some open source libraries.
```

Right:
```
Uses React (MIT), lodash (MIT), and PostgreSQL (PostgreSQL License).
See NOTICES for details.
```

### Mistake 4: Implying endorsement (CC licenses)

Wrong:
```
Officially recommended by Jane Smith!
```

Right:
```
Based on work by Jane Smith, CC BY 4.0
```

---

## Attribution by License Type

| License | Copyright Notice | License Text | Changes Noted | NOTICE File |
|---------|-----------------|--------------|---------------|-------------|
| MIT | Required | Required | No | No |
| BSD | Required | Required | No | No |
| Apache 2.0 | Required | Required | Required | If present |
| GPL | Required | Required | Required | No |
| LGPL | Required | Required | Required | No |
| MPL | Required | Required | Required | No |
| CC BY | Required | Link required | Required | N/A |
| CC0 | Not required | Not required | Not required | N/A |

---

## Tools for Managing Attribution

### Automated License Detection

- **FOSSA** - Enterprise license compliance
- **Snyk** - Security + license scanning
- **WhiteSource (Mend)** - License management
- **license-checker** (npm) - List dependency licenses
- **pip-licenses** (Python) - License info for pip packages

### SPDX

SPDX (Software Package Data Exchange) provides standardized license identifiers:

```
SPDX-License-Identifier: Apache-2.0
```

This makes license information machine-readable and unambiguous.

---

## When Attribution Isn't Required

Only a few situations don't require attribution:

1. **Public domain** (CC0, Unlicense) - No attribution required, but often polite
2. **Private use** - Most licenses only require attribution on distribution
3. **Facts and ideas** - Copyright doesn't cover facts, only expression

Even when not legally required, attribution is often expected by community norms (especially in academia).
