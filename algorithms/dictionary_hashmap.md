# Dictionary ( Hashmap in python )
---

## What is Disctionary

A hash map stores key-value pairs and provides:

Average O(1) time complexity for insertion, deletion, and lookup.

In Python:
```commandline
d = {"a": 1, "b": 2}
print(d["a"])  # Output: 1
```
## Why use Hashmap

 Fast lookups by key — Benefit: O(1) average time
 Counting frequency — Benefit: e.g. word count, char count
 Grouping items — Benefit: anagrams, buckets
 Avoiding duplicates — Benefit: hash set or value tracker
 Mapping data — Benefit: like indexes, graphs, caching
 
## Basic Operations

```commandline
d = {}
d["key"] = 100          # Insert
print(d.get("key"))      # Get with fallback
print("key" in d)        # Check existence
d.pop("key")            # Delete
```

## Built-in Functions & Patterns
- get(key, default): avoids KeyError
- setdefault(key, default): inserts default if key missing
- Counter(): from collections for frequency counting
- defaultdict(list): groups by key automatically

```commandline
from collections import defaultdict
anagrams = defaultdict(list)
for word in words:
    key = "".join(sorted(word))
    anagrams[key].append(word)
```

## When to use
- You want O(1) lookup
- You need to count, group, or map elements
- You want to avoid duplicates quickly

## When not to use
- you need ordered data → use OrderedDict or list
- You need index-based access → use list
- You care about memory tightness → hash maps have overhead

---
### Ordered list 
- When order in which the elements for inserted matters. 
- Since python 3.7 all dict are ordered list

### Memoization 
When we save the output of a function call in dictionary so when the same input is called the  
result is picked from dictionary rather than calling function