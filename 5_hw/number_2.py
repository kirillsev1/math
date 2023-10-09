from number_1 import newton
from math import pi


def radius(x):
    return 2 / 3 * pi * x ** 3 + 1 / 3 * pi * x ** 2 * 10 - 60


def dif_radius(x):
    return 2 * pi * x ** 2 + 20 / 3 * pi * x


if __name__ == "__main__":
    """
    V = 1/3 * S(основания) * h
    V = 2/3 * pi * R^3"
    V = 2/3 * pi * R^3 + 1/3 * S(основания) * h"
    
    S = pi * R^2"
    f(R) = 2/3 * pi * R^3 + 1/3 * pi * R^2 * h - V
    """
    print(newton(radius, dif_radius, 3, 10 ** (-6)))
