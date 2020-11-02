

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# TODO: create another class for Node


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0


    def pop(self):
        pass


    # TODO: need to finish that
    def push(self, object):
        node = Node()
        node.value = object
        node.next = None
        self.
        self.size += 1


    # ---- Getters & Setters ---- #

    def getSize(self):
        return self.size


    def getNodeValue(self):
        return self.node.value


    def setNodeValue(self, value):
        self.node.value = value






