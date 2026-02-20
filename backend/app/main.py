from fastapi import FastAPI

from app.api import auth, consultation, profiles
from app.core.config import settings
from app.db import base  # noqa: F401
from app.db.session import create_db_and_tables

app = FastAPI(title=settings.app_name, version="1.0.0")


@app.on_event("startup")
def startup_event() -> None:
    create_db_and_tables()


@app.get("/")
def root():
    return {
        "service": settings.app_name,
        "status": "running",
        "disclaimer": settings.disclaimer,
    }


app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(profiles.router, prefix=settings.api_prefix)
app.include_router(consultation.router, prefix=settings.api_prefix)
