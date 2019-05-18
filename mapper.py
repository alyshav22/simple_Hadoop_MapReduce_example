#!/usr/bin/env python
import sys

#import a list of stopwords from sklearn
from sklearn.feature_extraction import stop_words
import string

stopwords = set(stop_words.ENGLISH_STOP_WORDS)

# get all input from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()

    # remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            print(f'{word}\t1')


