# IBCS Operational Layer · Minimal Reference Simulation (MRS)

[Zenodo DOI: 10.5281/zenodo.20900697](https://doi.org/10.5281/zenodo.20900697)

This repository provides a deliberately minimal executable research substrate for **Invariant-Based Coordination Science (IBCS)** as defined by:

- **Paper 6 — Invariant-Based Coordination Science (IBCS)**, the theoretical authority.
- **Paper 6.1 — IBCS Operational Addendum and Implementation Framework**, the operational implementation framework.

The repository does not redefine the canonical theory or represent the downstream IBCS research program as complete.

## Implementation Boundary

The canonical IBCS invariant is:

`C = {I, T, K}`

and the canonical reflexive mapping is:

`C′ = R(Sᵢ, C)`

Paper 6 and Paper 6.1 define convergence over transformed invariant outputs `C′` under their specified mathematical conditions.

The current minimal executable uses the intent component `T` as a quantitative projection for convergence observation. This T-projected observable does not redefine canonical full-`C′` convergence and should not be interpreted as exhaustive IBCS compliance verification.

Notation is kept distinct throughout this repository:

- `σ` = Serenpoint
- `ε` = convergence threshold or tolerance, as applicable

## What the Minimal Reference Simulation Demonstrates

The current MRS provides a compact executable starting point for exploring:

- heterogeneous bounded decision surfaces;
- independent evaluation of `R(Sᵢ, C)` from a shared invariant;
- zero inter-agent communication in the canonical update cycle;
- bounded surface evolution;
- T-projected convergence observation; and
- generation of a Serenpoint candidate under the implemented projection.

The shared canonical invariant remains read-only during the simulation while the decision surfaces evolve.

## Quickstart

Run the basic executable example:

```bash
python simulation/mrs/example_basic_mrs_run.py
```

The example reports agent intent outputs, pairwise T-projected distances, and whether the implemented projected stopping condition has been reached.

Because the current example uses a T-projected observable, its reported result is best interpreted as a **Serenpoint candidate under the implemented projection** rather than complete canonical fixed-point verification.

## MRS Architecture

Paper 6.1 operationalizes the MRS through five components:

1. **Invariant Store** — holds the shared read-only invariant `C = {I, T, K}`.
2. **Agent Pool** — contains heterogeneous agents with distinct decision surfaces `Sᵢ`.
3. **Surface Generator** — produces and updates bounded heterogeneous surfaces.
4. **Reflexive Engine** — independently evaluates `R(Sᵢ, C)`.
5. **Convergence Monitor** — observes agent outputs and evaluates the stopping condition.

The Convergence Monitor observes convergence; it is not the mechanism producing convergence.

## Repository Structure

```text
simulation/mrs/
    example_basic_mrs_run.py
    ...

compliance/cts/
    README.md
    cts_core.py
    cts_monitor.py
    cts_rules.py

docs/
    mrs_overview.md
    ...
```

The ellipses indicate that additional repository files may be present. This README highlights only the paths directly relevant to the audited MRS and CTS boundary.

## Compliance Test Suite (CTS v1.0)

The repository includes minimal executable checks corresponding to the five CTS v1.0 criteria:

- **CTS-1 — Invariant Preservation**
- **CTS-2 — Serenpoint Stability**
- **CTS-3 — Cross-Surface Convergence**
- **CTS-4 — Noise Robustness**
- **CTS-5 — Drift Resistance**

The canonical criteria are defined in Paper 6 and operationalized in Paper 6.1. Where the current executable checks use a projection, proxy, Boolean outcome, or simplified observable, those implementations do not redefine the canonical criterion.

See `compliance/cts/README.md` for the implementation boundary and interpretation of results.

## Documentation

- MRS overview: `docs/mrs_overview.md`
- CTS implementation notes: `compliance/cts/README.md`

Other repository documentation may describe additional design or extension material. The two documents above contain the audited boundary for the current minimal MRS/CTS implementation.

## Research Boundary

This repository is a starting substrate for continued IBCS implementation research. It does **not** attempt to pre-empt downstream work identified by Paper 6.1, including broader simulation libraries, richer domain-specific implementations, later CTS development, benchmark suites, certification processes, or production deployment frameworks.

Accordingly, passing the current minimal executable checks should not, by itself, be described as exhaustive proof of full IBCS compliance.

## Reference

- **Paper 6:** *Invariant-Based Coordination Science (IBCS)*
- **Paper 6.1:** *IBCS Operational Addendum and Implementation Framework*

Paper 6 defines the canonical theory. Paper 6.1 provides the operational implementation framework. This repository provides a deliberately minimal executable substrate derived from those specifications.
