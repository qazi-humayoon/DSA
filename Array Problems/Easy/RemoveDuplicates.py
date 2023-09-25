#Brute Force Approach
#Time Complexity O(NLogN + N), Space Complexity O(N)
# nums = [-1,0,0,0,0,3,3]
# b = set()
# for i in range(len(nums)):
#     b.add(nums[i])
# k = len(b)
# j = 0
# for x in b:
#     nums[j] = x
#     j += 1
# print(k)
# print(b)


# arr = [1,2,2,3,4,5,5,6,7]
# n = len(arr)
# j = 1
# for i in range(1,n):
#     if arr[i] != arr[i - 1]:
#         arr[j] = arr[i]
#         j += 1
# print(j)

#Time Complexity O(N)

#same as earlier approach but the other way (Striver)
# i = 0
# for j in range(1,len(nums)):
#     if nums[j] != nums[i]:
#         nums[i + 1] = nums[j]
#         i += 1
# return i + 1  
# we have to use i + 1 because the index starts from 0 and we have to return the length of the list. so i + 1

