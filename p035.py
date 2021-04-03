#!/usr/bin/env python3

# ===============================================================================
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?
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


def circ_num(n):
    n = [i for i in str(n)]
    num_circ_arr = []
    for i in range(len(n)):
        n = n + [n.pop(0)]
        num_circ_arr.append(int("".join(n)))
    return num_circ_arr


def check_circ_pr(n):
    for i in circ_num(n):
        if len(PrimeFactors(i)) > 1:
            return False
    return True


def solution():
    circ_pr = 0
    p = Primes(1e6)
    for i in p:
        if check_circ_pr(i):
            circ_pr += 1
    return circ_pr


if __name__ == '__main__':
    print(solution())
