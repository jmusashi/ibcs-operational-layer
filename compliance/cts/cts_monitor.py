"""
CTS Monitor
Coordinates execution of CTS-1 through CTS-5.
"""

from .cts_core import CTSResult
from .cts_rules import (
    cts1_invariant_preservation,
    cts2_serenpoint_stability,
    cts3_cross_surface,
    cts4_noise_robustness,
    cts5_drift_resistance
)

class CTSMonitor:

    def run_all(self, C_history, outputs_at_convergence, t_conv, t_max,
                noisy_converged, I0, T0, I_final, T_final):

        result = CTSResult()

        # CTS-1: Invariant Preservation
        for i in range(len(C_history) - 1):
            cts1_invariant_preservation(C_history[i], C_history[i+1], result)

        # CTS-2: Serenpoint Stability
        cts2_serenpoint_stability(t_conv, t_max, result)

        # CTS-3: Cross-Surface Consistency
        cts3_cross_surface(outputs_at_convergence, result)

        # CTS-4: Noise Robustness
        cts4_noise_robustness(noisy_converged, result)

        # CTS-5: Drift Resistance
        cts5_drift_resistance(I0, T0, I_final, T_final, result)

        return result.summary()
