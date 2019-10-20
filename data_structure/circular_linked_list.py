# 순환 연결 리스트

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def initNode():
    global node1, node2, node3, node4
    node1 = Node("first node")
    node2 = Node("second node")
    node3 = Node("third node")
    node4 = Node("fourth node")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1


def main():
    initNode()
    start = node1
    node = node1
    while True:
        print(node.data)
        node = node.next
        if node == start:
            break

main()