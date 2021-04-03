#!/usr/bin/env python3

# ===============================================================================
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
# ===============================================================================


def FindChain(num):
    chain = 0
    while num > 1:
        chain += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
    return chain


def solution():
    n = int(1e6)
    max_chain = 0
    for i in range(n):
        new_chain = FindChain(i)
        if max_chain < new_chain:
            print("New max chain = {0}. Number = {1}".format(new_chain, i))
            max_chain = new_chain


if __name__ == '__main__':
    solution()
