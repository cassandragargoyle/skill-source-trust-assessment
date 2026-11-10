# Forking

There are three levels of customisation. Prefer the lowest one that works.

| Level | What you change | How |
| ----- | --------------- | --- |
| **Use** | region, domain and purpose of an assessment | in the request to the agent; no change of files |
| **Extend** | a new region or domain profile | add a profile file (see [CONTRIBUTING.md](CONTRIBUTING.md)); ideally contribute it back by pull request |
| **Fork** | codes, rules, workflow, validator | fork the repository and change the methodology |

## Installing your fork

```bash
npx skills add <your-account>/skill-source-trust-assessment
```

## Marking modified results

A fork that changes the methodology must not present its results as assessments under the reference methodology. Set in every result:

```json
"methodology": {
  "id": "source-trust-assessment",
  "version": "0.1.0",
  "repository": "<your-account>/skill-source-trust-assessment",
  "commit": "<commit>",
  "modified": true,
  "modifications": "Added a weighted score as a derived view; codes unchanged."
}
```

Adding profiles alone is **not** a modification of the methodology (`modified: false`).

## Staying up to date

```bash
git remote add upstream https://github.com/CassandraGargoyle/skill-source-trust-assessment.git
git fetch upstream
git merge upstream/main
```

Keep your changes in separate files where possible (own profiles, own ADRs) to avoid merge conflicts in `methodology.md` and `SKILL.md`.
