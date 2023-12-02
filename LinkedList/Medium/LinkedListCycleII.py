#Brute Force
# TC: O(N * LogN or 1)
# SC: O(N)

# mpp = {}
# temp = head
# while temp:
#     if temp in mpp:
#         return temp
#     mpp[temp] = 1
#     temp = temp.next
# return

#_________________________________________________________________________

#Optimal
# TC: O(N)
# SC: O(1)

# slow = head
# fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#         while slow!= fast:
#             slow = slow.next
#             fast = fast.next
#         return slow
# return None