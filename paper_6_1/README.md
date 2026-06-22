# Paper 6.1 – Operational addendum

This package implements the **mapping layer** between:

- Paper 6 theoretical invariants, and
- The concrete MRS + CTS substrate in this repository.

It is intentionally small and explicit:

- `mapping_mrs.py` – maps invariants to MRS configurations and runs
- `mapping_cts.py` – maps governance invariants to CTS configurations and evaluations
- `simulation_examples.py` – minimal scenarios that exercise the mappings

You can use this package as the canonical entry point for:

- Demonstrations
- Experiments
- Higher‑level tooling (e.g., Paper 7 orchestration)
