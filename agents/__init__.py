"""Customer-free teaching agents included with the SE-OS template."""

from .base_agent import AgentRequest, AgentResult, BaseAgent
from .outcome_framer import OutcomeFramerAgent

__all__ = ["AgentRequest", "AgentResult", "BaseAgent", "OutcomeFramerAgent"]
