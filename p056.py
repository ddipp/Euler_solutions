#!/usr/bin/env python3

# ===============================================================================
# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a**b, where a, b < 100,
# what is the maximum digital sum?
# ===============================================================================


def DigiSum(n):
    return sum(int(i) for i in str(n))


def solution():
    s = 0
    for a in range(100):
        for b in range(100):
            s = max(s, DigiSum(a**b))
    return s


if __name__ == '__main__':
    print(solution())
