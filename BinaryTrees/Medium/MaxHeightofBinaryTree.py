#Using the Level Order Traversal

# from collections import deque
# q = deque()
# res = []
# q.append(root)

# if not q:
#     return None

# while q:
#     qlen = len(q)
#     level = []
#     for i in range(qlen):
#         node = q.popleft()
#         level.append(node)

#         if node.left:
#             q.append(node.left)

#         if node.right:
#             q.append(node.right)
#     res.append(level)

# return len(res)


#________________________________________________________________________________________

# Using Recursion

    # if not root: return 0

    # lh = maxDepth(root.left)
    # rh = maxDepth(root.right)

    # return 1 + max(lh,rh)