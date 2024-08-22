class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = TreeNode(value)
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = TreeNode(value)
                        break
                    else:
                        current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self):
        stack = []
        result = []
        current = self.root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.value)
                current = current.right
        return result

# Example usage:
# Create a binary tree
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Search for a value
print(tree.search(4))  # Output: True
print(tree.search(9))  # Output: False

# Perform an inorder traversal
print(tree.inorder_traversal())  # Output: [2, 3, 4, 5, 6, 7, 8]
