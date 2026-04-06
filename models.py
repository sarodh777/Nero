from pydantic import BaseModel
from typing import List

class Patient(BaseModel):
    id: int
    severity: str
    wait_time: int

class Observation(BaseModel):
    patients: List[Patient]
    available_beds: int
    available_doctors: int

class Action(BaseModel):
    action_type: str
    patient_id: int | None = None

class Reward(BaseModel):
    value: float
