"""
Mapping from Paper 6 invariants to MRS configurations and runs.
"""

from typing import Dict, Any

from simulation.mrs.mrs_core import MRSCore
from simulation.mrs.reflexive_engine import ReflexiveEngine
from simulation.mrs.convergence_monitor import ConvergenceMonitor
from simulation.mrs.surface_generator import SurfaceGenerator


def build_mrs_configuration(invariant_name: str) -> Dict[str, Any]:
    """
    Return an MRS configuration dictionary aligned with a named Paper 6 invariant.

    This is intentionally simple at first: it encodes only a few knobs that can be
    extended as the mapping becomes more detailed.
    """
    # TODO: refine these presets as the invariant catalog is formalized.
    if invariant_name == "baseline_convergence":
        return {
            "max_runs": 50,
            "tolerance": 1e-3,
            "initial_state": {},
        }

    if invariant_name == "governance_constrained":
        return {
            "max_runs": 50,
            "tolerance": 1e-3,
            "initial_state": {},
            "enable_governance_hooks": True,
        }

    # Default: conservative baseline
    return {
        "max_runs": 20,
        "tolerance": 1e-2,
        "initial_state": {},
    }


def run_mrs_with_monitor(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run the MRS engine with a convergence monitor and return a simple result bundle.

    The result bundle is intentionally lightweight:
    - final_state: the last state produced by the MRS run
    - convergence_report: summary from the ConvergenceMonitor
    - surfaces: any generated surfaces (if enabled)
    """
    mrs = MRSCore(config=config)
    reflexive_engine = ReflexiveEngine(mrs)
    monitor = ConvergenceMonitor()
    surface_gen = SurfaceGenerator()

    for _ in range(config.get("max_runs", 20)):
        state = reflexive_engine.step()
        monitor.observe(state)
        surface_gen.capture(state)
        if monitor.has_converged(tolerance=config.get("tolerance", 1e-2)):
            break

    return {
        "final_state": state,
        "convergence_report": monitor.report(),
        "surfaces": surface_gen.export(),
    }
