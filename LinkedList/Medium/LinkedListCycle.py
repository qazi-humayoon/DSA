#Brute Force
# TC: O(N * LogN or 1)
# SC: O(N)

# mpp = {}
# temp = head
# while temp:
#     if temp in mpp:
#         return True
#     mpp[temp] = 1
#     temp = temp.next
# return False

#_________________________________________________________________________

#Optimal
# TC: O(N)
# SC: O(1)
# if head is None:
#     return False
# slow = head
# fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#         return True
# return False
