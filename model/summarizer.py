from transformers import pipeline


summary_model = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text):

    if len(text) < 100:
        return text


    result = summary_model(
        text,
        max_length=120,
        min_length=30,
        do_sample=False
    )


    return result[0]["summary_text"]