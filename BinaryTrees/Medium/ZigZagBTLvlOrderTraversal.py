#Optimal NeetCode TC O(N) and SC O(N)

# if not root:
#     return []

# res = []
# q = deque()
# q.append(root)

# while q:
#     level = []
#     for i in range(len(q)):
#         node = q.popleft()
#         level.append(node.val)

#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)

#     level = reversed(level) if len(res) % 2 else level
#     res.append(level)

# return res

#_________________________________________________________________________________________________________________


#Leetcode solution My Approach

# from collections import deque

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# def levelOrder(root):
#     if not root:
#         return []

#     res = []
#     ans = []
#     q = deque()
#     q.append(root)

#     while q:
#         qLen = len(q)
#         level = []

#         for i in range(qLen):
#             node = q.popleft()

#             if node:
#                 level.append(node.data)

#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#         if level:
#             res.append(level)
#     i = 1
#     n = len(res)
#     while i < n:
#         res[i] = list(reversed(res[i]))
#         i += 2
    

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


# # Calling the levelOrder method and printing the result
# result = levelOrder(root)
# print(result)
#_______________________________________________________________________________

#GFG Solution
# from collections import deque
# if not root:
#     return []

#     res = []
#     ans = []
#     q = deque()
#     q.append(root)

#     while q:
#         qlen = len(q)
#         level = []

#         for i in range(qlen):
#             node = q.popleft()

#             if node:
#                 level.append(node.data)

#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)

#         if level:
#             res.append(level)

#     i = 1
#     n = len(res)

#     while i < n:
#         res[i] = list(reversed(res[i]))
#         i += 2
#     for i in res:
#         for j in range(len(i)):
#             ans.append(i[j])
#     return ans
    