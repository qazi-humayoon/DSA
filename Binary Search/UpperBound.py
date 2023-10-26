#Brute Force o(N)

# def upperbound(arr,n,x):

#     for i in range(n):
#         if arr[i] > x:
#             # upper bound found
#             return i
#     return n

# arr = [3, 5, 8, 9, 15, 19]
# n = 6
# x = 9
# res = upperbound(arr,n,x)
# print(res)

#Optimal

#Tc O(logN)

def upperbound(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1,2,3,4,5]
n = 6
x = 2
res = upperbound(arr,n,x)
print(res)