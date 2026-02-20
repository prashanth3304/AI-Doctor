from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Consultation(SQLModel, table=True):
    __tablename__ = "consultations"

    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patients.id", index=True)
    specialist: str
    age: int
    symptoms: str
    duration: str
    severity: str
    existing_diseases: str
    medication_history: str
    sleep_pattern: str
    diet_habits: str
    emergency_flag: bool = False
    emergency_message: str = ""
    soap_subjective: str
    soap_objective: str
    soap_assessment: str
    soap_plan: str
    ai_advice: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
