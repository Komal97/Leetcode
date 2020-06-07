'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
from collections import deque

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if (len(self.stack) == 0):
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_value = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < min_value:
                min_value = self.stack[i]
        return min_value