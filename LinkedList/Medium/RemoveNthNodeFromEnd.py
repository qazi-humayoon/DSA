#Brute Force
# TC O(len(LL) + len(N))
# SC O(1)

# cnt = 0
# temp = head
# while temp:
#     cnt += 1
#     temp = temp.next
# if cnt == n:
#     newhead = head.next
#     return newhead
# res = cnt // 2
# temp = head
# while temp:
#     res -= 1
#     if res == 0:
#         break
#     temp = temp.next
# temp.next = temp.next.next
# return head
# #___________________________________________________________________

#Optimal 
# TC O(len(LL))
# SC O(1)

# fast = head
# slow = head
# for i in range(n):
#     fast = fast.next
# if fast is None:
#     return head.next
# while fast.next:
#     fast = fast.next
#     slow = slow.next
# slow.next = slow.next.next
# return head