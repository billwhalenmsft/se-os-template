from __future__ import annotations

import unittest

from agents import AgentRequest, OutcomeFramerAgent


class OutcomeFramerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.agent = OutcomeFramerAgent()

    def test_returns_review_ready_shape(self) -> None:
        result = self.agent.run(
            AgentRequest(
                text="  Reduce   synthetic meeting preparation time. ",
                context={"owner": "Example Owner"},
            )
        )

        self.assertEqual(result.agent, "outcome-framer")
        self.assertEqual(result.output["objective"], "Reduce synthetic meeting preparation time")
        self.assertEqual(result.output["owner"], "Example Owner")
        self.assertEqual(len(result.output["success_measures"]), 2)
        self.assertIn("Require exact approval before any external write.", result.output["guardrails"])

    def test_rejects_empty_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            self.agent.run(AgentRequest(text="   "))


if __name__ == "__main__":
    unittest.main()
