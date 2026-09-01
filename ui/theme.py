import gradio as gr


def create_theme():
    return gr.themes.Soft(
        primary_hue="indigo",
        secondary_hue="slate",
        neutral_hue="slate",
        font=[
            gr.themes.GoogleFont("Inter"),
            "system-ui",
            "sans-serif"
        ],
    )