# 단순 연결 리스트

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def initNode():
    global node1, node2, node3
    node1 = Node("first node")
    node2 = Node("second node")
    node3 = Node("third node")
    node1.next = node2
    node2.next = node3

def makeNode():
    initNode()
    print(node1)
    print(node2)
    print(node3)

def deleteNode():
    del_node = node1.next
    node1.next = del_node.next
    print(node1.next.data)
    print(node3.data)

def addNode():
    node4 = Node("new second node")
    tmp_node = node1.next
    node1.next = node4
    node4.next = tmp_node
    print(node1.data)
    print(node1.next.data)
    print(node1.next.next.data)

def main():
    makeNode()
    print()
    deleteNode()
    print()
    addNode()

main()