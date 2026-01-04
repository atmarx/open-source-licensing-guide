# Eclipse Public License (EPL)

**Type:** Weak copyleft (file-level)
**Current Version:** 2.0 (2017)
**SPDX Identifier:** `EPL-2.0`

The Eclipse Public License is what happens when IBM decides to do open source properly. It's the license behind the Eclipse IDE, Jakarta EE, and a substantial portion of enterprise Java tooling.

If you've written Java professionally, you've probably used EPL-licensed software. You may not have noticed—which is sort of the point.

## The Basics

EPL is a weak copyleft license, similar in philosophy to the MPL. The copyleft applies at the file level:

- **Modifications to EPL files** must remain EPL
- **New files you add** can use any license
- **Combining with other code** is allowed, including proprietary code

This makes EPL practical for enterprise use. You can build proprietary products that include EPL components without opening your entire codebase.

## Key Provisions

### File-Level Copyleft

Like MPL, EPL's copyleft is contained. If you modify an EPL file, your modifications are EPL. But your own code stays yours.

This is weaker than GPL (which would claim your entire combined work) but stronger than MIT or Apache (which have no copyleft at all).

### Patent Grant

EPL includes an explicit patent license. Contributors grant users a license to any patents that would be infringed by their contributions.

This is similar to Apache 2.0's patent provisions. It provides meaningful protection against patent claims from contributors.

### Patent Retaliation

If you sue anyone over patent claims related to the software, your license terminates. This discourages patent aggression while using EPL software.

### Secondary License Option (EPL 2.0)

EPL 2.0 introduced a "Secondary License" mechanism. Projects can designate GPL-2.0 (or later) as a secondary license, allowing code to be used under either EPL or GPL terms.

This was specifically designed to address GPL compatibility concerns. If a project enables the secondary license, you can treat the code as GPL-compatible.

## History

### IBM Origins

Eclipse started as an IBM project in 2001. IBM released it under the Common Public License (CPL), then transitioned to EPL 1.0 in 2004 when the Eclipse Foundation was established.

The license was designed from the start for foundation governance—IBM wanted to create something the community could trust, not just something IBM controlled.

### EPL 2.0 (2017)

The update to EPL 2.0 modernized the license and added the secondary license mechanism for GPL compatibility. It also cleaned up language and improved international enforceability.

## EPL vs. MPL

Both are weak copyleft, file-level licenses. The differences are subtle:

| Aspect | EPL 2.0 | MPL 2.0 |
|--------|---------|---------|
| Copyleft scope | File-level | File-level |
| Patent grant | Yes | Yes |
| Patent retaliation | Yes | Yes |
| GPL compatibility | Via secondary license option | Built-in (Sec. 3.3) |
| Origin | IBM/Eclipse Foundation | Mozilla |

In practice, they're similar enough that the choice often comes down to ecosystem. Eclipse projects use EPL; Mozilla-adjacent projects use MPL.

## When to Use EPL

**Good fit:**

- Projects in the Eclipse/Jakarta ecosystem
- Enterprise Java tooling
- When you want file-level copyleft with patent protection
- Foundation-governed projects wanting IBM/Eclipse alignment

**Consider alternatives if:**

- GPL compatibility is essential and you can't use the secondary license option
- You want strong copyleft (use GPL)
- You want maximum permissiveness (use Apache 2.0)
- You're not in the Java/Eclipse ecosystem (MPL might be more recognized)

## What This Means For You

### Using EPL Code

You can use EPL code in proprietary projects. The copyleft only applies to the EPL files themselves:

- Include EPL components: **allowed**
- Modify EPL files: **modifications must be EPL**
- Add your own files: **your choice of license**
- Distribute combined work: **allowed, with attribution**

### Choosing EPL

EPL makes sense if you're building in the Eclipse ecosystem or want the credibility of a foundation-backed license with enterprise heritage.

The weak copyleft means companies can adopt your project without legal anxiety, while the copyleft ensures improvements to your code stay open.

## The Graybeard's Take

EPL is quietly successful. It doesn't generate the passion of GPL vs. MIT debates, but it's been running major infrastructure for two decades. The Eclipse IDE alone has shaped how millions of developers work.

IBM did something right here: they created a license, established a foundation, and stepped back enough to let the community take ownership. The Eclipse Foundation governance is genuinely independent. Projects can come and go without IBM's permission.

That's harder than it sounds. Most corporate open source efforts stumble on governance—the company wants control, the community wants independence, and the tension eventually breaks something. Eclipse found a balance that's held for twenty years.

The license itself is fine. Solid weak copyleft, good patent provisions, reasonable compatibility options. But the real story is the governance model it enabled.

