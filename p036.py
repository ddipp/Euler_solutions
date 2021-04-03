#!/usr/bin/env python3

# ===============================================================================
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)
# ===============================================================================


def ispalindrom(n):
    return n == n[::-1]


def solution():
    s = 0
    for i in range(1, int(1e6)):
        if ispalindrom(str(i)) and ispalindrom(bin(i)[2:]):
            s += i
    return s


if __name__ == '__main__':
    print(solution())
