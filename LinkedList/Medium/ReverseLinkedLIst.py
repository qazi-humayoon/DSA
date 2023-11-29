# TC O(N)
# SC O(1) 
#Itervative
    # currnode = head
    # nextnode = head
    # prev = None
    # while currnode:
    #     nextnode = nextnode.next
    #     currnode.next = prev
    #     prev = currnode
    #     currnode = nextnode
    # head = prev
    # return head

#____________________________________________________________________

#TC O(N)
#SC O(1)
    # recursive
    # if head is None or head.next is None:
    #     return head
    # new_head = reverseLinkedList(head.next)
    # front = head.next
    # front.next = head
    # head.next = None
    # return new_head
        