#!/usr/bin/env python3

# ===============================================================================
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.
# ===============================================================================

# import time
# start_time = time.time()

import itertools as it


def check_pandigital(s):
    res = int(''.join(s[:4]))
    for i in range(1, 5):
        f1 = int(''.join(s[4:(4 + i)]))
        f2 = int(''.join(s[(4 + i):]))
        if res == f1 * f2:
            return res


def solution():
    result = []
    for s in it.permutations("123456789"):
        r = check_pandigital(s)
        if r and r not in result:
            result.append(r)
    return sum(result)


if __name__ == '__main__':
    print(solution())

# print("--- %s seconds ---" % (time.time() - start_time))
