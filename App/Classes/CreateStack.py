

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# TODO: create another class for Node


class Stack:

    ######
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    ######
    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    ######
    def push(self, object):
        node = Node(object)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    ######
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    ######
    def isEmpty(self):
        return self.size == 0

    ######
    def __str__(self):
        current = self.head.next
        output = ""
        while current:
            output += str(current.value) + "->"
            current = current.next
        return output[:-2]


    # ---- Getters & Setters ---- #

    ######
    def getSize(self):
        return self.size

    ######
    def getNodeValue(self):
        return self.node.value

    ######
    def setNodeValue(self, value):
        self.node.value = value



# my_stack = Stack()
#
# my_stack.push(2)
# my_stack.push(4)
# my_stack.push(6)
# my_stack.push(8)
#
# print(my_stack)
# print(my_stack.getSize())
