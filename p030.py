#!/usr/bin/env python3

# ===============================================================================
# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
#     1634 = 1**4 + 6**4 + 3**4 + 4**4
#     8208 = 8**4 + 2**4 + 0**4 + 8**4
#     9474 = 9**4 + 4**4 + 7**4 + 4**4
#
# As 1 = 1**4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers
# of their digits.
# ===============================================================================


def solution():
    s = 0
    for x1 in range(10):
        for x2 in range(10):
            for x3 in range(10):
                for x4 in range(10):
                    for x5 in range(10):
                        for x6 in range(10):
                            n1 = x6 + x5 * 10 + x4 * 100 + x3 * 1000 + x2 * 10000 + x1 * 100000
                            n2 = x6**5 + x5**5 + x4**5 + x3**5 + x2**5 + x1**5
                            if n1 == n2 and n1 > 1:
                                s += n1
    return s


if __name__ == '__main__':
    print(solution())
