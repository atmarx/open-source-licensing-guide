# The BSD Advertising Clause Disaster

**Era:** 1990s
**Lesson:** License proliferation and clause accumulation create real problems

## What Happened

The original BSD license, used by the University of California, Berkeley for their Unix distributions, contained four clauses. The third one seemed innocent enough:

> All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by the University of California, Berkeley and its contributors.

One acknowledgment. Not a big deal, right?

## The Problem

BSD code was good. Really good. Projects incorporated BSD-licensed components enthusiastically. Each project that used the original BSD license required its own acknowledgment.

Then projects started combining code from multiple BSD-licensed sources. Each source required its own specific acknowledgment text. By the late 1990s, some software distributions required pages of acknowledgments—one for every BSD-licensed component they included.

NetBSD at one point had 75 different required acknowledgments. Some products had so many required notices that printing them all was impractical. The advertising clause had become a bureaucratic nightmare.

Worse, different organizations had modified the clause with their own names, creating what was effectively a new license each time. You couldn't just satisfy "the BSD advertising clause"—you had to satisfy *each project's specific* advertising clause.

## The Resolution

In 1999, William Hoskins, director of the Office of Technology Licensing at UC Berkeley, officially removed the advertising clause from the BSD license.[^bsd-removal] The university encouraged all BSD-licensed projects to do the same.

This gave us the modern 2-clause and 3-clause BSD licenses:

- **2-clause BSD (Simplified BSD):** Just attribution and disclaimer
- **3-clause BSD (New BSD):** Attribution, disclaimer, and non-endorsement
- **4-clause BSD (Original):** Now considered obsolete

Most projects migrated. The advertising clause problem faded into history.

## The Lesson

**License clauses accumulate.** What seems trivial for one project becomes a burden when code is combined. The BSD advertising clause wasn't malicious—it was just shortsighted.

This is why license simplicity matters. Every clause you add is a clause that will be inherited by everyone who uses your code, combined with all the other clauses they've inherited from everyone else.

The simpler your license, the less friction it creates downstream. MIT's popularity isn't an accident—it imposes almost nothing on users.

## What We'd Do Differently Today

- Use standardized license texts instead of customizing per-project
- Think about how clauses interact when code is combined
- Prefer minimal licenses unless additional clauses serve a clear purpose

The BSD advertising clause wasn't a legal catastrophe—nobody went to court over it. But it created enough friction that the community eventually had to fix it. Better to learn from their experience than to repeat it.

[^bsd-removal]: See [BSD Advertising Clause Removal](../reference/sources.md#bsd-advertising-clause-removal)
