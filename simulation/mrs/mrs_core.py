# mrs_core.py
# Minimal Reference Simulation (MRS) — IBCS Operational Layer
# Aligned with Paper 6.1, Section 6

from .reflexive_engine import ReflexiveEngine
from .surface_generator import SurfaceGenerator


class MinimalReferenceSystem:
    """
    Minimal Reference System (MRS)
    Implements the operational loop defined in Paper 6.1:

        1. Initialize invariant C = {I, T, K}
        2. Generate heterogeneous surfaces Si
        3. Apply contraction-based R(Si, C)
        4. Update surfaces with bounded drift
        5. Monitor convergence toward a Serenpoint σ

    This class orchestrates the entire MRS cycle.
    """

    def __init__(self, num_agents=3, L=0.4):
        """
        Initialize the MRS with:
        - num_agents: number of heterogeneous surfaces
        - L: Lipschitz constant for contraction mapping R
        """
        self.num_agents = num_agents
        self.reflexive_engine = ReflexiveEngine(L=L)
        self.surface_gen = SurfaceGenerator()

        # Shared invariant C = {I, T, K}
        self.C = {
            "I": "Agent-Class: Generic, Version 1.0",
            "T": 0.5,
            "K": {"history": [], "depth": 0},
        }

        # Generate initial heterogeneous surfaces
        self.surfaces = [self.surface_gen.generate_surface() for _ in range(num_agents)]

    def step(self):
        """
        Perform one MRS iteration:
        - Apply R(Si, C) for each agent
        - Collect updated T values
        - Update surfaces with bounded drift
        """
        outputs = []

        # Apply contraction mapping R to each surface
        for surface in self.surfaces:
            C_new = self.reflexive_engine.apply(surface, self.C)
            outputs.append(C_new["T"])

        # Update shared invariant T to the mean of outputs
        # (Paper 6.1: shared invariant must remain synchronized)
        self.C["T"] = sum(outputs) / len(outputs)

        # Update surfaces with bounded drift
        self.surfaces = [self.surface_gen.update_surface(s) for s in self.surfaces]

        return outputs

    def pairwise_distances(self, values):
        """
        Compute pairwise absolute differences between agent outputs.
        Used for convergence detection.
        """
        dists = []
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                dists.append(abs(values[i] - values[j]))
        return dists
