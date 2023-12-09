#Optimal  GFG
# Tc O(N + K)
# Sc O(K)

# lis =""
# last = head
# while last:
#     lis+=str(last.data)
#     last= last.next
# lis = int(lis)
# return Node(lis+1)

#____________________________________________________________________________________________

#Optimal Coding Ninjas
# Tc O(N)
# Sc O(N)

# We use recursion backtracking in this method to solve the problem
# def add_helper(temp):  #Creating a func which calculates if temp is None then return 1 
#     if temp is None:
#         return 1
    
#     carry = add_helper(temp.next) #Using recurison to call helper again and again then based on that adding 1 to last node of the ll using backtracking
#     temp.data += carry

#     if temp.data < 10:  #if the data after adding 1 remained under 10 then we return 0
#         return 0
#     temp.data = 0     #if the data becomes 0 after adding the carry 1 then we return 1 to add another node or make other nodes zero also depending on the no give
#     return 1

# def addOne(head: Node) -> Node:
#     # write your code here
#     carry = add_helper(head)      #Carry carries what is return by helper func whether it is 0 or 1 

#     if carry == 1:                # If the carry is 1 at last then we end up creating another node for the linkedlist
#         new_node = Node(1)
#         new_node.next = head
#         head = new_node
#     return head                   # If the carry is not 1 and it is 0 then we simply return the head
    