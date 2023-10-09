import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


def build_plot(x, y, dydx_start, dydx_end):
    cs = CubicSpline(x, y, bc_type=((1, dydx_start), (1, dydx_end)))

    x_new = np.linspace(0, 4, 100)
    y_new = cs(x_new)

    plt.figure(figsize=(8, 6))
    plt.plot(x_new, y_new, label="Cubic Spline")
    plt.scatter(x, y, c="red", label="Data Points")
    plt.xlabel("x")
    plt.ylabel("S(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("numpy_number_2")


if __name__ == "__main__":
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([1, 3, 3, 4, 2])
    build_plot(x, y, -2, 1)
