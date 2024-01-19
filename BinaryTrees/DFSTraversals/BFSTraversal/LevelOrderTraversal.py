from collections import deque

class TreeNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []

    res = []
    q = deque()
    q.append(root)

    while q:
        qLen = len(q)
        level = []

        for i in range(qLen):
            node = q.popleft()

            if node:
                level.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        if level:
            res.append(level)

    return res
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Calling the levelOrder method and printing the result
result = levelOrder(root)
print(result)