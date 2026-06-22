# mrs_core.py
# Minimal Reference Simulation (MRS) — IBCS Operational Layer
# Aligned with Paper 6.1, Section 6

from surface_generator import generate_initial_surface, update_surface
from reflexive_engine import reflexive_update
from convergence_monitor import ConvergenceMonitor

class Agent:
    def __init__(self, agent_id, invariant, surface):
        self.id = agent_id
        self.C = invariant
        self.S = surface

    def step(self):
        C_prime = reflexive_update(self.S, self.C)
        self.S = update_surface(self.S)
        return C_prime

def run_mrs(num_agents=3, max_steps=50, epsilon=0.01):
    # Shared invariant C = {I, T, K}
    C = {
        "I": "Generic-Agent",
        "T": [1.0, 0.0],  # simple directional vector
        "K": []
    }

    # Initialize agents
    agents = []
    for i in range(num_agents):
        Si = generate_initial_surface(i)
        agents.append(Agent(i, C, Si))

    monitor = ConvergenceMonitor(epsilon)

    for t in range(max_steps):
        outputs = []

        for agent in agents:
            C_prime = agent.step()
            outputs.append(C_prime)

        if monitor.check_convergence(outputs, t):
            print(f"Serenpoint reached at t={t}")
            print("sigma =", outputs[0])
            return outputs[0]

    print("No convergence within max_steps")
    return None

if __name__ == "__main__":
    run_mrs()
