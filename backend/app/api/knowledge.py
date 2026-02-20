from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlmodel import Session

from app.api.deps import get_current_user
from app.db.session import get_session
from app.models.knowledge import KnowledgeDocument
from app.models.user import User
from app.services.rag_service import ingest_knowledge_file, query_knowledge

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

DATA_DIR = Path("knowledge_uploads")
DATA_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_knowledge(
    title: str = Form(...),
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
):
    save_path = DATA_DIR / file.filename
    save_path.write_bytes(await file.read())

    doc = KnowledgeDocument(uploaded_by=current_user.id, title=title, source_path=str(save_path))
    session.add(doc)
    session.commit()

    index_result = ingest_knowledge_file(str(save_path))
    return {"message": "Knowledge file uploaded", "index": index_result}


@router.post("/query")
def query(payload: dict, current_user: User = Depends(get_current_user)):
    _ = current_user
    return query_knowledge(payload.get("question", ""))
