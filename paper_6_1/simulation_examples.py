"""
Simulation examples that exercise the Paper 6.1 mappings.
"""

from .mapping_mrs import build_mrs_configuration, run_mrs_with_monitor
from .mapping_cts import build_cts_configuration, evaluate_cts


def run_baseline_convergence_example() -> None:
    """
    Run a simple MRS convergence scenario aligned with the 'baseline_convergence' invariant.
    """
    config = build_mrs_configuration("baseline_convergence")
    result = run_mrs_with_monitor(config)
    print("Baseline convergence example:")
    print(result["convergence_report"])


def run_governance_constrained_example() -> None:
    """
    Run an MRS scenario with CTS governance checks enabled.
    """
    mrs_config = build_mrs_configuration("governance_constrained")
    mrs_result = run_mrs_with_monitor(mrs_config)

    cts_config = build_cts_configuration("baseline_governance")
    cts_result = evaluate_cts(mrs_result, cts_config)

    print("Governance‑constrained example:")
    print("Convergence:", mrs_result["convergence_report"])
    print("Compliance:", cts_result["summary"])


def run_reflexive_adjustment_example() -> None:
    """
    Placeholder for a reflexive adjustment scenario where CTS feedback alters MRS configuration.

    This will eventually:
    - run an initial MRS configuration
    - evaluate CTS
    - adjust configuration based on violations
    - re‑run MRS and compare convergence/compliance
    """
    print("Reflexive adjustment example is not yet implemented.")
