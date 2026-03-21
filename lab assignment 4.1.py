 4.1.1
 import numpy as np

identity_matrix = np.eye(4)

print("4x4 Identity Matrix:")
print(identity_matrix)

4.1.1.2
import numpy as np


A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nMatrix Addition (A + B):")
print(addition)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (A x B):")
print(multiplication)