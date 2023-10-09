import numpy as np
import matplotlib.pyplot as plt


def build_plot(x, y):
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]

    alpha = [0] * (n - 1)
    beta = [0] * (n - 1)
    l = [1] * n
    mu = [0] * n
    z = [0] * n

    for i in range(1, n - 1):
        alpha[i] = h[i - 1] / (h[i - 1] + h[i])
        beta[i] = 1 - alpha[i]

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    c = [0] * n

    for i in range(n - 2, -1, -1):
        c[i] = z[i] - mu[i] * c[i + 1]

    b = [0] * (n - 1)
    d = [0] * (n - 1)

    for i in range(n - 1):
        b[i] = ((y[i + 1] - y[i]) / h[i]) - (h[i] * (c[i + 1] + 2 * c[i]) / 3)
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    def S(x_value):
        for i in range(n - 1):
            if x[i] <= x_value <= x[i + 1]:
                xi = x[i]
                yi = y[i] + b[i] * (x_value - xi) + c[i] * (x_value - xi) ** 2 + d[i] * (x_value - xi) ** 3
                return yi

    x_values = np.linspace(0, 4, 1000)
    y_values = [S(xi) for xi in x_values]

    plt.plot(x_values, np.cos(x_values), label="cos(x)")
    plt.plot(x_values, y_values, label="Зажатый кубический сплайн")
    plt.scatter(x, y, color="red", label="Исходные точки")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Зажатый кубический сплайн, интерполирующий cos(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("number_3")


if __name__ == "__main__":
    x = np.linspace(0, np.pi / 2, 5)
    y = np.cos(x)
    build_plot(x, y)
