# AI and Open Source: The License Gap

**Year:** 2022–present

**Lesson:** Open source licenses were written for humans sharing code with humans — not for machines that learn from it

## What Happened

In June 2021, GitHub launched Copilot — an AI coding assistant trained on billions of lines of public code.  That code included files licensed under [GPL](../licenses/copyleft/gpl.md), [MIT](../licenses/permissive/mit.md), [Apache](../licenses/permissive/apache-2.md), [AGPL](../licenses/other/agpl.md), and every other license in this guide.  The tool could generate code that looked remarkably like its training data, sometimes reproducing functions nearly verbatim.  License headers were nowhere to be found in the output.

This raised a question that open source licensing had never had to answer: **when a machine learns from licensed code, does the output inherit the license?**

Nobody knew.  The licenses didn't say.  They were written in an era when "copying" meant a human reading code and typing it into another file.  The entire open source licensing framework — decades of carefully worded permissions, obligations, and copyleft triggers — had no mechanism for a statistical model that ingests millions of files and produces something new-ish.

What followed was the first serious collision between AI and open source licensing.  It's still unfolding.

## The Lawsuit

On November 3, 2022, a class action was filed against GitHub, Microsoft, and OpenAI in the Northern District of California.[^copilot-lawsuit]  The plaintiffs — open source developers whose code had been used to train Copilot — alleged that the tool violated the DMCA by stripping copyright notices and license headers from training data, breached the terms of open source licenses, and engaged in unfair competition.

The case became a test of whether existing law could handle AI-generated code at all.

It didn't go cleanly for either side.  In July 2024, Judge Tigar dismissed the DMCA claims, ruling that the plaintiffs hadn't shown Copilot reproduced their code identically enough to trigger DMCA section 1202(b).[^copilot-dismissal]  The court set a high bar: if the AI output isn't a near-identical copy, stripping attribution doesn't violate the DMCA.

But two claims survived: open source license violation and breach of contract.[^copilot-remaining]  These are the claims that matter most for this guide.  The question isn't whether Copilot copies code character-for-character — it's whether training on licensed code and generating similar output constitutes use that triggers license obligations.

The plaintiffs appealed the DMCA dismissal to the Ninth Circuit in September 2024, arguing that the court's "identicality" requirement reads a limitation into the DMCA that doesn't exist.  As of early 2026, the appeal and the remaining claims are still pending.[^copilot-appeal]

## The Copyright Paradox

While the Copilot case wound through the courts, the U.S. Copyright Office dropped a bombshell.

In January 2025, the Copyright Office published Part 2 of its report on AI and copyright, focused on the copyrightability of AI-generated output.[^usco-report]  The key finding: prompting an AI system is not sufficient to make a human the author of the output.  Code generated entirely by AI cannot be copyrighted.

This creates an extraordinary paradox for open source licensing.

Open source licenses are copyright licenses.  They work because the author holds copyright and grants specific permissions under specific conditions.  If AI-generated code has no copyright holder, there's no copyright to license.  The entire framework — permissive, copyleft, all of it — assumes someone *owns* the code being licensed.

So here's the bind: the AI was trained on copyrighted, licensed code.  Its output may be *derived from* that code in some meaningful sense.  But the output itself may not be copyrightable.  Does the training data's license still apply?  Can copyleft propagate through a neural network?  If the output isn't copyrightable, can it be licensed at all?

No court has answered these questions.  No license was written to address them.

## When the Machine Remembers

Meanwhile, in Munich, a court made the first major European ruling on AI and copyright.

On November 11, 2025, Munich Regional Court I ruled that OpenAI had infringed copyright by training its models on song lyrics belonging to GEMA, Germany's music collecting society.[^gema-openai]  The court found that when training data becomes embedded in model weights and can be reproduced through simple prompts, that constitutes reproduction under EU copyright law — even though the "copy" exists as probability distributions across billions of numerical parameters.

The ruling matters for open source because it establishes a principle: **memorization is reproduction.**  If a model can reproduce a function from a GPL-licensed project when prompted, that reproduction may trigger copyright obligations.  The GEMA case dealt with song lyrics, but the logic extends to any copyrighted material — including source code.

OpenAI has appealed, and the ruling isn't final.  But combined with the Entr'ouvert v. Orange decision in Paris (February 2024, €860,000 in damages for GPL v2 violations[^entrouvert]) and the Steck v. AVM ruling in Berlin (June 2024, enforcing LGPL user rights to modify and reinstall[^steck-avm]), European courts are proving far more willing than American courts to enforce open source licenses with real consequences — and to extend copyright principles into novel technical territory.

## The Transparency Response

Legislatures didn't wait for the courts.

California's AB 2013, the Generative AI Training Data Transparency Act, took effect January 1, 2026.[^ab-2013]  It requires developers of generative AI systems to publicly disclose what data they trained on — including whether copyrighted materials were used, the sources and owners of training datasets, and descriptions of the data.  The disclosures must be posted on the developer's website and updated whenever the model is substantially modified.

OpenAI, Anthropic, and Google all published disclosures by the deadline, with varying levels of detail.  xAI filed a lawsuit challenging the law's constitutionality.

AB 2013 doesn't resolve the licensing question, but it makes it harder to hide from.  When a company must publicly state that it trained on GPL-licensed code, the question of whether it complied with the GPL becomes a lot easier to investigate.

## The Definition Problem

In October 2024, the Open Source Initiative released version 1.0 of the Open Source AI Definition (OSAID) — an attempt to define what "open source" means when applied to AI systems.[^osaid]

