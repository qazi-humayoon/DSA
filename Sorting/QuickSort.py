# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     j = high

#     while i < j:
#         while arr[i] <= pivot and i <= high - 1:
#             i += 1

#         while arr[j] > pivot and j >= low + 1:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[low], arr[j] = arr[j], arr[low]
#     return j

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

def quicksort(arr,low,high):
    if low < high:
        pindex = partition(arr,low,high)
        quicksort(arr,low,pindex - 1)
        quicksort(arr,pindex + 1,high)

arr = [8,5,2,4,1,9]
n = len(arr)
quicksort(arr,0,n - 1)

for i in range(n):
    print(arr[i],end=" ")
