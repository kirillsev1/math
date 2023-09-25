from math import cos, sin, log


def newton(func, dif_func, x0, e):
    count = 0
    x = x0
    f_x = func(x)
    df_x = dif_func(x)
    while f_x / df_x > e:
        count += 1
        x = x - f_x / df_x
        f_x = func(x)
        df_x = dif_func(x)
    return x


def first(x):
    return x ** 5 + x - 1


def first_dif(x):
    return 5 * x ** 4 + 1


def second(x):
    return 6 * x + 5 - sin(x)


def second_dif(x):
    return 6 + cos(x)


def third(x):
    return log(x) + x ** 2 - 3


def third_dif(x):
    return 1 / x + 2 * x


if __name__ == "_main__":
    print("-- 1 --")
    print("a) f(x) = x^5 + x - 1")
    print(f"x = {newton(first, first_dif, 1, 10 ** (-8))}", end="\n\n")

    print("b) f(x) = 6x + 5 - sin(x)")
    print(f"x = {newton(second, second_dif, 0, 10 ** (-8))}", end="\n\n")

    print("b) f(x) = ln(x) + x^2 - 3")
    print(f"x = {newton(third, third_dif, 2, 10 ** (-8))}", end="\n\n")
