#!/usr/bin/python

#WORD COUNT

def word_count(phrase):
    words = phrase.split(" ")
    words = filter(None, words)
    count = {}
    for word in words:
        count[word] = 1 if word not in count else count[word] + 1
    print count

word_count("Those Beats dropped so so so hard hard hard")