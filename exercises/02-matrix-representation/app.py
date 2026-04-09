import numpy as np  # Import NumPy to use it later
import random  # To generate random values in pure Python

def create_matrix(n, m, mode="pure"):
    lst = []
    if mode == "numpy":
        return np.random.randint(0, 100, size=(n, m))
    return [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

# Test the function with the following values:
matrix1 = create_matrix(3, 3, "pure")
matrix2 = create_matrix(3, 3, "numpy")

print("Matrix in pure Python:", matrix1)
print("Matrix in NumPy:\n", matrix2)
