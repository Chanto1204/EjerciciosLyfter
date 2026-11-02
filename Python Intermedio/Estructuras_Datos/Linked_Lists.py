class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def append(self, new_node):

    if self.head is None:
        self.head = new_node
        return
    
    current_node = self.head

    while current_node.next is not None:
        current_node = current_node.next
    
    current_node.next = new_node





