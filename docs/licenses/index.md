<div class="hero hero-half" markdown>
  <img src="../assets/images/licenses-hero.webp" alt="Art deco illustration of legal documents">
  <div class="hero-overlay">
    <h1>Software Licenses</h1>
    <p>The agreements that govern code</p>
  </div>
</div>

This section covers the most widely used open source licenses for software. Each license page explains the terms, typical use cases, and practical implications.

## License Families

Licenses are grouped by their philosophical approach:

### Permissive Licenses

These licenses grant maximum freedom with minimal requirements—typically just attribution.

<div class="grid cards" markdown>

-   :material-feather:{ .lg .middle } **[MIT](permissive/mit.md)**

    ---

    Simplest and shortest. The default for JavaScript, Ruby, and general-purpose projects.

-   :material-shield-check:{ .lg .middle } **[Apache 2.0](permissive/apache-2.md)**

    ---

    Includes patent grant. Standard in enterprise, Java, and Cloud Native ecosystems.

-   :material-school:{ .lg .middle } **[BSD](permissive/bsd.md)**

    ---

    Academic origins. Common in BSD systems and networking projects.

</div>

### Copyleft Licenses

These licenses require derivative works to preserve the same freedoms.

<div class="grid cards" markdown>

-   :material-shield-lock:{ .lg .middle } **[GPL](copyleft/gpl.md)**

    ---

    Strong copyleft. Applies to the entire combined work.

-   :material-shield-half-full:{ .lg .middle } **[LGPL](copyleft/lgpl.md)**

    ---

    Weak copyleft. Only library modifications must be shared.

-   :material-file-document-check:{ .lg .middle } **[MPL 2.0](copyleft/mpl.md)**

    ---

    Weak copyleft. Only modified files must be shared.

</div>

### Other Licenses

Special cases that don't fit neatly into the above categories.

<div class="grid cards" markdown>

-   :material-infinity:{ .lg .middle } **[Public Domain](other/public-domain.md)**

    ---

    No restrictions. Maximum freedom, no attribution required.

-   :material-web:{ .lg .middle } **[AGPL](other/agpl.md)**

    ---

    Network copyleft. Closes the "SaaS loophole" for web services.

-   :material-eye:{ .lg .middle } **[Source Available](other/source-available.md)**

    ---

    Not open source. Code is viewable but usage is restricted.

</div>

## Choosing a License

For guidance on selecting a license for your own project, see the [Choosing a License](../guides/choosing-a-license.md) guide.

## License Identifiers

Each license has an SPDX identifier—a short, standardized code used in package managers and license scanners:

- `MIT` - MIT License
- `Apache-2.0` - Apache License 2.0
- `GPL-3.0-only` - GNU General Public License v3.0 only
- `GPL-3.0-or-later` - GNU General Public License v3.0 or later

Using SPDX identifiers in your projects helps automated tools understand your licensing.
