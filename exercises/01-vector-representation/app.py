import numpy as np  # Import NumPy to use it later

def create_vector(lst, mode="pure"):
    "Converts a list into a vector in pure Python or in NumPy."
    if mode == "numpy":
        return np.array(lst)
    return list(lst)


# Test the function with the following values:
vector1 = create_vector([1, 2, 3], "pure")
vector2 = create_vector([1, 2, 3], "numpy")

print("Vector in pure Python:", vector1)
print("Vector in NumPy:", vector2)