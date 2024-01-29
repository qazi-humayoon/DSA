#For the Kth smallest element  Time complexity: O(N) for traversal and O(N) for res space complexity
# res = []
# def traversal(root):
#     if not root:
#         return 
#     else:
#         traversal(root.left)
#         res.append(root.val)
#         traversal(root.right)
# traversal(root)
# # res.sort()   #In a BST whenever we do InOrder Traversal we dont need to sort it. because inorder always given bst in sorted array
# return res[k - 1]
        


# NOTE: For the Kth Largest Element we can do the same logic and just return the res[n - k] and it will return kth largest element
# SAME COMPEXITY HERE ALSO