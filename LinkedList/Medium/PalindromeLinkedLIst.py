#Brute
# TC O(N)
# SC O(N)
# write your code here
# if head is None or head.next is None:
#     return True
# temp = []
# while head:
#     temp.append(head.data)
#     head = head.next
# for i in range(len(temp)//2):
#     if temp[i] != temp[len(temp)-i-1]:
#         return False
# return True

#_____________________________________________________________________

#Optimal
# TC O(N/2),O(N/2),O(N/2),
# SC O(1)
def reverse_ll(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_ll(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head

def isPalindrome(head):

    if head is None or head.next is None:
        return True
    slow= head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    new_head = reverse_ll(slow.next)
    first = head
    second = new_head
    while second:
        if first.data != second.data:
            reverse_ll(new_head)
            return False
        first = first.next
        second = second.next
    reverse_ll(new_head)
    return True