class TreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root):
    res = []

    def traversal(root):
        if root is None:
            return
        
        else:
            res.append(root.data)
            traversal(root.left)
            traversal(root.right)

    traversal(root)

    return res

# Constructing the binary tree with nodes from 1 to 10

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)


# Perform inorder traversal starting from the root (1) and get the result list
result_list = preorder_traversal(root)

# Print the result list
print("Preorder Traversal Result:", result_list)


        