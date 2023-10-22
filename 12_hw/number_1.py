import math

from simpson_method import simpson_integration


def func_a(x):
    return x / math.sqrt(x ** 2 + 9)


def func_b(x):
    return x ** 2 * math.log(x, math.e)


if __name__ == "__main__":
    res_16 = simpson_integration(func_a, 0, 4, 16)
    res_32 = simpson_integration(func_a, 0, 4, 32)
    print("a^a")
    print(f"a) n = 16: {res_16}| n = 32: {res_32}\nexact = 2\n")

    res_16 = simpson_integration(func_b, 1, 3, 16)
    res_32 = simpson_integration(func_b, 1, 3, 32)
    print(f"b) n = 16: {res_16}| n = 32: {res_32}\nexact = 6,99862")
