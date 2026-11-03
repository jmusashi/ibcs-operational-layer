# Minimal Reference Simulation (MRS)

#### IBCS Operational Addendum – Paper 6.1
#### Documentation Overview

The Minimal Reference Simulation (MRS) is the canonical testbed defined by Paper 6 and operationalized by Paper 6.1 for examining IBCS behavior. It centers on three properties: heterogeneous decision surfaces, zero inter-agent communication, and finite-step convergence toward a Serenpoint σ under the canonical convergence conditions.

This document distinguishes three layers throughout:

1. **Canonical specification** — the theory and mathematical criteria defined in Paper 6.
2. **Operational specification** — the implementation guidance provided by Paper 6.1.
3. **Current reference implementation** — the deliberately minimal executable research substrate in this repository.

## Implementation Status

The canonical IBCS invariant is:

`C = {I, T, K}`

and canonical cross-surface convergence is defined over transformed invariant outputs `C′`.

The current executable reference deliberately uses the intent component `T` as a minimal quantitative projection for convergence observation. This T-projected measurement does not redefine the canonical convergence criterion and should not be interpreted as exhaustive IBCS compliance verification.

Paper 6 remains the theoretical authority. Paper 6.1 provides the operational implementation framework. This repository provides a minimal executable substrate for continued research, testing, and extension.

## 1. Purpose of the MRS

Paper 6.1 describes an operational MRS architecture consisting of an Invariant Store, Agent Pool, Surface Generator, Reflexive Engine, and Convergence Monitor.

The MRS is intended to provide an implementation-oriented substrate for:

- evaluating the reflexive function `R(Sᵢ, C)`;
- observing convergence behavior toward Serenpoint `σ`;
- supporting invariant-preservation, drift-resistance, and related CTS checks; and
- providing a reproducible starting point for further IBCS implementation research.

The repository implementation is intentionally minimal and should be read alongside the canonical Paper 6 criteria and the Paper 6.1 operational guidance.

## 2. Architecture Overview

Paper 6.1 defines five operational components:

```text
Invariant Store
    ↓
Agent Pool
    ↓
Surface Generator
    ↓
Reflexive Engine
    ↓
Convergence Monitor
```

- **Invariant Store** — holds the shared canonical `C = {I, T, K}` as read-only simulation input.
- **Agent Pool** — contains heterogeneous agents with distinct decision surfaces `Sᵢ`.
- **Surface Generator** — produces and updates bounded heterogeneous surfaces.
- **Reflexive Engine** — independently evaluates `R(Sᵢ, C)` for each agent.
- **Convergence Monitor** — observes agent outputs and evaluates the stopping criterion. It is an observer of convergence, not the mechanism producing convergence.

No inter-agent communication is part of the canonical MRS update cycle.

## 3. Invariant Structure

The shared invariant is:

`C = {I, T, K}`

Paper 6.1 operationalizes the invariant with well-formedness constraints including:

- **I** is non-null and unambiguous;
- **T** has non-zero magnitude, is coherent, and is non-inverted; and
- **K** is continuous within the specified tolerance.

Paper 6.1 also specifies uniqueness of `I` within the same coordination substrate.

The canonical invariant remains read-only during the MRS simulation. Agents independently evaluate transformed outputs from the same shared `C` while their decision surfaces evolve.

## 4. Decision Surfaces

Paper 6.1 requires decision surfaces to be bounded and heterogeneous, and surface updates to remain domain-consistent and within the applicable `S_max` bound.

Decision surfaces represent local agent context and evolve independently during the simulation.

## 5. Reflexive Function R

The canonical reflexive mapping is:

`C′ = R(Sᵢ, C)`

Paper 6 and Paper 6.1 specify properties including idempotence, Lipschitz continuity with `L < 1`, cross-surface consistency, boundedness, and preservation of invariant well-formedness.

The current executable example provides a deliberately minimal contraction-style realization on the intent projection. It should not by itself be interpreted as establishing the complete mathematical convergence guarantee specified by Paper 6.

## 6. Simulation Cycle

Paper 6.1 specifies the following operational cycle at each timestep `t`:

1. Agent `i` reads its current decision surface `Sᵢ(t)`.
2. Agent `i` independently computes `C′ᵢ(t) = R(Sᵢ(t), C)`.
3. Agent `i` updates its decision surface.
4. The Convergence Monitor observes the transformed outputs.

Canonical convergence is detected when:

`‖C′ᵢ − C′ⱼ‖ < ε` for all agent pairs `i, j`.

Here:

- `σ` denotes the Serenpoint;
- `ε` denotes the convergence threshold.

When canonical convergence is detected, Paper 6.1 records `σ = C′₁` because the outputs are within the specified convergence criterion.

### Current executable measurement boundary

The present minimal executable uses pairwise distance over the `T` component as its quantitative convergence observable. It therefore observes a projection of canonical `C′` convergence rather than implementing a general metric over the complete invariant space.

This projection is intentional and does not redefine the canonical criterion.

## 7. Serenpoint Verification

Paper 6 and Paper 6.1 specify post-convergence fixed-point verification:

`R(Sᵢ, σ) = σ`

for all compliant agents.

This fixed-point condition belongs to the canonical IBCS specification. The current minimal executable should not be interpreted as performing full fixed-point verification unless that check is explicitly implemented.

Accordingly, a value identified by the current T-projected stopping rule is best treated as a **Serenpoint candidate under the implemented projection**, pending the complete canonical verification appropriate to the implementation under study.

## 8. CTS Relationship

Paper 6 and Paper 6.1 define five CTS v1.0 criteria:

- **CTS-1:** Invariant Preservation
- **CTS-2:** Serenpoint Stability
- **CTS-3:** Cross-Surface Convergence
- **CTS-4:** Noise Robustness
- **CTS-5:** Drift Resistance

The repository contains executable checks corresponding to these criteria under:

`compliance/cts/`

The present implementation is deliberately minimal. Where an executable check uses a projection, proxy, Boolean outcome, or simplified observable, it should not be interpreted as redefining or exhaustively implementing the complete mathematical criterion.

The repository documentation therefore distinguishes the canonical CTS requirement from the current executable check.

## 9. Illustrative Convergence Trace

A projected convergence trace may take the following form:

```text
t = 1
Outputs: [0.58, 0.52, 0.55]
Distances: 0.06, 0.03, 0.03

t = 2
Outputs: [0.552, 0.528, 0.540]
Distances: 0.024, 0.012, 0.012

t = 3
Outputs: [0.5408, 0.5312, 0.536]
Distances: 0.0096, 0.0048, 0.0048
```

This trace is **illustrative**. It is not presented here as a reproduced execution result of the current repository. Reproducible execution results should be generated directly from the current implementation and reported with their run conditions.

## 10. File Locations

- MRS implementation: `simulation/mrs/`
- Basic executable example: `simulation/mrs/example_basic_mrs_run.py`
- CTS implementation: `compliance/cts/`
- This documentation: `docs/mrs_overview.md`

## 11. References

- **Paper 6:** *Invariant-Based Coordination Science (IBCS)*
- **Paper 6.1:** *IBCS Operational Addendum and Implementation Framework*

Paper 6 defines the canonical theory. Paper 6.1 provides the operational implementation layer. This repository is a deliberately minimal executable research substrate derived from those specifications.
