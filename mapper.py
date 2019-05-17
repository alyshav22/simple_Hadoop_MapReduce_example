#!/usr/bin/env python
import os.path
from sklearn.feature_extraction import stop_words
import string

stopwords = set(stop_words.ENGLISH_STOP_WORDS)


f = open(os.path.expanduser('~') + '/shakespeare.txt', 'r')
outfile = os.path.expanduser('~') + '/intermediate_result'
g = open(outfile, 'w')
g.close()
# get all lines from stdin
for line in f:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = line.translate(str.maketrans('', '', string.punctuation))

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            #print(f'{word}\t1')
            g=open(outfile, 'a')
            g.write(f'{word}\t1\n')
            g.close()

f.close()

