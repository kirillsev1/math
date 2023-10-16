import math


def midpoint(f, a, b, n):
    h = (b - a) / n
    integral = 0

    for i in range(n):
        x_mid = a + (i + 0.5) * h
        integral += f(x_mid)

    integral *= h

    return integral


def number_a(x):
    return x / math.sin(x)


def number_b(x):
    return math.atan(x) / x


if __name__ == "__main__":
    result_16 = midpoint(number_a, 0, math.pi, 16)
    result_32 = midpoint(number_a, 0, math.pi, 32)
    print(result_16, result_32)

    result_16 = midpoint(number_b, 0, 1, 16)
    result_32 = midpoint(number_b, 0, 1, 32)
    print(result_16, result_32)
