class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(root):
    def isSymmetricUtil(root1, root2):
            # If the tree is empty, it is symmetric
        if not root:
            return True
        # If either subtree is None, they are symmetric if both are None
        if not root1 or not root2:
            return root1 == root2
        # Check if the values of the current nodes are equal
        # and if the left subtree of the first is symmetric with the right subtree of the second,
        # and if the right subtree of the first is symmetric with the left subtree of the second
        return (root1.data == root2.data) and isSymmetricUtil(root1.left, root2.right) and isSymmetricUtil(root1.right, root2.left)
    
    # Check if the left subtree and right subtree of the root are symmetric
    return isSymmetricUtil(root.left, root.right)

# Main function

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Checking if the tree is symmetric
res = isSymmetric(root)

# Displaying the result
if res:
    print("The tree is symmetrical")
else:
    print("The tree is NOT symmetrical")
