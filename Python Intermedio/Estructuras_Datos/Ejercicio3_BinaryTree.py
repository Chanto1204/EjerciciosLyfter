class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def _print_node(self, node):
        if node is None:
            return

        print(node.data)
        self._print_node(node.left)
        self._print_node(node.right)

    def print_structure(self):
        self._print_node(self.root)

tree = BinaryTree()

tree.root = Node("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.right = Node("D")

tree.print_structure()