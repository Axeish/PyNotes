# Linkedlist in Python and Algorithm Design

This section covers arrays (also called lists in Python) 

---

## What is an Linkedlist?
A linked list is a linear data structure where each element (called a node) contains:

- A value
- A reference (pointer) to the next node

Unlike arrays, linked lists do not store elements in contiguous memory. Instead, each node points to the next one.

---

in python 
```commandline
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

```

