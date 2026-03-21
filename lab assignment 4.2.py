import numpy as np

# Input 5x3 matrix
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input(f"Enter row {i+1} (3 values): ").split()))
    A.append(row)

A = np.array(A)

# Input 3x2 matrix
print("\nEnter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (2 values): ").split()))
    B.append(row)

B = np.array(B)

# Multiply matrices
result = np.dot(A, B)

print("\n5x3 Matrix:")
print(A)

print("\n3x2 Matrix:")
print(B)

print("\nProduct Matrix (5x3 × 3x2):")
print(result)