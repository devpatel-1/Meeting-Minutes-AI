import os
import tempfile


def validate_audio_file(audio_path: str) -> None:
    """Validate that an audio file exists and is an MP3."""

    if not audio_path:
        raise ValueError("Please upload an audio file.")

    if not os.path.exists(audio_path):
        raise ValueError("Audio file could not be found.")

    extension = os.path.splitext(audio_path)[1].lower()

    if extension != ".mp3":
        raise ValueError("Please upload an MP3 file.")


def save_uploaded_audio(audio_path: str) -> str:
    """
    Create a temporary copy of the uploaded audio file.

    Returns:
        Path to the temporary audio file.
    """

    validate_audio_file(audio_path)

    temp_file = tempfile.NamedTemporaryFile(
        suffix=".mp3",
        delete=False
    )

    with open(audio_path, "rb") as source:
        temp_file.write(source.read())

    temp_file.close()

    return temp_file.name


def cleanup_file(file_path: str) -> None:
    """Remove a temporary file if it exists."""

    if file_path and os.path.exists(file_path):
        os.remove(file_path)