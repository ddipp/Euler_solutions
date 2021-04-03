#!/usr/bin/env python3

# ==============================================================================
# In the 20×20 grid below, four numbers along a diagonal line have been marked
# in red.
#
# ... in p011.txt ...
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the
# same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# ==============================================================================

table = []


def LoadFromFile():
    f = open('p011.txt', mode='r')
    return [list(map(int, l.split(' '))) for l in f]


def comp_sequence(x, y, dx, dy, n):
    res = 1
    global table
    for i in range(n):
        res *= table[y + i * dy][x + i * dx]
    return res


def solution():
    global table
    max_prod = 0
    seq_len = 4
    table = LoadFromFile()
    h = len(table)
    v = len(table[0])
    for y in range(v):
        for x in range(h):
            if x + seq_len <= h:
                max_prod = max(max_prod, comp_sequence(x, y, 1, 0, seq_len))
            if y + seq_len <= v:
                max_prod = max(max_prod, comp_sequence(x, y, 0, 1, seq_len))
            if y + seq_len <= v and x + seq_len <= h:
                max_prod = max(max_prod, comp_sequence(x, y, 1, 1, seq_len))
            if y + seq_len <= v and x - seq_len >= -1:
                max_prod = max(max_prod, comp_sequence(x, y, -1, 1, seq_len))
    return max_prod


if __name__ == '__main__':
    print(solution())
