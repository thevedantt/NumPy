# NumPy for AI & Machine Learning

## What is NumPy?
**NumPy** (Numerical Python) is a Python library used for fast mathematical operations on large datasets.
It provides the `ndarray` object, which is the base of all AI/ML data processing.

## Why NumPy is Important for AI/ML
- AI models work on **numbers**, not text or images.
- Images, datasets, and weights all become **NumPy arrays**.
- Significantly **faster** than Python lists.
- Used by **TensorFlow**, **PyTorch**, and **Scikit-learn**.

## NumPy Setup
**Requirement:** Python 3.9+

### Installation
```bash
pip install numpy==2.3.1
```

### Verification
```python
import numpy as np
print(np.__version__)
```

## Core Concepts Covered

| File | Description |
| :--- | :--- |
| **[basic.py](basic.py)** | Array creation, shape, indexing |
| **[arithmetic.py](arithmetic.py)** | Element-wise operations |
| **[slicing.py](slicing.py)** | Selecting rows & columns |
| **[broadcasting.py](broadcasting.py)** | Operations with different shapes |
| **[filtering.py](filtering.py)** | Conditional selection |
| **[aggregate.py](aggregate.py)** | Sum, mean, max, min |
| **[randomnos.py](randomnos.py)** | Random numbers for ML |