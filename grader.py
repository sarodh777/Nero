import random
from env import HospitalEnv

def baseline_agent(env):
    """Random selection agent"""
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

def smart_agent(env):
    """Prioritizes critical patients and considers wait times"""
    state = env.reset()
    total_reward = 0
    
    while True:
        if not state["patients"]:
            break
        
        # Sort: critical first, then by longest wait time
        patients_sorted = sorted(
            state["patients"],
            key=lambda p: (
                0 if p["severity"] == "critical" else 1,
                -p["wait_time"]
            )
        )
        
        patient = patients_sorted[0]
        action = type("obj", (), {"action_type": "assign_bed", "patient_id": patient["id"]})
        state, reward, done, _ = env.step(action)
        total_reward += reward.value
        
        if done:
            break
    
    return total_reward

def grade():
    """Compare baseline vs smart agent"""
    env1 = HospitalEnv()
    env2 = HospitalEnv()
    
    baseline_score = baseline_agent(env1)
    smart_score = smart_agent(env2)
    
    improvement = ((smart_score - baseline_score) / baseline_score * 100) if baseline_score != 0 else 0
    
    return {
        "baseline_score": baseline_score,
        "smart_agent_score": smart_score,
        "improvement_percent": improvement,
        "winner": "Smart Agent" if smart_score > baseline_score else "Baseline"
    }
