# #Brute Force
# #Tc :- O(N*2)
# #Sc :- O(N) if we consider the space use to solve the ans

# def leaders(arr,n):  
#     ans = []
    
#     for i in range(n):
#         leader = True

#         # Checking whether arr[i] is greater than all 
#         # the elements in its right side
#         for j in range(i+1, n):
#             if arr[j] > arr[i]:
#                 # If any element found is greater than current leader,
#                 # curr element is not the leader.
#                 leader = False
#                 break

#         # Push all the leaders in ans array.
#         if leader:
#                 ans.append(arr[i])

#     return ans
# # Array Initialization
# arr = [10, 22, 12, 3, 0, 6]
# n = len(arr)

# res = leaders(arr,n)
# print(res)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = len(a)
# rotate = []
# for _ in range(n):
#     rotate.append([0]*n)
# for i in range(n):
#     for j in range(n):
#         rotate[j][n - i - 1] = a[i][j]
# for i in range(len(rotate)):
#     for j in range(len(rotate[0])):
#         print(rotate[i][j],end=" ")
#     print()

  
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(a)
for i in range(n):
    for j in range(i):
        a[i][j],a[j][i] = a[j][i],a[i][j]
for i in range(n):
    a[i].reverse()
for i in range(n):
    for j in range(len(a[0])):
        print(a[i][j],end=" ")
    print()