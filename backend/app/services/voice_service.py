def speech_to_text(language: str) -> dict:
    return {
        "language": language,
        "text": "STT placeholder: integrate Whisper/faster-whisper for production.",
    }


def text_to_speech(text: str, language: str) -> dict:
    return {
        "language": language,
        "audio_url": "tts-placeholder.wav",
        "message": f"TTS placeholder generated for: {text[:50]}",
    }
