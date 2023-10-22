import math

from simpson_method import simpson_integration


def func_a(x):
    return x ** 3


def func_b(x):
    return math.sin(x)


if __name__ == "__main__":
    print(f"a) {simpson_integration(func_a, 0, 1, 32)}")

    print(f"b) {simpson_integration(func_b, 0, math.pi, 32)}")
