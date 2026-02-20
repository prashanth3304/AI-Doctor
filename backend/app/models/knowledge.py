from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class KnowledgeDocument(SQLModel, table=True):
    __tablename__ = "knowledge_documents"

    id: Optional[int] = Field(default=None, primary_key=True)
    uploaded_by: int = Field(foreign_key="users.id", index=True)
    title: str
    source_path: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
