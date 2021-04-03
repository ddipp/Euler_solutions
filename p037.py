#!/usr/bin/env python3

# ===============================================================================
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime at
# each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# ===============================================================================


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


def truncatable_check_right(myprime):
    for x in range(1, len(myprime)):
        if len(PrimeFactors(int(myprime[:len(myprime) - x]))) == 1:
            pass
        else:
            return False
    return True


def truncatable_check_left(myprime):
    for x in range(1, len(myprime)):
        if len(PrimeFactors(int(myprime[x:]))) == 1:
            pass
        else:
            return False
    return True


def two_sided_truncatable_check(prime):
    myprime = str(prime)
    if (truncatable_check_left(myprime) is True) and (truncatable_check_right(myprime) is True):
        return True
    else:
        return False


def solution():
    prime_iterator = Primes()
    while next(prime_iterator) != 7:
        pass
    n = 0
    primes_sum = 0

    while n < 11:
        prime = next(prime_iterator)
        if two_sided_truncatable_check(prime):
            primes_sum += prime
            n += 1

    return primes_sum


if __name__ == '__main__':
    print(solution())
