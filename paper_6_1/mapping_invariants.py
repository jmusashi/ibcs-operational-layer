"""
mapping_invariants.py
Paper 6.1 – Invariant Mapping Layer

This module operationalizes the invariants defined in Paper 6 by providing
runtime‑checkable structures, validation utilities, and mapping functions
that bind the conceptual invariants to executable logic.

The invariants here serve as the backbone for CTS, MRS, and simulation layers.
"""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class Invariant:
    """A single invariant with a name and a validation rule."""
    name: str
    description: str

    def validate(self, context: Dict[str, Any]) -> bool:
        """
        Validate the invariant against a runtime context.
        Override this method for custom invariant logic.
        """
        return True


class InvariantRegistry:
    """Registry for all invariants used across the operational layer."""

    def __init__(self):
        self._invariants: Dict[str, Invariant] = {}

    def register(self, invariant: Invariant):
        self._invariants[invariant.name] = invariant

    def validate_all(self, context: Dict[str, Any]) -> Dict[str, bool]:
        """Validate all invariants against a given context."""
        return {name: inv.validate(context) for name, inv in self._invariants.items()}

    def list_invariants(self) -> List[str]:
        return list(self._invariants.keys())


# Global registry instance
invariants = InvariantRegistry()
