# Hospital Resource Allocation Environment

Simulates hospital decision-making for AI agents to optimize patient bed allocation under constraints.

## Project Structure

```
baseline_agent.py      - Random selection agent (baseline score: 1.5)
smart_agent.py         - Priority-based agent (prioritizes critical patients)
env.py                 - Hospital environment with state management
models.py              - Pydantic models for type safety
grader.py              - Comprehensive grading system
test_scenarios.py      - Test suite with multiple scenarios
Dockerfile             - Container configuration
```

## Quick Start

### Option 1: Direct Python (with venv)
```powershell
.\.venv\Scripts\Activate.ps1
python baseline_agent.py
python smart_agent.py
python -c "from grader import grade; import json; print(json.dumps(grade(), indent=2))"
```

### Option 2: Full Path (no venv activation needed)
```powershell
.\.venv\Scripts\python.exe baseline_agent.py
.\.venv\Scripts\python.exe smart_agent.py
.\.venv\Scripts\python.exe test_scenarios.py
```

### Option 3: Docker
```powershell
docker build -t hospital-env .
docker run hospital-env
```

## Agents

### 🎲 Baseline Agent
- **Strategy**: Random patient selection
- **Score**: 1.5
- **File**: `baseline_agent.py`

### 🧠 Smart Agent
- **Strategy**: Prioritizes critical severity patients, considers wait times
- **Score**: 1.5 (on default scenario)
- **File**: `smart_agent.py`

### 📊 Grader
- Compares both agents
- Calculates improvement percentage
- Provides structured results
- **File**: `grader.py`

## Test Scenarios

The `test_scenarios.py` runs comprehensive tests on three scenarios:

1. **Default** (1 critical, 1 normal) - Simple case
2. **All Critical** (3 critical patients, 2 beds) - Resource constraint
3. **High Wait Time Mix** - Mixed severity with varying wait times

## Environment Details

### State
```python
{
    "patients": [
        {"id": int, "severity": str, "wait_time": int},
        ...
    ],
    "available_beds": int,
    "available_doctors": int
}
```

### Actions
```python
{
    "action_type": "assign_bed",
    "patient_id": int
}
```

### Rewards
- Critical patient assigned: +1.0
- Normal patient assigned: +0.5
- No bed available: -0.5
- Critical patient wait > 3: -1.0 per step

## Installation

### Dependencies
- Python 3.10+
- pydantic

### Setup
```powershell
cd path\to\python01
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pydantic
```

## Running Tests

```powershell
# Test all scenarios
python test_scenarios.py

# Test individual agents
python baseline_agent.py
python smart_agent.py

# Get grading results
python -c "from grader import grade; result = grade(); print(result)"
```

## Next Steps

1. **Improve Agent Strategy** - Add reinforcement learning
2. **More Scenarios** - Test with varying bed availability
3. **Metrics Dashboard** - Real-time performance tracking
4. **API Interface** - RESTful endpoint for agent interaction
5. **Machine Learning** - Train agents with Q-learning or policy gradients

## Files Modified

- ✅ `env.py` - Fixed infinite loop (increased beds from 1 to 2)
- ✅ `models.py` - Pydantic models for type safety
- ✅ `baseline_agent.py` - Working baseline
- ✅ `smart_agent.py` - New priority-based agent
- ✅ `grader.py` - Full grading implementation
- ✅ `test_scenarios.py` - Comprehensive test suite

