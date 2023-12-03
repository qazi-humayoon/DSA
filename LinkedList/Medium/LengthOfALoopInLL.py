#Optimal
# TC O(N * 1 or Log(n))
# SC O(N)

# mpp = {}
# temp = head
# timer = 1
# while temp:
#     if temp in mpp:
#         value = mpp[temp]
#         return timer - value
#     mpp[temp] = timer
#     timer += 1
#     temp = temp.next
# return 0

#________________________________________________________________


#Optimal
# TC O(N)
# SC O(1)

# cnt = 1
# slow = head
# fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#         slow = fast.next
#         while slow != fast:
#             slow = slow.next
#             cnt += 1
#         return cnt
# return 0