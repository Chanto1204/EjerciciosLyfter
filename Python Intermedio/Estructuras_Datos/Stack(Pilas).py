#PIlAS(Stack)

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        self.top = None 

    def push(self, new_node):

        new_node.next = self.top
        self.top = new_node

    def pop(self):

        if self.top is None:
            print("La pila está vacía")
            return

        self.top = self.top.next


