# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution:
    def topView(self, root):
        ans = []
        if not root:
            return ans
        
        mpp = {}
        q = deque([(root, 0)])
        
        while q:
            node, line = q.popleft()
            
            mpp[line] = node.val
            
            if node.left:
                q.append((node.left, line - 1))
            
            if node.right:
                q.append((node.right, line + 1))
        
        for val in sorted(mpp.keys()):
            ans.append(mpp[val])
        
        return ans

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
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
root.left.right.right = TreeNode(9)
root.left.right.left = TreeNode(8)

# Creating an instance of the Solution class
sol = Solution()

# Calling the topView function
result = sol.topView(root)

# Printing the result
print(result)
