# convergence_monitor.py
# Convergence detection logic

import math

class ConvergenceMonitor:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def distance(self, C1, C2):
        # Compare intent vectors only (simplified)
        T1 = C1["T"]
        T2 = C2["T"]
        return math.sqrt((T1[0] - T2[0])**2 + (T1[1] - T2[1])**2)

    def check_convergence(self, outputs, t):
        for i in range(len(outputs)):
            for j in range(i + 1, len(outputs)):
                if self.distance(outputs[i], outputs[j]) > self.epsilon:
                    return False

        print(f"[t={t}] Convergence detected")
        return True
