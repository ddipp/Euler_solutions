#!/usr/bin/env python3

# ===============================================================================
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
# by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
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


def solution():
    sum_primes = [i for i in Primes(999, 10000)]
    sum_primes_plus_3330 = []
    for i in sum_primes:
        if i + 3330 in sum_primes and i + 3330 * 2 in sum_primes:
            sum_primes_plus_3330.append([i, i + 3330, i + 3330 * 2])

    for i in sum_primes_plus_3330:
        symbol_array = [''.join(sorted(str(y))) for y in i]
        if symbol_array[0] == symbol_array[1] and symbol_array[0] == symbol_array[2]:
            ok = '<---------- ' + str(i[0]) + str(i[1]) + str(i[2])
            print(symbol_array, i, ok)
        else:
            ok = ''


if __name__ == '__main__':
    solution()
