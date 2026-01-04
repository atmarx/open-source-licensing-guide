# GNU Affero General Public License (AGPL)

The AGPL is the GPL's stronger sibling. It extends copyleft to cover a loophole in the GPL: software provided over a network. If you run modified AGPL software as a web service, you must provide source to users of that service.

## At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `AGPL-3.0-only` / `AGPL-3.0-or-later` |
| **Type** | Strong copyleft (network) |
| **Patent Grant** | Yes |
| **Scope** | Entire work + network provision |
| **Distribution Trigger** | Yes, including network use |

## What It Allows

- :material-check: Commercial use
- :material-check: Modification
- :material-check: Distribution
- :material-check: Private use

## What It Requires

- :material-alert: Disclose source code
- :material-alert: License derivatives under AGPL
- :material-alert: **Provide source to network users**
- :material-alert: Include copyright and license
- :material-alert: Document changes

## What It Prohibits

- :material-close: Sublicensing under different terms
- :material-close: Holding authors liable
- :material-close: Tivoization

## The "Network Copyleft" Provision

Here's the key difference from GPL. Section 13 of AGPL states:

> if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network... an opportunity to receive the Corresponding Source

### What this means:

```
GPL:
Server with modified code → Users access via web → No source required
(No "distribution" occurs)

AGPL:
Server with modified code → Users access via web → Source required
(Network access triggers obligation)
```

The AGPL closes what free software advocates call the "SaaS loophole" or "ASP loophole."

## Why AGPL Exists

When the GPL was written, software was distributed on physical media. If you used it, you had a copy. The GPL's obligations triggered on distribution.

Cloud computing changed this. Companies could:

1. Take GPL software
2. Modify it heavily
3. Run it as a web service
4. Never "distribute" anything
5. Keep all modifications proprietary

The AGPL addresses this by making network access equivalent to distribution.

## AGPL in Practice

### What counts as "interacting remotely"?

Users must interact with the software over a network. Examples:

- Web applications
- API services
- SaaS platforms
- Any service where users send data and receive responses

### What must you provide?

- Complete corresponding source code
- Build scripts and dependencies needed to compile
- A way for users to obtain the source (download link, offer to provide)

### Common implementations:

- Link to source in web interface footer
- `/source` endpoint that provides download
- Link in API responses
- Link in documentation

## Who Uses AGPL?

Projects choose AGPL strategically:

### Open source projects wanting SaaS contributions back

If a cloud company runs your software as a service, AGPL ensures they share improvements.

### Dual-licensing businesses

AGPL can be the "open source" option, with commercial licenses available for companies that don't want AGPL obligations.

### Examples:
- **MongoDB** (before SSPL change)
- **Grafana** (partially)
- **Nextcloud**
- **Mastodon**

## Corporate Wariness

Many companies have policies against AGPL:

- Google bans AGPL in its codebase
- Many enterprises treat AGPL as radioactive

This is by design—if you don't want to share source, don't use AGPL code. But it limits adoption compared to more permissive licenses.

## AGPL vs GPL

| Aspect | GPL | AGPL |
|--------|-----|------|
| Distribution triggers | Yes | Yes |
| Network use triggers | No | Yes |
| Corporate acceptance | Cautious | Very limited |
| SaaS protection | None | Strong |

## Criticism and Controversy

### "Too broad"

Some argue AGPL's network provision is vague. What counts as "interacting"? At what level of integration?

### "Unclear boundaries"

If your proprietary application uses an AGPL library, what's required? The boundaries are less clear than GPL's.

### "Hurts adoption"

The corporate bans mean AGPL projects get less contribution from large tech companies.

## When to Use AGPL

AGPL is a good choice when:

- You're building software likely to be run as a service
- You want cloud providers to contribute back
- You're using dual licensing as a business model
- You believe strongly in software freedom principles

Consider alternatives if:

- Wide corporate adoption is important
- You're building a library (LGPL might fit better)
- The network provision doesn't match your use case
