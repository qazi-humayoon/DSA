def mergesort(arr,low,high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right  = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low,high+1):
        arr[i] = temp[i - low]

        
arr = [3,8,4,1,5,9,2]
n = len(arr)

mergesort(arr,0,n-1)
for i in range(n):
    print(arr[i],end=" ")