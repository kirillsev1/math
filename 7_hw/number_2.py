from pprint import pprint
from number_1 import tridiag_solve


def generate_diagonals(n):
    return n, [-1] * n, [2] * n, [-1] * n, [1] * n


if __name__ == "__main__":
    first = 5
    pprint(f"n = {first}:\n{tridiag_solve(*generate_diagonals(first))}\n")
    second = 10
    pprint(f"n = {second}:\n{tridiag_solve(*generate_diagonals(second))}\n")
    third = 50
    pprint(f"n = {third}:\n{tridiag_solve(*generate_diagonals(third))}\n")
