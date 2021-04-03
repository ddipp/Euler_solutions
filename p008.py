#!/usr/bin/env python3

# ===============================================================================
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 × 9 × 8 × 9 = 5832.
#
# ... in file p08.txt ...
#
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?
# ===============================================================================


def solution():
    f = open('p008.txt', mode='r')
    diginumber = ''.join((i.strip() for i in f))
    max_product = 0
    for x in range(len(diginumber[:-12])):
        multipl = 1
        for i in range(13):
            multipl = multipl * int(diginumber[x + i])
        max_product = max(multipl, max_product)
    return max_product


if __name__ == '__main__':
    print(solution())
