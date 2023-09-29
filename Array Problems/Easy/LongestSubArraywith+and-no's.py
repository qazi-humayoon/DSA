#Brute Force
#Time Complexity :- O(N^3) approx because i and j are diminishing
#Space Complexity :- O(1)

# def longest(a,k):
#     n = len(a) # size of the array.
#     length = 0
#     for i in range(n):  # starting index
#          for j in range(i,n): # ending index
#                 # add all the elements of
#                 # subarray = a[i...j]:
#                 s = 0
#                 for l in range(i,j+1):
#                    s += a[l]
#                 if s == k:
#                      length = max(length,j-i+1)
#     return length        


# a = [2, 3, 5, 1, 9]
# k = 10      
# res = longest(a,k)
# print("The longest subarray with sum k is :-",res)

#_________________________________________________________________________________________________________________________________

#Brute Force at Best Case
#Time Complexity :- O(N^2)
#Space Complexity :- O(1)

# def longest(a,k):
#     n = len(a) # size of the array.
#     length = 0
#     for i in range(n):  # starting index
#          s = 0
#          for j in range(i,n): # ending index
#               s += a[j]
#               if s == k:
#                    length = max(length,j-i+1)
#     return length

# a = [2, 3, 5, 1, 9]
# k = 10
# res = longest(a,k)
# print("The longest subarray with sum k is :-",res)

#_________________________________________________________________________________________________________________________________              


#Optimal solution if the array has +ive and -ive values.
#Time Complexity :- O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
#Space Complexity :- O(N) as we are using a map data structure.

def longest(a,k):
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen

a = [1,2,1,0,1,1]
k = 4
length = longest(a,k)
print(f"The length of the longest subarray is: {length}")