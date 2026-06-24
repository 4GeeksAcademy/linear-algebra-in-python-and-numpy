import pytest
import numpy as np
from app import compute_eigen  # Make sure to import the function correctly

# --- Eigenvalue Computation Tests ---

@pytest.mark.it("Correctly computes eigenvalues in 'pure' mode (without eigenvectors)")
def test_compute_eigen_pure():
    A = [[3, 2], [1, 4]]
    expected = [5, 2]
    eigenvalues, eigenvectors = compute_eigen(A, "pure")
    
    assert pytest.approx(eigenvalues) == expected, f"Expected {expected}, but got {eigenvalues}"
    assert eigenvectors is None, "In 'pure' mode, eigenvectors should not be returned"

@pytest.mark.it("Correctly computes eigenvalues and eigenvectors in 'numpy' mode")
def test_compute_eigen_numpy():
    A = [[3, 2], [1, 4]]
    expected = np.array([5, 2])
    eigenvalues, eigenvectors = compute_eigen(A, "numpy")

    assert np.allclose(sorted(eigenvalues), sorted(expected)), f"Expected {expected}, but got {eigenvalues}"
    assert isinstance(eigenvectors, np.ndarray), "Eigenvectors should be a NumPy array"

# --- Error Handling ---

@pytest.mark.it("Returns an error message when the matrix is not square")
def test_compute_eigen_non_square():
    A = [[1, 2, 3], [4, 5, 6]]  # Not square
    result = compute_eigen(A, "pure")
    assert isinstance(result, str), "Expected a string error message from compute_eigen"
    assert "must be square" in result.lower(), f"Expected error message to mention 'must be square', but got: {result}"
