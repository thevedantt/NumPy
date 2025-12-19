import numpy as np

# Basic Aggregation (for context)
arr = np.random.randint(0, 10, (3, 4))
print("Original Array:\n", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

# ==========================================
# ADVANCED CONCEPTS: Aggregation
# ==========================================
print("\n--- Advanced Aggregation Concepts ---")

# 1. Reduction Operations: reduce()
# doc: Applies the ufunc to the elements of the array, reducing the dimension by 1.
# syntax: var = <ufunc>.reduce(array, axis=0, dtype=None)
print("\n1. Reduce Operation (add.reduce equivalent to sum):")
sum_reduce = np.add.reduce(arr, axis=0)
print(f"Sum via reduce (axis=0): {sum_reduce}") 
# Explanation: Equivalent to np.sum(arr, axis=0), but explicit about the reduction ufunc.

# 2. Accumulate: accumulate()
# doc: Accumulates the result of applying the operator to all elements.
# syntax: var = <ufunc>.accumulate(array, axis=0)
print("\n2. Accumulate Operation (cumulative sum):")
cumsum_acc = np.add.accumulate(arr, axis=1)
print(f"Cumulative Sum via accumulate (axis=1):\n{cumsum_acc}")
# Explanation: Returns an array of the same size, showing intermediate steps.

# 3. Outer Product: outer()
# doc: Apply the ufunc to all pairs (a, b) with a in A and b in B.
# syntax: var = <ufunc>.outer(A, B)
a = np.array([1, 2, 3])
b = np.array([4, 5])
outer_prod = np.multiply.outer(a, b)
print("\n3. Outer Product (multiply.outer):")
print(f"Vectors: a={a}, b={b}")
print(f"Outer Product:\n{outer_prod}")
# Explanation: Creates a matrix where element (i, j) is a[i] * b[j].

# 4. Peak to Peak (ptp)
# doc: Range of values (maximum - minimum) along an axis.
# syntax: np.ptp(a, axis=None)
range_vals = np.ptp(arr, axis=1)
print("\n4. Peak-to-Peak (Range) along axis 1:")
print(range_vals)
# Explanation: Useful for checking data spread.

# 5. Percentiles and Quantiles
# doc: Compute list of percentiles.
# syntax: np.percentile(a, q, axis=None)
p50 = np.percentile(arr, 50)
print(f"\n5. 50th Percentile (Median): {p50}")
# Explanation: Robust statistic, less sensitive to outliers than mean.
