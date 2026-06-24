import numpy as np  


matrix = [[1, 2, 3], [4, 5, 6]]


def transpose(matrix, mode="pure"):
    "Transpose valid matrix."

    if len(matrix[0]) != len(matrix[1]):
        return "invalid matrix"
    
    else:
        if mode == 'pure':
            return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        else:
            matrix = np.array(matrix)
            return matrix.T
        

print(transpose(matrix, "pure"))
print(transpose(matrix, "numpy"))