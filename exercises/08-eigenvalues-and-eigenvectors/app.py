import numpy as np  

def compute_eigen(A, mode="numpy"):
    if len(A) != len(A[0]):
        return "must be square"
    
    else:
        if mode == 'pure':
            a, b = A[0]
            c, d = A[1]

            lambda1 = ((a + d) + ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2
            lambda2 = ((a + d) - ((a + d)**2 - 4*(a*d - b*c))**0.5) / 2

            return ([lambda1, lambda2], None)

        else:
            A = np.array(A)
            return np.linalg.eig(A)


A = [[3, 2], [1, 4]]
print(compute_eigen(A, "pure"))
print(compute_eigen(A, "numpy"))