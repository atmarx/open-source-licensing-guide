# VMware, Broadcom, and the Proxmox Moment

**Year:** 2023–present

**Lesson:** Proprietary licensing means no escape hatch

## What Happened

Every other case in this section tells the same story: an open source company changes its license, the community forks, life goes on. This one is different. This is what happens when there was never an open source escape hatch in the first place.

VMware built the virtualization industry. For two decades, vSphere was the hypervisor — the thing running your VMs, your infrastructure, your business. It was proprietary software, always had been. But it worked, the ecosystem was vast, and the switching costs were enormous.

On November 22, 2023, Broadcom completed its $61 billion acquisition of VMware.[^broadcom-acquisition] What followed was a masterclass in how proprietary licensing enables corporate extraction.

## The Enshittification

Within 90 days of closing, Broadcom dismantled nearly everything that made VMware work for its customers.

### Perpetual licenses — gone

December 2023: Broadcom announced VMware would no longer sell perpetual licenses.[^broadcom-perpetual] Subscription only, going forward. Every existing perpetual license holder would be migrated. By March 2025, Broadcom's CEO confirmed 60% of VMware users had been moved to subscriptions.

### Free ESXi — gone

February 2024: The free ESXi hypervisor was discontinued.[^free-esxi-eol] This was the product that taught a generation of sysadmins virtualization — used in homelabs, classrooms, and small businesses everywhere. Broadcom killed it because it didn't generate revenue.

### Product bundling — forced

VMware's portfolio was collapsed into two bundles: VMware Cloud Foundation (everything) and VMware vSphere Foundation (less everything). Pricing shifted from per-socket to per-core with increased minimums. Customers had to buy products they didn't need to keep the ones they did.

### Price increases — extreme

Customers reported renewal quotes 200–500% higher than their previous spend. Some saw increases of 800–1,500%.[^ecco-report] AT&T claimed in court filings that Broadcom proposed a 1,050% price increase — and estimated it would cost $50 million just to migrate away.[^att-lawsuit]

### Partner ecosystem — gutted

On December 23, 2023, Broadcom emailed VMware partners that their programs were ending. By February, roughly 2,200 of 4,000+ partners had been terminated. The replacement was an invitation-only program with approximately 50 elite global partners.

### Workforce — cut

Nearly 3,000 employees were laid off within weeks of the acquisition closing, with additional rounds through 2024.

!!! terminal inline end ""
    The cost of switching was always VMware's moat. Broadcom just decided to charge rent for the moat.

## Why Customers Were Trapped

This is the licensing lesson. VMware was proprietary software. Every customer's right to use the software came from a license agreement that the rights holder could change.

When Broadcom became the rights holder, they changed the terms. Perpetual licenses became subscriptions. Prices went up 10x. Product bundles were restructured. And customers had exactly two choices: **pay or migrate.**

There was no fork. There was no community version to fall back to. There was no right to continued use on the old terms. The switching costs — retraining staff, migrating workloads, requalifying infrastructure — meant most customers paid, at least initially.

This is what vendor lock-in looks like at $61 billion scale.

## The Open Source Alternative

Enter Proxmox.

Proxmox Virtual Environment has existed since 2005 — a KVM/QEMU-based virtualization platform built on Debian, licensed under [AGPL v3](../licenses/other/agpl.md).[^proxmox] For years it was the platform of choice in homelabs, European hosting providers, and cost-conscious shops. VMware admins knew it existed but rarely had a reason to switch.

Broadcom gave them one.

### The migration

Proxmox moved fast. Their April 2024 release (VE 8.2) shipped a VMware Import Wizard — a native tool for migrating ESXi virtual machines directly to Proxmox, supporting ESXi versions 6.5 through 8.0.[^proxmox-import] VMs could start running while data was still transferring.

In August 2024, Veeam added Proxmox as a first-class hypervisor in their backup platform, alongside vSphere and Hyper-V.[^veeam-proxmox] For enterprise shops where "but what about backups?" was the last objection, that objection was gone.

Proxmox VE 9.0 followed in August 2025, rebased on Debian 13 with enhanced migration tools and a new Datacenter Manager for multi-cluster deployments — explicitly targeting the enterprise VMware shops now looking for exits.[^proxmox-9]

### The numbers

The growth has been staggering:

- **1.5+ million installed hosts** across 140+ countries
- **650% growth** over seven years
- **16% global market mindshare** in server virtualization (up from ~10% in 2023)
- Gartner reported **340% year-over-year increase** in Proxmox evaluations
- **43% hypervisor adoption** in self-hosted environments

### Why AGPL matters here

Proxmox's license is the reason this story has a different ending than VMware's.

The software is free. All of it — every feature, no restrictions. Subscriptions buy you enterprise-tested updates and support, not access to the software itself. If Proxmox Server Solutions GmbH were acquired tomorrow and the new owner tried the Broadcom playbook, anyone could fork the code and continue. The [AGPL](../licenses/other/agpl.md) guarantees it.

