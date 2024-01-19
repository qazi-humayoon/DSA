class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def iterativepreorder(root):
    res = []
    stack = []
    if root:
        stack.append(root)

    while stack:
        cur = stack.pop()
        res.append(cur.data)

        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(8)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# root.right.right.left = TreeNode(9)
# root.right.right.right = TreeNode(10)


result = iterativepreorder(root)
# Print the result list
print("Iterative Inorder Traversal Result:", result)




        