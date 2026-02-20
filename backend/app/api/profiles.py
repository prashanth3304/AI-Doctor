from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.api.deps import get_current_user
from app.db.session import get_session
from app.models.patient import Patient
from app.models.user import User
from app.schemas.patient import PatientCreate

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.post("")
def create_profile(
    payload: PatientCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    patient = Patient(owner_user_id=current_user.id, **payload.model_dump())
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.get("")
def list_profiles(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    return session.exec(select(Patient).where(Patient.owner_user_id == current_user.id)).all()


@router.get("/{patient_id}")
def get_profile(
    patient_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    patient = session.get(Patient, patient_id)
    if not patient or patient.owner_user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Patient profile not found")
    return patient
