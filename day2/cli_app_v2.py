import sys
import re

def count_words(text):
    words = text.split()
    print("Jumlah kata:", len(words))

def reverse_text(text):
    reversed_text = text[::-1]
    print("Reverse:", reversed_text)

def to_upper(text):
    print("Uppercase:", text.upper())

def to_lower(text):
    print("Lowercase:", text.lower())

def show_stats(text):
    print("Jumlah Karakter:", len(text))
    print("Jumlah Kata:", len(text.split()))

def clean_text(text):
    clean = re.sub('[^A-Za-z0-9 ]+', '', text)
    print("Clean Karakter:", clean)

# Command mapping - this is what your senior suggested
commands = {
    "count": count_words,
    "reverse": reverse_text,
    "upper": to_upper,
    "lower": to_lower,
    "stats": show_stats,
    "clean": clean_text
}

if len(sys.argv) < 3:
    print("Usage: python cli_app_v2.py count \"text\"")
    sys.exit()

command = sys.argv[1]
text = sys.argv[2]

# Instead of if-elif chain, just look up and call the function
if command in commands:
    commands[command](text)
else:
    print("Command tidak dikenal")
