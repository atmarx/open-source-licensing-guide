# Free as in Freedom

If I had a dollar for every time someone said "but it's free!" without understanding what kind of free they meant, I could retire twice (to that stereotypical tropical island all of us graybeards tend to retire to). The English language did us no favors here.

In most Romance languages, there are two different words: one for "*free of charge*" and one for "*free to do with as you please*." English smashes them together into one word and expects us to figure it out from context.

We can't afford ambiguity when we're talking about legal rights. So let's fix that.

## The Two Meanings of "Free"

<div class="grid cards two-column" markdown>

-   :material-gift:{ .lg .middle } **Gratis**

    ---

    - Free of charge.
    - A free sample at the grocery store.
    - **Free beer.**

-   :material-lock-open-variant:{ .lg .middle } **Libre**

    ---

    - Free to use, modify, share.
    - Freedom of the press.
    - **Free speech.**

</div>

When Richard Stallman started the free software movement in 1983, he meant **libre**.[^gnu-manifesto] Free software is about freedom, not price. His famous formulation: **"Free as in free speech, not as in free beer."**

I've watched this confuse people for the better part of half a century. It still confuses people. But once you get it, a lot of other things click into place.

## Why This Distinction Matters

### Open source software can cost money

This surprises people, but there's nothing in any open source license that says you can't charge for the software. Red Hat built a multi-billion dollar business selling Linux. The license guarantees that once you have the software, you have certain freedoms—it doesn't say you're entitled to get it for free.

!!! terminal "Confusion Reigns"

    I remember when Red Hat went public in 1999.[^red-hat-ipo] People were incredulous: "How can you sell something that's free?" **They were confusing gratis with libre.**

### Proprietary software can be gratis

Your phone is full of apps that cost nothing. Chrome, Instagram, Gmail—all free *as in beer*. But try to look at their source code. Try to modify them. Try to redistribute them. You can't. **They're gratis but not libre.**

When something is free but not open source, ask yourself: what's the actual business model? Usually, **you're the product**.

### The Four Freedoms

The FSF defines libre software through four freedoms.[^four-freedoms] They're numbered starting from zero because programmers:

0. The freedom to **run** the program for any purpose
1. The freedom to **study** how the program works and modify it
2. The freedom to **redistribute** copies
3. The freedom to **distribute modified versions**

Notice that freedoms 1 and 3 are meaningless without source code. You can't study or meaningfully modify a compiled binary. This is why "open source" requires actual source availability, not just permission in principle.

## The Terminology Wars

Back in the 90s, we spent an embarrassing amount of energy arguing about what to call this stuff:

- **Free Software** — Stallman's original term, emphasizing freedom (libre)
- **Open Source** — Coined in 1998 to be more business-friendly, less political[^opensource-history]
- **FOSS** — Free and Open Source Software (a compromise)
- **FLOSS** — Free/Libre and Open Source Software (explicitly clarifying "libre")

These days, most people use "open source" in conversation and don't worry too much about the philosophical implications. But when you're reading licenses or making decisions about your own projects, **the libre/gratis distinction still matters**.

## A Practical Framework

When you're evaluating software, ask two separate questions:

1. **What does it cost?** (gratis vs paid)
2. **What rights do I have?** (libre vs proprietary)

<div class="grid cards two-column" markdown>

-   :material-check-circle:{ .lg .middle } **Gratis + Libre**

    ---

    Linux, Firefox, Python, Git — Free to use *and* free to modify, share, and build upon.

-   :material-alert-circle:{ .lg .middle } **Gratis + Proprietary**

    ---

    Chrome, Instagram, most mobile apps — Free to use, but you can't see the code, modify it, or redistribute.

-   :material-check-circle-outline:{ .lg .middle } **Paid + Libre**

    ---

    RHEL, support contracts, hosted services — Costs money, but you still have full rights to the code.

-   :material-close-circle:{ .lg .middle } **Paid + Proprietary**

    ---

    Windows, Photoshop, most commercial software — Costs money *and* restricts what you can do with it.

</div>

The most valuable quadrant for users is often libre—regardless of price. Here's why: if the original maintainer abandons the project, you can fork it. If they make decisions you disagree with, you can go your own way. If they get acquired and change direction, the code you depend on is still yours to use.

I've seen too many projects die because they depended on proprietary software that got discontinued. Libre software has a survival advantage that compounds over time.

[^gnu-manifesto]: See [The GNU Manifesto](../reference/sources.md#the-gnu-manifesto)
[^red-hat-ipo]: See [Red Hat IPO](../reference/sources.md#red-hat-ipo)
[^four-freedoms]: See [FSF Four Freedoms Definition](../reference/sources.md#fsf-four-freedoms-definition)
[^opensource-history]: See [Open Source Initiative History](../reference/sources.md#open-source-initiative-history)
