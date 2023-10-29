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

#_____________________________________________________________________________________________

#Recursive Binary Search

def binarysearch(a,low,high,target):
    if low > high: # Base case
        return -1

    mid = (low  + high) // 2
    if a[mid] == target:
        return mid
    elif target > a[mid]:
        return binarysearch(a,mid + 1,high,target)

    return binarysearch(a,low,mid - 1,target)


def search(a,target):
    return binarysearch(a, 0, len(a) - 1, target)

a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
res = search(a,target)
if res == -1:
    print("The element is present at index :",res)
else:
    print("The target is at index :",res)



