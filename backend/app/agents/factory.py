from app.agents.base import DoctorAgent
from app.agents.specialists import (
    CardiologistAgent,
    DermatologistAgent,
    GastroenterologistAgent,
    GeneralPhysicianAgent,
    HairSpecialistAgent,
    MentalHealthAdvisorAgent,
    NutritionistAgent,
)

AGENT_MAP: dict[str, DoctorAgent] = {
    "General Physician": GeneralPhysicianAgent(),
    "Gastroenterologist": GastroenterologistAgent(),
    "Dermatologist": DermatologistAgent(),
    "Cardiologist": CardiologistAgent(),
    "Nutritionist": NutritionistAgent(),
    "Mental Health Advisor": MentalHealthAdvisorAgent(),
    "Hair Specialist": HairSpecialistAgent(),
}


def get_doctor_agent(specialist: str) -> DoctorAgent:
    return AGENT_MAP.get(specialist, GeneralPhysicianAgent())
