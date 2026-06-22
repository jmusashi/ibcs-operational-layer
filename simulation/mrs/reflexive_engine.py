# reflexive_engine.py
import random

class ReflexiveEngine:
    """
    Contraction-based reflexive function R(Si, C).
    Implements the operational definition from Paper 6.1.

    Key properties:
    - Uses a Lipschitz constant L < 1 for guaranteed convergence.
    - Projects heterogeneous surfaces into a bounded scalar f(surface) ∈ [0, 1].
    - Updates T using a contraction mapping: T' = T - L * (T - f(surface)).
    """

    def __init__(self, L=0.4):
        """
        Initialize the reflexive engine.

        Parameters
        ----------
        L : float
            Lipschitz constant for the contraction mapping.
            Must satisfy 0 < L < 1 to ensure convergence.
        """
        if not (0.0 < L < 1.0):
            raise ValueError("L must be in (0, 1) for contraction mapping.")
        self.L = L

    def project_surface(self, surface):
        """
        Domain-agnostic projection f(surface).

        Converts a heterogeneous decision surface into a scalar in [0, 1].
        Higher load increases the value; higher noise and drift decrease it.
        """
        load = surface.get("load", 0.0)
        noise = surface.get("noise", 0.0)
        drift = surface.get("drift", 0.0)

        # Weighted projection with intuitive semantics
        value = 0.7 * load + 0.2 * (1.0 - noise) + 0.1 * (1.0 - drift)

        # Clamp to [0, 1]
        return max(0.0, min(1.0, value))

    def apply(self, surface, C):
        """
        Apply the reflexive function R to a single agent surface and invariant C.

        R(Si, C) = C' where:
            T' = T - L * (T - f(surface))

        This moves T toward f(surface) by a factor L, ensuring contraction.
        """
        T = C.get("T", 0.5)
        f_val = self.project_surface(surface)

        # Contraction update
        T_new = T - self.L * (T - f_val)

        # Keep T bounded in [0, 1]
        T_new = max(0.0, min(1.0, T_new))

        # Return updated invariant
        return {
            "I": C.get("I"),
            "T": T_new,
            "K": C.get("K"),
        }
