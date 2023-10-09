from number_1 import gauss


def create_matrix(matrix_len):
    return [[1 / (i + j + 1) for i in range(1, matrix_len + 1)] for j in range(1, matrix_len + 1)]


if __name__ == "__main__":
    # a
    matrix = create_matrix(2)
    matrix_len = len(matrix)
    equ = [1] * matrix_len
    result = gauss(matrix, equ, matrix_len)
    print(f"Корни в примере a: {result}")

    # b
    matrix = create_matrix(5)
    matrix_len = len(matrix)
    equ = [1] * matrix_len
    result = gauss(matrix, equ, matrix_len)
    print(f"Корни в примере b: {result}")

    # c
    matrix = create_matrix(10)
    matrix_len = len(matrix)
    equ = [1] * matrix_len
    result = gauss(matrix, equ, matrix_len)
    print(f"Корни в примере c: {result}")
