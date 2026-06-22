# reflexive_engine.py
# Reflexive function R(Si, C) -> C'

def reflexive_update(S, C):
    # Extract components
    I = C["I"]
    T = C["T"]
    K = C["K"]

    # Domain-specific transformation (simple contraction)
    signal = S["signal"]
    noise = S["noise"]

    # Updated intent moves slightly toward the agent's signal
    T_prime = [
        0.9 * T[0] + 0.1 * signal,
        0.9 * T[1] + 0.1 * noise
    ]

    # Continuity update
    K_prime = K + [(signal, noise)]

    # Construct updated invariant
    C_prime = {
        "I": I,
        "T": T_prime,
        "K": K_prime
    }

    return C_prime
