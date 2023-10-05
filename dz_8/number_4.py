from number_3 import gauss_seidel
from pprint import pprint


def generate_seidel_data(n, main_elem, side_elem, b):
    return [side_elem] * n, [main_elem] * n, [side_elem] * n, b, [0] * n


if __name__ == "__main__":
    max_iter = 10000
    n = 100
    b = [1] + [0] * (n - 2) + [-1]
    eps = 1e-3
    exact_solution = [1, -1] * (n // 2)
    solution = gauss_seidel(*generate_seidel_data(n, 2, 1, b), eps, max_iter, exact_solution)
    print(solution)
    print(f"iter: {solution[1]}\nrel_error: {solution[2]}\nrev_error: {solution[3]}")
