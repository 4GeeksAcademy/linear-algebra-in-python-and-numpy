import numpy as np


matrix = [[1, 2], [3, 4]]


def determinant(matrix, mode="pure"):
    "Finds a matrix determinant"

    if mode == 'pure':
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    else:
        matrix = np.array(matrix)

        return np.linalg.det(matrix)


def inverse_matrix(matrix, mode="pure"):
    "Inverse valid matrix."

    det = determinant(matrix)

    if det == 0:
        return "not invertible"

    else:
        if mode == 'pure':
            return [[matrix[1][1] / det, -matrix[0][1] / det], [-matrix[1][0] / det, matrix[0][0] / det]]
        
        else:
            matrix = np.array(matrix)

            return np.linalg.inv(matrix)

print(determinant(matrix, "pure"))
print(determinant(matrix, "numpy"))
print(inverse_matrix(matrix, "pure"))
print(inverse_matrix(matrix, "numpy"))