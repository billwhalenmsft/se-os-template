"""Minimal deterministic agent contract for local SE-OS experiments."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class AgentRequest:
    """Input accepted by a local teaching agent."""

    text: str
    context: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class AgentResult:
    """Structured output returned by a local teaching agent."""

    agent: str
    output: Mapping[str, Any]


class BaseAgent(ABC):
    """Base contract with shared input validation."""

    name: str
    description: str

    def run(self, request: AgentRequest) -> AgentResult:
        text = " ".join(request.text.split())
        if not text:
            raise ValueError("Agent request text must not be empty.")
        normalized = AgentRequest(text=text, context=dict(request.context))
        return AgentResult(agent=self.name, output=self.perform(normalized))

    @abstractmethod
    def perform(self, request: AgentRequest) -> Mapping[str, Any]:
        """Transform a validated request into structured local output."""
