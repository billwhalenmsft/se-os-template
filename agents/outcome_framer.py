"""Deterministic outcome-framing example with no network dependencies."""

from __future__ import annotations

from typing import Any, Mapping

from .base_agent import AgentRequest, BaseAgent


class OutcomeFramerAgent(BaseAgent):
    """Turns a request into a review-ready experiment frame."""

    name = "outcome-framer"
    description = "Frames a bounded request into outcome, measures, questions, and guardrails."

    def perform(self, request: AgentRequest) -> Mapping[str, Any]:
        objective = request.text.rstrip(".")
        owner = request.context.get("owner", "Demo Operator")
        return {
            "objective": objective,
            "owner": owner,
            "success_measures": [
                {
                    "name": "primary outcome",
                    "baseline": "capture a synthetic baseline",
                    "target": "define a measurable improvement",
                },
                {
                    "name": "quality",
                    "baseline": "record current error or correction rate",
                    "target": "define an acceptable reviewed threshold",
                },
            ],
            "open_questions": [
                "Who experiences the problem?",
                "What is the current measurable baseline?",
                "What decision should a human retain?",
            ],
            "guardrails": [
                "Use synthetic or explicitly authorized data.",
                "Keep the first implementation local and reversible.",
                "Require exact approval before any external write.",
            ],
        }
