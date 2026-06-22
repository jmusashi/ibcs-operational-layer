"""
CTS Rules
Implements CTS-1 through CTS-5 exactly as defined in Paper 6.1 Section 7.
"""

from .cts_core import CTSResult, EPS_C, EPS_X, EPS_I, EPS_T
import math

def dist(C1, C2):
    return abs(C1["T"] - C2["T"])

# ---------------------------------------------------------
# CTS-1: Invariant Preservation
# ---------------------------------------------------------

def cts1_invariant_preservation(C_prev, C_next, result: CTSResult):
    d = dist(C_prev, C_next)
    if d >= EPS_C:
        result.cts1_invariant_preservation = False
        result.log(f"CTS-1 FAIL: invariant drift = {d:.4f}")
    else:
        result.log(f"CTS-1 PASS: drift = {d:.4f}")

# ---------------------------------------------------------
# CTS-2: Serenpoint Stability
# ---------------------------------------------------------

def cts2_serenpoint_stability(t_conv, t_max, result: CTSResult):
    if t_conv >= t_max:
        result.cts2_serenpoint_stability = False
        result.log("CTS-2 FAIL: no convergence within t_max")
    else:
        result.log(f"CTS-2 PASS: converged at t={t_conv}")

# ---------------------------------------------------------
# CTS-3: Cross-Surface Consistency
# ---------------------------------------------------------

def cts3_cross_surface(outputs, result: CTSResult):
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            d = dist(outputs[i], outputs[j])
            if d >= EPS_X:
                result.cts3_cross_surface = False
                result.log(f"CTS-3 FAIL: surfaces {i},{j} diverged by {d:.4f}")
                return
    result.log("CTS-3 PASS: all surfaces consistent")

# ---------------------------------------------------------
# CTS-4: Noise Robustness
# ---------------------------------------------------------

def cts4_noise_robustness(converged, result: CTSResult):
    if not converged:
        result.cts4_noise_robustness = False
        result.log("CTS-4 FAIL: noisy run did not converge")
    else:
        result.log("CTS-4 PASS: noisy run converged")

# ---------------------------------------------------------
# CTS-5: Drift Resistance
# ---------------------------------------------------------

def cts5_drift_resistance(I0, T0, I_final, T_final, result: CTSResult):
    dI = 0 if I0 == I_final else 1  # identity must not change
    dT = abs(T_final - T0)

    if dI > EPS_I:
        result.cts5_drift_resistance = False
        result.log("CTS-5 FAIL: identity drift detected")

    if dT >= EPS_T:
        result.cts5_drift_resistance = False
        result.log(f"CTS-5 FAIL: intent drift = {dT:.4f}")

    if result.cts5_drift_resistance:
        result.log("CTS-5 PASS: identity and intent stable")
