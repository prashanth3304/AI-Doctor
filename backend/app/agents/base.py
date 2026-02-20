from dataclasses import dataclass


@dataclass
class ConsultationContext:
    symptoms: str
    duration: str
    severity: str
    age: int
    existing_diseases: str
    medication_history: str
    sleep_pattern: str
    diet_habits: str
    patient_history: str
    emergency_flag: bool


class DoctorAgent:
    name: str = "General Physician"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            f"{self.name} advice: monitor symptoms ({ctx.symptoms}), keep hydration, rest, "
            "and schedule an in-person consultation for diagnosis."
        )
