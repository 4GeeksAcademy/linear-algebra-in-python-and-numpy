import numpy as np


# vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

def sum_vectors(v1, v2, mode="pure"):
    """Función para sumar vectores con mode='pure' para operar con python puro
    o con mode='numpy' para operar con NumPy"""

    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    
    elif mode not in ['pure', 'numpy']:
        return "invalid mode"
    
    else:
        if mode == 'pure':
            return [v1[i] + v2[i] for i in range(len(v1))]
        
        else:
            v1 = np.array(v1)
            v2 = np.array(v2)

            sum_result = v1 + v2
            return sum_result


def subtract_vectors(v1, v2, mode="pure"):
    """Función para sumar vectores con mode='pure' para operar con python puro
    o con mode='numpy' para operar con NumPy"""

    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")
    
    elif mode not in ['pure', 'numpy']:
        return "invalid mode"
    
    else:
        if mode == 'pure':
            return [v1[i] - v2[i] for i in range(len(v1))]
        
        else:
            v1 = np.array(v1)
            v2 = np.array(v2)

            sub_result = v1 - v2
            return sub_result


sum_result_pure = sum_vectors(vector1, vector2, "pure")
sum_result_numpy = sum_vectors(vector1, vector2, "numpy")

sub_result_pure = subtract_vectors(vector1, vector2, "pure")
sub_result_numpy = subtract_vectors(vector1, vector2, "numpy")

print("Sum in pure Python:", sum_result_pure)
print("Sum in NumPy:", sum_result_numpy)
print("Subtraction in pure Python:", sub_result_pure)
print("Subtraction in NumPy:", sub_result_numpy)