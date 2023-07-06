# Exercise 23: Strings, Bytes and Character Encoding.

# What we are going to understand.
# 1) How modern computers store human languages for display and processing.
# 2) Encode and Decode python's stirngs intoa type called bytes.
# 3) handle errors during string and byte handling.
# 4) How to read code and find out what it means even if you've never seen it before.

# resource : languages.txt file contains list of human language names that are encoded in UTF-8.

import sys

script, input_encoding, error = sys.argv # argument variables

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<<-->>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)

