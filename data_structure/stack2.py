# 2개의 큐로 만들어진 stack

class queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop(0)

    def isEmpty(self):
        return not self.items


class stack:
    def __init__(self):
        self.main_Q = queue()
        self.sub_Q = queue()

    def push(self, item):
        while not self.main_Q.isEmpty():
            self.sub_Q.push(self.main_Q.pop())
        
        self.main_Q.push(item)

        while not self.sub_Q.isEmpty():
            self.main_Q.push(self.sub_Q.pop())

    def pop(self):
        return self.main_Q.pop()


S = stack()
S.push(1)
S.push(2)
S.push(3)
print(S.main_Q.items)
print(S.sub_Q.items)
print(S.pop()) # 3
print(S.main_Q.items)
print(S.sub_Q.items)