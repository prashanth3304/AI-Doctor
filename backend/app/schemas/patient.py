from pydantic import BaseModel, Field


class PatientCreate(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    allergies: str = ""
    bp_history: str = ""
    sugar_history: str = ""
    previous_illnesses: str = ""


class PatientResponse(PatientCreate):
    id: int
    owner_user_id: int
