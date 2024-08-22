class Node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def maketree(self, element, left_tree=None, right_tree=None):
        self.root = Node(element, left_tree.root if left_tree else None, right_tree.root if right_tree else None)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.element, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.element, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.element, end=' ')

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def calculate_height(self, node):
        if node is None:
            return 0
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return 1 + max(left_height, right_height)

# Example usage
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()

x.maketree(40)
y.maketree(60)
z.maketree(20, x)
r.maketree(50, right_tree=y)
s.maketree(30, r)
t.maketree(10, z, s)

# Traversals
print('Inorder Traversal')
t.inorder(t.root)
print()

print('Preorder Traversal')
t.preorder(t.root)
print()

print('Postorder Traversal')
t.postorder(t.root)
print()

# Counting nodes
total_nodes = t.count_nodes(t.root)
print(f'Total number of nodes: {total_nodes}')

# Calculating height
tree_height = t.calculate_height(t.root)
print(f'Height of the tree: {tree_height}')
