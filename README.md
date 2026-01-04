# Open Source Licensing Guide

An educational guide to open source licensing, written for researchers, developers, and anyone who needs to understand licensing without a law degree.

**Live site:** *(not yet deployed)*

## About

This guide explains open source licensing from first principles. It covers:

- **Concepts** — Foundational ideas like libre vs gratis, permissive vs copyleft
- **Software Licenses** — MIT, Apache, GPL, and others in detail
- **Creative Commons** — Licenses for non-code works (data, docs, media)
- **Practical Guides** — How to choose, use, and attribute properly
- **Lessons Learned** — Historical case studies of licensing gone wrong

## Voice and Approach

The guide is written from the perspective of a "graybeard" developer who's been in the industry since the beginning. This is a deliberate narrative device—see the [Preface](docs/preface.md) for context on why.

The voice is:
- First-person, experienced, mentoring
- Opinionated but fair
- Focused on practical wisdom over legal precision
- Willing to tell stories and share historical context

## Building Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Serve locally
mkdocs serve

# Build static site
mkdocs build
```

Or use the build script:
```bash
./mkdocs-build.sh
```

## Project Structure

```
docs/
├── index.md                 # Homepage
├── preface.md               # Author's note about voice and approach
├── concepts/                # Foundational concepts
├── licenses/                # Software licenses
│   ├── permissive/
│   ├── copyleft/
│   └── other/
├── creative-commons/        # CC licenses (separate from software)
├── guides/                  # Practical how-tos
├── lessons-learned/         # Historical case studies
├── reference/               # Quick comparison, glossary, sources
├── includes/                # Shared content (glossary definitions)
└── overrides/               # MkDocs Material theme customizations
```

## License

This work is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — Creative Commons Attribution-NonCommercial 4.0 International.

You may share and adapt for non-commercial purposes with attribution.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on voice, citations, and technical patterns.

## Author

Andrew Marx, with assistance from Claude (Anthropic).
