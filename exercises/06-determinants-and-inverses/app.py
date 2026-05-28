import numpy as np

def determinant(matrix, mode="pure"):
    """
    Computes the determinant of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute determinant.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The determinant value.
    """
    if mode == "pure":
        # Implement determinant calculation for pure Python lists
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for c in range(n):
                det += ((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c+1:] for row in matrix[1:]], mode="pure")
            return det
    elif mode == "numpy":
        return np.linalg.det(matrix)  # Determinant for NumPy arrays   
    else:
        raise ValueError("Invalid mode. Use 'pure' or 'numpy'.") 

def inverse_matrix(matrix, mode="pure"):
    """
    Computes the inverse of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute inverse.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The inverse matrix or a message if it doesn't exist.
    """
    if mode == "pure":
        # Implement inverse calculation for pure Python lists
        det = determinant(matrix, mode="pure")
        if det == 0:
            return "Inverse does not exist (determinant is zero)."
        n = len(matrix)
        if n == 1:
            return [[1 / matrix[0][0]]]
        elif n == 2:
            return [[matrix[1][1] / det, -matrix[0][1] / det],
                    [-matrix[1][0] / det, matrix[0][0] / det]]
        else:
            # For larger matrices, we can use the adjugate method
            adjugate = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    minor = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
                    adjugate[j][i] = ((-1) ** (i + j)) * determinant(minor, mode="pure")
            return [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
    elif mode == "numpy":
        try:
            return np.linalg.inv(matrix)  # Inverse for NumPy arrays
        except np.linalg.LinAlgError:
            return "Inverse does not exist (matrix is singular)." 
    else:
        raise ValueError("Invalid mode. Use 'pure' or 'numpy'.")

   
if __name__ == "__main__":
    # Example usage:
    matrix_list = [[4, 7], [2, 6]]
    print("Determinant (Pure Python):", determinant(matrix_list, mode="pure"))
    print("Inverse (Pure Python):", inverse_matrix(matrix_list, mode="pure"))

    matrix_array = np.array([[4, 7], [2, 6]])
    print("Determinant (NumPy):", determinant(matrix_array, mode="numpy"))
    print("Inverse (NumPy):", inverse_matrix(matrix_array, mode="numpy"))

