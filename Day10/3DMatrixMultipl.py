import numpy as np
A = np.random.randint(1, 5, (2, 3, 4))
B = np.random.randint(1, 5, (2, 4, 3))
C = np.matmul(A, B)
print("3D Matrix Multiplication:\n", C)
