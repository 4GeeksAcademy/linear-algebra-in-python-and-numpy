import numpy as np  

def transpose(matrix, mode="pure"):
    """
    Computes the transpose of a matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to transpose.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The transposed matrix.
    """
    if mode == "pure":
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]  # Transpose for pure Python lists
    elif mode =="numpy":
        return np.transpose(matrix)  # Transpose for NumPy arrays
    else:
        raise ValueError("Invalid mode. Use 'pure' or 'numpy'.")
    

# Example usage:
if __name__ == "__main__":
    # Using pure Python lists
    matrix_list = [[1, 2, 3], [4, 5, 6]]
    transposed_list = transpose(matrix_list, mode="pure")
    print("Transposed (Pure Python):")
    print(transposed_list)

    # Using NumPy arrays
    matrix_array = np.array([[1, 2, 3], [4, 5, 6]])
    transposed_array = transpose(matrix_array, mode="numpy")
    print("Transposed (NumPy):")
    print(transposed_array)

