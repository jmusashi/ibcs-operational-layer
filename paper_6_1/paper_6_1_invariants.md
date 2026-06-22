# Paper 6.1 — Invariants Mapping

This document defines the operational invariants derived from Paper 6 and
implemented in `mapping_invariants.py`. These invariants form the backbone
of the CTS, MRS, and simulation layers.

## Purpose of Invariants
Invariants ensure that the operational substrate behaves consistently across
surfaces, time, and reflexive loops. They provide the stability required for
continuity (M3) and governance (M4).

## Core Invariants

### 1. Structural Coherence
The system must maintain internal consistency across all layers.

### 2. Reflexive Integrity
The system must be able to observe its own state without destabilizing it.

### 3. Continuity Preservation
Events across surfaces must form a coherent chain.

### 4. Governance Compliance
All operations must respect governance constraints.

## Registry
All invariants are registered in `InvariantRegistry` and validated at runtime.
