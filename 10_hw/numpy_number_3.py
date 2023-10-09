import numpy as np
import matplotlib.pyplot as plt


def build_plot(x, y):
    spl = np.polyfit(x, y, 3)

    S = np.poly1d(spl)

    x_values = np.linspace(0, 4)
    y_values = S(x_values)

    plt.plot(x_values, y_values, label="Зажатый кубический сплайн")
    plt.plot(x_values, np.cos(x_values), label="cos(x)")
    plt.scatter(x, y, color="red", label="Исходные точки")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Зажатый кубический сплайн, интерполирующий cos(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("numpy_number_3")


if __name__ == "__main__":
    x = np.linspace(0, np.pi / 2, 5)
    y = np.cos(x)
    build_plot(x, y)
