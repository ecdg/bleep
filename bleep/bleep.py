# Censors messages that contain words that appear on a list of supplied "banned words."
import sys
from cs50 import get_string
from sys import argv


def main():
    # Ensures proper usage
    if len(sys.argv) != 2:
        print('Usage: python bleep.py dictionary')
        sys.exit(1)

    dictionary = sys.argv[1]

    # Data structure to store the words from the dictionary
    words = set()

    # Opens and reads from file then adds each word to the data structure
    file = open(dictionary, "r")
    for line in file:
        words.add(line.rstrip("\n").lower())
    file.close()

    # Prompts the user to provide a message
    message = get_string('What message would you like to censor?\n')

    # Returns a list of the words in the string
    list = message.split()

    # Compares the list of "tokens" (words) from the message w/ the banned words
    for token in list:
        for word in words:
            if word == token.lower():
                # Replaces the words that match with asterisks
                token = '*' * len(token)
        print(token + ' ', end='')

    print()
    sys.exit(0)


if __name__ == "__main__":
    main()
