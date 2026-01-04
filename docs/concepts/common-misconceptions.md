# Common Misconceptions

I've been correcting these myths for longer than some of you have been alive. They persist because they feel intuitive, because people repeat them without checking, and because the truth is a little more complicated than anyone wants it to be.

Let me save you from learning these the hard way.

## "Open source means I can do anything with it"

**The reality:** Open source means you have specific rights under specific conditions. Every open source license requires *something*—at minimum, preserving copyright notices and license text when you redistribute. Many require more.

I've watched companies get cease-and-desist letters because someone assumed "open source" meant "free for all." It doesn't.

## "If it's on GitHub, it's open source"

**The reality:** Code visibility is not a license. If a repository has no LICENSE file, you have **no legal right** to use that code beyond looking at it. None. Copyright applies automatically to all creative work.

GitHub's terms let you view and fork public repositories. That's about GitHub's platform, not about what you can do with the code itself.

!!! warning "No license = All rights reserved"
    If you find useful code without a license, you cannot legally use it in your projects. I know this seems absurd when the code is sitting right there in public. The law doesn't care what seems reasonable. Ask the author to add a license.

## "I don't need to comply if I'm not selling it"

**The reality:** License obligations are typically triggered by **distribution**, not by commerce. Giving away your software for free still counts as distribution. Putting it on GitHub is distribution. Sending it to a client—even if you don't charge—is distribution.

The only safe harbor is purely private use: code that never leaves your machine or your organization.

## "The license only applies to the original code, not my additions"

**The reality:** This depends entirely on which license:

- **Copyleft (GPL):** Your additions to a GPL work become GPL. That's the whole point.
- **Permissive (MIT):** Your additions are yours, but you still can't strip the license from the original code you included.

Even with the most permissive license, you can't pretend you wrote everything from scratch.

## "I can just rewrite it to avoid the license"

**The reality:** Copyright protects expression, not ideas. You can absolutely reimplement the same *functionality*. What you cannot do:

- Copy code and change variable names
- Copy the structure and organization with superficial changes
- Reference the original while reimplementing and claim it's independent

If you want a clean reimplementation, you need actual separation: someone reads the spec or documentation, someone *else* writes the code without ever seeing the original. This is called "clean room" implementation, and yes, companies actually do this when the stakes are high enough.

Courts can tell the difference between genuine reimplementation and a find-and-replace job.

## "Open source projects don't make money"

**The reality:** Open source is a development methodology and a licensing approach, not a business model. Many businesses are built on open source:

- Red Hat was acquired for $34 billion
- Elastic, MongoDB, HashiCorp—all publicly traded companies (though some have since abandoned open source licensing, which is its own lesson)
- Countless consultancies, hosting providers, and service businesses

Business models include support contracts, hosted services, dual licensing, open core (open source base with proprietary additions), and more.

## "GPL means I can't use it in commercial software"

**The reality:** You can absolutely use GPL software commercially. You can even *sell* GPL software. The GPL explicitly permits commercial use and distribution.

What you cannot do is distribute GPL software (or derivatives) without:
1. Providing source code
2. Granting GPL rights to recipients

If your use case involves distributing to customers, yes, there are obligations. If you're using GPL tools internally or running GPL software on your own servers, you're typically fine.

I've seen lawyers scare clients away from all GPL software because they didn't understand this distinction. It's cost companies real opportunities.

## "I found it on Stack Overflow, so it's free to use"

**The reality:** Stack Overflow content is licensed under CC BY-SA 4.0.[^stackoverflow] This means:

- You must provide attribution
- Derivative works must use a compatible license (share-alike)
- The share-alike requirement may conflict with your project's license

For a three-line snippet? Practically speaking, no one's going to sue you. But if you're copying substantial answers into your codebase, you're technically bound by CC BY-SA terms. I've seen this come up in acquisition due diligence.

## "License compatibility isn't a real problem"

**The reality:** I've watched license incompatibility kill projects. Examples:

- GPL v2 and Apache 2.0 were incompatible for years, creating real friction[^fsf-licenses]
- CDDL and GPL are still incompatible—this is why ZFS on Linux was legally murky for so long[^zfs-linux]
- Different copyleft licenses are often incompatible with each other

Before you combine libraries from different sources, verify their licenses work together. Compatibility matrices exist. Use them.

## "I can just put 'All rights reserved' to protect my code"

**The reality:** "All rights reserved" was once legally meaningful in some jurisdictions. Today, thanks to international treaties, copyright is automatic. That phrase adds nothing.

If you want people to use your code, choose a license. If you don't want people to use your code, you don't need to say anything—copyright already protects you by default.

But consider: code with no license is code that can't legally be used by anyone. If you're putting it in public, you probably want *someone* to be able to use it. Pick a license.

[^stackoverflow]: See [Stack Overflow Content License](../reference/sources.md#stack-overflow-content-license)
[^fsf-licenses]: See [FSF License Commentary List](../reference/sources.md#fsf-license-commentary-list)
[^zfs-linux]: See [ZFS Linux Licensing Issues](../reference/sources.md#zfs-linux-licensing-issues)
