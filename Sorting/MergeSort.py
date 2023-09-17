def merge(arr, low, mid, high):
    temp = []  # Temporary list to store merged values
    left = low  # Starting index of left half of arr
    right = mid + 1  # Starting index of right half of arr

    # Storing elements in the temporary list in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # If elements in the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If elements in the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Transferring all elements from the temporary list back to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)  # Sort the left half
    mergeSort(arr, mid + 1, high)  # Sort the right half
    merge(arr, low, mid, high)  # Merge the sorted halves

if __name__ == "__main__":

    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

    mergeSort(arr, 0, n - 1)

    print("After Sorting Array:")
    for i in range(n):
        print(arr[i], end=" ")
    print()


# One Way to implement the Merge Sort Algorithm
# def merge_sort(array):
#     if len(array) <= 1:
#         return array

#     mid = len(array) // 2
#     left = merge_sort(array[:mid])
#     right = merge_sort(array[mid:])

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result += left[i:]
#     result += right[j:]

#     return result
# array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# print(merge_sort(array))
