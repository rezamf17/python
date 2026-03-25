from text_cleaner import clean_text, stop_words
from text_analyzer import bigrams, trigrams, ngram_frequency
import sys
command = sys.argv[1]
text = sys.argv[2]

if command == "freq":
    clean = clean_text(text)
    freq = word_frequency(clean)

    result = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for word, count in result:
        print(f"{word}: {count}")
elif command == "bigram":
    clean = clean_text(text)
    grams = bigrams(clean)
    freq = ngram_frequency(grams)

    result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(result)

elif command == "trigram":
    clean = clean_text(text)
    grams = trigrams(clean)
    freq = ngram_frequency(grams)

    result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(result)