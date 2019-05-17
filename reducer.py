#!/usr/bin/env python
import sys
import os.path

f = open(os.path.expanduser('~') + '/intermediate_result', 'r')
outfile = os.path.expanduser('~') + '/final_result'
g = open(outfile, 'w')
g.close()
# maps words to their counts
word2count = {}

# input comes from STDIN
for line in f:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py -- split on tabs
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count

# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    #print(f'{word}\t{word2count[word]}')
    #print '%s\t%s'% ( word, word2count[word] )
    g=open(outfile, 'a')
    g.write(f'{word}\t{word2count[word]}\n')
    g.close()

f.close()
