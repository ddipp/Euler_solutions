#!/usr/bin/env python3

# ===============================================================================
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
# ... in p13.txt ...
# ===============================================================================


def SumDigitFromFile():
    f = open('p013.txt', mode='r')
    summ = sum(int(l) for l in f)
    return str(summ)[0:10]


if __name__ == '__main__':
    print(SumDigitFromFile())
