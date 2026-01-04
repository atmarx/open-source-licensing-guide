# The JSON License: A Joke That Wasn't Funny

**Lesson:** Don't add humor to legal documents

## What Happened

Douglas Crockford created JSON, the data format that powers most of the modern web. He also created a reference implementation and a small JavaScript library. He licensed it under a modified MIT license with one addition:[^json-license]

> The Software shall be used for Good, not Evil.

It was a joke. Crockford has said as much. A bit of whimsy in a legal document.

The problem: lawyers don't do whimsy.

## Why It Matters

### The clause is unenforceable... probably

What counts as "Evil"? Who decides? Is building surveillance software evil? Is building ad tech evil? Is building software for a government you disagree with evil?

No court has ruled on this clause. No one knows what it means legally. And that uncertainty is the problem.

### Enterprise legal departments rejected it

Companies doing their due diligence saw the clause and flagged it. Not because they intended to do evil, but because:

- The clause is ambiguous
- Ambiguity creates legal risk
- Legal departments minimize risk

IBM famously requested (and received) a license exception from Crockford.[^ibm-exception] Other companies just avoided the code entirely.

### Major distributions excluded it

Debian and Fedora classified the JSON license as non-free.[^debian-json] The "Good, not Evil" clause violates the Open Source Definition's requirement for no discrimination by field of endeavor.

From a strict reading, the JSON license isn't open source.

### It caused actual work

Maintainers of projects that depended on Crockford's JSON library had to:

- Replace the dependency with alternatives
- Seek explicit license exceptions
- Explain to their legal teams why a "Good, not Evil" clause existed

All because of a joke.

## The Lesson

**License text is legal text.** Every word matters. Every clause has consequences. What seems like harmless whimsy to an author becomes a compliance headache for users.

If you want to be funny, write a blog post. If you want to license code, use a standard license and resist the urge to customize.

The JSON license is a permanent cautionary tale about mixing humor with legal documents. Crockford is a brilliant engineer. His license joke has caused more aggregate paperwork than most actual license disputes.

## What To Do Instead

- Use standard, OSI-approved licenses without modification
- If you have opinions about how your software should be used, express them in documentation, not licenses
- If you must add clauses, have a lawyer review them

The "Good, not Evil" clause accomplished nothing except creating work for people who wanted to use JSON parsing. That's not a good outcome for anyone.

[^json-license]: See [Crockford's JSON License](../reference/sources.md#crockfords-json-license)
[^ibm-exception]: See [IBM JSON License Exception](../reference/sources.md#ibm-json-license-exception)
[^debian-json]: See [Debian JSON License Discussion](../reference/sources.md#debian-json-license-discussion)
