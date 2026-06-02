import gradio as gr
import tempfile

from services.transcript import process_audio



def generate_notes(audio):

    if audio is None:
        return "", ""


    result = process_audio(audio)


    return (
        result["transcript"],
        result["summary"]
    )



with gr.Blocks(
    title="Voice Notes AI"
) as app:


    gr.Markdown(
    """
    # 🎤 Voice Notes AI

    Speech → Transcript → AI Summary
    """
    )


    audio = gr.Audio(
        sources=[
            "microphone",
            "upload"
        ],
        type="filepath"
    )


    button = gr.Button(
        "Generate Notes"
    )


    transcript = gr.Textbox(
        label="Transcript",
        lines=12
    )


    summary = gr.Textbox(
        label="AI Summary",
        lines=8
    )


    button.click(
        generate_notes,
        inputs=audio,
        outputs=[
            transcript,
            summary
        ]
    )


app.launch()