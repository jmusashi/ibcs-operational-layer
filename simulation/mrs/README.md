# Minimal Reference System (MRS)

The Minimal Reference System (MRS) is the core simulation engine used in the
IBCS Operational Layer. It implements the contraction-based reflexive function
defined in Paper 6.1 and provides a reproducible reference implementation of:

- heterogeneous decision surfaces
- contraction-based reflexive mapping R(Si, C)
- bounded drift dynamics
- invariant synchronization
- Serenpoint (σ) detection
- convergence monitoring

---

## 📦 Folder Structure

simulation/mrs/
mrs_core.py
reflexive_engine.py
surface_generator.py
convergence_monitor.py
example_basic_mrs_run.py

---

## 🚀 Quickstart

Run the example simulation:

```bash
python simulation/mrs/example_basic_mrs_run.py
You will see:

agent outputs per iteration

pairwise distances

convergence detection

the Serenpoint σ

🔧 Core Components
ReflexiveEngine
Implements the contraction mapping:

Code
T' = T - L * (T - f(surface))
with 0 < L < 1 to guarantee convergence.

SurfaceGenerator
Produces heterogeneous surfaces with bounded drift:

load

noise

drift

All values remain in [0, 1].

MinimalReferenceSystem
Coordinates:

surface updates

invariant updates

application of R

synchronization of T

ConvergenceMonitor
Detects convergence when all pairwise distances fall below ε.

🎯 Serenpoint (σ)
The Serenpoint is the stable equilibrium reached when:

Code
|Ti - Tj| < ε   for all i, j
The example script prints σ when convergence occurs.

📄 Reference
This implementation corresponds to:

Paper 6.1 — The Minimal Reference System (MRS)  
(see Zenodo DOI in the main project documentation)