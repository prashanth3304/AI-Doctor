from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.agents.base import ConsultationContext
from app.agents.factory import get_doctor_agent
from app.api.deps import get_current_user
from app.core.config import settings
from app.db.session import get_session
from app.models.consultation import Consultation
from app.models.patient import Patient
from app.models.user import User
from app.schemas.consultation import ConsultationRequest, ConsultationResponse, SOAPNote
from app.services.emergency import detect_emergency
from app.services.soap import build_soap
from app.services.specialist_router import route_specialist

router = APIRouter(prefix="/consultation", tags=["consultation"])


@router.get("/required-questions")
def required_questions():
    return {
        "questions": [
            "Symptoms",
            "Duration",
            "Severity",
            "Age",
            "Existing diseases",
            "Medication history",
            "Sleep pattern",
            "Diet habits",
        ]
    }


@router.post("/start", response_model=ConsultationResponse)
def start_consultation(
    payload: ConsultationRequest,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    patient = session.get(Patient, payload.patient_id)
    if not patient or patient.owner_user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Patient not found")

    specialist = route_specialist(payload.symptoms)
    emergency_flag, emergency_message = detect_emergency(payload.symptoms)

    patient_history = (
        f"Allergies={patient.allergies}; BP={patient.bp_history}; "
        f"Sugar={patient.sugar_history}; Previous illnesses={patient.previous_illnesses}"
    )

    soap_dict = build_soap(
        symptoms=payload.symptoms,
        duration=payload.duration,
        severity=payload.severity,
        existing_diseases=payload.existing_diseases,
        medication_history=payload.medication_history,
        sleep_pattern=payload.sleep_pattern,
        diet_habits=payload.diet_habits,
        patient_history=patient_history,
        specialist=specialist,
    )

    context = ConsultationContext(
        symptoms=payload.symptoms,
        duration=payload.duration,
        severity=payload.severity,
        age=payload.age,
        existing_diseases=payload.existing_diseases,
        medication_history=payload.medication_history,
        sleep_pattern=payload.sleep_pattern,
        diet_habits=payload.diet_habits,
        patient_history=patient_history,
        emergency_flag=emergency_flag,
    )
    advice = get_doctor_agent(specialist).advice(context)
    advice = f"{advice}\n\nDisclaimer: {settings.disclaimer}"

    db_record = Consultation(
        patient_id=payload.patient_id,
        specialist=specialist,
        age=payload.age,
        symptoms=payload.symptoms,
        duration=payload.duration,
        severity=payload.severity,
        existing_diseases=payload.existing_diseases,
        medication_history=payload.medication_history,
        sleep_pattern=payload.sleep_pattern,
        diet_habits=payload.diet_habits,
        emergency_flag=emergency_flag,
        emergency_message=emergency_message,
        soap_subjective=soap_dict["subjective"],
        soap_objective=soap_dict["objective"],
        soap_assessment=soap_dict["assessment"],
        soap_plan=soap_dict["plan"],
        ai_advice=advice,
    )
    session.add(db_record)
    session.commit()

    return ConsultationResponse(
        specialist=specialist,
        emergency_flag=emergency_flag,
        emergency_message=emergency_message,
        disclaimer=settings.disclaimer,
        soap=SOAPNote(**soap_dict),
        advice=advice,
    )
