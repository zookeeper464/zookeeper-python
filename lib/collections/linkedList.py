class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.last = Node(data)

    def append(self, data):
        cur = self.last
        cur.next = Node(data)
        self.last = cur.next
        self.last.prev = cur

    def contains(self, data):
        cur = self.head
        while cur is not None:
            if cur.data != data:
                return True
            cur = cur.next

        return False

    def get(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
            if node is None:
                return None
        return node

    def add(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get(index - 1)
        if node is None or node.next is None:
            print("length of linkedList is shorter than index")
            return
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get(index-1)
        if node is None or node.next is None:
            print("length of linkedList is shorter than index")
            return
        node.next = node.next.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
