class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def allinone(root):
    pre_order, in_order, post_order = [], [], []
    stack = [(root, 1)]

    while stack:
        node, stage = stack.pop()

        # Part of pre-order traversal
        if stage == 1:
            pre_order.append(node.data)
            stage += 1
            stack.append((node, stage))

            if node.left is not None:
                stack.append((node.left, 1))

        # Part of in-order traversal
        elif stage == 2:
            in_order.append(node.data)
            stage += 1
            stack.append((node, stage))

            if node.right is not None:
                stack.append((node.right, 1))

        # Part of post-order traversal
        else:
            post_order.append(node.data)

    return in_order, pre_order, post_order

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.right.left = TreeNode(8)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# root.right.right.left = TreeNode(9)
# root.right.right.right = TreeNode(10)


# Perform inorder traversal starting from the root (1) and get the result list
pre_order, in_order, post_order = allinone(root)

print("The inorder Traversal is:", end=" ")
print(in_order)

print("The preorder Traversal is:", end=" ")
print(pre_order)

print("The postorder Traversal is:", end=" ")
print(post_order)
