import numpy as np

data= np.array([1,2,17])
data2= np.array([1.1,2.5,17.8])

#scalar operations
print(data+1)
print(data-1)
print(data*2)
print(data/2)
print(data%2)
print(data**2)

#vector operations
print(np.sqrt(data))
print(np.square(data))
print(np.round(data2))
print(np.ceil(data2))
print(np.floor(data2))
print(np.trunc(data2))

#taking data as radii and finding area 


#Element wise arithmatic operations
print(data+data2)
print(data-data2)
print(data*data2)
print(data/data2)
print(data%data2)
print(data**data2)

#comparsion opeators
print(data>data2)
print(data<data2)
print(data==data2)
print(data!=data2)
print(data>=data2)
print(data<=data2)

data[data>15]=0
print(data)

# ==========================================
# ADVANCED CONCEPTS: Arthmetic and Math
# ==========================================
print("\n--- Advanced Arithmetic Concepts ---")

# 1. In-place Operations
# doc: Modify array in-place, avoiding temporary array creation.
# syntax: +=, -=, *=, /=
# Explanation: More memory efficient for large arrays.
large_arr = np.ones(5)
print("\n1. In-place addition (+= 10):")
large_arr += 10
print(large_arr)

# 2. divmod
# doc: Return element-wise quotient and remainder simultaneously.
# syntax: np.divmod(x1, x2)
numerators = np.array([10, 20, 30])
denominators = np.array([3, 7, 7])
q, r = np.divmod(numerators, denominators)
print("\n2. divmod (Quotient and Remainder):")
print(f"Numerators: {numerators}, Denominators: {denominators}")
print(f"Quotients: {q}")
print(f"Remainders: {r}")

# 3. Floating Point Comparison (isclose)
# doc: Returns a boolean array where two arrays are element-wise equal within a tolerance.
# syntax: np.isclose(a, b, rtol=1e-05, atol=1e-08)
# Explanation: Never strictly compare floats (==) due to precision issues.
f1 = np.array([1.0, 1.0 + 1e-10])
f2 = np.array([1.0, 1.0])
print("\n3. isclose vs ==:")
print(f"Using == : {f1 == f2}") # Might be False for small diffs depending on precision (here close enough likely ok, but good practice)
print(f"Using isclose: {np.isclose(f1, f2)}")

# 4. clip
# doc: Limit the values in an array.
# syntax: np.clip(a, a_min, a_max)
vals = np.array([-10, 0, 10, 20, 30])
clipped = np.clip(vals, 0, 20)
print("\n4. Clip (Limit values to [0, 20]):")
print(f"Original: {vals}")
print(f"Clipped: {clipped}")
