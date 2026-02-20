from typing import Final

SPECIALISTS: Final = {
    "general": "General Physician",
    "gastro": "Gastroenterologist",
    "derma": "Dermatologist",
    "cardio": "Cardiologist",
    "nutrition": "Nutritionist",
    "mental": "Mental Health Advisor",
    "hair": "Hair Specialist",
}


def route_specialist(symptoms: str) -> str:
    text = symptoms.lower()
    if any(word in text for word in ["chest pain", "palpitation", "heart", "bp high"]):
        return SPECIALISTS["cardio"]
    if any(word in text for word in ["stomach", "acidity", "gas", "diarrhea", "constipation", "ulcer"]):
        return SPECIALISTS["gastro"]
    if any(word in text for word in ["rash", "itch", "acne", "eczema", "skin"]):
        return SPECIALISTS["derma"]
    if any(word in text for word in ["hair fall", "dandruff", "scalp", "hair loss", "alopecia"]):
        return SPECIALISTS["hair"]
    if any(word in text for word in ["anxiety", "depression", "stress", "panic", "suicidal"]):
        return SPECIALISTS["mental"]
    if any(word in text for word in ["diet", "nutrition", "weight", "obesity", "meal plan"]):
        return SPECIALISTS["nutrition"]
    return SPECIALISTS["general"]
