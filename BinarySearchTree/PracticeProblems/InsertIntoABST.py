class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert_into_BST(root, val):
    node = root
    if not node:
        return TreeNode(val)

    while node:
        if node.val <= val:
            if node.right is not None:
                node = node.right
            else:
                node.right = TreeNode(val)
                break
        else:
            if node.left is not None:
                node = node.left
            else:
                node.left = TreeNode(val)
                break
    return root


def print_in_order(root):
    if root is None:
        return

    print_in_order(root.left)
    print(root.val, end=" ")
    print_in_order(root.right)


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)

    print("Original Tree (Inorder Traversal): ", end="")
    print_in_order(root)
    print()

    val = 5
    updated_tree = insert_into_BST(root, val)

    print("Tree After Insertion (Inorder Traversal): ", end="")
    print_in_order(updated_tree)
    print()
