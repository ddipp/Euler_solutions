#!/usr/bin/env python3

# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
# by only moving to the right and down, is indicated in bold red and is equal to 2427.

# Find the minimal path sum, in 081.txt, a 31K text file containing a 80 by 80 matrix,
# from the top left to the bottom right by only moving right and down.


def LoadFromFile():
    f = open('p081.txt', mode='r')
    return [list(map(int, l.split(','))) for l in f]


def FindMaxPath():
    res = LoadFromFile()
    # path will be either from top or left, choose which ever is minimum
    for i in range(len(res)):
        for j in range(len(res[0])):
            if i == 0 and j > 0:
                res[i][j] += res[i][j - 1]
            elif i > 0 and j == 0:
                res[i][j] += res[i - 1][j]
            elif i > 0 and j > 0:
                res[i][j] += min(res[i - 1][j], res[i][j - 1])

    print(res[len(res) - 1][len(res[0]) - 1])


if __name__ == '__main__':
    FindMaxPath()
