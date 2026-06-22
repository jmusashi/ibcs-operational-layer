# Minimal Reference Simulation (MRS)
### IBCS Operational Addendum – Paper 6.1  
### Documentation Overview

The Minimal Reference Simulation (MRS) is the canonical testbed for validating IBCS behavior.  
It is defined in **Paper 6 (theory)** and fully operationalized in **Paper 6.1 (implementation)**.

The MRS demonstrates the three core properties of IBCS:

- **Heterogeneity** — agents begin with distinct decision surfaces  
- **Zero communication** — no messages, shared memory, or synchronization  
- **Finite-step convergence** — all agents converge to the same Serenpoint σ  

This document provides a complete overview of the MRS architecture, simulation cycle, and
compliance integration.

---

# 1. Purpose of the MRS

Paper 6.1 states:

> “The MRS consists of five components… It provides the operational architecture for implementing IBCS.”  

The MRS exists to:

- validate the reflexive function **R(Sᵢ, C)**  
- verify convergence to the Serenpoint **σ**  
- test drift resistance and invariant preservation  
- provide a reproducible baseline for all IBCS implementations  

It is the **reference implementation** for researchers and engineers.

---

# 2. Architecture Overview

The MRS consists of **five components** (Paper 6.1 §6.1):

+-----------------------+
|   Invariant Store     |  → Shared C = {I, T, K}
+-----------------------+
|
v
+-----------------------+
|      Agent Pool       |  → n agents, each with Si
+-----------------------+
|
v
+-----------------------+
|   Surface Generator   |  → produces heterogeneous bounded surfaces
+-----------------------+
|
v
+-----------------------+
|   Reflexive Engine    |  → applies R(Si, C)
+-----------------------+
|
v
+-----------------------+
|  Convergence Monitor  |  → detects Serenpoint σ
+-----------------------+

Code

Each agent runs independently.  
No communication occurs at any point.

---

# 3. Invariant Structure

The shared invariant is:

C = { I, T, K }

Code

Paper 6.1 defines the operational constraints:

- **I** must be non-null and unique  
- **T** must be coherent and non-inverted  
- **K** must be continuous and gap-free  

All agents load the same C at initialization.

---

# 4. Decision Surfaces

Paper 6.1 requires:

> “Surfaces must be bounded… and heterogeneous.”

The MRS enforces:

- **boundedness:** ‖Sᵢ‖ ≤ S_max  
- **heterogeneity:** Sᵢ ≠ Sⱼ for all i ≠ j  
- **domain consistency:** surfaces evolve realistically per timestep  

Surfaces represent each agent’s local context.

---

# 5. Reflexive Function R

The reflexive function is the core of IBCS:

C' = R(Si, C)

Code

Paper 6.1 requires:

- **idempotence**  
- **Lipschitz continuity (L < 1)**  
- **cross-surface consistency**  
- **invariant preservation**  

The MRS uses a contraction mapping to guarantee convergence.

---

# 6. Simulation Cycle

At each timestep t:

1. Agent reads its surface Sᵢ(t)  
2. Agent computes C′ᵢ(t) = R(Sᵢ(t), C)  
3. Agent updates its surface  
4. Convergence Monitor collects all C′ᵢ(t)  

Convergence is detected when:

‖C′ᵢ − C′ⱼ‖ < ε   for all i, j

Code

At that moment:

σ = C′₁

Code

Paper 6.1:

> “Set sigma = C′₁ (all outputs are identical at convergence).”

---

# 7. Serenpoint Verification

After σ is detected, the MRS verifies the fixed-point condition:

R(Si, σ) = σ

Code

If true for all agents, σ is a valid Serenpoint.

---

# 8. CTS Integration

The MRS integrates directly with the **Compliance Test Suite (CTS v1.0)**:

- **CTS‑1:** Invariant Preservation  
- **CTS‑2:** Serenpoint Stability  
- **CTS‑3:** Cross-Surface Consistency  
- **CTS‑4:** Noise Robustness  
- **CTS‑5:** Drift Resistance  

These tests ensure that:

- invariants remain stable  
- convergence occurs within bounds  
- heterogeneity does not break alignment  
- noise does not destabilize σ  
- identity and intent do not drift  

The CTS is implemented in:

compliance/cts/

Code

---

# 9. Example Output (From Simulation)

A typical convergence trace:

t = 1
Outputs: [0.58, 0.52, 0.55]
Distances: 0.06, 0.03, 0.03

t = 2
Outputs: [0.552, 0.528, 0.540]
Distances: 0.024, 0.012, 0.012

t = 3
Outputs: [0.5408, 0.5312, 0.536]
Distances: 0.0096, 0.0048, 0.0048

*** Serenpoint reached ***
σ = 0.5408

Code

This matches the operational example in Paper 6.1.

---

# 10. File Locations

- Simulation code:  
  `simulation/examples/example_basic_mrs_run.py`

- CTS implementation:  
  `compliance/cts/`

- This documentation:  
  `docs/mrs_overview.md`

---

# 11. References

- **Paper 6:** *Invariant-Based Coordination Science (IBCS)*  
- **Paper 6.1:** *IBCS Operational Addendum and Implementation Framework*  

Both documents define the canonical theory and operational layer of the MRS.

---

# End of Document