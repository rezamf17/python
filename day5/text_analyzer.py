def word_count(text):
    words = text.split()
    return len(words)


def word_frequency(text):
    words = text.split()

    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def most_common_word(freq):
    max_word = None
    max_count = 0

    for word, count in freq.items():
        if count > max_count:
            max_word = word
            max_count = count

    return max_word, max_count

def unique_words(text):
    words = text.split()
    return len(set(words))

def top_3_words(freq):
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3]

def bigrams(text):
    words = text.split()
    result = []
    for i in range(len(words) - 1):
        pair = (words[i], words[i+1])
        result.append(pair)
    return result

def trigrams(text):
    words = text.split()
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