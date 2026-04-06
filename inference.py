#!/usr/bin/env python3
"""
Inference module for Hospital Resource Allocation Environment
Runs both baseline and smart agents to evaluate performance
"""

import json
from baseline_agent import run as run_baseline
from smart_agent import run as run_smart


def main():
    """Run inference with both agents and display results"""
    print("=" * 60)
    print("Hospital Resource Allocation - Agent Inference")
    print("=" * 60)
    
    # Run baseline agent
    print("\n📊 Running Baseline Agent (Random Selection)...")
    baseline_score = run_baseline()
    print(f"✓ Baseline Score: {baseline_score:.2f}")
    
    # Run smart agent
    print("\n🧠 Running Smart Agent (Priority-Based)...")
    smart_score = run_smart()
    print(f"✓ Smart Agent Score: {smart_score:.2f}")
    
    # Calculate improvement
    improvement = ((smart_score - baseline_score) / baseline_score * 100) if baseline_score != 0 else 0
    winner = "Smart Agent" if smart_score > baseline_score else "Baseline"
    
    # Display results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    results = {
        "baseline_score": baseline_score,
        "smart_agent_score": smart_score,
        "improvement_percent": improvement,
        "winner": winner
    }
    print(json.dumps(results, indent=2))
    
    return results


if __name__ == "__main__":
    main()
