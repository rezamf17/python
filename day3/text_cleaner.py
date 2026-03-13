def clean_text(text):
    text = text.lower()

    punctuation = [".", ",", "!", "?", ":", ";"]

    for p in punctuation:
        text = text.replace(p, "")

    return text