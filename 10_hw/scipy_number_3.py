import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def build_plot(x, y):
    cs = CubicSpline(x, y, bc_type='clamped')  # Используем bc_type='clamped' для краевых условий

    x_values = np.linspace(0, np.pi / 2, 100)
    y_values = cs(x_values)

    plt.plot(x_values, y_values, label="Зажатый кубический сплайн")
    plt.plot(x_values, np.cos(x_values), label="cos(x)")
    plt.scatter(x, y, color="red", label="Исходные точки")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Зажатый кубический сплайн, интерполирующий cos(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("scipy_number_3")

if __name__ == "__main__":
    x = np.linspace(0, np.pi / 2, 5)
    y = np.cos(x)
    build_plot(x, y)
