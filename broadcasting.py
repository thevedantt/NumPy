import numpy as np

marks = np.array([50, 60, 70])
bonus = 5

print(marks + bonus)

data1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])


data2 = np.array([[1],[2],[3]])
print(data1 + data2) 

print(data2*marks)

# ==========================================
# ADVANCED CONCEPTS: Broadcasting
# ==========================================
print("\n--- Advanced Broadcasting Concepts ---")

# 1. Broadcasting Rules
# doc: Arrays can be broadcast if their trailing dimensions are compatible.
# Rule 1: Dimensions equal?
# Rule 2: One of them is 1?
# syntax: Implicit
# Explanation: Shapes (3, 1) and (3,) -> (3, 3) because (3, 1) + (1, 3) (after prepending 1)
row_vec = np.arange(3).reshape(1, 3) # Shape (1, 3)
col_vec = np.arange(3).reshape(3, 1) # Shape (3, 1)
matrix = row_vec + col_vec
print("\n1. Broadcasting (1,3) + (3,1) -> (3,3):")
print(matrix)

# 2. broadcast_to
# doc: Broadcast an array to a new shape.
# syntax: np.broadcast_to(array, shape)
scalar_arr = np.array([10])
broadcasted = np.broadcast_to(scalar_arr, (3, 3))
print("\n2. broadcast_to (Scalar to 3x3):")
print(broadcasted)
# Explanation: Creates a read-only view, memory efficient.

# 3. None/newaxis for Alignment
# doc: Adding dimensions to make shapes compatible.
# syntax: arr[:, None]
a = np.array([1, 2, 3])
b = np.array([4, 5])
# a is (3,), b is (2,). We want outer sum (3, 2).
# a[:, None] -> (3, 1). b -> (2,) -> (1, 2) implicitly.
outer_sum = a[:, None] + b
print("\n3. Outer Sum via Broadcasting:")
print(f"a: {a}, b: {b}")
print(f"Result (3x2):\n{outer_sum}")
