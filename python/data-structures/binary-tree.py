class TreeNode:
    def __init__(self, data):
        """
        TreeNode class represents each element in the binary tree.
        """
        self.data = data  # Data stored in the node
        self.left = None  # Reference to the left child node
        self.right = None  # Reference to the right child node

class BinaryTree:
    def __init__(self):
        """
        BinaryTree class represents the binary tree data structure.
        """
        self.root = None  # Reference to the root node
        self.size = 0  # Number of elements in the tree

    def __len__(self):
        """
        Returns the number of elements in the tree.
        """
        return self.size

    def insert(self, data):
        """
        Inserts an element into the binary tree.
        """
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)
        self.size += 1

    def _insert_recursively(self, node, data):
        """
        Helper method to recursively insert an element into the binary tree.
        """
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def _find_node(self, node, data):
        """
        Helper method to find a node with the given data in the tree.
        """
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._find_node(node.left, data)
        return self._find_node(node.right, data)

    def search(self, data):
        """
        Searches for an element in the binary tree.
        """
        node = self._find_node(self.root, data)
        return node is not None

    def _find_min(self, node):
        """
        Helper method to find the minimum element in the binary tree.
        """
        while node.left is not None:
            node = node.left
        return node

    def _delete_node(self, node, data):
        """
        Helper method to delete a node with the given data from the binary tree.
        """
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete_node(node.right, temp.data)
        return node

    def remove(self, data):
        """
        Removes an element from the binary tree.
        """
        if not self.search(data):
            raise ValueError("Element not found in the tree")
        self.root = self._delete_node(self.root, data)
        self.size -= 1

def main():
    """
    Main entry point.
    """
    bst = BinaryTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("Size of the binary tree: ", len(bst))
    print("Is 4 present in the tree? ", bst.search(4))
    bst.remove(4)
    print("Is 4 present in the tree after removal? ", bst.search(4))
    print("Size of the binary tree after removal: ", len(bst))

if __name__ == "__main__":
    main()
