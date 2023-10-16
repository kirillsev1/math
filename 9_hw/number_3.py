import numpy as np
from polynoms import polynomial
import matplotlib.pyplot as plt


def create_graph(x_axis, y_axis, x_graph, x_label, y_label, file_name):
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
    y_values = np.sin(x)
    plt.plot(x, y_values, label="sin(x)")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.savefig(file_name)


if __name__ == "__main__":
    x = np.linspace(0, np.pi / 2, 4)
    y = np.sin(x)
    x_graph = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    x_label, y_label = "x", "y"
    create_graph(x, y, x_graph, x_label, y_label, "number_3")
