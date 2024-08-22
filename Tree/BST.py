class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        if self.root is None:
            self.root = Node(element)
        else:
            self._insert(self.root, element)

    def _insert(self, node, element):
        if element < node.element:
            if node.left is None:
                node.left = Node(element)
            else:
                self._insert(node.left, element)
        else:
            if node.right is None:
                node.right = Node(element)
            else:
                self._insert(node.right, element)

    def delete(self, element):
        self.root = self._delete(self.root, element)

    def _delete(self, node, element):
        if node is None:
            return node
        if element < node.element:
            node.left = self._delete(node.left, element)
        elif element > node.element:
            node.right = self._delete(node.right, element)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.element = temp.element
            # Delete the inorder successor
            node.right = self._delete(node.right, temp.element)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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
bst = BinarySearchTree()
elements = [50, 30, 70, 20, 40, 60, 80]
for element in elements:
    bst.insert(element)

# Traversals
print('Inorder Traversal')
bst.inorder(bst.root)
print()

print('Preorder Traversal')
bst.preorder(bst.root)
print()

print('Postorder Traversal')
bst.postorder(bst.root)
print()

# Counting nodes
total_nodes = bst.count_nodes(bst.root)
print(f'Total number of nodes: {total_nodes}')

# Calculating height
tree_height = bst.calculate_height(bst.root)
print(f'Height of the tree: {tree_height}')

# Deleting a node
bst.delete(70)
print('Inorder Traversal after deleting 70')
bst.inorder(bst.root)
print()
