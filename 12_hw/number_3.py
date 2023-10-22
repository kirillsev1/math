from math import exp
import matplotlib.pyplot as plt


def central_difference(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


def approximate_function(func):
    exact_derivative = func(0)

    h_values = [10 ** -i for i in range(1, 17)]

    approximation_errors = []

    for h in h_values:
        approx_derivative = central_difference(func, 0, h)
        approximation_errors.append(abs(approx_derivative - exact_derivative))

    plt.loglog(h_values, approximation_errors, marker='o')
    plt.xlabel('Значение h (логарифмическая шкала)')
    plt.ylabel('Ошибка аппроксимации')
    plt.title('Зависимость ошибки аппроксимации от шага h')
    plt.grid(True)
    plt.savefig('number_3')


def number_3(x):
    return exp(x)


if __name__ == "__main__":
    approximate_function(number_3)
    print("Можно заметить, что при уменьшении h ошибка уменьшается,\nчто соответствует ожидаемому результату,"
          "\nтак как при более мелком разделении шага аппроксимация становится точнее.")
