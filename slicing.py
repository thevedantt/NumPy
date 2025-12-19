import numpy as np 

data = np.array([[1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15]])

#data[start:stop:step]

print(data[1])
print(data[-1])    
print(data[0:2])   
print(data[::2])
print(data[::-1])

#coulmn selection 
print(data[:,2])
print(data[:,-2])

print(data[0:1,0:3])
print(data[0:2,0:2])

print(data[2:,2:]) 

# ==========================================
# ADVANCED CONCEPTS: Slicing and Indexing
# ==========================================
print("\n--- Advanced Slicing Concepts ---")

# 1. Ellipsis (...)
# doc: Expands to the number of : objects needed for the selection tuple to index all dimensions.
# syntax: arr[..., index]
# Explanation: Useful for higher-dimensional arrays to select "everything up to this dimension".
big_arr = np.random.randint(0, 10, (2, 3, 4)) # 3D array
print("\n1. Ellipsis slicing (Selecting last column of every matrix):")
print(big_arr[..., -1])
# Explanation: Equivalent to big_arr[:, :, -1] but dimension-agnostic.

# 2. newaxis (Dimension Expansion)
# doc: Increases the dimension of the existing array by one more dimension.
# syntax: arr[np.newaxis, :] or arr[:, np.newaxis]
arr_1d = np.array([1, 2, 3])
arr_2d_col = arr_1d[:, np.newaxis]
print("\n2. newaxis (1D to Column Vector):")
print(f"Original shape: {arr_1d.shape}")
print(f"New shape: {arr_2d_col.shape}")
print(arr_2d_col)

# 3. Boolean Indexing with Assignment
# doc: Using a mask to assign values.
# syntax: arr[mask] = value
copy_data = data.copy()
copy_data[copy_data % 2 == 0] = -1 # Replace evens with -1
print("\n3. Boolean Assignment (Evens -> -1):")
print(copy_data)

# 4. Fancy Indexing (Integer Array Indexing)
# doc: Indexing with arrays of integers.
# syntax: arr[row_indices, col_indices]
# Explanation: Selects elements at (row[0], col[0]), (row[1], col[1]), etc.
rows = np.array([0, 1, 2])
cols = np.array([0, 4, 4]) # 1st col of 1st row, last of 2nd, last of 3rd
selected = data[rows, cols]
print("\n4. Fancy Indexing (Specific Points):")
print(f"Selecting (0,0), (1,4), (2,4) from data:")
print(selected)
