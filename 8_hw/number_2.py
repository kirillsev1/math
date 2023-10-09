from number_1 import jacoby


def generate_jacoby_data(n, main_elem, side_elem, b):
    return [side_elem] * n, [main_elem] * n, [side_elem] * n, b, [0] * n


if __name__ == "__main__":
    n = 100
    b = [2] + [1] * (n - 2) + [2]
    eps = 1e-6
    max_iter = 100000
    exact_solution = [1] * n
    solution = jacoby(*generate_jacoby_data(n, 3, -1, b), eps, max_iter, exact_solution)
    print(solution)
    print(f"iter: {solution[1]}\nrel_error: {solution[2]}\nrev_error: {solution[3]}")

    n = 100000
    b = [2] + [1] * (n - 2) + [2]
    exact_solution = [1] * n
    solution = jacoby(*generate_jacoby_data(n, 3, -1, b), eps, max_iter, exact_solution)
    print(solution)
    print(f"iter: {solution[1]}\nrel_error: {solution[2]}\nrev_error: {solution[3]}")
