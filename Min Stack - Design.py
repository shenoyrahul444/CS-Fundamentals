class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == []:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
print(obj.getMin())
obj.push(3)
print(obj.getMin())
obj.push(-10)
print(obj.getMin())
obj.pop()
print(obj.getMin())
print(obj.top())
obj.pop()
print(obj.getMin())


