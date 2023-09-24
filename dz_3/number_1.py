import math
from bisect_method import bisect


def first(x):
    return x ** 3 - 9


def second(x):
    return 3 * x ** 3 + x ** 2 - x - 5


def third(x):
    return math.cos(x) ** 2 + 6 - x


if __name__ == "__main__":
    func_1 = bisect(first, [2, 3], eps=10 ** -6)
    print(f"1) x**3 = 9, x = {func_1}")

    func_2 = bisect(second, [1, 2], eps=10 ** -6)
    print(f"2) 3x**3 + x**2 = x + 5, x = {func_2}")

    func_3 = bisect(third, [6, 7], eps=10 ** -6)
    print(f"3) cos**(2x) + 6 = x, x = {func_3}")
