# React's BSD+Patents Scare

**Year:** 2017

**Lesson:** Patent clauses matter, and community pressure works

## What Happened

React, Facebook's wildly popular JavaScript library, was licensed under [BSD-3-Clause](../licenses/permissive/bsd.md) with an additional patent grant. Sounds good, right? A [permissive license](../concepts/permissive-vs-copyleft.md) *plus* explicit patent protection.

The problem was the patent grant's termination clause:

> The license granted hereunder will terminate, automatically and without notice, if you (or any of your subsidiaries, corporate affiliates or agents) initiate directly or indirectly, or take a direct financial interest in, any Patent Assertion against Facebook or any of its subsidiaries or corporate affiliates.

In plain English: if you sue Facebook for *any* patent infringement (not just patents related to React), you lose your license to use React.

## Why It Was Problematic

!!! terminal inline end ""
    If your project targets enterprise adoption, your license *will* be reviewed by lawyers. They *will* find the problematic clauses.

### Asymmetric legal warfare

Large companies have large patent portfolios. If Company X had a legitimate patent dispute with Facebook about, say, advertising technology, using React gave Facebook leverage: *"Sue us and lose your React license."*

For companies that had built their entire frontend on React, this was a real risk.

### Enterprise adoption freeze

**Legal departments noticed.** Apache Software Foundation added Facebook's BSD+Patents license to their Category X list—"licenses that are NOT allowed at Apache."[^apache-category-x] This meant no Apache project could depend on React.

WordPress announced they would move away from React. Other major projects made similar statements.

### Developer backlash

The community was furious. Thousands of GitHub comments. Blog posts. Conference talks. The message was clear: this license was a dealbreaker.

## Facebook's Response

In September 2017, Facebook relicensed React under [MIT](../licenses/permissive/mit.md).[^react-license-change] No patent clause. No termination trigger. Just MIT.

They also relicensed Jest, Flow, Immutable.js, and other projects that had used the same license.

The change was complete within weeks of Apache's announcement. Community pressure worked.

## The Lessons

### Patent clauses can be poison pills

Facebook's intent may have been defensive—protecting themselves from patent trolls. The effect was offensive—giving themselves leverage against any company that might sue them for anything.

License clauses have consequences beyond their intended purpose.

### The community will push back

Facebook was used to getting their way. They had enormous leverage—React was everywhere. They could have said "take it or leave it."

But the community *did* leave it. Apache banned it. WordPress abandoned it. The threat of fragmentation was real.

### Enterprise legal review matters

Individual developers didn't notice the patent clause. Legal departments did. This is the gap between how developers think about licensing and how enterprises do.

### License changes can be fast

Facebook moved from "we're keeping the license" to "we've relicensed under MIT" in about two weeks. When an organization decides to act, license changes can happen quickly.

## The Apache Factor

The Apache Software Foundation's decision to ban Facebook's license was the turning point. Apache's Category X listing meant:

- No Apache project could use React
- Projects that depended on Apache projects couldn't easily use React
- The "ecosystem exclusion" threat became real

A single organization's principled stance created a cascade. Facebook could ignore individual developers. They couldn't ignore Apache.

## What We Learned

- Read the patent clause, not just the copyright license
- License additions can change permissive licenses into something else entirely
- Community pressure, coordinated effectively, can move large companies
- When adopting a dependency, consider whether you could replace it if the license changed

React's license scare ended well. The next one might not.

[^apache-category-x]: See [Apache Software Foundation Legal FAQ](../reference/sources.md#apache-software-foundation-legal-faq)
[^react-license-change]: See [React MIT Relicensing Announcement](../reference/sources.md#react-mit-relicensing-announcement)
