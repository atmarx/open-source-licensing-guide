# Redis Relicensing

**Year:** 2024

**Lesson:** The pattern continues

## What Happened

In March 2024, Redis Ltd. announced they were changing the license for Redis from [BSD-3-Clause](../licenses/permissive/bsd.md) to a dual license: RSALv2 (Redis Source Available License) and [SSPL](../licenses/other/source-available.md).[^redis-change]

!!! terminal inline end ""
    I've stopped being surprised. The pattern is locked in. The question isn't *whether* this can happen to a project, but *when*.

Neither is open source. After more than 15 years as one of the most permissively licensed infrastructure projects, Redis was no longer open source.

The stated reason was, by now, familiar: cloud providers were offering Redis as a service without contributing back or compensating Redis Ltd.

## The Immediate Response

### Valkey

AWS, Google, Oracle, Ericsson, and Snap announced Valkey—a fork of the last BSD-licensed Redis, to be hosted at the Linux Foundation.[^valkey] Within days, the project had major corporate backing and a path to independence.

The [playbook from OpenSearch and OpenTofu](./hashicorp-opentofu.md) was executed again, even faster.

### Redict

A separate fork, Redict, launched under the [LGPL](../licenses/copyleft/lgpl.md). It aimed for stronger [copyleft](../concepts/permissive-vs-copyleft.md) protection while remaining open source—a different philosophical choice than Valkey's permissive approach.

### Linux distribution responses

Fedora, Debian, and others began discussing removal of Redis and inclusion of Valkey. The distribution machinery that routes software to millions of users started shifting.

## Why This Matters

### The pattern is now undeniable

| Project | Year | Old License | New License | Fork |
|---------|------|-------------|-------------|------|
| MongoDB | 2018 | AGPL | SSPL | (various) |
| Elasticsearch | 2021 | Apache 2.0 | SSPL/Elastic | OpenSearch |
| Terraform | 2023 | MPL | BSL | OpenTofu |
| Redis | 2024 | BSD | RSALv2/SSPL | Valkey |

This is no longer *surprising*. It's **expected**.

### Fork response time keeps shrinking

MongoDB's community response took months to coalesce. Elasticsearch's fork (OpenSearch) emerged in weeks. OpenTofu launched in weeks. Valkey was announced within days of Redis's relicensing.

The infrastructure for forking major projects now exists. The playbook is established. Companies and foundations are ready to act.

### The BSD license didn't protect anyone

Redis was [BSD-licensed](../licenses/permissive/bsd.md)—as [permissive](../concepts/permissive-vs-copyleft.md) as possible. It didn't prevent the relicensing. Permissive licensing means the *current* code is free, but says nothing about future versions.

Only governance protects against relicensing, not license choice.

## Redis Ltd's Position

Redis Ltd argued:

- They need sustainable economics to continue developing Redis
- Cloud providers benefit disproportionately from their work
- The source is still available; most users are unaffected
- Only commercial Redis-as-a-Service competitors are restricted

These arguments are reasonable. They're also the same arguments every other relicensing company has made.

## The Community Perspective

Long-time Redis users felt betrayed:

- They contributed to, evangelized, and built on a BSD-licensed project
- Their contributions are now under a license they didn't choose
- The project they trusted changed the rules

Some users don't care—they use managed Redis services anyway, or their use case isn't affected. But the developers who built the Redis ecosystem feel differently.

## The Lessons

### If it can happen to Redis, it can happen to anything

Redis was *the* example of permissive open source success. Widely used, simply licensed, well-maintained. If Redis can relicense, no single-company project is safe.

### Fork infrastructure is mature

The combination of:
- Git (code is trivially forkable)
- Linux Foundation (instant governance and legitimacy)
- Corporate sponsors (funding and engineering)
- Cloud providers (operational expertise and motivation)

...means that forking is now a reliable response to relicensing.

### We're in a new equilibrium

The old model: company releases open source, builds business, everyone benefits.

The new model: company releases open source, cloud providers capture value, company relicenses, community forks, two projects compete.

This isn't a crisis anymore. It's how things work now.

## What To Do About It

**When adopting:**
- Assume single-company projects might relicense
- Check if a foundation fork exists or is likely
- Have migration plans for critical dependencies

**When building:**
- If you want to prevent relicensing, use foundation governance from the start
- If you might need to relicense later, be transparent about it early
- Understand that trust, once lost, doesn't return

**When contributing:**
- Understand what rights your contributions grant
- Consider whether the project's governance protects your interests
- Foundation projects have stronger contributor protections

Redis won't be the last. The question isn't whether this will happen again, but when and to which project.

[^redis-change]: See [Redis Dual License Change](../reference/sources.md#redis-dual-license-change)
[^valkey]: See [Linux Foundation Valkey Launch](../reference/sources.md#linux-foundation-valkey-launch)
