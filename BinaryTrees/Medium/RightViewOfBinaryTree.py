#SAME As left view of binary tree with changes only here that is upar nechai krna root.left and root.right ki
# traverse(node.left, level + 1)
# traverse(node.right, level + 1)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def rightSideView(root):
    res = []

    def traverse(root, level):
        if not root:
            return
        
        if len(res) == level:
            res.append(root.val)

        traverse(root.right, level + 1)
        traverse(root.left, level + 1)

    traverse(root, 0)
    return res

# Example usage:
# Assuming you have a tree like:
#    1
#   / \
#  2   3
#   \
#    4
#   / \
#  5   6
# You can create the tree and call the function like this:

# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(6)

# Calling the rightSideView function
result = rightSideView(root)

# Printing the result
print(result)
