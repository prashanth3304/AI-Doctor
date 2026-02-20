from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session

from app.api.deps import get_current_user
from app.db.session import get_session
from app.models.report import Report
from app.models.user import User
from app.services.report_parser import parse_abnormal_values

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/analyze")
async def analyze_report(
    patient_id: int = Form(...),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    content = await file.read()
    extracted = content.decode("utf-8", errors="ignore")[:5000]
    abnormalities = parse_abnormal_values(extracted)
    summary = (
        "Abnormal values detected." if abnormalities else "No obvious abnormal values detected from parsed text."
    )

    report = Report(
        patient_id=patient_id,
        file_name=file.filename,
        extracted_text=extracted,
        abnormal_findings="; ".join(abnormalities),
        summary=summary,
    )
    session.add(report)
    session.commit()
    return {
        "file": file.filename,
        "abnormal_findings": abnormalities,
        "summary": summary,
        "disclaimer": "AI extraction may miss details. Please verify with your doctor.",
    }
