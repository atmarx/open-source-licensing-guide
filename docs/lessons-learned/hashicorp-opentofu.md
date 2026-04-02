# HashiCorp and the OpenTofu Fork

**Year:** 2023

**Lesson:** The community will fork, faster than you think

## What Happened

HashiCorp built some of the most important infrastructure tools of the cloud era: Terraform, Vault, Consul, Nomad. All were open source under [MPL 2.0](../licenses/copyleft/mpl.md). Terraform, in particular, became the standard for infrastructure-as-code.

In August 2023, HashiCorp announced they were relicensing everything from MPL 2.0 to the Business Source License (BSL).[^hashicorp-bsl]

BSL is explicitly [not open source](../licenses/other/source-available.md). It restricts commercial use—specifically, it prohibits offering HashiCorp software as a competitive service. After four years, the code converts to a permissive license, but the current version is always restricted.

The terraform community had 11 days warning.

!!! terminal inline end ""
    Company releases open source. It becomes valuable. Company tries to capture that value. Community forks. This is the new equilibrium.

## The Fork

The response was immediate.

Within two weeks, the OpenTofu project launched—a fork of the last MPL-licensed Terraform.[^opentofu] By September, OpenTofu had joined the Linux Foundation.[^opentofu-lf] By January 2024, they released OpenTofu 1.6, their first stable version.

The speed was unprecedented. What might have taken months or years happened in weeks.

## Why It Happened So Fast

### Pre-existing frustration

The community had concerns about HashiCorp's stewardship before the relicensing. The Terraform provider ecosystem had friction with HashiCorp's registry policies. Trust was already eroding.

### Corporate backing

Multiple companies—Gruntwork, Spacelift, env0, Scalr—had built businesses on Terraform. The license change threatened their existence. They had strong incentives to fund and promote an alternative.

### The Linux Foundation

The Linux Foundation provided instant legitimacy and infrastructure. OpenTofu wasn't just a GitHub repo—it was a foundation project with governance, legal protection, and organizational support.

### Terraform's architecture

Terraform's plugin architecture meant the provider ecosystem wasn't tied to HashiCorp's code. Providers could work with OpenTofu without modification. The ecosystem was more portable than it appeared.

## HashiCorp's Position

HashiCorp argued:

- BSL still allows most uses—only competitive commercial services are restricted
- They needed to protect their business from cloud providers
- The relicensing was necessary for long-term investment in the tools

These arguments echoed MongoDB and Elastic. The pattern is familiar.

## The Current State

The story didn't end with a fork.

In April 2024, IBM announced it was acquiring HashiCorp for $6.4 billion.[^ibm-acquisition]  The deal closed in early 2025, and IBM began integrating Terraform into the Red Hat ecosystem.  The company that relicensed its open source tools to protect its business ended up selling the business entirely.

Both projects continue, but the landscape has shifted:

- **Terraform** — now an IBM/Red Hat product, still under BSL.  IBM has signaled continued investment, but the product's future is tied to IBM's hybrid cloud strategy, not HashiCorp's original vision.
- **OpenTofu** — Linux Foundation project, under [MPL 2.0](../licenses/copyleft/mpl.md).  Now at 95%+ feature parity with Terraform, with its own divergent features like state encryption and provider-defined functions.  Fedora and other distributions have begun adopting it as their default.

OpenTofu isn't just a protest fork anymore — it's a mature alternative with independent momentum.

## The Lessons

### Fork speed has increased

The time from license change announcement to functioning fork is now measured in weeks, not years. Corporate backing, foundation infrastructure, and community organizing have matured.

### The business model problem persists

HashiCorp faced the same economics as MongoDB and Elastic. Their response was the same. The open source business model for infrastructure software remains challenged.

### Contributor agreements matter

HashiCorp could relicense because their contributor agreements permitted it. OpenTofu cannot be relicensed the same way—the Linux Foundation's structure prevents it.

If you contribute to a project, understand [what rights you're granting](../concepts/rights-and-obligations.md).

### Relicensing doesn't always save the company

HashiCorp relicensed to protect its competitive position.  Two years later, they sold to IBM for $6.4 billion.  The BSL switch may have made the company more acquirable — a cleaner commercial product, fewer open source entanglements — but it didn't preserve HashiCorp's independence.  For the community that lost their open source tools, the relicensing now looks less like a survival strategy and more like a prelude to acquisition.

### Trust is hard to rebuild

HashiCorp wasn't a villain. They made a business decision many companies have made. But the community felt betrayed—especially given the 11-day notice. The IBM acquisition added another layer — contributors who built Terraform's ecosystem saw their work absorbed into a corporate product they had no say in selling.

## For Your Decisions

When adopting infrastructure tools:

- Check the governance, not just the current license
- Single-company projects carry relicensing risk
- Have migration plans for critical dependencies (see [my software building guide](https://build.xram.net/) for more on dependency evaluation)

When building open source:

- Your contributor agreement defines what's possible later
- Community trust compounds—and so does its loss
- If you might need to relicense, structure for it early (and be transparent)

HashiCorp isn't unique. They're just the most complete example of the pattern: open source builds the community, the company captures the value, and then the company itself gets captured.  The fork survives.  The original doesn't always.

[^hashicorp-bsl]: See [HashiCorp BSL License Change](../reference/sources.md#hashicorp-bsl-license-change)
[^opentofu]: See [OpenTofu Manifesto](../reference/sources.md#opentofu-manifesto)
[^opentofu-lf]: See [Linux Foundation OpenTofu Announcement](../reference/sources.md#linux-foundation-opentofu-announcement)
[^ibm-acquisition]: See [IBM HashiCorp Acquisition](../reference/sources.md#ibm-hashicorp-acquisition)
