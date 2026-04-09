import pytest
import numpy as np
from app import solve_system

# --- Solve System Tests ---

@pytest.mark.it("Correctly solves a linear system in 'pure' mode")
def test_solve_system_pure():
    A = [[1, 1], [3, -1]]                                                                                                                                                       
    b = [1, 7]                                                                                                                                                                  
    expected = [2, -1]
    result = solve_system(A, b, "pure")
    assert result == expected, f"Expected {expected}, but got {result}"

@pytest.mark.it("Correctly solves a linear system in 'numpy' mode")
def test_solve_system_numpy():
    A = [[1, 1], [3, -1]]
    b = [1, 7]
    expected = np.array([2, -1])
    result = solve_system(A, b, "numpy")
    assert np.allclose(result, expected), f"Expected {expected}, but got {result}"

# --- Error Handling ---

@pytest.mark.it("Returns an error message when the coefficient matrix is not invertible")
def test_solve_system_singular_matrix():
    A = [[1, 2], [2, 4]]  # Determinant = 0
    b = [3, 6]
    result = solve_system(A, b, "pure")
    assert isinstance(result, str), "Expected a string error message from solve_system"
    assert "not invertible" in result.lower(), f"Expected error message to mention 'not invertible', but got: {result}"
