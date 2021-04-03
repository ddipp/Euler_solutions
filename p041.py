#!/usr/bin/env python3

# ===============================================================================
#
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
# ===============================================================================


def ispandi(pandi):
    a = ['1', '12', '123', '1234', '12345', '123456', '1234567', '12345678', '123456789']
    for i in a[len(pandi) - 1:]:
        if ''.join(sorted(pandi)) == i:
            return True
    return False


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
    pandi = []
    while True:
        i = next(p)
        if ispandi(str(i)):
            pandi.append(i)
            print(i)
        elif i > 10000000:
            break
#        print(i)
    return max(pandi)


if __name__ == '__main__':
    print(solution())
