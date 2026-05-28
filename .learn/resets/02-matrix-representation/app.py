import numpy as np  # Import NumPy to use it later
import random  # To generate random values in pure Python

def create_matrix(n, m, mode="pure"):
    """
    Generates an n x m matrix with random values.

    Parameters:
    - n: int -> Number of rows.
    - m: int -> Number of columns.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - A matrix in the specified format.
    """
    
    if(mode=="pure"): 
        matrix = [[random.random() for j in range(m)] for i in range(n)]
    elif(mode=="numpy"):
        matrix = np.random.rand(n,m)
    else:
        raise ValueError("Mode must be 'pure' or 'numpy'")
    

    return matrix

# Test the function with the following values:
matrix1 = create_matrix(3, 4, "pure")
matrix2 = create_matrix(2, 2, "numpy")

print("Matrix in pure Python:", matrix1)
print("Matrix in NumPy:\n", matrix2)
