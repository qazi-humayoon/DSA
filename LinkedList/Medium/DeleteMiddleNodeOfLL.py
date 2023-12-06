#Brute force
# TC O(N + N/2)
# SC O(1)

# if head is None or head.next is None:
#     return None
# temp = head
# n = 0
# while temp:
#     n += 1
#     temp = temp.next
# res = n // 2
# temp = head
# while temp:
#     res -= 1
#     if res == 0:
#         temp.next = temp.next.next
#         break
#     temp = temp.next
# return head

#_______________________________________________________________________________-

#Optimal
# TC O(N/2)
# SC O(1)

# if head is None or head.next is None:
#     return None
# slow = head
# fast = head
# fast =fast.next.next
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
# slow.next = slow.next.next
# return head