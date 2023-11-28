#Introduction to linked list Coding Ninjas
        # head=None
        # last=None
        # for i in range(len(arr)):
        #     if head==None:
        #         head=Node(arr[i])
        #         last=head
        #     else:
        #         last.next=Node(arr[i])
        #         last=last.next
        # return head
#___________________________________________________________________________
#Insert Node at the beginning Coding Ninjas
    # newNode = Node(newValue)
    # newNode.next = list
    # list = newNode
    # return newNode
#___________________________________________________________________________
# Deletion in the Linked List last Node Coding Ninjas
    # if list is None:
    #     return
    
    # if list.next is None: 
    #     list.next = None
    #     return list

    # else:
    #     n = list
    #     while n.next.next is not None:
    #         n = n.next
    #     n.next = None
    #     return list
#_________________________________________________________________________
#Node Deletion in linked list LeetCode
        # node.val = node.next.val
        # node.next = node.next.next
#___________________________________________________________________________
#Count Nodes in the Linked List Coding Ninjas
    # count = 0
    # if head is None:
    #     return
    # else:
    #     while head is not None:
    #         count += 1
    #         head = head.next
    # return count
#___________________________________________________________________________
#Search in Linked List Coding Ninjas
        # n = head
        # while n is not None:
        #     if k == n.data:
        #         return 1
        #     n = n.next
        # return 0
#___________________________________________________________________________

#Introduction to DL Coding Ninjas

    # n = len(arr)
    # # 'head' variable stores the head of the
    # # doubly linked list
    # head = Node(arr[0])
    # temp = head

    # for i in range(1, n):
    #     # Attach current node to the "next"
    #     # of the previous node
    #     curNode = Node(arr[i])
    #     temp.next = curNode
    #     # Attach 'temp' to the previous of 'curNode'
    #     curNode.prev = temp
    #     temp = temp.next

    # return head

#___________________________________________________________________________

# Insertion at the end in DLL Coding Ninjas

    # new_node = Node(k)
    # n = head
    # if head is None:
    #     head = new_node
    # else:
    #     while n.next is not None:
    #         n = n.next
    #     n.next = new_node
    #     new_node.prev = n
    # return head
#___________________________________________________________________________

# Deletion of Last Node in DLL Coding Ninjas

    # if head is None:
    #     return 
    # if head.next is None:
    #     head = None
    # else:
    #     n = head
    #     while n.next is not None:
    #         n= n.next
    #     n.prev.next = None
    # return head
#___________________________________________________________________________

#Reverse in a DLL Coding Ninjas
#    if head.next is None:
#         return head

#     curr = head
#     temp = None

#     # Traverse the linked list to the end
#     while (curr != None):

#         temp = curr.prev
#         curr.prev = curr.next
#         curr.next = temp
#         curr = curr.prev 

#     # Update head with the previous node of temp
#     head = temp.prev 

#     # New head of the modified list is returned
#     return head