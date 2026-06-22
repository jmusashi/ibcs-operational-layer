"""
mapping_surfaces.py
Paper 6.1 – Surface Mapping Layer

This module defines the operational representation of surfaces (M0)
as described in Paper 6. Surfaces are the observable interfaces where
cognition interacts with the environment.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Surface:
    """A single operational surface."""
    name: str
    surface_type: str
    metadata: Dict[str, Any]


class SurfaceRegistry:
    """Registry for all surfaces in the operational environment."""

    def __init__(self):
        self._surfaces: Dict[str, Surface] = {}

    def register(self, surface: Surface):
        self._surfaces[surface.name] = surface

    def get(self, name: str) -> Surface:
        return self._surfaces.get(name)

    def list_surfaces(self):
        return list(self._surfaces.keys())


# Global registry instance
surfaces = SurfaceRegistry()
