from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Report(SQLModel, table=True):
    __tablename__ = "reports"

    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patients.id", index=True)
    file_name: str
    extracted_text: str
    abnormal_findings: str
    summary: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
