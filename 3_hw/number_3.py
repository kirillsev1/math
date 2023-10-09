from bisect_method import bisect


def first(x):
    return x ** 3 - 2


def second(x):
    return x ** 3 - 3


def third(x):
    return x ** 3 - 5


if __name__ == '__main__':
    print('1) f(x) = x**3 - 2')
    print(f"x = {bisect(first, [1, 2], 10 ** (-8))}\n")

    print('2) f(x) = x**3 - 3')
    print(f"x = {bisect(second, [1, 2], 10 ** (-8))}\n")

    print('3) f(x) = x**3 - 5')
    print(f"x = {bisect(third, [1, 2], 10 ** (-8))}")
