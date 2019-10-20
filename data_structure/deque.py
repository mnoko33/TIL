class Deque:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self, idx=-1):
        self.items.pop(idx)

D = Deque()
print(D)
D.push(1)
D.push(2)
D.push(3)
print(D.items)
D.pop()
print(D.items)
D.pop(0)
print(D.items)