import operator
from collections import Counter


def most_repeating_letter(word):
    counter = Counter(word).most_common(1)
    return counter[0][1]


def most_repeating_word(words):
    return max(words, key=most_repeating_letter)

print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']))


