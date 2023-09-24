# def quicksort(arr,low,high):
#     if low < high:
#         pindex = partition(arr,low,high)
#         quicksort(arr,low,pindex-1)
#         quicksort(arr,pindex+1,high)
# def partition(arr,low,high):
#     pivot = arr[low]
#     i = low
#     j = high
#     while i < j:
#         while arr[i] <= pivot and i <= high - 1:
#             i += 1
#         while arr[j] >= pivot and j >= low + 1:
#             j -= 1
#         if i < j:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#     temp = arr[low]
#     arr[low] = arr[j]
#     arr[j] = temp

#     return j


# arr = [9,2,4,3,6,7,1]
# n = len(arr)

# quicksort(arr,0,n-1)

# print(arr)

def quicksort(arr,low,high):
    if low < high:
        pindex = partition(arr,low,high)
        quicksort(arr,low,pindex-1)
        quicksort(arr,pindex+1,high)

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j


arr = [5,1,4,3,2,6]
n = len(arr)

print("Before quicksort")
for i in range(n):
    print(arr[i],end=" ")
# print()

quicksort(arr,0,n - 1)

print("after quicksort")
for i in range(n):
    
    print(arr[i],end=" ")
# print()
