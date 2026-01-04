# Software Licenses

This section covers the most widely used open source licenses for software. Each license page explains the terms, typical use cases, and practical implications.

## License Families

Licenses are grouped by their philosophical approach:

### Permissive Licenses

These licenses grant maximum freedom with minimal requirements—typically just attribution.

| License | Key Characteristic | Common In |
|---------|-------------------|-----------|
| [MIT](permissive/mit.md) | Simplest and shortest | JavaScript, Ruby, general-purpose |
| [Apache 2.0](permissive/apache-2.md) | Includes patent grant | Enterprise, Java, Cloud Native |
| [BSD](permissive/bsd.md) | Academic origins | BSD systems, networking |

### Copyleft Licenses

These licenses require derivative works to preserve the same freedoms.

| License | Strength | Scope |
|---------|----------|-------|
| [GPL](copyleft/gpl.md) | Strong | Entire combined work |
| [LGPL](copyleft/lgpl.md) | Weak | Library modifications only |
| [MPL 2.0](copyleft/mpl.md) | Weak | Modified files only |

### Other Licenses

Special cases that don't fit neatly into the above categories.

| License | Category | Purpose |
|---------|----------|---------|
| [Public Domain](other/public-domain.md) | No restrictions | Maximum freedom, no attribution |
| [AGPL](other/agpl.md) | Network copyleft | Closes the "SaaS loophole" |
| [Source Available](other/source-available.md) | Not open source | Viewable but restricted |

## Choosing a License

For guidance on selecting a license for your own project, see the [Choosing a License](../guides/choosing-a-license.md) guide.

## License Identifiers

Each license has an SPDX identifier—a short, standardized code used in package managers and license scanners:

- `MIT` - MIT License
- `Apache-2.0` - Apache License 2.0
- `GPL-3.0-only` - GNU General Public License v3.0 only
- `GPL-3.0-or-later` - GNU General Public License v3.0 or later

Using SPDX identifiers in your projects helps automated tools understand your licensing.
