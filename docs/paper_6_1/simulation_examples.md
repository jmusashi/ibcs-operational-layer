# Simulation examples

This section describes a set of minimal working examples (MWEs) that demonstrate  
how Paper 6 invariants are realized in the MRS + CTS substrate.

The corresponding code lives in:

- `paper_6_1.simulation_examples`
- `simulation/mrs/example_basic_mrs_run.py`

Example classes of scenarios:

1. **Baseline convergence run**  
   - Single MRS configuration  
   - Convergence monitor tracks a simple metric  
   - Demonstrates basic convergence guarantees from Paper 6.

2. **Governance‑constrained run**  
   - MRS run coupled with CTS checks  
   - CTS enforces a subset of governance invariants  
   - Demonstrates how violations are detected and surfaced.

3. **Reflexive adjustment run**  
   - MRS run where CTS feedback alters configuration between runs  
   - Demonstrates reflexive adaptation consistent with Paper 6.

Each example is designed to be small, inspectable, and extensible.
