# This Code Works for Coding Ninja's where we had to first write the Even no's and then ODD Numbers
# TC O(N)
#SC O(Even + Odd)
def segregateEvenOdd(head):
  temp = head
  even = []
  odd = []
  while temp:
    if temp.data%2==0:
      even.append(temp.data)
      temp = temp.next
    else:
      odd.append(temp.data)
      temp = temp.next
  res = even + odd
  cur = head
  for i in res:
    cur.data = i
    cur=cur.next
  return head

#____________________________________________________________________________

#Brute Force: LeetCode and Coding Ninjas where we are storing ODD and then EVEN Nodes
# TC O(2N)
# SC O(N)

# if head is None or head.next is None:
#   return head
# arr = []
# temp = head
# while temp and temp.next:
#   arr.append(temp.data)
#   temp = temp.next.next
# if temp:
#   arr.append(temp.data)

# temp = head.next
# while temp and temp.next:
#   arr.append(temp.data)
#   temp = temp.next.next
# if temp:
#   arr.append(temp.data)

# i = 0
# temp = head
# while temp:
#   temp.data = arr[i]
#   i += 1
#   temp = temp.next
# return head
  
#____-----______________------___________------________  

#Leetcode and Coding Ninjas Problem Solution in this code we are changing the Links of the ODD and EVEN Nodes

#Optimal Solution
# TC O(N)
# SC O(1)

# if not head: return None

# # odd points to the first node 
# odd = head
# # even points to the second node
# # evenHead will be used at the end to connect odd and even nodes
# even = head.next
# evenhead = head.next

# # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
# # If even is not None, then odd is not None. (odd before even)
# # If even.next is not None, then after we update odd to the next odd node, it cannot be None. (The next odd node is even.next)
# while even and even.next:
    
#     # Connect the current odd node to the next odd node
#     odd.next = odd.next.next
#     # Move the current odd node to the next odd node
#     odd = odd.next
    
#     #Same thing for even node
#     even.next = even.next.next
#     even = even.next

# # Connect the last odd node to the start of the even node
# odd.next = evenhead

# # head never changed, so return it
# return head