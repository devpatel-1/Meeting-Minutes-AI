import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

OPENAI_AUDIO_MODEL = "gpt-4o-mini-transcribe"

LLAMA_MODEL = "meta-llama/Llama-3.1-8B-Instruct"