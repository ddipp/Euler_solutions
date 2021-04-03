#!/usr/bin/env python3

# ===============================================================================
# The n^th term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
# so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word
# value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?
# ===============================================================================


def check_triangle(n):
    c = ((1 + 8 * n)**0.5 - 1) / 2
    if c == int(c):
        return True
    else:
        return False


def solution():
    alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    triangle_words_count = 0
    with open('p042.txt', mode='r') as f:
        line = f.readline()
        words = [l[1:-1] for l in line.split(',')]

    # For each word in file - calc sum and check on triangle
    for index in range(len(words)):
        word_sum = sum([alphabet.index(l) for l in words[index]])
        if check_triangle(word_sum):
            triangle_words_count += 1

    return triangle_words_count


if __name__ == '__main__':
    print(solution())
