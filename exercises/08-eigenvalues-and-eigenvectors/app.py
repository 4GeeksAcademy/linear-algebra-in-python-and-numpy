import numpy as np  

def compute_eigen(A, mode="numpy"):
    """
    Computes the eigenvalues and eigenvectors of a square matrix.

    Parameters:
    - A: list of lists or np.array -> Square matrix.
    - mode: str -> "pure" for manual calculation, "numpy" for np.linalg.eig().

    Returns:
    - List of eigenvalues (and eigenvectors if mode="numpy").
    """
    if mode == "pure":
        # For a 2x2 matrix [[a, b], [c, d]], the characteristic polynomial is:
        # λ^2 - (a + d)λ + (ad - bc) = 0
        a, b = A[0]
        c, d = A[1]

        trace = a + d
        determinant = a * d - b * c

        # Coefficients of the characteristic polynomial
        coeffs = [1, -trace, determinant]

        # Calculate eigenvalues using the quadratic formula
        discriminant = trace**2 - 4 * determinant
        if discriminant < 0:
            raise ValueError("The matrix has complex eigenvalues.")
        
        sqrt_disc = np.sqrt(discriminant)
        eigenvalue1 = (trace + sqrt_disc) / 2
        eigenvalue2 = (trace - sqrt_disc) / 2
        

        return [eigenvalue1, eigenvalue2]

    elif mode == "numpy":
        eigenvalues, eigenvectors = np.linalg.eig(A)
        return list(zip(eigenvalues, eigenvectors.T))
    else:
        raise ValueError("Invalid mode. Use 'pure' or 'numpy'.")
   
    return 
if __name__ == "__main__":
    A = [[4, -2], [1, 1]]

    eigen_numpy = compute_eigen(A, mode="numpy")
    print("Eigenvalues and Eigenvectors using NumPy:", eigen_numpy)

    eigen_pure = compute_eigen(A, mode="pure")
    print("Eigenvalues using pure Python:", eigen_pure)