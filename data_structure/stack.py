class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop(-1)
    def isEmpty(self):
        return not self.items
    

s = Stack()
print(s) # Stack object
print(s.isEmpty()) # True
s.push(1)
print(s.items) # [1]
s.pop()
print(s.items) # []