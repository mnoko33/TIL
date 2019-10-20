class Queue:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop(0)
    def isEmpty(self):
        return not self.items


Q = Queue()
print(Q) # Queue object
print(Q.isEmpty())
Q.push(1)
Q.push(2)
Q.push(3)
print(Q.items) # [1, 2, 3]
Q.pop()
Q.pop()
print(Q.items) # [3]