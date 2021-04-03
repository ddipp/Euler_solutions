#!/usr/bin/env python3

# ===============================================================================
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
# ===============================================================================


def Primes(n):
    D = {}
    q = 2
    while q < n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def solution():
    sum_primes = sum(i for i in Primes(2e6))
    return sum_primes


if __name__ == '__main__':
    print(solution())
