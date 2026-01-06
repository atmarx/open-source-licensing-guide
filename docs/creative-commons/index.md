---
title: Creative Commons Licenses
---

<div class="hero hero-half" markdown>
  <img src="../assets/images/creative-commons-hero.webp" alt="Art deco illustration of creative works">
  <div class="hero-overlay">
    <h1>Creative Commons Licenses</h1>
    <p>For everything that isn't code</p>
  </div>
</div>

Creative Commons (CC) licenses are designed for creative works—text, images, data, documentation, music, video—rather than software code. For researchers, these are often more relevant than software licenses because they apply to datasets, papers, educational materials, and other non-code outputs.

## Software vs Creative Works

| Aspect | Software Licenses (MIT, GPL) | Creative Commons |
|--------|------------------------------|------------------|
| Designed for | Source code, binaries | Creative works, data, media |
| Concerns | Compilation, linking, derivatives | Copying, adaptation, distribution |
| Patent provisions | Sometimes | No |
| Source code concept | Central | Not applicable |

!!! tip "Don't use CC for software"
    Creative Commons explicitly recommends against using CC licenses for software. Use MIT, Apache, or GPL instead. CC licenses don't address software-specific concerns like source code, compilation, and linking.

## The Building Blocks

Creative Commons licenses are modular. They combine four conditions:

<div class="grid cards two-column" markdown>

-   :material-account-star:{ .lg .middle } **Attribution (BY)**

    ---

    Must credit the creator. Present in all CC licenses except CC0.

-   :material-share-variant:{ .lg .middle } **ShareAlike (SA)**

    ---

    Derivatives must use the same license. The "copyleft" of Creative Commons.

-   :material-currency-usd-off:{ .lg .middle } **NonCommercial (NC)**

    ---

    No commercial use allowed. *Not considered "Free Culture" or open source.*

-   :material-pencil-off:{ .lg .middle } **NoDerivatives (ND)**

    ---

    No modifications allowed. *Not considered "Free Culture" or open source.*

</div>

## The Six Licenses

These elements combine into six standard licenses, from most to least permissive:

| License | Allows Commercial | Allows Derivatives | Requires ShareAlike |
|---------|------------------|-------------------|-------------------|
| [CC BY](cc-by.md) | Yes | Yes | No |
| [CC BY-SA](cc-by-sa.md) | Yes | Yes | Yes |
| [CC BY-NC](cc-by-nc.md) | No | Yes | No |
| [CC BY-NC-SA](cc-by-sa.md#cc-by-nc-sa) | No | Yes | Yes |
| [CC BY-ND](cc-by-nd.md) | Yes | No | — |
| [CC BY-NC-ND](cc-by-nd.md#cc-by-nc-nd) | No | No | — |

Plus [CC0](cc0.md), which waives all rights (public domain dedication).

## The Spectrum

```
More Free                                              Less Free
    ◄─────────────────────────────────────────────────────►

CC0 ─── CC BY ─── CC BY-SA ─── CC BY-NC ─── CC BY-ND ─── CC BY-NC-ND
 │        │          │            │            │             │
 │        │          │            │            │             │
 No       Credit     Credit +     Credit +     Credit +      Credit +
 rights   required   share-alike  no money     no changes    no money +
                                                             no changes
```

## Permissive vs Copyleft in CC

The same philosophical divide exists in Creative Commons:

- **CC BY** is permissive—like MIT for creative works
- **CC BY-SA** is copyleft—like GPL for creative works
- **NC and ND** are restrictions that don't exist in OSI-approved software licenses

## Common Use Cases

| Work Type | Common Choice | Why |
|-----------|---------------|-----|
| Research data | CC0 or CC BY | Maximum reuse, citation norms provide attribution |
| Documentation | CC BY or CC BY-SA | Allow adaptation, encourage sharing |
| Educational materials | CC BY or CC BY-NC | Depends on commercial concerns |
| Photographs | Varies widely | Photographers often want ND or NC |
| Academic papers | CC BY | Open access standard |

## Version Matters

Creative Commons licenses have versions. **Always use version 4.0**, the current version, which:

- Works internationally without "porting"
- Covers database rights (important for data)
- Has clearer language
- Addresses moral rights

Earlier versions (1.0, 2.0, 3.0) had regional "ported" versions and lacked some protections.

## The "Free Culture" Subset

The FSF and Creative Commons distinguish between "Free Culture" licenses and others:

**Free Culture approved:**
- CC0
- CC BY
- CC BY-SA

**Not Free Culture:**
- CC BY-NC (restricts use)
- CC BY-ND (restricts derivatives)
- Any combination with NC or ND

For maximum openness and reuse, choose from the Free Culture subset.
