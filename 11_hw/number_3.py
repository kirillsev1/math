from number_1 import number_a, number_b
import matplotlib.pyplot as plt
import math


def midpoint_integral(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        integral += f(x_mid)
    integral *= h
    return integral


def approximation_error(func, a, b, analytical_result, n, graph_name):
    n_values = [2 ** i for i in range(n)]
    errors = []

    for n in n_values:
        result = midpoint_integral(func, a, b, n)
        error = abs(result - analytical_result)
        errors.append(error)

    plt.loglog(n_values, errors, marker='o')
    plt.xlabel('Число частей (n)')
    plt.ylabel('Ошибка аппроксимации')
    plt.title('Зависимость ошибки от числа частей (log-log)')
    plt.grid(True)
    plt.savefig(graph_name)


if __name__ == "__main__":

    # compute_approximation_error(number_a, 0, 4, 2, 8, "number_3_a")

    approximation_error(number_b, 1, math.pi, 6.99862171, 8, "number_3_b")
