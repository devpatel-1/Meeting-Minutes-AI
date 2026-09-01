from openai import OpenAI

from .config import OPENAI_API_KEY, OPENAI_AUDIO_MODEL


def transcribe_audio(audio_path: str) -> str:

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is not configured."
        )

    client = OpenAI(
        api_key=OPENAI_API_KEY
    )

    with open(audio_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            model=OPENAI_AUDIO_MODEL,
            file=audio_file,
            response_format="text"
        )

    return transcription