# Time Complexity: O(H) where H is the height of the tree. This is due to the binary search applied while finding the node with value as key. All other operations performed are in constant time. O(H) ~ O(log N) in case of a full binary search tree (optimal time).

# Space Complexity: O(1) as no additional data structures or memory allocation is done
class TreeNode:
    """
    Definition of TreeNode structure
    for a binary tree node
    """
    def __init__(self, x):
        """
        Constructor to initialize the node with
        a value and set left and right pointers to null
        """
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        Function to delete a node with a specified
        key from the binary search tree
        """
        if root is None:
            # Return None if the root is empty
            return None

        if root.val == key:
            # Delete the node using the helper function
            return self.helper(root)

        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    # Delete the node using the helper function
                    root.left = self.helper(root.left)
                    break
                else:
                    if root.right is not None and root.right.val == key:
                        # Delete the node using the helper function
                        root.right = self.helper(root.right)
                        break
                    else:
                        root = root.right

        return dummy

    def helper(self, root):
        """
        Helper function to delete the node
        """
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        right_child = root.right
        last_right = self.find_last_right(root.left)
        last_right.right = right_child
        return root.left

    def find_last_right(self, root):
        """
        Helper function to find the last right node in a subtree
        """
        if root.right is None:
            return root
        return self.find_last_right(root.right)


def print_in_order(root):
    """
    Function to perform an in-order traversal
    of a binary tree and print its nodes
    """
    if root is None:
        return

    print_in_order(root.left)
    print(root.val, end=" ")
    print_in_order(root.right)


if __name__ == "__main__":
    solution = Solution()

    # Creating a sample tree for testing purposes
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Printing the original tree
    print("Original Tree (Inorder Traversal): ", end="")
    print_in_order(root)
    print()

    # Testing the deleteNode function
    key_to_delete = 3
    updated_tree = solution.deleteNode(root, key_to_delete)
    # Printing the tree after deletion
    print("Tree After Deletion (Inorder Traversal): ", end="")
    print_in_order(updated_tree)
    print()