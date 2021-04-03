#!/usr/bin/env python3

# ===============================================================================
# The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#
#     F1 = 1
#     F2 = 1
#     F3 = 2
#     F4 = 3
#     F5 = 5
#     F6 = 8
#     F7 = 13
#     F8 = 21
#     F9 = 34
#     F10 = 55
#     F11 = 89
#     F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?
# ===============================================================================


def Fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


def solution():
    f = Fib()
    n = 0
    for i in f:
        if len(str(i)) == 1000:
            return n
        n = n + 1


if __name__ == '__main__':
    print(solution())
