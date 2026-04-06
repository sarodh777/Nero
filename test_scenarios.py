import random
from env import HospitalEnv

class ScenarioTester:
    """Test agents in different scenarios"""
    
    @staticmethod
    def test_scenario(name, agent_func, patient_setup):
        """Run an agent on a specific scenario"""
        env = HospitalEnv()
        
        # Set up custom state
        env.state_data = {
            "patients": [p.copy() for p in patient_setup["patients"]],
            "available_beds": patient_setup["available_beds"],
            "available_doctors": patient_setup["available_doctors"]
        }
        
        state = env.state()
        total_reward = 0
        steps = 0
        
        while True:
            if not state["patients"]:
                break
            
            action = agent_func(state)
            if action is None:
                break
                
            state, reward, done, _ = env.step(action)
            total_reward += reward.value
            steps += 1
            
            if done or steps > 100:  # Prevent infinite loops
                break
        
        return {
            "scenario": name,
            "total_reward": total_reward,
            "steps": steps,
            "patients_remaining": len(state["patients"])
        }
    
    @staticmethod
    def baseline_strategy(state):
        """Random selection"""
        if state["patients"]:
            patient = random.choice(state["patients"])
            return type("obj", (), {"action_type": "assign_bed", "patient_id": patient["id"]})
        return None
    
    @staticmethod
    def smart_strategy(state):
        """Prioritize critical patients"""
        if state["patients"]:
            patients_sorted = sorted(
                state["patients"],
                key=lambda p: (0 if p["severity"] == "critical" else 1, -p["wait_time"])
            )
            patient = patients_sorted[0]
            return type("obj", (), {"action_type": "assign_bed", "patient_id": patient["id"]})
        return None

# Test Scenarios
scenarios = [
    {
        "name": "Default (1 critical, 1 normal)",
        "patients": [
            {"id": 1, "severity": "critical", "wait_time": 0},
            {"id": 2, "severity": "normal", "wait_time": 0}
        ],
        "available_beds": 2,
        "available_doctors": 1
    },
    {
        "name": "All Critical (Limited Beds)",
        "patients": [
            {"id": 1, "severity": "critical", "wait_time": 0},
            {"id": 2, "severity": "critical", "wait_time": 0},
            {"id": 3, "severity": "critical", "wait_time": 0}
        ],
        "available_beds": 2,
        "available_doctors": 1
    },
    {
        "name": "High Wait Time Mix",
        "patients": [
            {"id": 1, "severity": "normal", "wait_time": 5},
            {"id": 2, "severity": "critical", "wait_time": 2},
            {"id": 3, "severity": "normal", "wait_time": 3}
        ],
        "available_beds": 2,
        "available_doctors": 1
    }
]

if __name__ == "__main__":
    tester = ScenarioTester()
    
    print("\n" + "=" * 80)
    print(" " * 20 + "🏥 HOSPITAL AGENT TESTING SUITE")
    print("=" * 80)
    
    for scenario in scenarios:
        setup = {
            "patients": scenario["patients"],
            "available_beds": scenario["available_beds"],
            "available_doctors": scenario["available_doctors"]
        }
        
        print(f"\n📋 {scenario['name']}")
        print("-" * 80)
        
        baseline_result = tester.test_scenario(
            scenario["name"],
            tester.baseline_strategy,
            setup
        )
        
        smart_result = tester.test_scenario(
            scenario["name"],
            tester.smart_strategy,
            setup
        )
        
        print(f"{'Agent':<20} {'Reward':<15} {'Steps':<10} {'Remaining':<10}")
        print("-" * 80)
        print(f"{'🎲 Baseline':<20} {baseline_result['total_reward']:<15.2f} {baseline_result['steps']:<10} {baseline_result['patients_remaining']:<10}")
        print(f"{'🧠 Smart Agent':<20} {smart_result['total_reward']:<15.2f} {smart_result['steps']:<10} {smart_result['patients_remaining']:<10}")
        
        diff = smart_result['total_reward'] - baseline_result['total_reward']
        if diff > 0.01:
            winner = f"✅ Smart Agent wins (+{diff:.2f})"
        elif diff < -0.01:
            winner = f"❌ Baseline wins (+{-diff:.2f})"
        else:
            winner = "🔗 Tie"
        print(f"\n{winner}")
    
    print("\n" + "=" * 80)
    print("Testing complete!")
    print("=" * 80 + "\n")

