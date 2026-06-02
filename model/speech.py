from transformers import pipeline


speech_model = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base"
)


def speech_to_text(audio):

    result = speech_model(audio)

    return result["text"]