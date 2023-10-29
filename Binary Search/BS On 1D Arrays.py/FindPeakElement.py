#Brute Force O(N)
def peak(arr):
    n = len(arr)
    if n == 1:
        return 0
    for i in range(n):
        if i == 0:
            if arr[i] > arr[i + 1]:
                return 0
        elif i == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
        else:
            if (i == 0 or arr[i - 1]<arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
                return i
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = peak(arr)
print("The peak is at index:", ans)

#______________________-------------------------______________________------------------------______________----------------

#Optimal Solution with O(LogN)
def peak(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

            #Checking if it is peak element or not
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
         #if mid - 1 is less than mid that means peak doesnt exist that side 
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
        #used to handle if there are multiple peaks in an array
        else:
            high = mid - 1
    return mid


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = peak(arr)
print("The peak is at index:", ans)