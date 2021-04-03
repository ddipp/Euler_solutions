#!/usr/bin/env python3

# ===============================================================================
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# ===============================================================================


def Primes(f, t):
    D = {}
    q = 2
    while q < t:
        if q not in D:
            if q > f:
                yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def PrimeFactors(n):
    divisor = 2
    lis = []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            lis.append(divisor)
        else:
            divisor += 1
    if n != 1:
        lis.append(n)
    return lis


def solution():
    primes = [i for i in Primes(1, 5000)]
    sum_len = []
    max_le = 0
    for x in range(len(primes)):
        le = 0
        su = 0
        for i in primes[x:]:
            le += 1
            su += i
            if su > 1e6:
                break
            if len(PrimeFactors(su)) == 1:
                if max_le < le:
                    sum_len = [su, le]
                    max_le = le
                    print(sum_len)
        print(x)
    print(sum_len)


if __name__ == '__main__':
    solution()
