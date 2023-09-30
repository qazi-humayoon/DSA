#sorting the problem using the selection sort without using the sort library function
# def sorting(a,n):
#     for i in range(n-1):
#         mini = i
#         for j in range(i,n):
#             if a[mini] > a[j]:
#                 mini = j
#         temp = a[mini]
#         a[mini] = a[i]
#         a[i] = temp
#     return a

    
# a = [2,2,2,2,0,0,1,0]
# n = len(a)
# res = sorting(a,n)
# print(res)

#_____________________________________________________________________________________________________________________


#sorting the problem using the bubble sort without using the sort library function

# def sorting(a,n):
#     for i in range(n-1,0,-1):
#         for j in range(i):
#             if a[j] > a[j + 1]:
#                 temp = a[j + 1]
#                 a[j + 1] = a[j]
#                 a[j] = temp
#     return a

# a = [2,2,2,2,0,0,1,0]
# n = len(a)
# res = sorting(a,n)
# print(res)

#_____________________________________________________________________________________________________________________

#sorting the problem using the insertion sort without using the sort library function

# def sorting(a,n):
#     for i in range(n):
#         j = i
#         while j > 0 and a[j - 1] > a[j]:
#             temp = a[j - 1]
#             a[j - 1] = a[j]
#             a[j] = temp
#             j -= 1
#     return a


# a = [2,2,2,2,0,0,1,0]
# n = len(a)
# res = sorting(a,n)
# print(res)

#_____________________________________________________________________________________________________________________

#Better solution
#Time Complexity :- O(2*N)
#Space Complexity :- O(1)
# arr = [2,2,2,2,0,0,1,0]
# n = len(arr)
# count0 = 0
# count1 = 0
# count2 = 0
# for i in range(n):
#     if arr[i] == 0:
#         count0 += 1
#     elif arr[i] == 1:
#         count1 += 1
#     else:
#         count2 += 1
# for i in range(count0):
#         arr[i] = 0
# for i in range(count0,count0+count1):
#         arr[i] = 1
# for i in range(count0+count1,n):
#         arr[i] = 2
# print(arr)

#_____________________________________________________________________________________________________________________

#Optimal Solution (DUTCH NATIONAL FLAG ALGORITHM)
#Time Complexity :- O(N)
#Space Complexity :- O(1)

def sorting(arr,n):
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1
    return arr


arr = [0,1,1,0,1,2,1,2,0,0,0]
n = len(arr)
res = sorting(arr,n)
print(res)