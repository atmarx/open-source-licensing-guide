# GNU General Public License (GPL)

The GPL is the most important copyleft license and one of the most influential licenses in software history. Created by Richard Stallman and [the FSF](https://www.fsf.org/), it embodies the philosophy that software freedom must be preserved.

## Versions

| Version | SPDX Identifier | Year | Key Addition |
|---------|----------------|------|--------------|
| GPL v2 | `GPL-2.0-only` / `GPL-2.0-or-later` | 1991 | Established copyleft |
| GPL v3 | `GPL-3.0-only` / `GPL-3.0-or-later` | 2007 | Patents, anti-Tivoization |

Both versions remain in wide use. Some projects specify "GPL v2 or later," giving users the choice.

## At a Glance

| Attribute | Value |
|-----------|-------|
| **Type** | Strong copyleft |
| **Patent Grant** | Yes (v3 only) |
| **Scope** | Entire combined work |
| **Distribution Trigger** | Yes |

## What It Allows

- :material-check: Commercial use
- :material-check: Modification
- :material-check: Distribution
- :material-check: Private use
- :material-check: Patent use (v3)

## What It Requires

- :material-alert: Disclose source code (when distributing)
- :material-alert: License derivatives under GPL
- :material-alert: Include copyright and license
- :material-alert: Document changes

## What It Prohibits

- :material-close: Sublicensing under different terms
- :material-close: Holding authors liable
- :material-close: Tivoization (v3)

## The Core Mechanism

The GPL's power comes from copyright law. When you modify GPL code, your modifications become a "derivative work." Copyright law gives the original author control over derivative works. The GPL uses this control to require:

1. If you distribute the derivative work...
2. You must provide source code...
3. Under the same GPL terms

This is "copyleft"—using copyright to ensure freedom rather than restrict it.

```
GPL Code ──► Your Modifications ──► Distributed Binary
                                          │
                                          ▼
                              Must provide source code
                              Must use GPL license
```

## What Triggers GPL Obligations?

### Distribution is the trigger

GPL obligations only apply when you **distribute** the software—give it to someone else. You can:

- Modify GPL code internally with no obligations
- Run modified GPL code on your servers with no obligations
- Use GPL tools to build proprietary software

But the moment you distribute—give binaries to customers, publish downloads, ship devices—you must provide source and GPL rights.

### What counts as a "derivative work"?

This is the crucial (and contested) question:

| Scenario | Likely Derivative? |
|----------|-------------------|
| Modifying GPL source directly | Yes |
| Statically linking GPL library | Yes |
| Dynamically linking GPL library | Usually yes (disputed) |
| Separate process communication (pipes, sockets) | Usually no |
| Plugins loaded into GPL program | Depends on integration |
| Aggregating on same media | No |

The FSF takes an expansive view; others interpret more narrowly. When in doubt, consult legal counsel.

## GPL v2 vs GPL v3

### Patent Grant (v3)

GPL v3 includes an explicit patent grant. Contributors license their patents to users, and patent retaliation terminates your rights.

### Anti-Tivoization (v3)

GPL v3 addresses "Tivoization"—using hardware restrictions to prevent users from running modified software. Named after TiVo devices that ran modified Linux but prevented users from installing their own modifications.

GPL v3 requires that if you distribute GPL software in a device, you must provide whatever is needed to install modified versions (keys, instructions, etc.).

### Compatibility (v3)

GPL v3 is compatible with Apache 2.0; GPL v2 is not. This resolved a significant historical friction.

## "GPL v2 only" vs "GPL v2 or later"

Some projects specify exactly GPL v2 (like the Linux kernel). Others allow "v2 or any later version," giving users flexibility to use v3 terms if preferred.

The Linux kernel's "GPL v2 only" stance means it cannot incorporate GPL v3 code, and GPL v3 projects cannot use Linux-specific code.

## Commercial Use

GPL allows commercial use. You can:

- Sell GPL software
- Include GPL software in commercial products
- Charge for support, hosting, customization

What you cannot do is distribute without providing source and GPL rights. Many companies successfully commercialize GPL software through:

- **Dual licensing:** GPL for open source, paid license for proprietary use
- **Services:** Support, hosting, training
- **Open core:** GPL base, proprietary add-ons

## Notable Projects Using GPL

### GPL v2
- Linux kernel
- Git
- WordPress
- MariaDB

### GPL v3
- GNU Bash
- GIMP
- GNU Coreutils
- GCC (recent versions)
