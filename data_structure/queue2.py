# 2개의 stack으로 만들어진 queue

class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop(-1)

    def isEmpty(self):
        return not self.items


class queue:
    def __init__(self):
        self.main_S = stack()
        self.sub_S = stack()

    def push(self, item):
        while not self.main_S.isEmpty():
            self.sub_S.push(self.main_S.pop())
        
        self.sub_S.push(item)

        while not self.sub_S.isEmpty():
            self.main_S.push(self.sub_S.pop())

    def pop(self):
        return self.main_S.pop()

    def isEmpty(self):
        return not self.main_S.items

Q = queue()
Q.push(1)
Q.push(2)
Q.push(3)
print(Q.main_S.items)
print(Q.sub_S.items)
Q.pop()
print(Q.main_S.items)
print(Q.sub_S.items)
Q.push(1)
Q.push(2)
Q.push(3)
print(Q.main_S.items)
print(Q.sub_S.items)
Q.pop()
print(Q.main_S.items)
print(Q.sub_S.items)
