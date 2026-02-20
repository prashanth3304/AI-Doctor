from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    email: str
    full_name: str
    password: str = Field(min_length=8)
    role: str = "member"


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
