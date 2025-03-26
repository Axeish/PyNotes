# Asymptotic Notation Cheat Sheet

This cheat sheet summarizes the most common asymptotic notations used in algorithm analysis.

---

## Time Complexity Classes

| Notation     | Name               | Description                                         | Example Use Case                     |
|--------------|--------------------|-----------------------------------------------------|--------------------------------------|
| `O(1)`       | Constant Time       | Time does not grow with input size                 | Accessing a list by index            |
| `O(log n)`   | Logarithmic Time    | Time grows slowly with input size                  | Binary search                        |
| `O(n)`       | Linear Time         | Time grows proportionally with input               | Traversing a list                    |
| `O(n log n)` | Log-linear Time     | Slightly more than linear                          | Merge sort, quicksort                |
| `O(n^2)`     | Quadratic Time      | Time grows with square of input size               | Nested loops                         |
| `O(2^n)`     | Exponential Time    | Time doubles with every new element                | Recursive solutions without memo     |
| `O(n!)`      | Factorial Time      | Extremely slow, grows faster than exponential      | Permutations generation              |

---

## Notation Definitions

- **Big O (O)**: Worst-case upper bound.
- **Big Omega (Ω)**: Best-case lower bound.
- **Big Theta (Θ)**: Average-case tight bound (both upper and lower).

---

## Data Structure Operation Complexities

### List

| Operation             | Time Complexity |
|----------------------|-----------------|
| Access (by index)    | O(1)            |
| Append               | O(1)*           |
| Insert/Delete middle | O(n)            |
| Search (in)          | O(n)            |

### Dictionary (HashMap)

| Operation          | Time Complexity |
|-------------------|-----------------|
| Insert/Update     | O(1)            |
| Delete            | O(1)            |
| Search (key in)   | O(1)            |

### Set

| Operation        | Time Complexity |
|-----------------|-----------------|
| Add/Delete/Check| O(1)            |

---

## Growth Comparison (Informal)

```
O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)
```

Use this sheet whenever you analyze or compare algorithms.

---
