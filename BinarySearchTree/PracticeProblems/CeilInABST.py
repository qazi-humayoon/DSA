#Just writing the logic which is to be placed and not making the whole binary search tree

#Remember BST is that where left side is less than that of root node and right side is greater than that of root node

# Time Complexity: O(log(N)) {Similar to Binary Search, at a given time we’re searching one half of the tree, so the time taken would be of the order log(N) where N are the total nodes in the BST and log(N) is the height of the tree.}

# Space Complexity: O(1) {As no extra space is being used, we’re just traversing the BST.}


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_ceil(root, input_val):
    ceil = -1
    
    while root:
        if root.data == input_val:
            return input_val  # If input is found in the tree, return it as ceil.
        elif root.data < input_val:
            root = root.right  # Move to the right subtree if input is greater than current node's data.
        else:
            ceil = root.data   # Mark ceil to be current node's data.
            root = root.left   # Move to the left subtree to find a closer ceil value.
            
    return ceil  # Return computed ceil value.

if __name__ == "__main__":
    # Driver Code.
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.left.right.right = Node(8)
    root.right = Node(11)

    print(find_ceil(root, 6))  # Find and print the ceil of 6 in the BST.