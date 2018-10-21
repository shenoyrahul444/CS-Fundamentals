from collections import deque


class MovingAverage:

    def __init__(self, size):
        self.size = float(size)
        self.q = deque(maxlen=size)
        self.count = 0
        self.total = 0

    def next(self, val):
        if self.count < self.size:
            self.q.append(val)
            self.count += 1
            self.total += val
        else:
            self.total += val - self.q[0]
            self.q.append(val)
        return (self.total) / self.count

"""
We use a queue with a default size to maintain the numbers
Instead of summing the queue elements everytime, we change the total to account for new val and removal of oldest val
This way we keep tract of the moving average.

O(size) Space
O(1) Time 
"""