#!/usr/bin/env python3

# ===============================================================================
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# ===============================================================================


def ispalindrom(n):
    return str(n) == str(n)[::-1]


def solution():
    max_pal = 0
    for x in range(999, 800, -1):
        for y in range(999, 800, -1):
            if ispalindrom(x * y):
                max_pal = max(x * y, max_pal)
    return max_pal


if __name__ == '__main__':
    print(solution())
