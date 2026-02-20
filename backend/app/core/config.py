from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "AI Family Doctor Phase 1"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./family_doctor.db"
    jwt_secret: str = "phase1-change-this-secret"
    jwt_algorithm: str = "HS256"
    token_expire_minutes: int = 60 * 24
    disclaimer: str = (
        "This AI system provides medical guidance support only and is NOT a replacement "
        "for qualified doctors or emergency services."
    )


settings = Settings()
