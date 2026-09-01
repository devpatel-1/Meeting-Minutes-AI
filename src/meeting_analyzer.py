import os

from openai import OpenAI

from .prompts import MEETING_MINUTES_PROMPT


# ==================================================
# OPENAI CLIENT
# ==================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not configured."
    )

client = OpenAI(
    api_key=OPENAI_API_KEY
)


# ==================================================
# GENERATE MEETING MINUTES
# ==================================================

def generate_meeting_minutes(transcript: str) -> str:

    if not transcript or not transcript.strip():
        raise ValueError(
            "Transcript is empty."
        )

    prompt = MEETING_MINUTES_PROMPT.format(
        transcript=transcript
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional meeting "
                    "minutes assistant. "
                    "Analyze the transcript and create "
                    "accurate, concise and structured "
                    "meeting minutes. "
                    "Do not invent information."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()