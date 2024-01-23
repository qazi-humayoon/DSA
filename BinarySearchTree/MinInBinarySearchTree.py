#Recursive
# if not root:
#     return -1
# # Recursively searching for the minimum value.
# if root.left:
#     return minVal(root.left)
# return root.data


#_______________________________________________________

#Iterative
# def minVal(root):
#     # Base case for empty tree.
# if root is None:
#     return -1

# # Iterating through left child until we reach the minimum value.
# while root.left:
#     root = root.left

# return root.data