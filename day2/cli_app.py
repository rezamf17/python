import sys
import re

if len(sys.argv) < 3:
    print("Usage: python cli_app.py count \"text\"")
    sys.exit()

command = sys.argv[1]
text = sys.argv[2]

if command == "count":
    words = text.split()
    print("Jumlah kata:", len(words))
elif command == "reverse":
    words = text[::-1]
    print("Reverse:", words)
elif command == "upper":
    words = text.upper()
    print("Uppercase:", words)
elif command == "lower":
    words = text.lower()
    print("Lowercase:", words)
elif command == "stats":
    words = text
    print("Jumlah Karakter:", len(words))
    print("Jumlah Kata:", len(words.split()))
elif command == "clean":
    words = text
    clean = re.sub('[^A-Za-z0-9]+', '', words)
    print("Clean Karakter:", clean)
else:
    print("Command tidak dikenal")