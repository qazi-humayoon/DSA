# arr = [3,1,2,4]
# mini = 0
# total = 0
# n = len(arr)
# for i in range(n):
#     total += arr[i]
#     mini = arr[i]
#     for j in range(i + 1,n):
        
#         mini = min(mini,arr[j])
#         total += mini

# print(total)

# Explaination :
# We need to find the sum of minimum values of all possible subarrays
# Now the brute force is to try all the subarrays one by one .

# Now let's try to optimize the solution :
# Example : [ 3 , 1 , 2 , 4]
# here 3 is going to end in 1 subarray -> [3]
# here 1 is going to end in 2 subarray -> [3,1] , [1]
# here 2 is going to end in 3 subarray -> [3,1,2] , [1,2] , [2]
# here 4 is going to end in 4 subarray -> [3,1,2,4] , [1,2,4] ,[2,4] , [4]

# Now if we come to find the minimum :
# for 3 : 3 
# for 1 : 1,1
# for 2 : 1,1,2
# for 4 : 1,1,2,4

# If you look carefully for 2 or 4 for the first two subarray our minimum is 1 as 1 is smaller than 2 and 4 both

# For 3 we have no item before 3 which is smaller than 3 i.e. for every subarray 3 will be the minimum : = 3

# For 1 we have no item before 1 which is smaller than 1 i.e. for every subarray 1 will be the minimum: = 2

# For 2 the item before 2 which is smaller than 2 is 1 i.e. for subarrays which includes 1 our ans will be 1 and after that our ans = 2
# So what is the index of 1 --> 1 ans index of 2 --> 2
# So we have 2-1 = 1 subarray in which 2 is minimum and for rest one is minimum so we simply add ans for 1 and 2 = 2+2 = 4

# For 4 we have item 2 before 4 smaller than 4 .
# Index of 2 = 2 and index 4 = 3
# ans for 4  = ans for 2 + (3-2)*4 = 4+4 = 8

# the final ans is sum of all ans

# To find the just smaller index before an index use stack !!!!

# best = [0, 0, 0, 0, 0]
# ans = 0

# # i = 0
# best[0] = best[small_before[0]] + (0 - small_before[0]) * arr[0] = 0 + (0 - (-1)) * 3 = 3
# ans += best[0] = 3

# # i = 1
# best[1] = best[small_before[1]] + (1 - small_before[1]) * arr[1] = 0 + (1 - (-1)) * 2 = 4
# ans += best[1] = 7

# # i = 2
# best[2] = best[small_before[2]] + (2 - small_before[2]) * arr[2] = 0 + (2-(-1)) * 1 = 3
# ans += best[2] = 10

# # i = 3
# best[3] = best[small_before[3]] + (3 - small_before[3]) * arr[3] = 3 + (3 - 2) * 4 = 7
# ans += best[3] = 16

def sumSubarrayMins(arr):
    n = len(arr)
    small_before = [-1]*n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:small_before[i] = stack[-1]
        stack.append(i)
    best = [0]*(n+1)
    ans = 0
    for i in range(n):
        best[i] = best[small_before[i]] + (i - small_before[i])*arr[i]
        ans += best[i]
    return ans%1000000007
    
arr = [3,2,1,4]

ans = sumSubarrayMins(arr)
print(ans)