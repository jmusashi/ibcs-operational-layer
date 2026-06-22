# surface_generator.py
import random

class SurfaceGenerator:
    """
    Generates and updates heterogeneous decision surfaces Si.
    Surfaces must remain:
    - bounded
    - heterogeneous
    - domain-consistent
    - stable enough for contraction-based R to dominate

    This version uses small, controlled drift to ensure convergence.
    """

    def __init__(self):
        pass

    def generate_surface(self):
        """
        Create a new heterogeneous surface with bounded values.
        All fields are clamped to [0, 1].
        """
        surface = {
            "load": random.uniform(0.3, 0.9),
            "noise": random.uniform(0.05, 0.2),
            "drift": random.uniform(0.01, 0.05),
        }
        return surface

    def update_surface(self, surface):
        """
        Apply bounded, domain-consistent drift.
        Drift must be small relative to the contraction factor L.
        This prevents runaway divergence and ensures stable convergence.
        """
        surface["load"] += random.uniform(-0.02, 0.02)
        surface["noise"] += random.uniform(-0.005, 0.005)
        surface["drift"] += random.uniform(-0.003, 0.003)

        # Clamp all values to [0, 1]
        surface["load"] = max(0.0, min(1.0, surface["load"]))
        surface["noise"] = max(0.0, min(1.0, surface["noise"]))
        surface["drift"] = max(0.0, min(1.0, surface["drift"]))

        return surface
