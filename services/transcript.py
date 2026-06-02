from models.speech import speech_to_text
from models.summarizer import summarize_text


def process_audio(audio):

    transcript = speech_to_text(audio)

    summary = summarize_text(transcript)


    return {
        "transcript": transcript,
        "summary": summary
    }