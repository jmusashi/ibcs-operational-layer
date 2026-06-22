# surface_generator.py
# Decision surface generator for MRS

import random

def generate_initial_surface(agent_id):
    # Heterogeneous surfaces: each agent gets different values
    return {
        "signal": random.uniform(0, 1),
        "noise": random.uniform(0, 0.2),
        "agent_id": agent_id
    }

def update_surface(S):
    # Simple bounded update rule
    S["signal"] = max(0, min(1, S["signal"] + random.uniform(-0.05, 0.05)))
    S["noise"] = max(0, min(0.2, S["noise"] + random.uniform(-0.01, 0.01)))
    return S
