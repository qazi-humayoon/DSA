#Coding Ninjas
    # cur = root
    # while cur:
    #     if cur.data==x:
    #         return True
    #     elif cur.data>x:
    #         cur=cur.left
    #     else:
    #         cur=cur.right
    # return False
# #__________________________________________#__________________________________________#__________________________________________
#Coding Ninjas recursive same as leetcode

# if root == None:
#     return False
# elif (root.data == x):
#     return True
# elif(root.data < x):
#     # Recursively check for right subtree. 
#     return searchInBST(root.right, x)
# else:
#     # Recursively check for left subtree. 
#     return searchInBST(root.left, x)
#__________________________________________

#LeetCode
#  if not root:
#             return None
#         if root.val==val:
#             return root
#         elif root.val>val:
#             return self.searchBST(root.left,val)
#         elif root.val<val:
#             return self.searchBST(root.right,val)

#Striver leetcode
# while root and root.data != target:
#         root = root.left if target < root.data else root.right
# return root
# #__________________________________________#__________________________________________#__________________________________________

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_bst(root, target):
    # Recursive implementation to search for the target value in the binary search tree
    if not root:
        return None  # If the root is None, the target is not found
    if root.data == target:
        return root  # If the current node's value matches the target, return the node
    elif target < root.data:
        return search_bst(root.left, target)  # Search in the left subtree
    elif target > root.data:
        return search_bst(root.right, target)  # Search in the right subtree

def main():
    # Create a binary search tree
    root = Node(8)
    root.left = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right = Node(12)
    root.right.left = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    # Search for a node with the target value
    found = search_bst(root, 10)

    # Display the result based on whether the node is found or not
    if found:
        print("Node value with the given target found")
    else:
        print("Node value with the given target not found")

if __name__ == "__main__":
    main()
