import random
from env import HospitalEnv

def run():
    env = HospitalEnv()
    state = env.reset()
    total_reward = 0

    while True:
        if not state["patients"]:
            break

        patient = random.choice(state["patients"])
        action = type("obj", (), {"action_type": "assign_bed", "patient_id": patient["id"]})

        state, reward, done, _ = env.step(action)
        total_reward += reward.value

        if done:
            break

    return total_reward

if __name__ == "__main__":
    print("Baseline Score:", run())
