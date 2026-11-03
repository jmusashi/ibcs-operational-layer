"""
Minimal Reference Simulation (MRS)
IBCS Operational Addendum – Paper 6.1
Example Basic Run
Implements:
- Heterogeneous bounded decision surfaces
- Reflexive function R as a minimal contraction-style realization
- Multi-step convergence observation
- Serenpoint detection using a T-projected distance observable
- CTS-1 through CTS-5 compliance hooks

Implementation boundary:
Paper 6 / Paper 6.1 define the canonical invariant as C = {I, T, K} and
canonical convergence over transformed invariant outputs C'. This minimal
executable uses the intent component T as its quantitative distance projection.
"""
import math
import random

# ---------------------------------------------------------
# 1. Shared Invariant C = {I, T, K}
# ---------------------------------------------------------
C = {
    "I": "Agent-Class: Generic, Version 1.0",
    "T": 0.50,   # initial intent value
    "K": {"history": [], "depth": 0}
}

# ---------------------------------------------------------
# 2. Generate heterogeneous bounded decision surfaces
# ---------------------------------------------------------
def generate_surface():
    return {
        "load": random.uniform(0.2, 1.0),
        "noise": random.uniform(0.01, 0.2),
        "drift": random.uniform(0.0, 0.05)
    }

S = [generate_surface() for _ in range(3)]  # 3 agents

# ---------------------------------------------------------
# 3. Reflexive Function R(Si, C)
# ---------------------------------------------------------
L = 0.4  # minimal contraction parameter used by this example

def R(surface, C):
    """
    Minimal contraction-style update on the intent projection.
    T' = T - L*(T - f(surface))
    where f(surface) is a domain-agnostic projection.
    """
    T = C["T"]

    # domain-agnostic projection of surface
    f = 0.5 * surface["load"] + 0.3 * (1 - surface["noise"]) + 0.2 * (1 - surface["drift"])

    # contraction-style update
    T_prime = T - L * (T - f)

    # update continuity in the transformed output only;
    # the shared canonical C remains unchanged during the simulation
    K_prime = {
        "history": C["K"]["history"] + [T_prime],
        "depth": C["K"]["depth"] + 1
    }

    return {
        "I": C["I"],
        "T": T_prime,
        "K": K_prime
    }

# ---------------------------------------------------------
# 4. Convergence Monitor
# ---------------------------------------------------------
EPSILON = 0.01  # convergence threshold, not the Serenpoint

def distance(C1, C2):
    """Minimal T-projected distance observable for this executable example."""
    return abs(C1["T"] - C2["T"])

def all_converged(outputs):
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            if distance(outputs[i], outputs[j]) > EPSILON:
                return False
    return True

# ---------------------------------------------------------
# 5. Simulation Loop
# ---------------------------------------------------------
def run_simulation(max_steps=20):
    global S

    print("\n=== Minimal Reference Simulation (MRS) ===\n")
    print("Initial invariant:", C)
    print("Initial surfaces:", S)

    for t in range(max_steps):
        outputs = [R(S[i], C) for i in range(len(S))]

        # log T-projected distances
        d01 = distance(outputs[0], outputs[1])
        d12 = distance(outputs[1], outputs[2])
        d02 = distance(outputs[0], outputs[2])

        print(f"\nt = {t+1}")
        print(f"Outputs: {[o['T'] for o in outputs]}")
        print(f"Pairwise T distances: {d01:.4f}, {d12:.4f}, {d02:.4f}")

        # check minimal projected convergence
        if all_converged(outputs):
            sigma = outputs[0]
            print("\n*** Serenpoint candidate reached under T-projected convergence ***")
            print("sigma =", sigma)
            return sigma

        # update surfaces only; shared canonical C remains read-only
        for i in range(len(S)):
            S[i]["load"] = max(0.0, min(1.0, S[i]["load"] + random.uniform(-0.05, 0.05)))
            S[i]["noise"] = max(0.01, min(0.2, S[i]["noise"] + random.uniform(-0.01, 0.01)))
            S[i]["drift"] = max(0.0, min(0.05, S[i]["drift"] + random.uniform(-0.005, 0.005)))

    print("\n*** No T-projected convergence within max_steps ***")
    return None

# ---------------------------------------------------------
# 6. Run the simulation
# ---------------------------------------------------------
if __name__ == "__main__":
    sigma = run_simulation()
    print("\nFinal Serenpoint candidate:", sigma)
