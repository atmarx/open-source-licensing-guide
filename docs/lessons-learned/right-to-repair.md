# Right to Repair: When the License Owns the Machine

**Year:** 2015–present

**Lesson:** A license doesn't have to live in a text file anymore.  It can live in firmware, behind a digital lock, inside a tractor you already paid for.

## What Happened

For most of this guide, a license is a document.  You read it, you agree to it, you comply with it.  The thing being licensed is software, and the software sits on a disk where you can see it.

Then software climbed inside everything else.

Your tractor runs on it.  Your car unlocks features with it.  Your insulin pump, your phone, your refrigerator, your ventilator — all of it now ships with embedded code, and that code comes with terms.  Somewhere along the way the question stopped being *"what does this license permit?"* and became *"do I actually own the thing I bought?"*

The honest answer, increasingly, is no.  You own a licensed platform with restrictions.  And the clearest place to watch that shift happen was on a farm.

## The Tractor That Wouldn't Let You Fix It

John Deere builds machines that cost more than houses.  Farmers have repaired their own equipment for as long as equipment has existed — it's not a hobby, it's survival.  When a combine breaks down mid-harvest, a delay measured in days is a loss measured in a year's income.

Modern Deere equipment changed the math.  The diagnostic software, the electronic service tools, and the authorization keys needed to complete many repairs were available mainly to Deere's authorized dealers.[^deere-ftc]  A farmer could physically replace a part and still find the machine refused to run until a dealer technician plugged in and blessed the repair.  The hardware was theirs.  The software gate was not.

Farmers called it what it was: a repair monopoly enforced by code.  And because the lockout was a *software* mechanism, the usual remedy — go to an independent mechanic — didn't work.  The independent mechanic couldn't get the software either.

This is the part that matters for a licensing guide.  Deere wasn't suing anyone for copying its software.  It didn't have to.  The license terms and the technical lock did the enforcement automatically, on every machine, without a courtroom.  That's a power traditional copyright never gave anyone.

## The Reckoning

The pressure built for a decade, then broke fast.

In January 2025, the U.S. Federal Trade Commission — joined by the states of Illinois and Minnesota — sued John Deere, alleging it had illegally monopolized the market for repairs of its own equipment by withholding the software tools independent mechanics needed.[^deere-ftc]  That case is still being litigated as of early 2026.

Separately, a long-running private class action by farmers reached a settlement.  In 2026, Deere agreed to a proposed **$99 million** fund for farmers who had paid authorized dealers for repairs going back to January 2018, and — more importantly for everyone else — committed to make its digital diagnostic and repair tools available to farmers and independent repair providers for at least ten years.[^deere-settlement]  A federal court granted preliminary approval in May 2026, with a fairness hearing set for October.  It isn't final, and a settlement is not an admission.  But the direction is unmistakable.

The Environmental Protection Agency added a second front.  Manufacturers had argued that emissions law — the Clean Air Act's rules against tampering with engine controls — justified locking down repair software.  The EPA pushed back, clarifying that emissions compliance is not a blanket license to monopolize repair.[^epa-deere]  One of the favorite legal shields for the lockout got noticeably thinner.

## The Law That Made the Lock Legal

To understand why a software lock can override your ownership of a physical object, you have to look at one of the strangest pieces of copyright law on the books: **Section 1201 of the Digital Millennium Copyright Act.**

The DMCA's anti-circumvention provision, passed in 1998, makes it illegal to bypass a "technological protection measure" that controls access to a copyrighted work — *even if your underlying purpose is perfectly legal.*  It was written to stop DVD ripping and software piracy.  But firmware is a copyrighted work, and the access control sitting in front of it is a technological protection measure.  So when you bypass the lock to repair your own tractor, the manufacturer's argument is that you didn't just break a repair restriction — you violated federal copyright law.

Read that again, because it's the whole trick.  The legal question stopped being *"did you copy our software?"* and became *"did you bypass our digital lock?"*  Copying is what copyright was built to govern.  Circumvention is something else: it lets a manufacturer attach copyright's penalties to acts that have nothing to do with copying.

There is a release valve, and it is a deeply weird one.  Every three years the Librarian of Congress, advised by the Copyright Office, holds hearings and grants temporary **exemptions** to Section 1201.  Repair advocates have to show up each cycle and re-win the right to fix their own things.  They've made progress — exemptions covering vehicle software repair were granted in 2015 and broadened in the 2018 and 2021 cycles, and the 2024 rulemaking extended repair-related exemptions further.[^dmca-1201]  But an exemption is not a right.  It's a three-year lease on permission, and the burden of renewal falls on the public, not the manufacturer.

## Europe Picks a Side

While the U.S. fought this case by case, the European Union did what it increasingly does with software: it regulated the structure directly.

