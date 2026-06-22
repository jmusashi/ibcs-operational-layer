"""
Mapping from Paper 6 governance invariants to CTS configurations and evaluations.
"""

from typing import Dict, Any

from compliance.cts.cts_core import CTSCore
from compliance.cts.cts_rules import CTSRules
from compliance.cts.cts_monitor import CTSMonitor


def build_cts_configuration(invariant_name: str) -> Dict[str, Any]:
    """
    Return a CTS configuration aligned with a named governance invariant.

    At this stage, the configuration is a thin wrapper around rule selection.
    """
    rules = CTSRules()

    if invariant_name == "baseline_governance":
        selected_rules = rules.get_baseline_rules()
    elif invariant_name == "strict_governance":
        selected_rules = rules.get_strict_rules()
    else:
        selected_rules = rules.get_default_rules()

    return {
        "rules": selected_rules,
    }


def evaluate_cts(mrs_output: Any, cts_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluate CTS rules against MRS output and return a structured result.

    The result bundle includes:
    - is_compliant: bool
    - violations: list of violation descriptors
    - summary: human‑readable summary for operators
    """
    cts = CTSCore(rules=cts_config["rules"])
    monitor = CTSMonitor()

    evaluation = cts.evaluate(mrs_output)
    monitor.record(evaluation)

    return {
        "is_compliant": evaluation.is_compliant,
        "violations": evaluation.violations,
        "summary": monitor.summary(),
    }
