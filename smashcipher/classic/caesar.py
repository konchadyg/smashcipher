#!/usr/bin/env python3
from guess_language import guess_language


def caesar_shift(text, alphabet, offset):
    table = str.maketrans(alphabet, alphabet[offset:] + alphabet[:offset])
    return text.translate(table)


def ettubrute(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', lang='en'):
    solutions = []
    for x in range(1, len(alphabet)):
        shifted = caesar_shift(text, alphabet, x)
        if guess_language(shifted) == lang:
            solutions.append((x, shifted))
    return solutions


def main():
    text = input("Ciphertext: ")
    case_sensitive = input('Case sensitive: [y/N] ')
    alphabet = input('Alphabet: [ABCDEFGHIJKLMNOPQRSTUVWXYZ] ')
    if not alphabet:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lang = input('Language: [en] ')
    if not lang:
        lang = 'en'
    if case_sensitive != 'Y' and case_sensitive != 'y':
        text = text.upper()
        alphabet = alphabet.upper()
    print(ettubrute(text, alphabet, lang))

if __name__ == '__main__':
    main()
