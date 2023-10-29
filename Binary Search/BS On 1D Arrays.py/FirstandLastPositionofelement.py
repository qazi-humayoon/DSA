#Brute force  linear search with Tc O(N)
# def checking(arr,k):
#     n = len(arr)
#     first,last = -1,-1
#     for i in range(n):
#         if arr[i] == k:
#             if first == -1:
#                 first = i
#             last = i
#     return first,last
        


# arr = [3,4,13,13,13,20,40]
# k = 13
# ans = checking(arr,k)
# print(ans)

#__________________---------------------______________________________-_--------------------------------________________

#Using lower and upper bound to get first and last position
# TC : O(2LogN)

# def lb(arr,k):
#     n = len(arr)
#     low = 0
#     high = n - 1
#     ans = n
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] >= k:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans

# #Upper bound

# def ub(arr,k):
#     n = len(arr)
#     low = 0
#     high = n - 1
#     ans = n
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] > k:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans


# # ans = checking1(arr,k)
# # print(ans)

# def checking2(arr,k):
#     n = len(arr)
#     f = lb(arr,k)
#     if f == n or arr[f] != k:
#         return (-1,-1)
#     return (f,ub(arr,k) - 1)
# arr = [3,4,13,13,13,20,40]
# k = 13
# indexes = checking2(arr,k)
# print("The Starting and end index of element is :",indexes)


#__________________________________________________________________________________________________________________

#Using simple binary search to get first and last position
# TC : O(2LogN)

def firstoccurance(arr,k):
    n = len(arr)
    low = 0
    high = n - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            first = mid+jf
            high = mid - 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return first

def lastoccurance(arr,k):
    n = len(arr)
    low = 0
    high = n - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            last = mid
            low = mid + 1
        elif k > arr[mid]:
            low = mid = 1
        else:
            high = mid - 1
    return last


def firstandlast(arr, k):
    first = firstoccurance(arr,k)
    if first == -1:
        return (-1, -1)
    last = lastoccurance(arr, k)
    return (first, last)



arr = [3,4,13,13,13,20,40]
k = 13

ans = firstandlast(arr,k)
print("The first and last index is :",ans)