#Brute Force
# Tc :- O(N^2)
# Sc :- O(1)
# def reversepairs(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(i + 1,n):
#             if arr[i] > 2 * arr[j]:
#                 count += 1
#     return count
 
# arr = [4, 1, 2, 3, 1]
# res = reversepairs(arr)
# print(res)


#__________________---------------------___________________------------------________________________----------
#Optimal Solution
# Time Complexity: O(2N*logN), where N = size of the given array.
# Reason: Inside the mergeSort() we call merge() and countPairs() except mergeSort() itself. Now, inside the function
# countPairs(), though we are running a nested loop, we are actually iterating the left half once and the right half
# once in total. That is why, the time complexity is O(N). And the merge() function also takes O(N). The mergeSort()
# takes O(logN) time complexity. Therefore, the overall time complexity will be O(logN * (N+N)) = O(2N*logN).

# Space Complexity: O(N), as in the merge sort We use a temporary array to store elements in sorted order.


def merge(a, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if a[left] <= a[right]:
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(a[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(a[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        a[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def team(a,n):
    return mergeSort(a, 0, n - 1)


a = [4, 1, 2, 3, 1]
n = 5
cnt = team(a, n)
print("The number of reverse pair is:", cnt)


