#!/usr/bin/env python3

# ===============================================================================
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
#
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
# ===============================================================================


def solution():
    sum_of_sq = 0
    sq_of_sum = 0
    lis = [x for x in range(1, 101)]
    for x in lis:
        sum_of_sq += x * x
        sq_of_sum += x
    sq_of_sum = sq_of_sum ** 2
    return sq_of_sum - sum_of_sq


if __name__ == '__main__':
    print(solution())
