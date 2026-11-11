# Source Trust Assessment

An Agent Skill that tells an AI agent how to assess how far a publisher, a document or a single claim can be trusted, and to return a structured, reproducible result with evidence.

## What it does

- Rates the **source** with the Admiralty Code (NATO STANAG 2511): source reliability A–F and information credibility 1–6, written as `A1`, `B2` or `F6`. F and 6 mean *unknown*, not *worst*.
- Adds **legal authority** and **legal status**: whether the content is binding law, a draft, or no law at all. Bindingness comes only from the official version of a legal act.
- Records **evidence and provenance**: verbatim quotes with URLs, who assessed it, when, and what the information was derived from.
- Applies **profiles** for regions (`cz` Czech Republic, `eu` European Union) and domains (`bim` Building Information Modelling, draft).

The agent returns JSON that follows the bundled schema, followed by a short summary in the language of the user.

## Install

In Claude Code:

```text
/plugin install source-trust-assessment --marketplace cassandragargoyle/skill-source-trust-assessment
```

For other agents (Codex, Cursor, …):

```bash
npx skills add CassandraGargoyle/skill-source-trust-assessment
```

## Use

Ask in any language, for example:

- "How trustworthy is this article?"
- "Is it true that BIM is mandatory for all public contracts? Where does that claim come from?"
- "Ověř tento zdroj pro region cz."

## Limitations

- The result is not legal advice. Before acting on an obligation, read the official version of the legal act or ask a qualified professional.
- An assessment made by an AI agent alone is always marked as unverified until an expert reviews it.
- Check the quotes and URLs in the evidence. Sources that could not be retrieved are listed as unresolved.

## Data and privacy

- The skill sends no data anywhere by itself. It consists of instructions, reference files and one local validation script. It has no hooks, no MCP servers and no background processes, and it installs nothing.
- To assess a source, the agent opens the URLs you give it, or finds them with web search, using its own tools and permission settings. The skill tells the agent not to bypass login walls or bot protection.
- The validation script uses only the Python standard library, reads the JSON file you pass to it and makes no network requests.
- Nothing is stored by the skill, and it does not ask for personal data.

Full text: [Privacy policy](https://github.com/CassandraGargoyle/skill-source-trust-assessment/blob/main/PRIVACY.md).

## More

Methodology, profiles, design decisions and contribution rules are in the [repository](https://github.com/CassandraGargoyle/skill-source-trust-assessment). Licence: MIT.
