#!/usr/bin/env python3

# ===============================================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
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


if __name__ == '__main__':
    print(max(PrimeFactors(600851475143)))
