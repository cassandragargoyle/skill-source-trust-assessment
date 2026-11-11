"""Tests of the assessment validator: fixtures, methodology rules and schema consistency."""

import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "source-trust-assessment"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

spec = importlib.util.spec_from_file_location("validate_assessment", SKILL / "scripts" / "validate_assessment.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
SCHEMA = json.loads((SKILL / "assets" / "assessment.schema.json").read_text(encoding="utf-8"))


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class FixtureTests(unittest.TestCase):
    def test_valid_fixtures(self):
        for path in sorted((FIXTURES / "valid").glob("*.json")):
            with self.subTest(path.name):
                errors, _ = validator.validate(load(path), SCHEMA)
                self.assertEqual(errors, [])

    def test_invalid_fixtures(self):
        for path in sorted((FIXTURES / "invalid").glob("*.json")):
            with self.subTest(path.name):
                errors, _ = validator.validate(load(path), SCHEMA)
                self.assertTrue(errors, f"{path.name} should be invalid")

    def test_template_is_valid(self):
        errors, _ = validator.validate(load(SKILL / "assets" / "assessment.template.json"), SCHEMA)
        self.assertEqual(errors, [])


class RuleTests(unittest.TestCase):
    def setUp(self):
        self.doc = load(SKILL / "assets" / "assessment.template.json")

    def errors(self):
        return validator.validate(self.doc, SCHEMA)[0]

    def test_certified_expert_needs_authorization(self):
        self.doc["trust"]["assessedBy"] = "certified-expert"
        self.doc["trust"]["assessor"] = {"name": "Jan Novák"}
        self.assertTrue(any("authorization" in e for e in self.errors()))

    def test_legal_act_needs_status(self):
        self.doc["trust"]["legalStatus"] = "n/a"
        self.assertTrue(any("legalStatus" in e for e in self.errors()))

    def test_modified_methodology_needs_description(self):
        self.doc["methodology"]["modified"] = True
        self.assertTrue(any("modifications" in e for e in self.errors()))

    def test_evidence_index_in_range(self):
        self.doc["criteria"][0]["evidence"] = [5]
        self.assertTrue(any("out of range" in e for e in self.errors()))


class ConsistencyTests(unittest.TestCase):
    """Codes must be defined consistently in the schema, the vocabulary and the methodology."""

    def test_codes_in_vocabulary(self):
        vocab = (SKILL / "assets" / "vocabulary.ttl").read_text(encoding="utf-8")
        notations = set(re.findall(r'skos:notation "([^"]+)"', vocab))
        trust = SCHEMA["properties"]["trust"]["properties"]
        for field in ("sourceReliability", "informationCredibility", "legalAuthority", "legalStatus",
                      "verificationStatus", "assessedBy"):
            for code in trust[field]["enum"]:
                with self.subTest(field=field, code=code):
                    self.assertIn(str(code), notations)
        for field, codes in self.item_codes().items():
            for code in codes:
                with self.subTest(field=field, code=code):
                    self.assertIn(code, notations)

    def test_codes_in_methodology(self):
        text = (SKILL / "references" / "methodology.md").read_text(encoding="utf-8")
        codes = {"legalAuthority": SCHEMA["properties"]["trust"]["properties"]["legalAuthority"]["enum"],
                 **self.item_codes()}
        for field, values in codes.items():
            for code in values:
                with self.subTest(field=field, code=code):
                    self.assertIn(f"`{code}`", text)

    @staticmethod
    def item_codes() -> dict[str, list[str]]:
        props = SCHEMA["properties"]
        return {"evidence.relation": props["evidence"]["items"]["properties"]["relation"]["enum"],
                "criteria.criterion": props["criteria"]["items"]["properties"]["criterion"]["enum"]}

    def test_versions_match(self):
        skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        version = re.search(r'methodology-version: "([^"]+)"', skill_md).group(1)
        methodology = (SKILL / "references" / "methodology.md").read_text(encoding="utf-8")
        self.assertIn(f"Version {version}", methodology)
        self.assertIn(f"assessment-{version}.json", SCHEMA["$id"])

    def test_skill_name_matches_directory(self):
        skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        name = re.search(r"^name: (\S+)$", skill_md, re.M).group(1)
        self.assertEqual(name, SKILL.name)


if __name__ == "__main__":
    unittest.main()
