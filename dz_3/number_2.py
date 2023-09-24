import math

from bisect_method import bisect
from pygnuplot import gnuplot


def first_graph():
    g = gnuplot.Gnuplot(terminal='pngcairo font "arial,10" fontscale 1.0 size 600, 400', output='"2-first.png"')
    g.plot("[-10:10] [-10:10] 2 * x ** 3 - 6 * x - 1")


def second_graph():
    g = gnuplot.Gnuplot(terminal='pngcairo font "arial,10" fontscale 1.0 size 600, 400', output='"2-second.png"')
    g.plot("[-10:10] [-10:10] exp(x - 2) + x ** 3 - x")


def third_graph():
    g = gnuplot.Gnuplot(terminal='pngcairo font "arial,10" fontscale 1.0 size 600, 400', output='"2-third.png"')
    g.plot("[-10:10] [-10:10] 1 + 5 * x - 6 * x ** 3 - exp(2 * x)")


def first_equation(x):
    return 2 * x ** 3 - 6 * x - 1


def second_equation(x):
    return 2 * x ** 3 - 6 * x - 1


def third_equation(x):
    return 2 * x ** 3 - 6 * x - 1


if __name__ == '__main__':
    print("1) 2x**3 − 6x − 1=0")
    print(f"x = {bisect(first_equation, [-2, -1], 10 ** -6)}")
    print(f"x = {bisect(second_equation, [-0.5, 0.5], 10 ** -6)}")
    print(f"x = {bisect(third_equation, [1, 2], 10 ** -6)}\n")

    print("2) e**(x - 2) + x**3 - x = 0")
    print(f"x = {bisect(lambda x: math.e ** (x - 2) + x ** 3 - x, [-1, -10], 10 ** -6)}")
    print(f"x = {bisect(lambda x: math.e ** (x - 2) + x ** 3 - x, [-3, 0], 10 ** -6)}\n")

    print("3) 1 + 5x - 6x**3 - e**(2x) = 0")
    print(f"x = {bisect(lambda x: 1 + 5 * x - 6 * x ** 3 - math.e ** (2 * x), [0, -10], 10 ** -6)}")
    print(f"x = {bisect(lambda x: 1 + 5 * x - 6 * x ** 3 - math.e ** (2 * x), [0, -0.75], 10 ** -6)}")
    print(f"x = {bisect(lambda x: 1 + 5 * x - 6 * x ** 3 - math.e ** (2 * x), [1, -100], 10 ** -6)}")

    first_graph()
    second_graph()
    third_graph()
