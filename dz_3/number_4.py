import math
from bisect_method import bisect


def first(x):
    return math.pi * x ** 2 * (1 - x / 3) - 1


if __name__ == '__main__':
    ten = 10 ** (-3)
    print(bisect(first, [0, 2], ten))
    print(bisect(first, [2, 5], ten))
