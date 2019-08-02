import math
import pandas as pd

def word_count(txtfile):
    # open book
    # build list of words
    unique_words = []
    with open(txtfile, 'r') as f:
        for line in f:
            for word in line.split():
                unique_words.append(word)
    unique_words = list(unique_words)
    print(unique_words)

    # build dictionary
    dictionary = {}
    for i in unique_words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    # frequency of words
    summation = sum(dictionary.values())
    return dictionary,summation


