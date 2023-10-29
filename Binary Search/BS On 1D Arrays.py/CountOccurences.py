#Brute force
def count(arr: [int], n: int, x: int) -> int:
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt

arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
x = 8
ans = count(arr, n, x)
print("The number of occurrences is:", ans)

#_________________________________________________________________________________________________________________________

#In this code we get the first and last occurance and then subtract last from first + 1 which gives us total occurence
def firstOccurrence(arr, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(arr, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last

#No need for this function we can directly do. It was due to copy paste from first and last position.
#______________________________________________________________________________________

# def firstAndLastPosition(arr, n, k):
    # first = firstOccurrence(arr, n, k)
    # if first == -1:
    #     return (-1, -1)
    # last = lastOccurrence(arr, n, k)
    # return (first, last)
#______________________________________________________________________________________

def count(arr,n,x):
    first = firstOccurrence(arr, n, x)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, x)
    return last - first + 1


arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = 8
x = 8
ans = count(arr, n, x)
print("The number of occurrences is:", ans)