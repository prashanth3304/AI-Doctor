from pydantic import BaseModel, Field


class ConsultationRequest(BaseModel):
    patient_id: int
    symptoms: str = Field(min_length=3)
    duration: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    age: int = Field(ge=0, le=120)
    existing_diseases: str
    medication_history: str
    sleep_pattern: str
    diet_habits: str


class SOAPNote(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str


class ConsultationResponse(BaseModel):
    specialist: str
    emergency_flag: bool
    emergency_message: str
    disclaimer: str
    soap: SOAPNote
    advice: str
