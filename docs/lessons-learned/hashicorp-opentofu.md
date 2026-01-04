# HashiCorp and the OpenTofu Fork

**Year:** 2023
**Lesson:** The community will fork, faster than you think

## What Happened

HashiCorp built some of the most important infrastructure tools of the cloud era: Terraform, Vault, Consul, Nomad. All were open source under MPL 2.0. Terraform, in particular, became the standard for infrastructure-as-code.

In August 2023, HashiCorp announced they were relicensing everything from MPL 2.0 to the Business Source License (BSL).[^hashicorp-bsl]

BSL is explicitly not open source. It restricts commercial use—specifically, it prohibits offering HashiCorp software as a competitive service. After four years, the code converts to a permissive license, but the current version is always restricted.

The terraform community had 11 days warning.

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

Both projects continue:

- **Terraform** — HashiCorp's product, under BSL
- **OpenTofu** — Linux Foundation project, under MPL 2.0

OpenTofu has diverged from Terraform, adding features HashiCorp rejected. The projects are no longer fully compatible.

## The Lessons

### Fork speed has increased

The time from license change announcement to functioning fork is now measured in weeks, not years. Corporate backing, foundation infrastructure, and community organizing have matured.

### The business model problem persists

HashiCorp faced the same economics as MongoDB and Elastic. Their response was the same. The open source business model for infrastructure software remains challenged.

### Contributor agreements matter

HashiCorp could relicense because their contributor agreements permitted it. OpenTofu cannot be relicensed the same way—the Linux Foundation's structure prevents it.

If you contribute to a project, understand what rights you're granting.

### Trust is hard to rebuild

HashiCorp wasn't a villain. They made a business decision many companies have made. But the community felt betrayed—especially given the 11-day notice. Whether Terraform or OpenTofu "wins" long-term, the relationship between HashiCorp and its community is permanently changed.

## For Your Decisions

When adopting infrastructure tools:

- Check the governance, not just the current license
- Single-company projects carry relicensing risk
- Have migration plans for critical dependencies

When building open source:

- Your contributor agreement defines what's possible later
- Community trust compounds—and so does its loss
- If you might need to relicense, structure for it early (and be transparent)

HashiCorp isn't unique. They're just the latest example of a pattern that will continue.

[^hashicorp-bsl]: See [HashiCorp BSL License Change](../reference/sources.md#hashicorp-bsl-license-change)
[^opentofu]: See [OpenTofu Manifesto](../reference/sources.md#opentofu-manifesto)
[^opentofu-lf]: See [Linux Foundation OpenTofu Announcement](../reference/sources.md#linux-foundation-opentofu-announcement)