The EU's **Directive on the repair of goods** (Directive 2024/1799) was adopted in June 2024 and takes effect across member states from July 31, 2026.[^eu-repair]  It obliges manufacturers to provide spare parts, repair information, and technical documentation — for many product categories, for up to ten years — and, critically, it **prohibits the use of contractual clauses, hardware techniques, or software techniques that impede repair** unless a manufacturer can show a legitimate, objective justification.

Sit with that last clause.  A European regulator looked at the software lockout — the exact mechanism Deere used — and made it presumptively illegal.  Separate EU machinery rules push the same way for agricultural and industrial equipment, requiring repair and maintenance information on non-discriminatory terms.[^eu-repair]  Where American law treats the lock as legitimate until an exemption carves out a hole, European law treats the lock as suspect until the manufacturer justifies it.  Same technology, opposite default.

This is part of a larger pattern the licensing world is still adjusting to: **software licenses are no longer treated as purely private contracts.**  Regulators increasingly read them as competition-policy instruments — terms that shape who can compete in a repair market, not just who can copy a file.

## The Subscription Creep

The lockout has a quieter cousin, and it's worth a callout because it pulls on licensing from a different direction.

Software used to be something you bought once and owned.  Now it's something you rent continuously — Adobe Creative Cloud, Microsoft 365, the whole SaaS economy.  That shift was well underway in pure software.  What's new is the same logic migrating into physical things you thought you'd purchased outright:

- Automakers offering heated seats, extra horsepower, or driver-assist features as monthly subscriptions — hardware already installed in the car, switched on by a recurring payment.
- Devices that lose functionality when the vendor ends support, or when a cloud service they silently depend on goes dark.
- Features tied to an account rather than to the product, revocable from a server you don't control.

Call it **continuous entitlement.**  The vendor keeps a permanent hand on the switch.  And it tugs on licensing in a subtle way: when ownership becomes a recurring license to access capabilities baked into hardware you already hold, the line between "buying a product" and "licensing a platform" stops being a metaphor.  Right-to-repair is, at bottom, a rebellion against exactly this — the insistence that *possession should still mean something.*

## The Pattern

The John Deere fight matters far beyond agriculture because it exposed a principle that now applies to cars, phones, medical devices, smart appliances, and industrial robots alike:

> A software license, backed by a digital lock and anti-circumvention law, can quietly override traditional ownership of a physical object.

It's the same theme that runs through the [source-available relicensing](../licenses/other/source-available.md) stories and the [AI training](ai-licensing.md) questions, viewed from a different angle.  In each case the formal license text is only half the story.  The other half is the *mechanism* — the cloud dependency, the model weights, the firmware lock — that enforces terms automatically, at scale, without anyone reading a word.

For decades, "licensing" meant a document you could argue with.  The frontier now is licensing you can't see and can't negotiate, embedded in a machine you already paid for.  The farmers noticed first because the cost of not noticing was a lost harvest.  Everyone else gets to learn the lesson more slowly.

## For Your Decisions

If you buy or build products with embedded software:

- **Ask what you actually own.**  "Perpetual license," "subscription," and "purchase" mean very different things once firmware is involved.  Read for the lock, not just the price.
- **Watch for the anti-circumvention trap.**  In the U.S., bypassing a software lock can carry copyright penalties even when your purpose — repair, interoperability, research — is entirely legal.  Check whether a current DMCA §1201 exemption covers your use, and remember it expires.
- **If you sell into Europe,** the 2026 repair directive flips the default.  Software techniques that impede repair are now presumptively prohibited unless you can justify them.  Design for repairability, not against it.
- **If you write the license,** know that regulators are increasingly reading your terms as competition policy.  A clause that forecloses an independent repair market is no longer just a private bargain — it's an antitrust exhibit.

The tools to lock down a machine have never been cheaper or more effective.  Whether you're allowed to use them is the fight of the decade.  I've watched it go one way in the U.S. and the other way in Europe, and the only safe prediction is that "I bought it" and "I control it" are going to keep drifting apart until the law decides how far is too far.

[^deere-ftc]: See [FTC v. Deere Repair Lawsuit](../reference/sources.md#ftc-v-deere-repair-lawsuit)
[^deere-settlement]: See [Deere Right-to-Repair Settlement](../reference/sources.md#deere-right-to-repair-settlement)
[^epa-deere]: See [EPA Deere Clean Air Act Repair](../reference/sources.md#epa-deere-clean-air-act-repair)
[^dmca-1201]: See [DMCA Section 1201 Repair Exemptions](../reference/sources.md#dmca-section-1201-repair-exemptions)
[^eu-repair]: See [EU Repair of Goods Directive](../reference/sources.md#eu-repair-of-goods-directive)
