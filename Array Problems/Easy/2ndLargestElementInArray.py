#Brute Force 
# In this brute force approach we are sorting first and then wk the largest element is at n-1.
# a = [1,2,4,7,7,5]
# a.sort()
# n = len(a)
# largest = a[n - 1]
#  We use for loop to traverse in the array from length of array to check if there are any duplicates if there are no duplicates then we simply break out from loop
# for i in range(n-1,0,-1):
#     if a[i] < largest:
#         slarge = a[i]
#         break
# print(slarge)

# Time Complexity : Sort = O(NlogN) + for loop (Worst Case) = O(N) = O(NlogN + N)

#Better Solution
# a = [1,2,4,7,7,5]
# largest = a[0]
# n = len(a)
# for i in range(1,n):
#     if a[i] > largest:
#         largest = a[i]
# print(largest)

# slargest = -1
# for i in range(1,n):
#     if a[i] > slargest and a[i] != largest:
#         slargest = a[i]
# print(slargest)

# Time Complexity : O(N) + O(N) = O(2N)

#Optimal Solution
# a = [1,2,4,7,7,5]
# n = len(a)
# largest = a[0]
# slargest = -1
# for i in range(1,n):
#     if a[i] > largest:
#         slargest = largest
#         largest = a[i]
#     elif a[i] < largest and a[i] > slargest:
#         slargest = a[i]
# print(slargest)

# Time Complexity :  O(N)

a = [1,2,4,7,7,5]
n = len(a)
smallest = a[0]
ssmallest = float('inf')
for i in range(1,n):
    if a[i] < smallest:
        ssmallest = smallest
        smallest = a[i]
    elif a[i] != smallest and a[i] < ssmallest:
        ssmallest = a[i]
print(ssmallest)
    




