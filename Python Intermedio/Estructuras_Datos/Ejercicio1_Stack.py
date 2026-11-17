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

    def print_structure(self):
        current_node = self.top

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


stack = Stack()

stack.push(Node("A"))
stack.push(Node("B"))
stack.push(Node("C"))
stack.pop()

stack.print_structure()
