# Privacy policy

This policy covers the `source-trust-assessment` Agent Skill and Claude Code plugin published by CassandraGargoyle in this repository.

## What the skill does with data

- **The skill collects nothing.** It consists of instructions, reference files and one local validation script. It has no server, no hooks, no MCP servers, no telemetry and no background processes. CassandraGargoyle receives no data from people who use it.
- **Sources are read by the agent.** To assess a source, the AI agent opens the web pages you give it, or finds them with web search, using its own tools. These pages can contain personal data, such as the name of an author or an official. The agent reads such data only to assess the source and may quote it as evidence in the result.
- **Nothing is stored by the skill.** The assessment stays in your conversation, or in a file if you or the agent save one. The skill does not ask for personal data and does not keep any.
- **The validation script runs locally.** It uses only the Python standard library, reads the JSON file you pass to it and makes no network requests.

## Your AI provider

The conversation with your agent, including the pages it reads, is processed by the provider of that agent (for example Anthropic for Claude) under that provider's own privacy policy.

## Contact

Questions about this policy: open an issue at <https://github.com/CassandraGargoyle/skill-source-trust-assessment/issues>.
