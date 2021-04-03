#!/usr/bin/env python3

# ===============================================================================
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
# the 6th prime is 13.
#
# What is the 10 001st prime number?
# ===============================================================================


def Primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def solution():
    p = Primes()
    for i in range(10000):
        next(p)
    return next(p)


if __name__ == '__main__':
    print(solution())
