# Source Available Licenses

"Source available" means you can see the code, but it's not open source. These licenses restrict how you can use the software in ways that violate the Open Source Definition.

!!! warning "Not Open Source"
    These licenses are explicitly **not** OSI-approved. They restrict usage in ways incompatible with open source principles. Understanding them helps avoid confusion with actual open source.

## Why "Source Available" Exists

Companies releasing source-available software typically want to:

1. **Prevent cloud providers** from offering their software as a service
2. **Protect their business** while appearing "open"
3. **Allow inspection** for security and transparency
4. **Restrict competition** from larger companies

## Common Source-Available Licenses

---

### Server Side Public License (SSPL)

Created by MongoDB after Amazon offered MongoDB as a service.

**Key restriction:** If you offer the software as a service, you must release the source code of your entire service stack—not just the database, but everything around it.

**Why it's not open source:** The "all your infrastructure" requirement goes far beyond traditional copyleft. The OSI rejected SSPL as incompatible with the Open Source Definition.

**Who uses it:** MongoDB, Graylog

---

### Business Source License (BSL / BUSL)

Created by MariaDB, used by several companies.

**Key feature:** Restrictions expire after a set period (typically 4 years), after which the code becomes open source under a permissive license.

**Typical restriction:** No commercial production use. Development, testing, and non-production use are allowed.

**Why it's not open source:** Restricts commercial use, which violates OSD requirement of no discrimination by field of endeavor.

**Who uses it:** MariaDB MaxScale, HashiCorp (Terraform, Vault, etc.), Couchbase, Sentry

---

### Elastic License 2.0

Created by Elastic after AWS launched their own Elasticsearch service.

**Key restrictions:**
- Cannot provide the software as a managed service
- Cannot circumvent license key functionality

**Why it's not open source:** Explicitly restricts use as a service.

**Who uses it:** Elasticsearch, Kibana

---

### Commons Clause

An addendum that can be applied to open source licenses to add restrictions.

**Key restriction:** Cannot sell the software or offer it as a commercial service.

**Why it's not open source:** Restricts commercial use.

**Example:** "Apache 2.0 with Commons Clause" is **not** Apache 2.0.

---

### Fair Source License

Attempts to find middle ground with staged openness.

**Key feature:** Free up to a certain number of users/developers, then requires commercial license.

**Why it's not open source:** Discriminates based on use.

---

## The Cloud Provider Conflict

The rise of source-available licensing is largely a response to cloud providers:

1. Company releases open source database/tool
2. AWS/Azure/GCP offer it as a managed service
3. Cloud provider captures value without contributing
4. Original company struggles to compete
5. Company switches to restrictive license

This has created an ongoing tension between open source principles and business sustainability.

## Recognizing Source-Available

Be alert to:

- **Recent license changes** - If a project switched licenses, check why
- **Non-OSI-approved licenses** - Verify with the OSI license list
- **"Open Source" in marketing** - Compare against actual license
- **Additional restrictions** - Any limit on commercial use or hosting

## Implications for Users

### If you're evaluating software:

| Consideration | Open Source | Source-Available |
|--------------|-------------|------------------|
| Internal use | Generally fine | Read carefully |
| Managed service | Generally fine | Usually prohibited |
| Modifications | Can distribute | May be restricted |
| Long-term risk | Low | License may change again |

### If you're choosing a license:

Source-available licenses may:

- Reduce adoption and contributions
- Create confusion and distrust
- Limit community growth
- Signal business model over community

## The Terminology Problem

"Open source" is not a trademark, so anyone can claim it. Watch for:

- **"Open source at heart"**
- **"Source available open source"**
- **"Open core with source-available extensions"**
- **"Practically open source"**

If it's not OSI-approved, it's not open source by the accepted definition.

## Projects That Changed Licenses

| Project | Was | Became | Year |
|---------|-----|--------|------|
| MongoDB | AGPL | SSPL | 2018 |
| Elasticsearch | Apache 2.0 | Elastic License + SSPL | 2021 |
| Terraform | MPL 2.0 | BSL | 2023 |
| Vault | MPL 2.0 | BSL | 2023 |
| Redis | BSD | RSALv2 + SSPL | 2024 |

These changes often spawn forks under the original license (OpenSearch from Elasticsearch, OpenTofu from Terraform).
