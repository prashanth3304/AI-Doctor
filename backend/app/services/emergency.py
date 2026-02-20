EMERGENCY_TERMS = [
    "chest pain",
    "breathing difficulty",
    "can't breathe",
    "shortness of breath",
    "suicidal",
    "suicide",
    "self harm",
]


def detect_emergency(symptoms: str) -> tuple[bool, str]:
    text = symptoms.lower()
    if any(term in text for term in EMERGENCY_TERMS):
        return (
            True,
            "Emergency warning: possible high-risk symptoms detected. Call emergency services now or go to nearest ER.",
        )
    return False, "No emergency red flags detected from current text."
