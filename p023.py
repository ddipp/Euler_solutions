#!/usr/bin/env python3

# ===============================================================================
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers. However, this upper
# limit cannot be reduced any further by analysis even though it is known that
# the greatest number that cannot be expressed as the sum of two abundant
# numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# ===============================================================================

# import time
# start_time = time.time()

an = []


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


def AbundantNumbers(n):
    i = 12
    while i <= n:
        if i < sum(divisors(i)):
            yield i
        i += 1


def SumOfTwoAbundantNumbers(n):
    # FIXME: very slowly algorithm
    for i in an:
        if (n - i) in an:
            return True
    return False


def solution():
    global an
    snan = 0
    a = AbundantNumbers(28123)
    an = [x for x in a]
    for i in range(28123):
        if SumOfTwoAbundantNumbers(i):
            pass
        else:
            snan += i
#            print("Sum = {0}, i = {1}".format(snan, i))
    return snan


if __name__ == '__main__':
    print(solution())

# print("--- %s seconds ---" % (time.time() - start_time))
