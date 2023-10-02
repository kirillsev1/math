from number_1 import jacoby
from pprint import pprint


def generate_seidel_data(n, eps, max_iter):
    return [3] * n, [-1] * n, [-1] * n, [2] + [1] * (n - 2) + [2], [0] * n, eps, max_iter


if __name__ == "__main__":
    result_1 = jacoby(*generate_seidel_data(n=10, eps=1e-6, max_iter=1000))
    pprint(result_1[0])
    print(f"iterations: {result_1[-1]}\nerror: {result_1[-2]}\n")

    result_3 = jacoby(*generate_seidel_data(n=100, eps=1e-6, max_iter=1000))
    pprint(result_3[0])
    print(f"iterations: {result_3[-1]}\nerror: {result_3[-2]}\n")

    result_2 = jacoby(*generate_seidel_data(n=1000000, eps=1e-6, max_iter=1000))
    pprint(result_2[0])
    print(f"iterations: {result_2[-1]}\nerror: {result_2[-2]}")
