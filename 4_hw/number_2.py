from fixed_iter import fixed_iter


def first(x):
    return (2 * x + 2 / x ** 2) / 3


def second(x):
    return (2 * x + 3 / x ** 2) / 3


def third(x):
    return (2 * x + 5 / x ** 2) / 3


if __name__ == '__main__':
    tolerance = 100
    initial = 1.0

    val = fixed_iter(first, initial, tolerance)
    print(f"Кубический корень при A = 2: {val:.53f}")

    val = fixed_iter(second, initial, tolerance)
    print(f"Кубический корень при A = 3: {val:.53f}")

    val = fixed_iter(third, initial, tolerance)
    print(f"Кубический корень при A = 5: {val:.53f}")
