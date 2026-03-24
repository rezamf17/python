from text_cleaner import clean_text, stop_words
from text_analyzer import word_count, word_frequency, most_common_word, unique_words, top_3_words
import sys
command = sys.argv[1]
text = sys.argv[2]

if command == "freq":
    clean = clean_text(text)
    freq = word_frequency(clean)

    result = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for word, count in result:
        print(f"{word}: {count}")
# file = open("day3/sample.txt", "r")
# text = file.read()

# clean = clean_text(text)
# stop = stop_words(text)

# count = word_count(clean)
# freq = word_frequency(clean)
# common = most_common_word(freq)
# unique = unique_words(freq)
# top_words = top_3_words(freq)

# print("Total words:", count)
# print("Word frequency:", freq)
# print("Most common word:", common)
# print("Unique Words:", unique)
# print("Top 3 Words:", top_words)
# print("CLEAN:", clean)
# print("STOP:", stop)

