## Slicing list

```
# arr[start:stop:step]
# About slicing:
# - start defaults to 0
# - stop defaults to len(arr)
# - step defaults to 1

# Python slicing uses the syntax arr[start:stop:step]
# - arr[::-1] means start from end to start in steps of -1, which reverses the list.
# - arr[1:4] gives elements from index 1 to 3.
# - arr[:3] means from beginning to index 2.
# - arr[2:] means from index 2 to end.
# - arr[::2] means every second element from beginning to end.
#
# Negative slicing:
# - arr[-1] is the last element
# - arr[-2:] gives the last two elements
# - arr[:-1] gives all elements except the last
# - arr[-3:-1] gives the third and second to last elements
# - arr[::-1] reverses the array (step -1 from end to start)
```

* So slicing is tolerant, while indexing is strict. so invalid slicing will return []