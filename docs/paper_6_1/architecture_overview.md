# Architecture overview

Paper 6.1 introduces an operational architecture with three main strata:

- **Theory layer (Paper 6):**  
  Defines invariants, convergence guarantees, and governance constraints.

- **Substrate layer (MRS + CTS):**  
  Implements those invariants as mechanisms:
  - `simulation/mrs/` – multi‑run substrate, reflexive engine, surface generator
  - `compliance/cts/` – compliance rules, monitoring, and constraint enforcement

- **Mapping layer (Paper 6.1):**  
  `paper_6_1/` binds theory to substrate:
  - Encodes which invariants are realized by which components
  - Provides simulation examples that exercise specific invariants
  - Exposes a minimal API for external tooling and Paper 7 extensions

The rest of this section decomposes these mappings into MRS, CTS, and simulation examples.
