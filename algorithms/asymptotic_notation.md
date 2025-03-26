# Asymptotic Notation 

---

##  What is Asymptotic Notation?
Asymptotic notation is used to describe the **time complexity** and **space complexity** of an algorithm in terms of input size `n`. It helps us understand how algorithms perform when the input grows large.

---

## Why is it a big deal
- evaluate algorithm efficiency
- make choices between two solution
- design scalable system

---

## Big O, Big Ω, and Big Θ
### 1. **Big O (O)** — Worst-case performance
Example: `O(n)` means the algorithm might take time proportional to `n` operations in the worst case.

### 2. **Big Omega (Ω)** — Best-case performance
Example: `Ω(1)` means in the best case, it takes constant time.

### 3. **Big Theta (Θ)** — Average/typical case (tight bound)
Example: `Θ(n log n)` means both worst and best case hover around that.

