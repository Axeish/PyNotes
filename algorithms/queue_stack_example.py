# stack_queue/examples.py

"""
Solutions to classic Stack and Queue problems from LeetCode.
Includes:
- Valid Parentheses
- Min Stack
- Queue using Stacks
- Daily Temperatures
"""

# 1. Valid Parentheses (LeetCode 20)
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

# 2. Min Stack (LeetCode 155)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# 3. Implement Queue Using Stacks (LeetCode 232)
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        self.peek()
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

# 4. Daily Temperatures (LeetCode 739)
def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # stores index of temps
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append(i)
    return answer

# Sample test block
if __name__ == "__main__":
    print("Valid Parentheses ({}):".format("()[]{}"), is_valid_parentheses("()[]{}"))

    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print("MinStack getMin():", ms.getMin())  # -3
    ms.pop()
    print("MinStack top():", ms.top())        # 0
    print("MinStack getMin():", ms.getMin())  # -2

    q = MyQueue()
    q.push(1)
    q.push(2)
    print("MyQueue peek():", q.peek())        # 1
    print("MyQueue pop():", q.pop())          # 1
    print("MyQueue empty():", q.empty())      # False

    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Daily Temperatures:", daily_temperatures(temps))
