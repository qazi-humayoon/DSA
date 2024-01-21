#Optimal

# if not p and not q: #If the nodes of both the trees are empty then they are same
#         return True

# if not p or not q or p.val != q.val: #If either one node is empty between two trees or there value is not equal then false
#     return False

#Using recursion to traverse in both trees at the same time
# return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) 