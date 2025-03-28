# Stack and Queue in Python 
Stack and Queue are linear data Structure 
most commonly used for modelorder, backtracking and scheduling 

## Stack

A stack is a data structure that follows LIFO: Last In, First Out.

### Key operations :
- push(x): Add an element to the top
- pop(): Remove the top element
- peek() / top(): View the top element without removing it
- is_empty(): Check if the stack is empty

```commandline

stack = []
stack.append(10)      # push
stack.pop()           # pop
stack[-1]             # peek
not stack             # is_empty
```

## Queue

A queue is a data structure that follows FIFO: First In, First Out.

### Key operations 

- enqueue(x): Add an element to the end
- dequeue(): Remove from the front
- peek(): View the front element
- is_empty(): Check if the queue is empty

```commandline
from collections import deque
queue = deque()
queue.append(10)      # enqueue
queue.popleft()       # dequeue
queue[0]              # peek
not queue             # is_empty
```

## Uses

| Situation |Stack | Queue |
|-----------|------|-------|
| backtracking(DFS ) | yes| No|
|Breadth First Search| No | yes|
|Matching expression| yes | no |
| task Scheduling | No|yes|