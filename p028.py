#!/usr/bin/env python3

# ===============================================================================
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
#                  [21]  22  23  24  [25]
#                  20  [7]  8   [9]  10
#                  19   6  [1]   2   11
#                  18  [5]  4   [3]  12
#                  [17]  16  15  14  [13]
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
# ===============================================================================


def GRing(n):
    s = 1
    yield [1]
    while s < n:
        s += 2
        yield [s**2, s**2 - 1 * (s - 1), s**2 - 2 * (s - 1), s**2 - 3 * (s - 1)]


def solution():
    summ = 0
    ring = GRing(1001)
    for i in ring:
        summ += sum(i)
    return summ


if __name__ == '__main__':
    print(solution())
