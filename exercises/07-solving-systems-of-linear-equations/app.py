import numpy as np


def solve_system(A, b, mode="numpy"):
    """
    Solves the linear system Ax = b.

    Parameters:
    - A: list of lists or np.array -> Coefficient matrix.
    - b: list or np.array -> Result vector.
    - mode: str -> "pure" for manual computation, "numpy" for np.linalg.solve().

    Returns:
    - The solution vector x.
    """
    if mode == "pure":
        # Ax =b
        # here A is 2x2 matrix where a[0] i-hat and a[1]= j-hat
        # b is the result i-hat and j-hat
        # x is the solution vector which we need to find
        # now assign the values

        a, b1 = A[0]
        c, d = A[1]
        e, f = b

        det = a*d - b1*c
        if det == 0:
            raise ValueError("The system does not have a unique solution.")
        elif det != 0:
            # Determinant tells:
            # can the system be solved uniquely?
            # or are lines overlapping/parallel?now we have a,b,c,d,e,f
            # if det is zero then we have infinite solutions or no single solution
            x = (e*d - b1*f) / det
            y = (a*f - e*c) / det
            vector = [x, y]
            return vector

    elif mode == "numpy":
        solved_system = np.linalg.solve(A, b)
        vector = solved_system 
        return vector
    else:
        raise ValueError("Invalid mode. Use 'pure' or 'numpy'.")


if __name__ == "__main__":
    A = [[3, 2], [1, 4]]
    b = [5, 6]

    solution_numpy = solve_system(A, b, mode="numpy")
    print("Solution using NumPy:", solution_numpy)

    solution_pure = solve_system(A, b, mode="pure")
    print("Solution using pure Python:", solution_pure)
