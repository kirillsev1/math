import math
from fixed_iter import fixed_iter


def first(x):
    return (2 * x + 2) ** (1 / 3)


def second(x):
    return math.log(7 - x)


def third(x):
    return math.log(4 - math.sin(x))


if __name__ == '__main__':
    print("1) x**3 = 2x + 2")

    initial = 1.768
    tolerance = 100
    print(f"F(z) = {first(fixed_iter(first, initial, tolerance)):.20f}")

    print("2) e**x + x = 7")
    initial = 1.66
    print(f"F(z) = {second(fixed_iter(second, initial, 10)):.20f}")

    print("3) e**x + sin(x) = 4")
    initial = 1.05
    print(f"F(z) = {third(fixed_iter(third, initial, tolerance)):.20f}")
