# convergence_monitor.py
# Convergence detection logic

class ConvergenceMonitor:
    """
    Monitors convergence of the Minimal Reference System (MRS).

    Responsibilities:
    - Compute pairwise distances between agent outputs
    - Check if all distances fall below a convergence threshold ε
    - Track iteration count and detect non-convergence
    - Identify the Serenpoint σ when convergence occurs
    """

    def __init__(self, epsilon=0.01, max_steps=50):
        """
        Parameters
        ----------
        epsilon : float
            Convergence threshold. All pairwise distances must be < epsilon.
        max_steps : int
            Maximum number of iterations before declaring non-convergence.
        """
        self.epsilon = epsilon
        self.max_steps = max_steps

    def has_converged(self, distances):
        """
        Check if all pairwise distances are below the convergence threshold.

        Parameters
        ----------
        distances : list of float
            Pairwise absolute differences between agent outputs.

        Returns
        -------
        bool
            True if all distances < epsilon, False otherwise.
        """
        return all(d < self.epsilon for d in distances)

    def run_until_convergence(self, mrs):
        """
        Execute the MRS loop until convergence or max_steps is reached.

        Parameters
        ----------
        mrs : MinimalReferenceSystem
            The MRS instance containing surfaces, invariant C, and step() logic.

        Returns
        -------
        dict
            {
                "converged": bool,
                "steps": int,
                "sigma": float or None,
                "history": list of (outputs, distances)
            }
        """
        history = []

        for t in range(1, self.max_steps + 1):
            outputs = mrs.step()
            distances = mrs.pairwise_distances(outputs)
            history.append((outputs, distances))

            if self.has_converged(distances):
                sigma = sum(outputs) / len(outputs)
                return {
                    "converged": True,
                    "steps": t,
                    "sigma": sigma,
                    "history": history,
                }

        # No convergence
        return {
            "converged": False,
            "steps": self.max_steps,
            "sigma": None,
            "history": history,
        }
