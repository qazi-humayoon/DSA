#My Approach. I used Inorder which gives a sorted array for every correct BST and then i check if res[i] >= res[i + 1] which means it is not a corrct BST else return True

# res = []
# def traverse(root):
#     if root is None:
#         return 

#     else:
#         traverse(root.left)
#         res.append(root.val)
#         traverse(root.right)
# traverse(root)

# for i in range(len(res) - 1):
#     if res[i] >= res[i + 1]:
#         return False
#         break
# return True

#__________________________________________________________________________________________________
# Time Complexity: O(N) where N is the number of nodes in the binary tree. Since we are traversing and checking each node the time complexity is proportional to the number of does in the binary tree.

# Space Complexity: O(1) as no additional data structure or memory allocation is done during the traversal, though an O(N) is used as auxiliary space by the recursion stack.

class TreeNode:
    """
    Definition of TreeNode structure
    for a binary tree node
    """
    def __init__(self, x):
        # Value of the node
        self.val = x
        # Pointer to the left child node
        self.left = None 
        # Pointer to the right child node
        self.right = None 

class Solution:
    """
    Class implementing solution
    to check if a given binary
    tree is a valid binary search tree (BST)
    """
    def isValid(self, root):
        """
        Function to check if a given binary
        tree is a valid binary search tree (BST).
        Calls the helper function isValidBST
        with initial min and max values.
        """
        return self.isValidBST(root, float('-inf'), float('inf'))

    def isValidBST(self, root, minVal, maxVal):
        """
        Helper function to recursively validate the BST property.
        """
        if not root:
            # Base case: an empty
            # tree is a valid BST
            return True
        
        # Checks if the current node
        # violates the BST property
        if root.val >= maxVal or root.val <= minVal:
            return False

        # Recursively checks left and right
        # subtrees with updated constraints
        # that every value on its left subtree
        # should be smaller than the current node
        # and every value on its right subtree
        # should be greater than the current node
        return self.isValidBST(root.left, minVal, root.val) and self.isValidBST(root.right, root.val, maxVal)


def printInOrder(root):
    """
    Function to perform an in-order traversal
    of a binary tree and print its nodes.
    """
    if not root:
        # If null, return and
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

    # Checking if the created tree is a valid BST
    isValidBST = solution.isValid(root)

    if isValidBST:
        print("The tree is a valid BST.")
    else:
        print("The tree is not a valid BST.")