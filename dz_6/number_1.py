def gauss_elimination(matrix, equ, matrix_len):
    matrix = [row + [equ[i]] for i, row in enumerate(matrix)]
    for i in range(matrix_len):
        max_row = i
        for k in range(i + 1, matrix_len):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        for j in range(i + 1, matrix_len):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, matrix_len + 1):
                matrix[j][k] -= factor * matrix[i][k]

    return matrix


def gauss(matrix, equ, matrix_len):
    matrix = gauss_elimination(matrix, equ, matrix_len)
    matrix_len = len(matrix)
    x = [0] * matrix_len

    for i in range(matrix_len - 1, -1, -1):
        x[i] = matrix[i][-1]
        for j in range(i + 1, matrix_len):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    return x


if __name__ == "__main__":
    matrix = [
        [2, -2, -1],
        [4, 1, -2],
        [-2, 1, -1]
    ]
    matrix_len = len(matrix)
    equ = [-2, 1, -3]
    result = gauss(matrix, equ, matrix_len)

    print(f"Корни: {result}")
