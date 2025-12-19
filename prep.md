# NumPy Prep (AI/ML Focused)

## How NumPy is Used in Real AI/ML Pipelines

**Raw Data** (CSV, images, text)  
↓  
**Converted into NumPy Arrays**  
↓  
**Preprocessing using NumPy**  
- Scaling
- Filtering
- Slicing  
↓  
**Passed to ML Models**  
(Scikit-learn / TensorFlow / PyTorch)

> **Note:** NumPy acts as the bridge between raw data and ML models.

---

## 🎯  Questions (AI/ML Focused)

---

## 🔹 Beginner Level

### 1. What is NumPy and why is it faster than Python lists?
**NumPy** is a numerical computing library. It is faster because:
- Uses **contiguous memory**.
- Uses **C-level optimizations**.
- Supports **vectorized operations**.

---

### 2. What is `ndarray`?
`ndarray` is a multi-dimensional array object in NumPy used to store numeric data.

```python
import numpy as np
arr = np.array([1, 2, 3])
```

### 3. Difference between list and NumPy array?

| Feature | Python List | NumPy Array |
| :--- | :--- | :--- |
| **Speed** | Slow | Very fast |
| **Data Types** | Can store mixed types | Stores same data type |
| **Mechanism** | Uses loops | Uses vectorization |

### 4. What does shape represent?
`shape` tells:
- Number of rows
- Number of columns
- Number of dimensions

```python
arr.shape
```

---

## 🔹 Intermediate Level

### 5. Explain broadcasting with an example.
**Broadcasting** allows NumPy to perform operations on arrays of different sizes.

```python
arr = np.array([1, 2, 3])
print(arr + 5)
```

**Result:**
```text
[6 7 8]
```
*Used in feature scaling and bias addition.*

### 6. What is vectorization?
**Vectorization** means performing operations without loops.

```python
arr * 2
```
*This is faster and used in ML computations.*

### 7. Difference between slicing and indexing?
- **Indexing** gets one value.
- **Slicing** gets multiple values.

```python
arr[0]      # Indexing
arr[0:2]    # Slicing
```

### 8. How does NumPy handle memory efficiently?
- Stores data in **contiguous memory**.
- Avoids unnecessary copies.
- Uses **views** instead of duplicates.

---

## 🔹 Advanced Level (AI/ML Interviews)

### 9. How is NumPy used in neural networks?
NumPy is used to:
- Store input data.
- Store weights and biases.
- Perform matrix multiplication.
- Calculate loss and gradients.

### 10. Why is broadcasting important in bias addition?
Bias is a single value but needs to be added to all neurons. **Broadcasting** automatically applies it.

```python
output = weights + bias
```

### 11. Explain `axis` in aggregation functions.
`axis` tells the direction of operation.

```python
arr.sum(axis=0)  # column-wise
arr.sum(axis=1)  # row-wise
```
*Used in loss and metric calculations.*

### 12. How does NumPy support large-scale data processing?
- Fast mathematical operations.
- Low memory usage.
- Efficient slicing and filtering.
- Works well with ML frameworks.

### 13. Difference between view and copy in NumPy?
- **View**: Shares data. Changes affect the original array.
- **Copy**: Creates new data. Changes do NOT affect the original.

```python
b = a.view()
c = a.copy()
```

### 14. Why is NumPy preferred before Pandas in ML pipelines?
- NumPy is **faster**.
- ML libraries expect **NumPy arrays**.
- Pandas is mainly for data analysis, not heavy computation.
