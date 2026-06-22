"""
mapping_governance.py
Paper 6.1 – Governance Mapping Layer

This module implements the governance constraints (M4) that ensure
the operational substrate behaves safely, predictably, and coherently.
"""

from dataclasses import dataclass
from typing import Dict, Any, Callable


@dataclass
class GovernanceRule:
    """A single governance rule."""
    name: str
    description: str
    rule: Callable[[Dict[str, Any]], bool]


class GovernanceEngine:
    """Evaluates governance rules against runtime contexts."""

    def __init__(self):
        self._rules: Dict[str, GovernanceRule] = {}

    def register(self, rule: GovernanceRule):
        self._rules[rule.name] = rule

    def evaluate(self, context: Dict[str, Any]) -> Dict[str, bool]:
        return {name: rule.rule(context) for name, rule in self._rules.items()}

    def list_rules(self):
        return list(self._rules.keys())


# Global governance engine
governance = GovernanceEngine()
