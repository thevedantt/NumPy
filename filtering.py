import numpy as np

ages = np.array([[12, 15, 18, 22, 25, 28, 32, 35, 40, 45],
                 [13,14,19,23,26,29,34,38,42,47]])

print(ages)

teenagers = ages[ages<18]
adults = ages[ages>=18]
valid_age=ages[(ages>=18) & (ages<=35)]
even_ages=ages[ages%2==0]
odd_ages=ages[ages%2!=0]

slected_age= np.where(ages>=18, ages, 0)
print(slected_age)
print(teenagers)
print(adults)
print(valid_age)
print(even_ages)
print(odd_ages)

# ==========================================
# ADVANCED CONCEPTS: Filtering and Masking
# ==========================================
print("\n--- Advanced Filtering Concepts ---")

# 1. np.where (Ternary Operation)
# doc: Return elements chosen from x or y depending on condition.
# syntax: np.where(condition, x, y)
# Explanation: Vectorized if-else. If condition is True, yield x, else y.
scores = np.array([55, 85, 40, 90])
results = np.where(scores >= 50, 'Pass', 'Fail')
print("\n1. np.where (Pass/Fail):")
print(f"Scores: {scores}")
print(f"Results: {results}")

# 2. np.select (Multi-condition)
# doc: Return values from choice list depending on which condition is true.
# syntax: np.select(condlist, choicelist, default=0)
conditions = [scores >= 90, scores >= 50]
choices = ['A', 'B']
grades = np.select(conditions, choices, default='F')
print("\n2. np.select (Grading):")
print(f"Grades: {grades}")
# Explanation: Cleaner than nested np.where for multiple conditions.

# 3. np.any and np.all
# doc: Test whether any or all array elements along a given axis evaluate to True.
# syntax: np.any(a, axis=None), np.all(a, axis=None)
print("\n3. any() and all():")
print(f"Any score > 80? {np.any(scores > 80)}")
print(f"All scores > 50? {np.all(scores > 50)}")
# Explanation: Quick boolean checks on entire arrays.

# 4. nonzero (Finding Indices)
# doc: Return the indices of the elements that are non-zero.
# syntax: np.nonzero(a)
indices = np.nonzero(scores > 80)
print("\n4. Indices of scores > 80:")
print(indices)
# Explanation: Returns a tuple of arrays, one for each dimension, containing indices.
