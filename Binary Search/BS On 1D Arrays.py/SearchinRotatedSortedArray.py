#Brute Force O(N)
# def search(arr,n,k):
#     for i in range(n):
#         if arr[i] == k:
#             return i
        

# arr = [12,15,18,2,4]
# k = 2
# n = len(arr)
# res = search(arr,n,k)
# print("The element is present at : ",res)

#____________________________________________________________________________________________________________________

#Optimal Binary Search
def search(arr,n,k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
           return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
               high = mid - 1
            else:
               low = mid + 1
        else:
            if arr[mid]<= k and k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return mid
        

arr = [12,15,18,2,4]
k = 2
n = len(arr)
res = search(arr,n,k)
print("The element is present at : ",res)