def clean_text(text):
    text = text.lower()

    punctuation = [".", ",", "!", "?", ":", ";"]

    for p in punctuation:
        text = text.replace(p, "")

    return text

def stop_words(text):
    text = text.lower()

    conjunction = ["the", "is", "of" ," a ", "an"]

    for p in conjunction:
        text = text.replace(p, "")

    return text