# CTS mapping

The CTS layer in `compliance/cts/` enforces the governance and constraint structure  
assumed by Paper 6.

Key components:

- `cts_core.py` – CTS orchestration and evaluation pipeline
- `cts_rules.py` – rule definitions and constraint encodings
- `cts_monitor.py` – monitoring of CTS outcomes and violations

Paper 6.1 maps:

- **Governance invariants** → rule sets in `cts_rules.py`
- **Constraint satisfaction** → evaluation logic in `cts_core.py`
- **Violation handling** → monitoring and escalation in `cts_monitor.py`

The Python module `paper_6_1.mapping_cts` exposes a small API to:

- Construct CTS configurations aligned with specific Paper 6 invariants
- Run CTS checks against MRS outputs
- Report compliance status in a form suitable for operators and higher‑level tooling.
