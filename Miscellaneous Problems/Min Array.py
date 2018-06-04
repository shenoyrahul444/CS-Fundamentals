"""
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

"""

from heapq import *     # For implementing Priority queue
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.top = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        print("Pushed")
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        print("Popped")
        if self.stack:
            self.stack.pop()
            
    def top(self):
        """
        :rtype: int
        """
        print("Top")
        if self.stack:
            return self.stack[:-1]

    def getMin(self):
        """
        :rtype: int
        """
        print("Min")
        print(self.stack)

        print(heapify(self.stack)[0])
        print(self.stack)

        # return [0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(10)
obj.push(-3)
obj.push(1)
obj.push(-8)
obj.push(-9)
print(obj.stack)
print(obj.getMin())
# print(obj.stack)
obj.pop()
print(obj.getMin())
# param_3 = obj.top()
# param_4 = obj.getMin()