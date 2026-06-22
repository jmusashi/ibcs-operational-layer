"""
mapping_continuity.py
Paper 6.1 – Continuity Mapping Layer

This module implements the continuity engine (M3), which binds
surfaces, invariants, and reflexive loops into a coherent operational field.
"""

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ContinuityEvent:
    """A single event in the continuity chain."""
    surface: str
    action: str
    payload: Dict[str, Any]


class ContinuityEngine:
    """Tracks continuity across surfaces and time."""

    def __init__(self):
        self._events: List[ContinuityEvent] = []

    def record(self, event: ContinuityEvent):
        self._events.append(event)

    def history(self) -> List[ContinuityEvent]:
        return self._events

    def last(self) -> ContinuityEvent:
        return self._events[-1] if self._events else None


# Global continuity engine
continuity = ContinuityEngine()
