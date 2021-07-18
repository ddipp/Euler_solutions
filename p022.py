#!/usr/bin/env python3

# ===============================================================================
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into alphabetical
# order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
# obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
# ===============================================================================

import string

i = []


def LoadFromFile():
    global i
    f = open('p022.txt', mode='r')
    for lis in f:
        n = lis.split(',')
        for e in n:
            i.append(e[1:-1])


def word_sum(w):
    alphabet = list(string.ascii_uppercase)
    alphabet.insert(0, '')
    w_s = 0
    for lis in w:
        w_s += alphabet.index(lis)
    return w_s


def calc_cost():
    glob_sum = 0
    global i
    for w in i:
        glob_sum += word_sum(w) * (i.index(w) + 1)
    return glob_sum


if __name__ == '__main__':
    LoadFromFile()
    i.sort()
    print(calc_cost())
