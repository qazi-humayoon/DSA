#Introduction to linked list Coding Ninjas
        head=None
        last=None
        for i in range(len(arr)):
            if head==None:
                head=Node(arr[i])
                last=head
            else:
                last.next=Node(arr[i])
                last=last.next
        return head
#___________________________________________________________________________
#Insert Node at the beginning Coding Ninjas
    newNode = Node(newValue)
    newNode.next = list
    list = newNode
    return newNode
#___________________________________________________________________________
# Deletion in the Linked List last Node Coding Ninjas
    if list is None:
        return
    
    if list.next is None: 
        list.next = None
        return list

    else:
        n = list
        while n.next.next is not None:
            n = n.next
        n.next = None
        return list
#_________________________________________________________________________
#Node Deletion in linked list LeetCode
        node.val = node.next.val
        node.next = node.next.next
#___________________________________________________________________________
#Count Nodes in the Linked List Coding Ninjas
    count = 0
    if head is None:
        return
    else:
        while head is not None:
            count += 1
            head = head.next
    return count
#___________________________________________________________________________
#Search in Linked List Coding Ninjas
        n = head
        while n is not None:
            if k == n.data:
                return 1
            n = n.next
        return 0
#___________________________________________________________________________