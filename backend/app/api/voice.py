from fastapi import APIRouter

from app.services.voice_service import speech_to_text, text_to_speech

router = APIRouter(prefix="/voice", tags=["voice"])


@router.post("/stt")
def stt(payload: dict):
    return speech_to_text(payload.get("language", "en"))


@router.post("/tts")
def tts(payload: dict):
    return text_to_speech(payload.get("text", ""), payload.get("language", "en"))
