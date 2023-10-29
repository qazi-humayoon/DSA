#Brute Force O(N)
# def search(arr,n,k):
#     for i in range(n):
#         if arr[i] == k:
#             return True
#     return False
        

# arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
# k = 2
# n = len(arr)
# res = search(arr,n,k)
# print("The element is present at : ",res)

#____________________________________________________________________________________________________________________

#Optimal Binary Search

#Code Similar as Rotated Sorted Array
def search(arr,n,k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
           return mid              #By adding this line will take care if the array as duplicates or not. Do Debugg
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue
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
        

arr = [3,3,1,2,3,3,3,3,3]
k = 1
n = len(arr)
res = search(arr,n,k)
print("The element is present at : ",res)