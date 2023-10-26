#Time Complexity of Binary Search is O(LogN) because at each step we are dviding the array by half i.e 2 which leads to O(logN)
# Rather than traversing in the whole array which take O(N)

def binarysearch(a,target):
    n = len(a)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low  + high) // 2
        if a[mid] == target:
            return mid
        elif target > a[mid]:
            low = mid + 1
        else:
            high = mid - 1 

    return -1

a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
res = binarysearch(a,target)
print("The element is present at index :",res)