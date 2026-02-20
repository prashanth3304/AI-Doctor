def build_soap(
    symptoms: str,
    duration: str,
    severity: str,
    existing_diseases: str,
    medication_history: str,
    sleep_pattern: str,
    diet_habits: str,
    patient_history: str,
    specialist: str,
) -> dict[str, str]:
    subjective = (
        f"Symptoms: {symptoms}. Duration: {duration}. Severity: {severity}. "
        f"Sleep pattern: {sleep_pattern}. Diet habits: {diet_habits}."
    )
    objective = (
        f"Known history from profile: {patient_history}. Existing diseases: {existing_diseases}. "
        f"Medication history: {medication_history}."
    )
    assessment = f"AI triage routed this case to {specialist} based on symptom keywords."
    plan = (
        "Provide preliminary self-care guidance, monitor progression, and seek licensed medical review. "
        "Escalate immediately if red-flag symptoms worsen."
    )
    return {
        "subjective": subjective,
        "objective": objective,
        "assessment": assessment,
        "plan": plan,
    }
