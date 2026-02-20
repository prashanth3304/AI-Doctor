from app.agents.base import ConsultationContext, DoctorAgent


class GeneralPhysicianAgent(DoctorAgent):
    name = "General Physician"


class GastroenterologistAgent(DoctorAgent):
    name = "Gastroenterologist"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Gastro guidance: use bland diet, avoid spicy/fried foods, hydrate well, and seek care "
            "if vomiting blood, severe dehydration, or persistent pain occurs."
        )


class DermatologistAgent(DoctorAgent):
    name = "Dermatologist"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Skin guidance: avoid irritants/new products, keep affected area clean/dry, and consult "
            "dermatology for persistent rash, fever, or spreading lesions."
        )


class CardiologistAgent(DoctorAgent):
    name = "Cardiologist"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Cardiac guidance: avoid exertion, monitor pulse/BP if possible, and obtain urgent "
            "clinical evaluation for chest discomfort or palpitations."
        )


class NutritionistAgent(DoctorAgent):
    name = "Nutritionist"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Nutrition guidance: maintain balanced portions, reduce sugar/salt/processed foods, "
            "and track weekly weight and meal patterns."
        )


class MentalHealthAdvisorAgent(DoctorAgent):
    name = "Mental Health Advisor"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Mental health guidance: establish sleep routine, reduce stress triggers, and speak to a "
            "licensed counselor/psychiatrist for persistent low mood or anxiety."
        )


class HairSpecialistAgent(DoctorAgent):
    name = "Hair Specialist"

    def advice(self, ctx: ConsultationContext) -> str:
        return (
            "Hair guidance: avoid harsh chemicals/heat styling, ensure protein and iron intake, and "
            "consult specialist for sudden or patchy hair loss."
        )
