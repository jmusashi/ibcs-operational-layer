# MRS mapping

The MRS engine in `simulation/mrs/` is the primary realization of the dynamic substrate  
assumed in Paper 6.

Key components:

- `mrs_core.py` – core MRS orchestration and run lifecycle
- `reflexive_engine.py` – reflexive loop logic and state updates
- `surface_generator.py` – generation of observable surfaces for operators and monitors
- `convergence_monitor.py` – tracking of convergence metrics over runs

Paper 6.1 maps:

- **State spaces** in Paper 6 → MRS internal state representations
- **Transition relations** → update rules in `reflexive_engine.py`
- **Convergence criteria** → checks in `convergence_monitor.py`
- **Surfaces** → outputs from `surface_generator.py`

The Python module `paper_6_1.mapping_mrs` provides explicit functions that  
link named invariants from Paper 6 to concrete MRS configurations and runs.
