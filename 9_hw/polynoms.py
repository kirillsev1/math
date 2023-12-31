import matplotlib.pyplot as plt
import numpy as np


def polynomial(x: int | float, x_axis: list, coefficients: list) -> int | float:
    res = coefficients[0]
    multiplier = 1
    for i in range(1, len(x_axis)):
        multiplier *= (x - x_axis[i - 1])
        res += coefficients[i] * multiplier
    return res


def create_plot(x_axis, y_axis, x_graph, x_label, y_label, file_name):
    n = len(x_axis)
    coefficients = np.zeros(n)
    coefficients[0] = y_axis[0]
    y = y_axis.copy()

    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x_axis[j] - x_axis[j - i])
        coefficients[i] = y[i]

    x = x_graph
    y = [polynomial(x_value, x_axis, coefficients) for x_value in x]

    plt.figure(figsize=(8, 4))
    plt.scatter(x_axis, y_axis, color="red", label="Исходные точки")
    plt.plot(x, y, "b-", label="Интерполирующий полином")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    # plt.savefig(file_name)
    return y[-1]
