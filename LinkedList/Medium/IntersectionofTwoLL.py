#Brute Force
# TC O(temp* hash + temp1*hash)
# SC O(N)

# if not firstHead or not secondHead: return None
#         temp = firstHead
#         mpp = {}
#         while temp:
#             mpp[temp] = 1
#             temp = temp.next
#         temp1 = secondHead
#         while temp1:
#             if temp1 in mpp:
#                 return temp1
#             mpp[temp1] = 1
#             temp1 = temp1.next
#         return None

#_______________________________________________________________________________-

         # || For Better Approach Check my Notebook which contains the better solution ||

#__________________________________________________________________________________
# Optimal
# TC O(N1 + N2)
# SC O(1)

#Checking if the headA or headB is None then return the LL
# if headA is None or headB is None:
#         return None
#     t1 = headA
#     t2 = headB
#     while t1 != t2: #This is the Stopping Condition until headA and headB are not equal
#         t1 = t1.next #Moving Both headA and headB simultaneously
#         t2 = t2.next

#         if t1 == t2:  #This is used to check if the nodes of both LL are equal then return either t1 or t2 of the LL's
#             return t1
#         if t1 == None:  #In this part if t1 reaches None we shift it back to the Opp LL head i.e headB
#             t1 = headB  ##In this part if t2 reaches None we shift it back to the Opp LL head i.e headA
#         if t2 == None:
#             t2 = headA
#     return t1 #This condition is used to check if at the first part they are colliding i.e when t1 == t2 and then return t1