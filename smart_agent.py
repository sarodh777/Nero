import random
from env import HospitalEnv

def run():
    """Smart agent that prioritizes critical patients and considers wait times"""
    env = HospitalEnv()
    state = env.reset()
    total_reward = 0

    while True:
        if not state["patients"]:
            break

        # Sort patients: critical first, then by longest wait time
        patients_sorted = sorted(
            state["patients"],
            key=lambda p: (
                0 if p["severity"] == "critical" else 1,  # Critical patients first
                -p["wait_time"]  # Then by longest wait time
            )
        )

        # Pick the best patient
        patient = patients_sorted[0]
        action = type("obj", (), {"action_type": "assign_bed", "patient_id": patient["id"]})

        state, reward, done, _ = env.step(action)
        total_reward += reward.value

        if done:
            break

    return total_reward

if __name__ == "__main__":
    print("Smart Agent Score:", run())
