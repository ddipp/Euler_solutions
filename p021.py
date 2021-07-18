#!/usr/bin/env python3

# ===============================================================================
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
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


def ListToDict(lis):
    d = {}.fromkeys(lis, 0)
    for i in lis:
        d[i] += 1
    return d


def divisors(n):
    df = ListToDict(PrimeFactors(n))
    div = [1]
    for p, r in df.items():
        div = [d * p**e for d in div for e in range(r + 1)]
    div.sort()
    return div[:-1]


def solution():
    s = 0
    for a in range(1, 10000):
        b = sum(divisors(a))
        if a != b and a == sum(divisors(b)):
            s += a
    return s


if __name__ == '__main__':
    print(solution())
