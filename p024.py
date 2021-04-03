#!/usr/bin/env python3

# ===============================================================================
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# ===============================================================================

# import time
# start_time = time.time()

import itertools as it


def solution():
    x = 1
    for i in it.permutations("0123456789"):
        if x == 1e6:
            return ''.join(i)
        else:
            x += 1


if __name__ == '__main__':
    print(solution())

# print("--- %s seconds ---" % (time.time() - start_time))
