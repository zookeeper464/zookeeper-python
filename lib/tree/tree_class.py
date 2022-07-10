class Node(object):
    def __init__(self, name,data):
        self.name = name
        self.data = data
        self.child = []

    def add(self, obj):
        self.child.append(obj)
