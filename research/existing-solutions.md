# Existing Solutions

Comparison of existing skills and tools with this project. Not distributed with the skill.

Status: **preliminary** – collected from a design discussion on 2026-11-10; the entries below have not yet been reviewed in detail. Absence of a better match here is not proof that none exists.

| Project | What it does | What to take from it | Difference from this project |
| ------- | ------------ | -------------------- | ---------------------------- |
| [Source Credibility Evaluation Protocol](https://ruleskill.com/skills/garethmanning/source-credibility-evaluation-protocol) (GarethManning/education-agent-skills) | credibility of digital information using lateral reading and SIFT; education, websites, social media | verification workflow, working with external evidence | no versioned methodology, no region/domain profiles, no legal authority |
| [Source Verification](https://skillmd.com/skills/construct-ai-primary/source-verification) | checks authority, currency and accuracy of sources when producing AI output | simple activation, clear "when to use" | general procedure, not a configurable framework |
| [GitHub – Doublecheck](https://github.com/github/awesome-copilot/blob/main/skills/doublecheck/SKILL.md) | three-layer verification of AI output: extract claims, find supporting/contradicting sources, check hallucinations | structured report, separation of claims and evidence, contradiction check | no source rating scale, no provenance of methodology |

## Where to search further

- Catalogues: [skills.sh](https://skills.sh), [SkillsMD](https://skillsmd.dev), [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills), [Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills), [GitHub Awesome Copilot](https://github.com/github/awesome-copilot)
- Terminal: `npx skills find "source credibility"`, `"source verification"`, `"fact checking"`, `"research validation"`
- Search terms: *source credibility assessment*, *source reliability evaluation*, *information quality assessment*, *source provenance*, *evidence evaluation*

## Positioning

Distinguishing properties to communicate:

- **Evidence-based** – every rating cites evidence with quotes.
- **Region-aware** – legal hierarchy and institutions per jurisdiction.
- **Domain-aware** – document types and institutions per field (BIM first).
- **Reproducible** – results carry methodology version, profiles and provenance.
- **Separates trust from bindingness** – Admiralty codes plus legal authority (ADR-001).
