#Optimal 
# TC O(max(N1,N2))
# SC O(max(N1,N2)) can't optimize as question is asking to return 


# temp1 = head1
# temp2 = head2
# dummynode = Node(-1)
# curr = dummynode
# carry = 0
# while temp1 or temp2:
#     Sum = carry
#     if temp1:
#         Sum = Sum + temp1.data
#     if temp2:
#         Sum = Sum + temp2.data

#     newnode = Node(Sum % 10)
#     carry = Sum // 10

#     curr.next = newnode
#     curr = curr.next

#     if temp1:
#         temp1 = temp1.next
#     if temp2:
#         temp2 = temp2.next

# if carry:
#     newNode = Node(carry)
#     curr.next = newNode
# return dummynode.next

#____________________________________________________________________________________________________________

#GFG Problem  same as uppar wala but we have to reverse both LL first then add them up and then reverse it back and return the ans

#Reversing the LL first head

# prev = None
# while first:
#     temp = first.next
#     first.next = prev
#     prev = first
#     first = temp

# #Reversing the LL 2nd head
# prev1 = None
# while second:
#     temp = second.next
#     second.next = prev1
#     prev1 = second
#     second = temp

# temp1 = prev
# temp2 = prev1
# dummynode = Node(0)
# curr = dummynode
# carry = 0
# while temp1 or temp2:
#     Sum = carry
#     if temp1:
#         Sum = Sum + temp1.data
#     if temp2:
#         Sum = Sum + temp2.data

#     newnode = Node(Sum % 10)
#     carry = Sum // 10

#     curr.next = newnode
#     curr = curr.next

#     if temp1:
#         temp1 = temp1.next
#     if temp2:
#         temp2 = temp2.next

# if carry:
#     newNode = Node(carry)
#     curr.next = newNode

# #Reversing the LL back to original way
# ans = dummynode.next
# prev2 = None
# while ans:
#     temp = ans.next
#     ans.next = prev2
#     prev2 = ans
#     ans = temp

# return prev2
