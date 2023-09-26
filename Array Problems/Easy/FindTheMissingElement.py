
#My approaches which wasnt accepted in leetcode
# nums = [3,0,1]
# temp = []
# for i in range(1,len(nums)+1):
#     temp.append(i)
# for i in range(len(nums)):
#     if temp[i] not in nums:
#         print(temp[i])

#_____________________________________________________________________________________________________________________________

# def finding(nums,n):
#     for i in range(1,n+1):
#         if i not in nums:
#             return i


# nums = [9,6,4,2,3,5,7,0,1]
# n = len(nums)
# res = finding(nums,n)
# print(res)

#_____________________________________________________________________________________________________________________________

#Brute force approach

# def brute(arr,n):
#     for i in range(1,n+1):
#         flag = 0
#         for j in range(n):
#             if arr[j] == i:
#                 flag = 1
#                 break
#         if flag == 0:
#             return i

# arr = [1,2,0,4]
# n = len(arr)
# res = brute(arr,n)
# print(res)

#Time Complexity is O(N^2) and space complexity is O(1)

#_____________________________________________________________________________________________________________________________

# #Better Approach
def missing(arr,n):
    hash = [0] *(n + 1) # hash array

    # storing the frequencies:
    for i in range(n - 1):
        hash[arr[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1,n+1):
        if hash[i] == 0:
            return i
     # The following line will never execute.
     # It is just to avoid warnings.
    return -1

arr = [1, 2, 4, 5]
n = 5 # here im taking n as 5 because the max no is 5 thus im not taking len(arr)
res = missing(arr,n)
print("The missing number is :-",res)

#_____________________________________________________________________________________________________________________________

#optimal approach

# def missingNumber(a, N):
#     # Summation of first N numbers:
#     summation = (N * (N + 1)) // 2

#     # Summation of all array elements:
#     s2 = sum(a)

#     # count = 0 (can use this method also to sum the no elements in the array)
#     # for i in range(n-1):
#     #     count += a[i]
#     # miss = summation - count

#     missingNum = summation - s2
#     return missingNum


# N = 5
# a = [1, 2, 4, 5]
# ans = missingNumber(a, N)
# print("The missing number is:", ans)

#_____________________________________________________________________________________________________________________________

#Time Complexity = O(N)
#Space Complexity = O(1)

#optimal approach

# def missingNumber(a, N):
#     xor1 = 0
#     xor2 = 0

#     for i in range(N - 1):
#         xor2 = xor2 ^ a[i]  # XOR of array elements
#         xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
#     xor1 = xor1 ^ N  # XOR up to [1...N]

#     return xor1 ^ xor2  # the missing number


# def main():
#     N = 5
#     a = [1, 2, 4, 5]
#     ans = missingNumber(a, N)
#     print("The missing number is:", ans)


# if __name__ == '__main__':
#     main()

