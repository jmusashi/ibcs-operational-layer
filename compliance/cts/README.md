# Convergence Test Suite (CTS)

This folder contains the **compliance layer** for validating  
implementations of the Minimal Reference System (MRS).

CTS ensures that an implementation satisfies the formal guarantees of  
Invariant‑Based Coordination Science (IBCS), including:

- contraction of heterogeneous surfaces  
- invariant synchronization  
- bounded drift  
- finite‑step convergence  
- Serenpoint σ detection  

---

## 📌 How to Use CTS

1. Run any MRS simulation (e.g., `example_basic_mrs_run.py`).
2. The `ConvergenceMonitor` automatically:
   - tracks pairwise distances  
   - checks contraction  
   - detects convergence  
   - reports the Serenpoint σ  

No additional configuration is required.

---

## 📁 Files in This Folder

- **README.md** — this document  
- Additional compliance scripts will be added in future releases  

---

## 🧭 Purpose

CTS provides a **standardized, reproducible** way to verify that any  
MRS‑based system behaves according to the mathematical guarantees  
defined in Papers 6 and 6.1.

It is the foundation for:

- Paper 7 (Cross‑Domain Structural Cognition)  
- Paper 8 (Domain Projection Systems)  
- Paper 9.x (Monasterial Scale and 4RGE fabric)  
