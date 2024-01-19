class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterativepostorder(root):
    post_order = []
    if not root:
        return post_order

    stack1 = []
    stack1.append(root)
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        post_order.append(stack2.pop().data)

    return post_order


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


result = iterativepostorder(root)
# Print the result list
print("Iterative Inorder Traversal Result:", result)

