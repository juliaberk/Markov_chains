"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as f:
        return f.read()
    #return "Contents of your file as one long string"


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # code for bi-gram
    # chains = {}

    # words = text_string.split()
    # words.append(None)

    # for i in range(len(words)-2):
    #     key = (words[i], words[i+1])

    #     if chains.get(key):
    #         chains[key].append(words[i+2])
    #     else:
    #         chains[key] = [words[i+2]]

    # return chains

    # code for tri-gram
    chains = {}

    words = text_string.split()
    words.append(None)

    ngram = 3

    for i in range(len(words)-ngram):
        key = []

        for j in range(ngram):
            key.append(words[i+j])
        key = tuple(key)

        if chains.get(key):
            chains[key].append(words[i+ngram])
        else:
            chains[key] = [words[i + ngram]]

    return chains


def make_text(chains):
    """Return text from chains."""

    #bygram = sorted(chains)[0]

    while True:
        bygram = choice(chains.keys())

        if bygram[0][0].isupper():
            break

    words = list(bygram)

    while choice(chains[bygram]):
        # words.extend([bygram[0], bygram[1]])
        new_word = choice(chains[bygram])
        if new_word is None:
            break
        words.append(new_word)

        # resetting for bi-gram
        # bygram = (bygram[1], new_word)

        # resetting for tri-gram
        bygram = (bygram[1], bygram[2], new_word)

    return " ".join(words)


# input_path = "green-eggs.txt"
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
