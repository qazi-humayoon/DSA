#Optimal
def isBalanced(self, root):
    return self.dfsHeight(root) != -1

def dfsHeight(self, root):
    if root is None:
        return 0

    left_height = self.dfsHeight(root.left)
    if left_height == -1:
        return -1

    right_height = self.dfsHeight(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1

# Example usage:
# Create a sample balanced tree
#          1
#         / \
#        2   3
#       / \
#      4   5
