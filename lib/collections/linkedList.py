class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def size(self):
        cur = self.head
        num = 0
        while cur is not None:
            cur = cur.next
            num += 1
        return num

    def append(self, data):
        cur = self.head
        while cur is not None:
            cur = cur.next
        cur.next = Node(data)

    def pop(self):
        cur = self.head
        if cur.next is not None:
            while cur.next.next is not None:
                cur = cur.next
        temp = cur.next
        cur.next = None
        return temp

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
