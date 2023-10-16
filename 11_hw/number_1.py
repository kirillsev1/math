import math


def trapezoidal(func_to_integrate, a_limit, b_limit, n):
    h = (b_limit - a_limit) / n
    x_values = [a_limit + i * h for i in range(n + 1)]
    integral = 0.5 * (func_to_integrate(a_limit) + func_to_integrate(b_limit))

    for i in range(1, n):
        integral += func_to_integrate(x_values[i])

    return integral * h


def number_a(x):
    return x / math.sqrt(x ** 2 + 9)


def number_b(x):
    return x ** 2 * math.log(x, math.e)


if __name__ == "__main__":
    result_16 = trapezoidal(number_a, 0, 4, 16)
    result_32 = trapezoidal(number_a, 0, 4, 32)
    print(result_16, result_32)

    result_16 = trapezoidal(number_b, 1, 3, 16)
    result_32 = trapezoidal(number_b, 1, 3, 32)
    print(result_16, result_32)