The definition was immediately controversial.  The core tension: OSAID requires access to information about training data sufficient to reproduce it, but stops short of requiring the training data itself to be released.  The Software Freedom Conservancy's Bradley Kuhn described the drafting process as filled with "substantial acrimony."  Meta, which uses "open source" to describe its Llama models, participated in drafting but disagreed with the final definition.

The controversy echoes a familiar pattern from this guide.  When MongoDB created SSPL to address cloud providers, the OSI rejected it as not meeting the Open Source Definition.  When companies call their AI models "open source" while keeping training data proprietary, OSAID tries to draw a line — but critics say it drew the line in the wrong place.

OSI views version 1.0 as a starting point and plans to update the definition by Q4 2026.  Meanwhile, companies continue to use the term "open source" for AI models that would never qualify under the traditional Open Source Definition — and the market hasn't punished them for it.

## The Lessons

### Open source licenses assumed human readers

Every license in this guide was written to govern what happens when a person reads, copies, modifies, and distributes code.  None of them contemplated a system that processes millions of files into statistical weights and generates new code from the patterns.  This isn't a flaw in the licenses — it's a gap that didn't exist until recently.  But gaps don't stay theoretical when billions of dollars flow through them.

### The copyright system is confused

If AI-generated code can't be copyrighted, it can't be open source licensed either — because open source licenses are copyright licenses.  But if AI-generated code *can* incorporate copyrighted expression from its training data, the licenses might still apply.  Courts, regulators, and the Copyright Office are pulling in different directions.  This will take years to resolve.

### Memorization changes the calculus

The GEMA ruling establishes that if a model can reproduce copyrighted material, the encoding in model weights is itself a reproduction.  For code, this means an AI that can reproduce GPL functions when prompted may be creating copies subject to the GPL — even if it can also produce novel code that isn't.  The practical question shifts from "was it trained on GPL code?" (it was) to "can it reproduce GPL code?" (sometimes).

### Transparency is arriving whether the industry likes it or not

AB 2013 forces disclosure of training data sources.  EU regulations are moving in the same direction.  Once it's publicly documented that a model trained on copyleft-licensed code, enforcement becomes a question of will, not evidence.

### "Open source AI" doesn't mean what "open source" means

The traditional Open Source Definition is about source code access and freedom to modify.  OSAID tries to extend this to AI, but the training data question — the AI equivalent of "source code" — remains contested.  When a company calls its model "open source" while keeping the training data proprietary, they're using the term differently than this guide does.

## For Your Decisions

If you're using AI coding assistants:

- Treat AI-generated code as having **unknown provenance** until verified.  It may contain fragments of licensed code.
- Run generated code through license scanning tools before committing it to projects with specific license requirements
- Be especially cautious with [copyleft](../concepts/permissive-vs-copyleft.md) obligations — if the generated code is derived from GPL sources, your project may have obligations you didn't anticipate
- Document which code is AI-generated.  If licensing questions arise later, you'll need to know what came from where

If you're releasing open source code:

- Your code will be used to train AI models.  This is already happening and no license currently prevents it with certainty
- [Copyleft](../licenses/copyleft/gpl.md) licenses provide the strongest *theoretical* argument that AI output derived from your code carries obligations — but no court has confirmed this
- [Permissive](../licenses/permissive/mit.md) licenses require attribution that AI tools routinely strip.  Whether this constitutes a violation is an open question
- Consider whether your license choice accounts for AI training as a use case.  None of them do explicitly — yet

If you're building AI systems:

- AB 2013 and similar laws mean your training data choices are becoming public.  Plan accordingly
- The GEMA ruling means memorization creates legal exposure.  Deduplication and output filtering are becoming compliance requirements, not nice-to-haves
- "Open source" as applied to AI models is a term in flux.  Be precise about what you mean

The honest answer to most AI licensing questions right now is "nobody knows."  The legal system is working through it.  But "nobody knows" isn't "anything goes."  The cases are being filed, the rulings are coming, and the answers that emerge will reshape how open source works for everyone.

[^copilot-lawsuit]: See [Doe v. GitHub Copilot Lawsuit](../reference/sources.md#doe-v-github-copilot-lawsuit)
[^copilot-dismissal]: See [Doe v. GitHub DMCA Claims Dismissed](../reference/sources.md#doe-v-github-dmca-claims-dismissed)
[^copilot-remaining]: See [Doe v. GitHub Remaining Claims](../reference/sources.md#doe-v-github-remaining-claims)
[^copilot-appeal]: See [Doe v. GitHub Ninth Circuit Appeal](../reference/sources.md#doe-v-github-ninth-circuit-appeal)
[^usco-report]: See [US Copyright Office AI Report Part 2](../reference/sources.md#us-copyright-office-ai-report-part-2)
[^gema-openai]: See [GEMA v. OpenAI Munich Ruling](../reference/sources.md#gema-v-openai-munich-ruling)
[^entrouvert]: See [Entr'ouvert v. Orange GPL Damages](../reference/sources.md#entrouvert-v-orange-gpl-damages)
[^steck-avm]: See [Steck v. AVM LGPL Enforcement](../reference/sources.md#steck-v-avm-lgpl-enforcement)
[^ab-2013]: See [California AB 2013 Training Data Transparency](../reference/sources.md#california-ab-2013-training-data-transparency)
[^osaid]: See [OSI Open Source AI Definition](../reference/sources.md#osi-open-source-ai-definition)
