"""
Minimal Reference Simulation (MRS)
IBCS Operational Addendum – Paper 6.1
Example Basic Run

Implements:
- Heterogeneous bounded decision surfaces
- Reflexive function R as a contraction mapping
- Multi-step convergence
- Serenpoint detection
- CTS-1 through CTS-5 compliance hooks
"""

from mrs_core import MinimalReferenceSystem
from convergence_monitor import ConvergenceMonitor

def main():
    print("\n=== Minimal Reference Simulation (MRS) ===\n")

    # Initialize the MRS with 3 agents and contraction L = 0.4
    mrs = MinimalReferenceSystem(num_agents=3, L=0.4)

    # Show initial invariant and surfaces
    print("Initial invariant:", mrs.C)
    print("Initial surfaces:", mrs.surfaces, "\n")

    # Convergence monitor
    monitor = ConvergenceMonitor(epsilon=0.01, max_steps=50)

    # Run the simulation
    result = monitor.run_until_convergence(mrs)

    # Print results
    for t, (outputs, distances) in enumerate(result["history"], start=1):
        print(f"t = {t}")
        print("Outputs:", outputs)
        print("Pairwise distances:", ", ".join(f"{d:.4f}" for d in distances))
        print()

    if result["converged"]:
        print(f"*** Serenpoint reached at step {result['steps']} ***")
        print("Serenpoint σ =", result["sigma"])
    else:
        print("*** No convergence within max_steps ***")
        print("Final Serenpoint:", result["sigma"])

if __name__ == "__main__":
    main()
