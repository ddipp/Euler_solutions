#!/usr/bin/env python3

# ===============================================================================
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# ===============================================================================

import math


def SumFact(n):
    return sum(math.factorial(int(x)) for x in str(n))


def solution():
    s = 0
    for i in range(3, 100000):
        if i == SumFact(i):
            s += i
    return s


if __name__ == '__main__':
    print(solution())
