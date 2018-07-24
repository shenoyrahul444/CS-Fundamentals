"""
Problem : Implement a queue using 2 stacks
Thought: Think of a queue in terms of stacks. It is a sliding window, with the top of the queue adding elements and the rear of the queue removing elements
        So, a stack for adding elements, and a stack for popping elements


"""
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def add(self,element):
        self.s1.append(element)
        print("Added ",element)

    def pop(self):
        if self.s2:
            return self.s2.pop()
        elif self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        else:
            print("The queue is empty!")

    def __str__(self):
        import json
        return json.dumps(self.s2[::-1]+ self.s1)

q = Queue()

q.add(1)
q.add(2)
q.add(3)
print(q)
print("Popped ",q.pop())
q.add(4)
print("Popped ",q.pop())
print(q)
