#Iterative approach is also at the bottom       #
                                                #
#----____----____----_____-----_____-----____----

# Time Complexity: O(H) where H is the height of the binary search tree as we are traversing along the height of the tree. In comparison to LCA in a binary tree where the time complexity is O(N), finding LCA in a binary search tree is more optimised.

# Space Complexity: O(1) as no additional data structure or memory allocation is done during the traversal and algorithm.

# Definition of TreeNode structure
# for a binary tree node
class TreeNode:
    # Constructor to initialize the node with a
    # value and set left and right pointers to null
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to find the lowest common ancestor (LCA)
    # of two nodes in a binary search tree (BST)
    def lowestCommonAncestor(self, root, p, q):
        # Check if the root is None
        if root is None:
            # If None, return None as there's no LCA
            return None
        
        # Store the value of the current root node
        curr = root.val
        
        # If both p and q values are greater
        # than the current root's value
        if curr < p.val and curr < q.val:
            # Recursively search in the
            # right subtree for the LCA
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q values are smaller
        # than the current root's value
        if curr > p.val and curr > q.val:
            # Recursively search in the
            # left subtree for the LCA
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If the values are on either side of the current root's value,
        # or one of the values matches the current root's value,
        # return the current root as the LCA
        return root

# Function to perform an in-order traversal
# of a binary tree and print its nodes
def printInOrder(root):
    # Check if the current node
    # is None (base case for recursion)
    if root is None:
        # If None, return and
        # terminate the function
        return
    
    # Recursively call printInOrder
    # for the left subtree
    printInOrder(root.left)
    
    # Print the value of the current node
    print(root.val, end=" ")

    # Recursively call printInOrder
    # for the right subtree
    printInOrder(root.right)

if __name__ == "__main__":
    solution = Solution()

    # Creating a sample tree
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    print("Inorder Traversal of Tree:")
    printInOrder(root)
    print()
    
    # Node with value 2
    p = root.left.left
    
    # Node with value 4
    q = root.left.right
    
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {lca.val if lca else None}")


    #_____________________________________________________________________________________________________

    #Iterative approach
    
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            curr = root.val
            if curr < p.val and curr < q.val:
                root = root.right
            elif curr > p.val and curr > q.val:
                root = root.left
            else:
                return root
        return None