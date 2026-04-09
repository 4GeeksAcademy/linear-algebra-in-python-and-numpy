import numpy as np  

def solve_system(A, b, mode="numpy"):
    "Solves the linear system Ax = b."

    if mode == 'pure':
        det = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])

        if det == 0:
            return "not invertible"
        else:
            inv = [[A[1][1] / det, -A[0][1] / det], [-A[1][0] / det, A[0][0] / det]]

        return [sum(inv[i][k] * b[k] for k in range(len(b))) for i in range(len(inv))]

    else:
        A = np.array(A)
        b = np.array(b)
        return np.linalg.solve(A, b)


A = [[2, 3], [4, -1]]
b = [5, 1]

print(solve_system(A, b, "pure"))
print(solve_system(A, b, "numpy"))