The AGPL goes further than the GPL — if someone runs a modified Proxmox as a network service, they must share the source. This prevents the "SaaS loophole" that drove the SSPL and BSL licensing changes we see in other cases. But more importantly for this story, it prevents what happened to VMware customers: total dependence on a single vendor's goodwill.

## The Broader Fallout

Proxmox wasn't the only beneficiary. Nutanix saw revenue jump 16% year-over-year, added 2,700+ new customers in fiscal 2025, and explicitly credited VMware defectors on earnings calls.[^nutanix] Microsoft pushed Hyper-V for Azure hybrid scenarios. Even OpenStack saw renewed interest.

In Europe, regulators took notice. CISPE (Cloud Infrastructure Service Providers in Europe) filed action at the EU General Court in July 2025 to annul the European Commission's original approval of the acquisition.[^cispe] A separate antitrust complaint followed in January 2026.

A late-2024 survey of VMware customers found **98% were considering or already using alternatives.** Gartner predicted 35% of VMware workloads would migrate to alternatives by 2028.

## The Lessons

### Proprietary licensing is a one-way door

Every VMware customer accepted license terms that gave the vendor unilateral power to change pricing, bundling, and availability. This is normal for proprietary software. It's also a risk that most organizations don't price into their adoption decisions until it's too late.

### Open source licensing protects users, not just developers

Most of the cases in this guide focus on how licenses affect developers and companies. The VMware story shows the user side. AGPL doesn't just keep Proxmox's code available — it guarantees that no acquisition, no corporate restructuring, no change of ownership can take the software away from the people running it.

### Switching costs are the real lock-in

VMware's license wasn't complicated. The lock-in was operational: years of accumulated infrastructure, tooling, training, and institutional knowledge. Broadcom bet that switching costs would keep customers paying 10x more. For many, they were right — at least in the short term.

### The free tier was the pipeline

Killing free ESXi was tactically rational (it didn't generate revenue) and strategically catastrophic (it generated the next generation of VMware administrators). Proxmox's model — everything free, pay for support — captures this pipeline effect without the vulnerability. You can't kill what you don't control.

### Acquisition is a licensing event

When Broadcom bought VMware, every customer's relationship with the software changed overnight. The license was the same, but the licensor was different. For proprietary software, that distinction matters enormously. For AGPL software, it doesn't — the license outlives the company.

## For Your Decisions

When adopting infrastructure software:

- Treat proprietary licensing as a risk factor, not just a cost
- Calculate switching costs honestly — they're the real lock-in
- Prefer platforms where the software license survives a change of ownership
- An open source alternative that's "good enough" today may be the only option tomorrow

When evaluating open source alternatives:

- [AGPL](../licenses/other/agpl.md) and [GPL](../licenses/copyleft/gpl.md) provide the strongest user protections against vendor capture
- Community governance (foundations, multiple maintainers) adds a layer beyond licensing
- The "free tier" isn't charity — it's the pipeline. Sustainable open source funds development through support, not access restrictions

The VMware story is still unfolding. But the licensing lesson is already clear: when your infrastructure runs on software someone else controls, you are one acquisition away from having your costs dictated to you. Open source licensing — real open source, with copyleft protections — is the only structural defense against this.

[^broadcom-acquisition]: See [Broadcom VMware Acquisition](../reference/sources.md#broadcom-vmware-acquisition)
[^broadcom-perpetual]: See [Broadcom Ends VMware Perpetual Licenses](../reference/sources.md#broadcom-ends-vmware-perpetual-licenses)
[^free-esxi-eol]: See [Free ESXi Hypervisor Discontinued](../reference/sources.md#free-esxi-hypervisor-discontinued)
[^ecco-report]: See [ECCO Broadcom Licensing Report](../reference/sources.md#ecco-broadcom-licensing-report)
[^att-lawsuit]: See [AT&T Broadcom VMware Lawsuit](../reference/sources.md#att-broadcom-vmware-lawsuit)
[^proxmox]: See [Proxmox Virtual Environment](../reference/sources.md#proxmox-virtual-environment)
[^proxmox-import]: See [Proxmox VE 8.2 VMware Import Wizard](../reference/sources.md#proxmox-ve-82-vmware-import-wizard)
[^veeam-proxmox]: See [Veeam Proxmox VE Support](../reference/sources.md#veeam-proxmox-ve-support)
[^proxmox-9]: See [Proxmox VE 9.0 Release](../reference/sources.md#proxmox-ve-90-release)
[^nutanix]: See [Nutanix VMware Migration Growth](../reference/sources.md#nutanix-vmware-migration-growth)
[^cispe]: See [CISPE Broadcom Acquisition Challenge](../reference/sources.md#cispe-broadcom-acquisition-challenge)
