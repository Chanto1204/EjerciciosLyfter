class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:

    def __init__(self):
        self.head = None
        self.tail = None 

    def push_left(self, new_node):

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def push_right(self, new_node):

        if self.head is None:
            self.tail = new_node
            self.head = new_node
            return

        new_node.prev = self.tail 
        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("No hay ningún nodo")
            return
        removed_node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def pop_right(self):
        if self.tail is None:
            print("No hay ningún nodo")
            return
        removed_node = self.tail
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


deque = Deque()
print("Agregando")

deque.push_left(Node("A"))
deque.push_right(Node("B"))
deque.push_left(Node("C"))
deque.push_right(Node("D"))

deque.print_structure()

print("Lo que quedo al eliminar")
deque.pop_left()
deque.pop_right()
deque.print_structure()

print("Agregando después de vaciar")
deque.push_right(Node("E"))
deque.print_structure()