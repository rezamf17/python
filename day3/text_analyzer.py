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