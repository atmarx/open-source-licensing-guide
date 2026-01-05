# Rights and Obligations

Here's something I wish someone had explained to me earlier in my career: every open source license is fundamentally a **trade**. The creator grants you certain rights. In exchange, you accept certain obligations.

This is not charity. This is not "take whatever you want." This is a bargain, and like any bargain, both parties have to hold up their end.

## Rights Commonly Granted

Let's start with what you get. Most open source licenses grant some combination of these:

<div class="grid cards two-column" markdown>

-   :material-play-circle:{ .lg .middle } **Use**

    ---

    Run the software for any purpose—personal, commercial, educational, governmental—without restriction or payment. This is so universal that people forget it's a grant. Proprietary software often restricts what you can use it for.

-   :material-magnify:{ .lg .middle } **Study**

    ---

    Examine the source code to understand how it works. This is one of the freedoms that defines open source. You're not just getting a black box—you're getting the blueprint.

-   :material-pencil:{ .lg .middle } **Modify**

    ---

    Change the software to fix bugs, add features, adapt it to your needs. You own your modifications (though what you can do with the combined work depends on the license).

-   :material-share-variant:{ .lg .middle } **Distribute**

    ---

    Share copies with others, either unchanged or with your modifications included.

-   :material-key-chain:{ .lg .middle } **Sublicense** *(sometimes)*

    ---

    Some licenses allow you to grant rights to others—essentially passing on the permission. Permissive licenses generally allow this. Copyleft licenses require you to pass along the same license, unchanged.

</div>

## Obligations Commonly Required

Now for your end of the bargain. What do licenses require in return?

### Attribution

Almost every open source license requires attribution—acknowledgment of the original creators. This typically means:

- Preserving copyright notices in the code
- Including the license text when you distribute
- Sometimes listing the project in an "about" screen or documentation

!!! tip "Attribution is nearly universal"
    Even the most permissive licenses require attribution. MIT? Attribution. BSD? Attribution. Apache? Attribution plus NOTICE file preservation.

    The only exceptions are public domain dedications like CC0 or the Unlicense, which explicitly waive this requirement.

I've seen companies get sloppy about attribution because they think permissive means "no obligations." It doesn't. It means *fewer* obligations, not zero.

### License Preservation

You must include a copy of the license with distributed software. This isn't bureaucratic pedantry—it's how recipients know their rights. If you strip the license, you're not just being rude; you're breaking the terms that gave you permission in the first place.

### Disclaimer Preservation

Those "AS IS" and "NO WARRANTY" clauses? They must be preserved. This protects the original authors from liability. Courts take this seriously.

### Source Code Provision (copyleft only)

Here's where copyleft adds requirements. When you distribute GPL software (or derivatives), you must make source code available to recipients:

- **GPL:** Source for the entire derivative work
- **LGPL:** Source for modifications to the library itself
- **AGPL:** Source for network users too, not just people who get copies

### Same License (copyleft only)

Copyleft licenses require derivative works to use the same (or compatible) license. Your modifications inherit the license. This is the "viral" aspect that makes some lawyers nervous.

## What Triggers Obligations?

This is crucial. Most people don't realize that **private use triggers almost nothing**.

| Action | Triggers Obligations? |
|--------|----------------------|
| Running the software privately | No |
| Modifying for personal use | No |
| Using internally in your company | Generally no |
| Distributing to others | **Yes** |
| Selling copies | **Yes** |
| Including in a product you ship | **Yes** |
| Offering as a network service | Depends on license |

The key word is **distribution**. Until you give the software to someone else, most license obligations are dormant. This is why you can use GPL tools to build proprietary software—using the tool isn't distribution, and the output isn't a derivative work.

But the moment you ship that code to customers, share it with contractors, or let someone download it? Now you're distributing, and the obligations wake up.

## A Quick Reference

| License | Attribution | Include License | Disclose Source | Same License |
|---------|-------------|-----------------|-----------------|--------------|
| MIT     | Yes         | Yes             | No              | No           |
| Apache 2.0 | Yes      | Yes             | No              | No           |
| GPL     | Yes         | Yes             | Yes             | Yes          |
| LGPL    | Yes         | Yes             | For library only | For library only |
| MPL     | Yes         | Yes             | For modified files | For modified files |

## The Patent Question

I should mention patents, because they've become increasingly important.

**Apache 2.0** includes an explicit patent grant—contributors give you a license to any patents they hold that cover the contributed code.[^apache-patent] This is a big deal for enterprise adoption.

**GPL v3** includes patent provisions, partly in response to some legal maneuvering by certain large companies.[^gpl-history]

**MIT and BSD** are silent on patents. This doesn't mean you're getting a patent grant—it means the license simply doesn't address the question.

If you're working in a domain where patents are common (mobile, video codecs, certain enterprise areas), the patent provisions of your license choice matter more than usual.

[^apache-patent]: See [Apache License 2.0 Text](../reference/sources.md#apache-license-20-text)
[^gpl-history]: See [GPL License History](../reference/sources.md#gpl-license-history)
