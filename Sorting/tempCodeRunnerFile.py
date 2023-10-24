# def sorting(arr):
#     n = len(arr)
#     for i in range(n-1):
#         mini = i
#         for j in range(i,n):
#             if arr[mini] > arr[j]:
#                 mini = j
#         arr[mini],arr[i] = arr[i],arr[mini]
#     return arr

# arr = [13,46,24,52,20,9]
# res = sorting(arr)
# print(res)


# def sorting(arr):
#     n = len(arr)
#     for i in range(n-1,0,-1):
#         for j in range(n-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr




# arr = [13,46,24,52,20,9]
# res = sorting(arr)
# print(res)


# def sorting(arr):
#     n = len(arr)
#     for i in range(n):
#         j = i
#         while j > 0 and arr[j - 1] > arr[j]:
#             arr[j-1],arr[j] = arr[j],arr[j-1]
#             j -= 1
#     return arr


# arr= [13,46,24,52,20,9]
# res = sorting(arr)
# print(res)


# def merge(arr,low,mid,high):
#     temp = []
#     left = low
#     right = mid + 1
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1
    
#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     for i in range(low,high+1):
#         arr[i] = temp[i - low]




# def mergesort(arr,low,high):
#     if low >= high:
#         return 
#     mid = (low + high) // 2
#     mergesort(arr,low,mid)
#     mergesort(arr,mid+1,high)
#     merge(arr,low,mid,high)

# arr = [3,2,4,1,5]
# n = len(arr)
# res = mergesort(arr,0,n-1)
# print("The sorted array using merge sort is O(NLOGN) O(N)")
# for i in range(n):
#     print(arr[i],end = " ")


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
#             arr[i],arr[j] = arr[j],arr[i]
        
#     arr[low],arr[j]= arr[j],arr[low]

#     return j

# def quicksort(arr,low,high):
#     if low < high:
#         pindex = partition(arr,low,high)
#         quicksort(arr,low,pindex - 1)
#         quicksort(arr,pindex + 1,high)


# arr = [4,3,2,1,7,9,5,6]
# n = len(arr)
# res = quicksort(arr,0,n - 1)
# print("the sorted array is trr",arr)


# a = [1,2,22,3,4,5]
# n = len(a)
# maxi = 0
# for i in range(n):
#     if a[i] > maxi:
#         maxi = a[i]
# print(maxi)

# a = [1,2,22,3,4,5]
# n = len(a)
# largest = 0
# slargest = -1
# for i in range(n):
#     if a[i] > largest:
#         largest = a[i]
# for i in range(n):
#     if a[i] > slargest and a[i] != largest:
#         slargest = a[i]
# print(largest,slargest)

# a = [1,2,22,3,4,5]
# n = len(a)

# a = [1,2,2,2,2,3]
# n = len(a)
# s = set()
# for i in range(n):
#     s.add(a[i])
# ans = list(s)

# j = 0
# for x in s:
#     a[j] = x
#     j += 1
# print(ans)
# print(a)
# print(len(s))


# a = [1,2,3,4,5,6,7]
# k = 3
# n = len(a)
# k = k % n
    
# def rotating(l,r):
#     while l < r:
#         a[l],a[r] = a[r],a[l]
#         l += 1
#         r -= 1


# rotating(0,k-1)
# rotating(k,n-1)
# rotating(0,n-1)
# print(a)

# a = [1,2,2,3,3,4,5,6]
# b = [2,3,3,5,6,6,7]
# # i = 0
# # j = 0
# union = []
# # while i < len(a) and j < len(b):
# #     if a[i] == b[j]:
# #         union.append(a[i])
# #         i += 1
# #         j += 1
    
# #     elif a[i] < b[j]:
# #         i += 1


# #     else:
# #         j += 1
# # print(union)
# j = 0
# for i in range(len(a)):
#     if a[i] == b[j]:
#         union.append(a[i])
#         j += 1
# print(union)


    


