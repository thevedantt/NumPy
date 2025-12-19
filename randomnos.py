import numpy as np

rng = np.random.default_rng(seed=1)
print(rng.integers(low=1, high=101, size=3))
print(rng.integers(low=1, high=101, size=(3,3)))

print(np.random.uniform(low=1, high=101, size=3))

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# ==========================================
# ADVANCED CONCEPTS: Random Number Generation
# ==========================================
print("\n--- Advanced Random Concepts ---")

# 1. Generator API (New vs Legacy)
# doc: The Generator provides access to a wide range of distributions and is faster/safer.
# syntax: rng = np.random.default_rng(seed=None)
# Explanation: 'rng' methods are preferred over 'np.random.func'.
print("\n1. Generator API Distributions:")
# Standard Normal (mean=0, stdev=1)
normals = rng.standard_normal(size=5)
print(f"Standard Normal: {normals}")

# 2. Choice with Probabilities
# doc: Generates a random sample from a given 1-D array.
# syntax: rng.choice(a, size=None, replace=True, p=None)
choices = ['Apple', 'Banana', 'Cherry']
probs = [0.1, 0.7, 0.2] # Must sum to 1
pick = rng.choice(choices, size=3, p=probs)
print("\n2. Weighted Choice (Apple 10%, Banana 70%, Cherry 20%):")
print(pick)
# Explanation: Allows simulating biased events.

# 3. Permutations vs Shuffle
# doc: permutation returns a copy, shuffle modifies in-place.
# syntax: rng.permutation(x), rng.shuffle(x)
arr_orig = np.array([10, 20, 30])
arr_perm = rng.permutation(arr_orig)
print("\n3. Permutation (Original unchanged):")
print(f"Original: {arr_orig}")
print(f"Permuted: {arr_perm}")

# 4. Advanced Distributions
# doc: Complex statistical distributions.
# syntax: rng.beta(a, b), rng.gamma(shape, scale)
beta_vals = rng.beta(a=2, b=5, size=3)
print("\n4. Beta Distribution (a=2, b=5):")
print(beta_vals)
# Explanation: Useful for Bayesian statistics and modeling probabilities.
