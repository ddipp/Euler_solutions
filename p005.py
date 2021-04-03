#!/usr/bin/env python3

# ===============================================================================
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
# ===============================================================================


def divide_by_each(n, l):
    for x in l:
        if n % x != 0:
            return False
    return True


def solution():
    n = 40
    lis = range(1, 21)
    while True:
        if divide_by_each(n, lis):
            return n
        n += 20


if __name__ == '__main__':
    print(solution())
