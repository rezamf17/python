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

def bigrams(text):
    result = []
    for i in range(len(words) - 1):
        pair = (words[i], words[i+1])
        result.append(pair)
    return result

def trigrams(words):
    result = []
    for i in range(len(words) - 2):
        trio = (words[i], words[i+1], words[i+2])
        result.append(trio)
    return result

def ngram_frequency(ngrams):
    freq = {}
    for gram in ngrams:
        freq[gram] = freq.get(gram, 0) + 1
    return freq

def ngram_frequency(ngrams):
    freq = {}
    for gram in ngrams:
        freq[gram] = freq.get(gram, 0) + 1
    return freq