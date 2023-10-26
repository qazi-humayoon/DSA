#Brute force doing linear search

# def lowerbound(arr,n,x):
#     for i in range(n):
#         if arr[i] >= x:
#             return i
#     return n

# arr = [3, 5, 8, 15, 19]
# n = len(arr)
# x = 9
# res = lowerbound(arr,n,x)
# print("The lower bound is the index :",res)

#______________________________-----------------___________________-------------------_______________-------------________


#Optimal
#TC O(LogN)

def lowerbound(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        # maybe an answer
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            # look for smaller greater index on the left
            high = mid - 1
        else:
            low = mid + 1 #look on the right
    return ans
        

arr = [1,2,2,3]
n = len(arr)
x = 0
res = lowerbound(arr,n,x)
print("The lower bound is the index :" ,res)