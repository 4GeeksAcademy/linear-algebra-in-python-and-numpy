import numpy as np


# vectors and matrices
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]


def dot_product(v1, v2, mode="pure"):
    "Computes the dot product of two vectors."

    if len(v1) != len(v2):
        return "vectors must have the same length"
    
    elif mode not in ['pure', 'numpy']:
        return "Invalid mode"
    
    else:
        if mode == 'pure':
            return sum(v1[i] * v2[i] for i in range(len(v1)))
        
        else:
            v1 = np.array(v1)
            v2 = np.array(v2)

            return np.dot(v1, v2)


def matrix_product(A, B, mode="pure"):
    "Computes the product of two matrices."

    if len(A[0]) != len(B):
        return "incompatible matrix dimensions"
    
    elif mode not in ['pure', 'numpy']:
        return "invalid mode"
    
    else:
        if mode == 'pure':
            return [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
        
        else:
            A = np.array(A)
            B = np.array(B)

            return np.dot(A, B)


dot_result_pure = dot_product(vector1, vector2, "pure")
dot_result_numpy = dot_product(vector1, vector2, "numpy")


matrix_result_pure = matrix_product(matrix1, matrix2, "pure")
matrix_result_numpy = matrix_product(matrix1, matrix2, "numpy")

print("Dot product in pure Python:", dot_result_pure)
print("Dot product in NumPy:", dot_result_numpy)
print("Matrix product in pure Python:", matrix_result_pure)
print("Matrix product in NumPy:", matrix_result_numpy)
