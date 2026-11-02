class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, new_node):

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def dequeue(self):
        if self.head is None:
            print("La fila está vacía")
            return

        removed_node = self.head
        self.head = self.head.next

        return removed_node.data