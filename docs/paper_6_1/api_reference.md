# API reference (Paper 6.1 layer)

The Paper 6.1 mapping layer exposes a small, explicit API surface.

## `paper_6_1.mapping_mrs`

- `build_mrs_configuration(invariant_name: str) -> dict`  
  Returns an MRS configuration aligned with a named Paper 6 invariant.

- `run_mrs_with_monitor(config: dict) -> object`  
  Runs the MRS engine with convergence monitoring enabled.

## `paper_6_1.mapping_cts`

- `build_cts_configuration(invariant_name: str) -> dict`  
  Returns a CTS configuration aligned with a governance invariant.

- `evaluate_cts(mrs_output: object, cts_config: dict) -> object`  
  Evaluates CTS rules against MRS outputs.

## `paper_6_1.simulation_examples`

- `run_baseline_convergence_example() -> None`  
- `run_governance_constrained_example() -> None`  
- `run_reflexive_adjustment_example() -> None`  

These functions are thin orchestration wrappers that tie together MRS, CTS,  
and the mappings defined in this addendum.
