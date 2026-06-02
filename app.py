from transformers import pipeline
import gradio as gr
import tempfile

speech_model = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base"
)

def transcribe_audio(audio_path):
    if audio_path is None:
        return "", None

    try:
        result = speech_model(audio_path)

        transcript = result["text"]

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt",
            mode="w",
            encoding="utf-8"
        )

        temp_file.write(transcript)
        temp_file.close()

        return transcript, temp_file.name

    except Exception as e:
        return f"Error: {str(e)}", None


with gr.Blocks(title="Voice Notes AI") as app:

    gr.Markdown(
        """
        # 🎤 Voice Notes AI

        Convert speech into text using Whisper AI.
        """
    )

    audio_input = gr.Audio(
        sources=["microphone", "upload"],
        type="filepath",
        label="Record or Upload Audio"
    )

    transcribe_btn = gr.Button("Transcribe")

    transcript_output = gr.Textbox(
        label="Transcript",
        lines=10
    )

    download_output = gr.File(
        label="Download Transcript"
    )

    clear_btn = gr.ClearButton(
        [audio_input, transcript_output, download_output]
    )

    transcribe_btn.click(
        fn=transcribe_audio,
        inputs=audio_input,
        outputs=[transcript_output, download_output]
    )

app.launch()