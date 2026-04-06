from models import Reward

class HospitalEnv:
    def __init__(self):
        self.state_data = None

    def reset(self):
        self.state_data = {
            "patients": [
                {"id": 1, "severity": "critical", "wait_time": 0},
                {"id": 2, "severity": "normal", "wait_time": 0}
            ],
            "available_beds": 2,
            "available_doctors": 1
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        reward = 0
        patient = next((p for p in self.state_data["patients"] if p["id"] == action.patient_id), None)

        if action.action_type == "assign_bed" and patient:
            if self.state_data["available_beds"] > 0:
                self.state_data["available_beds"] -= 1

                if patient["severity"] == "critical":
                    reward += 1.0
                else:
                    reward += 0.5

                self.state_data["patients"].remove(patient)
            else:
                reward -= 0.5

        for p in self.state_data["patients"]:
            p["wait_time"] += 1
            if p["wait_time"] > 3 and p["severity"] == "critical":
                reward -= 1.0

        done = len(self.state_data["patients"]) == 0

        return self.state(), Reward(value=reward), done, {}
