import matplotlib.pyplot as plt


def build_plot(x_points, y_points, s_0, s_4):
    delta_x = [x_points[i + 1] - x_points[i] for i in range(len(x_points) - 1)]
    delta_y = [y_points[i + 1] - y_points[i] for i in range(len(y_points) - 1)]

    second_derivatives = [0] * len(x_points)
    second_derivatives[0] = 6 / delta_x[0] * (delta_y[0] / delta_x[0] - s_0)

    for i in range(1, len(x_points) - 1):
        second_derivatives[i] = (6 / (delta_x[i - 1] + delta_x[i]) *
                                 (delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1]))

    second_derivatives[-1] = 6 / delta_x[-1] * (s_4 - delta_y[-1] / delta_x[-1])

    a = y_points[:-1]
    b = [0] * len(x_points)
    d = [0] * len(x_points)

    for i in range(len(x_points) - 1):
        b[i] = delta_y[i] / delta_x[i] - delta_x[i] * (2 * second_derivatives[i] + second_derivatives[i + 1]) / 6
        d[i] = (second_derivatives[i + 1] - second_derivatives[i]) / (6 * delta_x[i])

    x_spline = [x / 100 for x in range(400)]
    y_spline = [0] * len(x_spline)

    for i in range(len(x_points) - 1):
        for j in range(len(x_spline)):
            if x_points[i] <= x_spline[j] <= x_points[i + 1]:
                x_interval = x_spline[j] - x_points[i]
                y_spline[j] = (a[i] + b[i] * x_interval +
                               second_derivatives[i] / 2 * x_interval ** 2 + d[i] * x_interval ** 3)

    plt.plot(x_points, y_points, "o", label="Исходные точки")
    plt.plot(x_spline, y_spline, label="Кубический сплайн")
    plt.xlabel("x")
    plt.ylabel("S(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig("number_2")


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [1, 3, 3, 4, 2]
    build_plot(x, y, -2, 1)
