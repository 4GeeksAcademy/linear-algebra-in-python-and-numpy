import numpy as np


# vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

def sum_vectors(v1, v2, mode="pure"):
    """
    Computes the element-wise sum of two vectors.

    Parameters:
    - v1: list or np.array -> First vector.
    - v2: list or np.array -> Second vector.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - A vector with the element-wise sum.
    """
 
    pass  # Remove this line when implemented

def subtract_vectors(v1, v2, mode="pure"):
    """
    Computes the element-wise subtraction of two vectors.

    Parameters:
    - v1: list or np.array -> First vector.
    - v2: list or np.array -> Second vector.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - A vector with the element-wise subtraction.
    """

    pass  # Remove this line when implemented


sum_result_pure = sum_vectors(vector1, vector2, "pure")
sum_result_numpy = sum_vectors(vector1, vector2, "numpy")

sub_result_pure = subtract_vectors(vector1, vector2, "pure")
sub_result_numpy = subtract_vectors(vector1, vector2, "numpy")

print("Sum in pure Python:", sum_result_pure)
print("Sum in NumPy:", sum_result_numpy)
print("Subtraction in pure Python:", sub_result_pure)
print("Subtraction in NumPy:", sub_result_numpy)