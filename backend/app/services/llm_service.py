from app.core.config import settings


def advisory_response(specialist: str, soap: dict, emergency: bool, emergency_message: str) -> str:
    base = (
        f"Consulting Specialist: {specialist}.\n"
        f"Summary: {soap['assessment']}\n"
        "Advice: Stay hydrated, maintain symptom diary, avoid self-medication changes, and seek in-person clinical review."
    )
    if emergency:
        base += f"\n{emergency_message}"
    base += f"\nDisclaimer: {settings.default_disclaimer}"
    return base
