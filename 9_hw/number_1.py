import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolation(x, x_data, y_data):
    result = 0.0
    n = len(x_data)
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result


def interpolate_and_plot(x_data, y_data):
    x_interp = []
    y_interp = []

    for x in range(min(x_data), max(x_data) + 1):
        x_interp.append(x)
        y_interp.append(lagrange_interpolation(x, x_data, y_data))

    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, label="Узлы интерполяции", color='red')
    plt.plot(x_interp, y_interp, label="Интерполяционный полином", linestyle='dashed')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Интерполяция полиномом Лагранжа')
    plt.legend()
    plt.grid(True)
    plt.savefig("number_1.png")


x_data = [1800, 1850, 1900, 2000, 2050]
y_data = [280, 283, 291, 370, 465]
interpolate_and_plot(x_data, y_data)
