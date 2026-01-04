# BSD Licenses

The BSD licenses are a family of permissive licenses originating from the University of California, Berkeley. They're closely related to MIT but have an academic heritage and some historical quirks.

## The BSD Family

There are several BSD license variants:

| Variant | Clauses | Key Difference |
|---------|---------|----------------|
| **2-Clause BSD** (Simplified) | 2 | Just attribution and disclaimer |
| **3-Clause BSD** (New BSD) | 3 | Adds non-endorsement clause |
| **4-Clause BSD** (Original) | 4 | Adds advertising clause (obsolete) |
| **0-Clause BSD** (Zero BSD) | 0 | No requirements at all |

The 2-Clause and 3-Clause variants are in common use today.

---

## 2-Clause BSD (Simplified BSD)

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `BSD-2-Clause` |
| **Type** | Permissive |
| **Patent Grant** | No |
| **Copyleft** | No |

### Key Terms

Essentially identical to MIT:

1. Retain copyright notice and license in source distributions
2. Retain copyright notice and disclaimer in binary distributions

That's it. Functionally equivalent to MIT with slightly different wording.

---

## 3-Clause BSD (New BSD, Modified BSD)

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `BSD-3-Clause` |
| **Type** | Permissive |
| **Patent Grant** | No |
| **Copyleft** | No |

### Key Terms

The same as 2-Clause BSD, plus:

3. **Non-endorsement clause:** You may not use the project name or contributor names to endorse or promote products derived from the software without written permission.

This third clause provides explicit protection against implied endorsement. MIT achieves similar effect through general trademark law, but BSD makes it explicit.

---

## 4-Clause BSD (Original BSD)

!!! warning "Deprecated"
    The 4-Clause BSD license is considered obsolete and should not be used for new projects.

The original BSD license included an "advertising clause" requiring all advertising materials mentioning the software to include a specific acknowledgment. When many BSD-licensed projects were combined, this created "advertising clause hell"—pages of required acknowledgments.

The University of California officially dropped this clause in 1999. Projects using the 4-clause version should consider updating.

---

## 0-Clause BSD (Zero BSD)

### At a Glance

| Attribute | Value |
|-----------|-------|
| **SPDX Identifier** | `0BSD` |
| **Type** | Public domain equivalent |
| **Patent Grant** | No |
| **Copyleft** | No |

Zero BSD removes all requirements, including attribution. It's functionally equivalent to a public domain dedication but uses the familiar BSD legal framework. This can be useful in jurisdictions where "public domain" is legally unclear.

---

## BSD vs MIT

The differences are minimal:

| Aspect | BSD 2-Clause | BSD 3-Clause | MIT |
|--------|--------------|--------------|-----|
| Attribution | Yes | Yes | Yes |
| Non-endorsement | Implicit | Explicit | Implicit |
| Wording | Academic style | Academic style | Plain language |

For practical purposes, choose whichever you prefer. They're legally equivalent in effect.

## When to Use BSD

BSD licenses are a good choice when:

- You're working in the BSD ecosystem (FreeBSD, OpenBSD, NetBSD)
- You prefer the slightly more explicit non-endorsement clause (3-clause)
- You want MIT-equivalent terms with traditional academic licensing

## Notable Projects Using BSD

### 3-Clause BSD
- FreeBSD
- NetBSD
- Go (programming language)
- Django
- Nginx

### 2-Clause BSD
- OpenBSD portions
- Various academic projects
