# Elasticsearch and the OpenSearch Fork

**Year:** 2021
**Lesson:** License changes spawn forks, and forks can succeed

## What Happened

Elastic, the company behind Elasticsearch and Kibana, changed their license.[^elastic-change] These tools had been Apache 2.0—about as permissive as it gets. Suddenly they were dual-licensed under SSPL and the Elastic License 2.0.

Neither is open source. The Apache-licensed Elasticsearch was gone.

Their stated reason: Amazon. AWS offered Elasticsearch as a managed service and had even created their own distribution called "Open Distro for Elasticsearch." Elastic felt AWS was benefiting from their work without contributing back.

## Amazon's Response

AWS did something unexpected: they forked.

Within weeks of Elastic's announcement, AWS launched OpenSearch—a fork of the last Apache-licensed Elasticsearch and Kibana.[^opensearch] They committed to maintaining it under Apache 2.0 and created the OpenSearch project with independent governance.

This wasn't just a corporate fork. AWS invested in community building, accepted external contributions, and positioned OpenSearch as the community continuation of what Elasticsearch used to be.

## The Fallout

### Two competing projects

The search engine market now has:

- **Elasticsearch** — Elastic's product, under restrictive licenses
- **OpenSearch** — AWS-backed fork, under Apache 2.0

Both are actively developed. Both have users. The community split.

### Cloud provider detente

Other cloud providers (like AWS) can offer OpenSearch. They cannot offer Elasticsearch without licensing agreements.

This was exactly Elastic's goal—but the cost was fragmenting the ecosystem.

### Community trust

Elastic had positioned themselves as open source champions for years. The relicensing felt like a betrayal to many users. The AWS fork gave those users somewhere to go.

## The Ironies

### AWS as open source defender

Amazon Web Services—frequently criticized for profiting from open source without contributing—became the defender of open source licensing in this story. They forked to preserve Apache 2.0, funded ongoing development, and built community governance.

The company that many saw as the problem became, in this instance, part of the solution.

### The trademark fight

Elastic owned the "Elasticsearch" trademark. AWS couldn't use it. Hence "OpenSearch"—a rebrand for a fork. Trademarks, not copyright, determined what the fork could be called.

### Elastic's business continued

Elastic didn't collapse. Their stock recovered. Their business model shifted but survived. The license change accomplished its business goal, even as it cost community goodwill.

## The Lessons

### Forks are real threats

Before this, many assumed that forking a major project was impractical—too much engineering effort, too little community interest. OpenSearch proved otherwise. With sufficient resources and motivation, forks can succeed.

### Trademarks matter

Elastic controlled "Elasticsearch." AWS had to rebrand. If you're building an open source project, your trademark is separate from your copyright and license. Protect it.

### Community governance prevents this

Single-company projects can relicense at will. Foundation-governed projects (Apache, Linux, Mozilla) cannot—the contribution agreements don't permit it. If you're choosing a dependency, governance structure is a risk factor.

### The cloud wars reshape open source

This wasn't really about licensing philosophy. It was about business competition between Elastic and AWS. Open source licensing became a battleground for corporate strategy.

## What This Means For You

When adopting infrastructure software:

- Check the license AND the governance
- Single-company projects can change licenses
- Foundation projects have stronger guarantees
- Have a contingency plan (could you switch to a fork?)

When building open source:

- Decide early whether you want single-company control or community governance
- Understand that permissive licensing means cloud providers can compete with you
- If that's unacceptable, consider your licensing carefully from the start—changing later has costs

[^elastic-change]: See [Elastic License Change Announcement](../reference/sources.md#elastic-license-change-announcement)
[^opensearch]: See [OpenSearch Fork Announcement](../reference/sources.md#opensearch-fork-announcement)
