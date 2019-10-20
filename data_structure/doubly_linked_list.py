# 이중 연결 리스트

class Node:
    def __init__(self, data, before=None, next=None):
        self.data = data
        self.before = before
        self.next = next

def initNodes():
    global node1, node2, node3, node4, node5
    node1 = Node("1 node")
    node2 = Node("2 node")
    node3 = Node("3 node")
    node4 = Node("4 node")
    node5 = Node("5 node")

    node1.next = node2
    node2.before = node1
    node2.next = node3
    node3.before = node2
    node3.next = node4
    node4.before = node3
    node4.next = node5
    node5.before = node4

def addNode():
    global node3_4
    node3_4 = Node("between 3 and 4 node")
    _next = node3.next
    _before = node3
    node3.next = node3_4
    node4.before = node3_4
    node3_4.next = _next
    node3_4.before = _before

def deleteNode():
    global node3_4
    # delete node3_4
    _next = node3_4.next
    _before = node3_4.before
    _before.next = _next
    _next.before = _before
    del node3_4

def main():
    initNodes()

    addNode()
    node = node1
    while True:
        print('data', node.data)
        if not node.next:
            break
        node = node.next

    deleteNode()
    node = node1
    while True:
        print('data', node.data)
        if not node.next:
            break
        node = node.next
main()