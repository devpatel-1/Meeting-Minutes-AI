import gradio as gr

from src.transcription import transcribe_audio
from src.meeting_analyzer import generate_meeting_minutes
from src.utils import validate_audio_file

from ui.theme import create_theme
from ui.styles import CUSTOM_CSS


# ==================================================
# PROCESS MEETING
# ==================================================

def process_meeting(audio_path):

    if not audio_path:
        raise gr.Error(
            "Please upload a meeting recording."
        )

    try:

        # ------------------------------------------
        # Validate uploaded file
        # ------------------------------------------

        validate_audio_file(audio_path)

        # ------------------------------------------
        # Step 1: Audio → Transcript
        # ------------------------------------------

        transcript = transcribe_audio(audio_path)

        if not transcript:
            raise gr.Error(
                "Unable to generate a transcript."
            )

        # ------------------------------------------
        # Step 2: Transcript → Meeting Minutes
        # ------------------------------------------

        meeting_minutes = generate_meeting_minutes(
            transcript
        )

        if not meeting_minutes:
            raise gr.Error(
                "Unable to generate meeting minutes."
            )

        return meeting_minutes, transcript

    except gr.Error:
        raise

    except Exception as e:
        raise gr.Error(str(e))


# ==================================================
# APPLICATION UI
# ==================================================

with gr.Blocks(
    title="Meeting Minutes AI"
) as app:

    # ----------------------------------------------
    # Header
    # ----------------------------------------------

    with gr.Column(
        elem_classes="app-header"
    ):

        gr.Image(
            value="assets/logo.png",
            show_label=False,
            container=False,
            height=100
        )

        gr.Markdown(
            """
            <div class="app-title">
                Meeting Minutes AI
            </div>

            <div class="app-subtitle">
                Transform your meeting recordings into
                clear, structured minutes with AI.
            </div>
            """
        )

    # ----------------------------------------------
    # Upload Section
    # ----------------------------------------------

    with gr.Column(
        elem_classes="result-card"
    ):

        gr.Markdown(
            "### 📁 Upload Meeting Recording"
        )

        gr.Markdown(
            "Upload an MP3 recording of your meeting."
        )

        audio_input = gr.Audio(
            sources=["upload"],
            type="filepath",
            format="mp3",
            label="Meeting Recording"
        )

        generate_button = gr.Button(
            "✨ Generate Meeting Minutes",
            variant="primary",
            size="lg"
        )

    # ----------------------------------------------
    # Meeting Minutes
    # ----------------------------------------------

    gr.Markdown(
        "## 📋 Meeting Minutes",
        elem_classes="section-title"
    )

    minutes_output = gr.Markdown(
        value="Your generated meeting minutes will appear here."
    )

    # ----------------------------------------------
    # Transcript
    # ----------------------------------------------

    gr.Markdown(
        "## 📝 Full Transcript",
        elem_classes="section-title"
    )

    transcript_output = gr.Textbox(
        placeholder="The meeting transcript will appear here...",
        lines=15,
        interactive=False
    )

    # ----------------------------------------------
    # Button Action
    # ----------------------------------------------

    generate_button.click(
        fn=process_meeting,
        inputs=audio_input,
        outputs=[
            minutes_output,
            transcript_output
        ],
        show_progress="full"
    )

    # ----------------------------------------------
    # Footer
    # ----------------------------------------------

    gr.HTML(
        """
        <div class="app-footer">
            <span class="heart">❤️</span>
            Made with Love and Passion by
            <span class="author">Dev Patel</span>
        </div>
        """
    )


# ==================================================
# START APPLICATION
# ==================================================

if __name__ == "__main__":

    app.launch(
        theme=create_theme(),
        css=CUSTOM_CSS
    )