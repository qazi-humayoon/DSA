class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def iterativeinorder(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.data)
        cur = cur.right

    return res


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


result = iterativeinorder(root)
# Print the result list
print("Iterative Inorder Traversal Result:", result)