# Permissive vs Copyleft

This is the great divide. I've watched friendships strain over this debate, seen mailing list flamewars that went on for months, sat through conference talks where the speaker clearly thought the other side were fools or villains.

They're not. Both camps are trying to maximize freedom—they just disagree about what that means and how to achieve it.

## The Core Difference

Both permissive and copyleft licenses make source code available and grant freedoms. They differ in one crucial aspect: **what happens when someone modifies and redistributes the software**.

### Permissive Licenses

> "Do whatever you want with this code. Just give me credit."

Permissive licenses impose minimal restrictions:

- Use the code in proprietary software? Go ahead.
- Modify it without sharing your changes? That's fine.
- Sublicense under different terms? Sure.
- Use it commercially? Of course.

**Examples:** MIT, BSD, Apache 2.0

**The philosophy:** Maximize adoption and freedom for immediate users. If the code ends up in a closed-source product, that's the user's choice to make.

### Copyleft Licenses

> "You can use and modify this code, but if you distribute it, you must share your modifications under the same terms."

Copyleft licenses come with strings attached:

- Modifications must be shared under the same license
- Source code must be made available to recipients
- The freedoms must propagate downstream

**Examples:** GPL, LGPL, AGPL, MPL

**The philosophy:** Ensure that improvements benefit the entire community. Freedom must be protected, or it will be eroded.

## The Philosophical Argument

I've been in the room when these debates happened. Here's how both sides see it:

**The permissive argument:** "True freedom means no restrictions. If I give you something, it's yours—do what you want. Forcing people to share isn't freedom, it's coercion. And pragmatically, companies won't touch copyleft code, so permissive licenses lead to wider adoption and more overall good."

**The copyleft argument:** "Unrestricted freedom leads to restriction. If I give you free code and you turn it into a proprietary product, my gift enabled taking freedom away from your users. Copyleft isn't a restriction—it's a protection. It ensures that freedom propagates."

Both arguments are internally consistent. Which one resonates with you probably depends on your values and experiences.

## Visualizing the Difference

```
Permissive (MIT):

Original Code ──► Your Modifications ──► Proprietary Product (allowed)
     │                   │
     └── open            └── can be closed


Copyleft (GPL):

Original Code ──► Your Modifications ──► Distributed Product
     │                   │                        │
     └── open            └── must stay open ──────┘
```

## Strong vs Weak Copyleft

Not all copyleft is created equal. The community has developed a spectrum:

| Type | Scope | Example |
|------|-------|---------|
| **Strong copyleft** | Entire combined work must be open | GPL |
| **Weak copyleft** | Only modifications to original files must be open | LGPL, MPL |

Weak copyleft was a compromise. "Fine," the thinking went, "you can use our library in your proprietary application—but if you fix a bug in *our* code, that fix needs to come back." It's copyleft with a narrower blast radius.

## When to Choose Each

After decades of watching projects succeed and fail, here's my practical advice:

### Choose permissive when:

- You want maximum adoption
- You're creating a standard or reference implementation
- You're comfortable with companies using your code without contributing back
- Your project benefits from being embedded everywhere (libraries, tools)
- You're in an ecosystem where permissive is the norm (JavaScript, for instance)

### Choose copyleft when:

- You want improvements to come back to the community
- You're building something that could be "embraced and extended" by well-resourced competitors
- Software freedom is a core principle for you
- You want to create business pressure for companies to contribute back or pay for commercial licenses
- You're building an application rather than a library

## The Business Reality

Let me be direct about something: companies generally prefer permissive licenses. Legal departments understand them easily. There's no risk of accidentally "infecting" proprietary code. Compliance is straightforward.

This has real consequences. MIT and Apache-licensed projects often see more corporate contribution and adoption than GPL projects. Whether that's a feature or a bug depends on your goals.

Some projects thread the needle with **dual licensing**: GPL for open source use, commercial license for companies that don't want copyleft obligations. MySQL did this for years. It works, but it requires maintaining clear ownership of the codebase (usually via contributor license agreements).

## The Compatibility Problem

Here's where things get messy. Permissive code can flow into copyleft projects—MIT code can become part of a GPL project. But copyleft code generally can't flow into differently-licensed projects. And different copyleft licenses are often incompatible with each other.

This has caused real problems. The ZFS filesystem couldn't be included in Linux for years because of CDDL/GPL incompatibility.[^zfs-linux] The original Mozilla Public License had GPL friction until MPL 2.0 was written.[^mpl-faq]

Before you combine code from different projects, check the licenses. Compatibility matrices exist. Use them.

[^zfs-linux]: See [ZFS Linux Licensing Issues](../reference/sources.md#zfs-linux-licensing-issues)
[^mpl-faq]: See [Mozilla MPL 2.0 FAQ](../reference/sources.md#mozilla-mpl-20-faq)
