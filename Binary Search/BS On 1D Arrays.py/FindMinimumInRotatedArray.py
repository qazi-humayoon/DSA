#Brute Force O(N)

# def findMin(arr: [int]):
#     n = len(arr)  # size of the array.
#     mini = float ('inf')
#     for i in range(n):
#         # Always keep the minimum.
#         mini = min(mini, arr[i])
#     return mini


# arr = [4, 5, 6, 7, 0, 1, 2, 3]
# ans = findMin(arr)
# print("The minimum element is:", ans)

#_____________________________------------________________________-----------------__________________-----------------_______

#Optimal Binary Search

def findMin(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float('inf')
    while low <= high:  
        mid = (low + high) // 2
        
        if arr[low] <= arr[mid]: #Checking if low - mid is sorted which is low will be minimum element(common sense)
            ans = min(ans,arr[low]) #after getting min we move and check if right side has min element or not
            low = mid + 1
        else:
            ans = min(ans,arr[mid]) #if low - mid isnt sorted then arr[mid] is min and then we move to left side to  check further
            high = mid - 1 #moving to left side to check if any further min is present or not
    return ans

arr = [8,9,10,11,1,2,3,4,5]
ans = findMin(arr)
print("The minimum element is:", ans)