from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Patient(SQLModel, table=True):
    __tablename__ = "patients"

    id: Optional[int] = Field(default=None, primary_key=True)
    owner_user_id: int = Field(foreign_key="users.id", index=True)
    name: str
    age: int
    allergies: str = ""
    bp_history: str = ""
    sugar_history: str = ""
    previous_illnesses: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
