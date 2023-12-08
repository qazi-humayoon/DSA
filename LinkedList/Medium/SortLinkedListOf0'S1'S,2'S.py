# Brute 
# TC O(2*N)
# SC O(1) 
# if not head or not head.next:
#         return head
#     cnt0 = 0
#     cnt1 = 0
#     cnt2 = 0
#     n = 0
#     temp = head
#     while temp:
#         if temp.data == 0:
#             cnt0 += 1
#         elif temp.data == 1:
#             cnt1 += 1
#         else:
#             cnt2 += 1
#         n += 1
#         temp = temp.next


#     temp = head
#     for i in range(cnt0):
#         temp.data = 0~
#         temp = temp.next
#     for j in range(cnt0,cnt0+cnt1):
#         temp.data = 1
#         temp = temp.next
#     for k in range(cnt0+cnt1,n):
#         temp.data = 2
#         temp = temp.next
#     return head

#____________________---------------______________---------------_____________-----------------_________________

# Optimal 
# TC O(N)
# SC O(1)
    # if not head or not head.next:
    #     return head
    # zero_head = Node(-1)
    # one_head = Node(-1)
    # two_head = Node(-1)

    # zero = zero_head
    # one = one_head
    # two = two_head

    # temp = head
    # while temp:
    #     if temp.data == 0:
    #         zero.next = temp
    #         zero = zero.next
    #     elif temp.data == 1:
    #         one.next = temp
    #         one = one.next
    #     else:
    #         two.next = temp
    #         two = two.next
    #     temp = temp.next
    # zero.next = one_head.next if one_head.next else two_head.next
    # one.next = two_head.next
    # two.next = None

    # new_head = zero_head.next

    # return new_head