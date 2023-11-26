#Brute force approach
#Time Complexity : O(N*3)
#Space Complexity : O(1)

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# n = len(a)
# maxlen = float('-inf')
# for i in range(n):
#     for j in range(i,n):
#         Sum = 0
#         for k in range(i,j+1):
#             Sum += a[k]
#         maxlen = max(maxlen,Sum)
        
# print(maxlen)

#__________________________________________________________________________________________________________________________

#Better force approach
#Time Complexity : O(N*2)
#Space Complexity : O(1)

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# n = len(a)
# maxlen = float('-inf')
# for i in range(n):
#     Sum = 0
#     for j in range(i,n):
       
#         Sum += a[j]
#         maxlen = max(maxlen,Sum)
        
# print(maxlen)

# __________________________________________________________________________________________________________________________

#Optimal force approach
#Time Complexity : O(N)
#Space Complexity : O(1)

#Kadane's Algorithm

# a = [-7 -8 -16 -4 -8 -5 -7 -11 -10 -12 -4 -6 -4 -16 -10 ]
# n = len(a)
# maxi = float ('-inf')
# Sum = 0
# for i in range(n):
#     Sum += a[i]
#     if Sum > maxi:
#         maxi = Sum
#     if Sum < 0:
#         Sum = 0
# if Sum == 0:
#     print("0")
# print(maxi)

# ____ ____ ____ ____ ____ ____ _____ ____ ____ ____ ____ ___ ___

#Kadane's Algorithm Follow Up Question if we have to return the Sub-Array Elements

# a = [-2, -3, 4, -1, -2, 1, 5, -3]
# n = len(a)
# maxi = float ('-inf')
# Sum = 0
# start = 0
# ansstart,ansend = -1,-1
# for i in range(n):
#     if Sum == 0:
#         start = i
#     Sum += a[i]
#     if Sum > maxi:
#         maxi = Sum
#         ansstart = start
#         ansend = i

#     if Sum < 0:
#         Sum = 0
# for i in range(ansstart,ansend):
#     print(a[i],end=" ")
# # print(maxi) 