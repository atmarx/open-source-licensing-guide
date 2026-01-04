# Apache License 2.0

The Apache License 2.0 is a permissive license that adds important protections beyond MIT, particularly around patents. It's favored by enterprise projects and the cloud-native ecosystem.

## At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `Apache-2.0` |
| **Type** | Permissive |
| **Patent Grant** | Yes |
| **Copyleft** | No |
| **License Length** | ~2,500 words |

## What It Allows

- :material-check: Commercial use
- :material-check: Modification
- :material-check: Distribution
- :material-check: Private use
- :material-check: Sublicensing
- :material-check: Patent use

## What It Requires

- :material-alert: Include copyright notice
- :material-alert: Include license text
- :material-alert: Document changes to the code
- :material-alert: Include NOTICE file (if present)

## What It Prohibits

- :material-close: Holding authors liable
- :material-close: Using trademarks
- :material-close: Patent litigation against contributors

## Key Points

### Explicit Patent Grant

The defining feature of Apache 2.0 is its patent clause. Every contributor grants you a license to any patents they hold that cover the code they contributed. This provides meaningful protection for users.

!!! info "Patent Retaliation Clause"
    If you sue anyone over patent infringement related to the software, you lose your patent license to the code. This discourages patent warfare.

### Change Documentation

Unlike MIT, Apache 2.0 requires you to document modifications:

> You must cause any modified files to carry prominent notices stating that You changed the files

This is typically done with comments in the modified files or in a CHANGELOG.

### The NOTICE File

Apache projects often include a NOTICE file containing attribution information. If present, you must include this file when redistributing.

### Trademark Clarity

Apache 2.0 explicitly states it does not grant trademark rights. You can use Apache-licensed code, but you can't claim association with the Apache Software Foundation or use project trademarks without permission.

## Apache 2.0 vs MIT

| Aspect | Apache 2.0 | MIT |
|--------|------------|-----|
| Patent grant | Explicit | None |
| Change notices | Required | Not required |
| NOTICE file | Must preserve | N/A |
| Length | ~2,500 words | ~170 words |
| Trademark clause | Explicit | None |

Choose Apache 2.0 over MIT when:

- Patent protection matters (enterprise, large projects)
- You want change tracking
- You're contributing to the Apache ecosystem

## Compatibility

Apache 2.0 is compatible with:

- GPL v3 (Apache code can go into GPL v3, not vice versa)
- MIT, BSD (can combine freely)
- Most permissive licenses

Apache 2.0 is **not compatible** with GPL v2 due to the patent clause. This was a significant issue historically but matters less now that GPL v3 exists.

## When to Use Apache 2.0

Apache 2.0 is a good choice when:

- You want permissive licensing with patent protection
- You're building enterprise or cloud infrastructure
- Your project may receive contributions from many organizations
- You want clear trademark boundaries

## Notable Projects Using Apache 2.0

- Kubernetes
- Android (AOSP)
- TensorFlow
- Apache HTTP Server
- Kafka
- Spark
- OpenTelemetry
- Swift
