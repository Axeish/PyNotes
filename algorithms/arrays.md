# Arrays in Python and Algorithm Design

This section covers arrays (also called lists in Python) 

---

## What is an Array?
An array ( list ) is a collection of items stored at contiguous memory locations. 

```python
arr = [1, 2, 3, 4, 5]
```


---

## Common Operations & Their Time Complexity

| Operation            |  Python Syntax     | Time Complexity |
|----------------------|--------------------|-----------------|
| Access               | `arr[i]`           | O(1)            |
| Append               | `arr.append(x)`    | O(1)*           |
| Insert at position   | `arr.insert(i, x)` | O(n)            |
| Delete by index      | `del arr[i]`       | O(n)            |
| Search (in)          | `x in arr`         | O(n)            |
| Loop through         | `for x in arr`     | O(n)            |
| Slice                | `arr[a:b]`         | O(k)            |

Note: Append is  O(1)* — because resizing happens occasionally.

---

## Internal Mechanics
- Python lists are **dynamic arrays**.
- They **resize automatically**, doubling in size when needed.
- Insertions/removals in the middle require shifting elements.

---

## When to Use Arrays
- When you need **fast access** via index.
- When the number of elements is not fixed at compile time.
- For problems involving **sliding windows**, **prefix sums**, or **two pointers**.

---

## Coding Patterns
- **Two pointers**: For sorted arrays or pair sums.
- **Sliding window**: For subarray problems.
- **Prefix sum**: For range query optimizations.

---
> #### *What is a Dynamic Array?
> A **dynamic array** is a resizable array that automatically allocates more memory when needed. Python's `list` is implemented as a dynamic array.
>
> - On `append()`, if the current capacity is full, Python internally creates a larger array, copies all elements, and appends the new one.
> - This resizing step takes O(n) time, but it happens infrequently.
> - That's why `append()` is considered **amortized O(1)**.
>
> In contrast to static arrays (like in C or Java), dynamic arrays do not require you to define a fixed size in advance.
#### *Language Comparison: Static vs. Dynamic Arrays
 
| Language      | Memory Allocation | Static Arrays    | Dynamic Arrays         |
|---------------|-------------------|------------------|-------------------------|
| C / C++       | Manual             | Yes              | Yes (via malloc/vector) |
| Java          | Manual + Managed   | Yes (`int[]`)    | Yes (`ArrayList`)       |
| Python        | Automatic          | No               | Yes (`list`)            |
| JavaScript    | Automatic          | No               | Yes (`[]`)              |
| TypeScript    | Automatic (typed)  | No               | Yes (`number[]`)        |
