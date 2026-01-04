# Java Licensing: The Oracle Tax

**Year:** 2018-2019
**Lesson:** "Free" can become expensive overnight

## What Happened

Java is everywhere. Enterprise applications, Android apps, big data systems, financial services. For decades, Java was effectively free—Sun Microsystems provided the JDK at no cost, and developers built empires on it.

Then Oracle acquired Sun.

For years, nothing much changed. Oracle continued providing the JDK. Developers continued using it. The ecosystem continued growing.

Then, in 2018, Oracle changed the licensing model.[^oracle-jdk-change]

## The Licensing Shift

Oracle announced that starting with Java 11:

- Oracle JDK would require a commercial license for production use
- Updates to Oracle JDK 8 (the most widely deployed version) would require a subscription
- Only "Oracle OpenJDK" builds would remain free, but without long-term support

The pricing shocked many organizations. Oracle's Java SE subscription was based on processor count or named user count. For large enterprises, the annual cost could reach millions of dollars.

For software that had been "free" for twenty years.

## The Panic

Companies scrambled. IT departments received urgent questions from executives: "Are we compliant? How much do we owe Oracle?"

The confusion was immense:

- **Which Java were you running?** Oracle JDK? OpenJDK? Something else?
- **What version?** Different versions had different licensing implications
- **Where was it deployed?** Development was still free; production wasn't
- **Who distributed it?** Did your vendor bundle Java? Were they compliant?

Oracle's licensing audits became a source of corporate anxiety. Stories circulated of companies receiving surprise licensing bills.

## The Community Response

### Alternative Distributions Emerged

The Java ecosystem rallied. Because OpenJDK itself remained GPL-licensed, anyone could build and distribute it:

- **AdoptOpenJDK** (now Eclipse Adoptium/Temurin) — Community-driven builds
- **Amazon Corretto** — Amazon's no-cost distribution with long-term support
- **Azul Zulu** — Commercial vendor offering free and paid tiers
- **Red Hat OpenJDK** — For Red Hat customers
- **BellSoft Liberica** — Another commercial alternative
- **Microsoft Build of OpenJDK** — Yes, Microsoft now distributes Java

The message was clear: you don't need Oracle's Java. The code is open source. Others will provide it.

### Long-Term Support Fragmented

Sun had provided updates indefinitely. Oracle wanted subscriptions for long-term support. The community organized alternatives.

Eclipse Adoptium provides free LTS builds. Amazon commits to long-term Corretto support. The ecosystem adapted, but coordination became more complex.

## The Deeper Lesson

### Java Was Always Open Source

Here's what many people missed: OpenJDK has been GPL-licensed since 2007. Oracle JDK and OpenJDK were functionally identical for most purposes. Oracle's licensing change affected *Oracle's distribution*, not Java itself.

The code remained free. Only Oracle's packaging, support, and branding required payment.

This distinction matters enormously. Oracle couldn't close Java any more than Oracle could close Linux. The GPL prevented it. What Oracle could do was change their *service* model—and many organizations discovered they'd been paying for Oracle's brand when free alternatives existed.

### The Audit Culture

Oracle's aggressive licensing enforcement—not just for Java, but across their product line—became notorious. "Oracle audit" became shorthand for an expensive, stressful experience.

This culture pushed organizations away from Oracle dependencies entirely. Some companies adopted policies against using any Oracle software, even free products, to avoid future licensing entanglements.

## The Lessons

### "Free" needs definition

Was Java free? The code was GPL. But organizations used Oracle's distribution without understanding the difference between "open source code" and "Oracle's packaged product." When Oracle changed terms on their product, users felt betrayed—even though the code remained free.

### Dependency on a single vendor is risky

Organizations that assumed "Java = Oracle JDK" had a single point of failure. When Oracle changed terms, migration was painful. Organizations that understood "Java = OpenJDK with multiple distributions" had options.

### Open source licenses protect the code

Oracle couldn't revoke the GPL on OpenJDK. They couldn't prevent competitors from offering builds. They couldn't close the source. The license did exactly what it was designed to do: ensure the code remained free even when the steward's interests changed.

### Corporations have long memories

Oracle's licensing changes—combined with their litigation against Google and their general approach to acquisitions—have made many organizations Oracle-averse. The short-term licensing revenue may have cost Oracle long-term mindshare.

## What This Means For You

When using "free" enterprise software:

- Understand which entity provides your distribution
- Know the difference between open source code and vendor distributions
- Have migration plans for alternative distributions
- Track licensing changes proactively

When evaluating Java specifically:

- Eclipse Adoptium (Temurin) is a safe, community-governed choice
- Major cloud vendors provide their own free distributions
- Oracle JDK is fine if you're willing to pay—but you have options
- The code is the same; you're choosing support and governance

The Java licensing saga demonstrated that open source governance matters as much as the license. The GPL protected the code. But the community's ability to organize alternative distributions—quickly, credibly, at scale—is what actually preserved Java's accessibility.

Oracle still makes money from Java subscriptions. But they no longer control Java's destiny. The community made sure of that.

[^oracle-jdk-change]: See [Oracle JDK Licensing Changes](../reference/sources.md#oracle-jdk-licensing-changes)

