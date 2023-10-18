# Time Complexity: O(N4), where N = size of the array.
# Reason: Here, we are mainly using 4 nested loops. But we not considering the time complexity of sorting as we are just sorting 4 elements every time.

# Space Complexity: O(2 * no. of the quadruplets) as we are using a set data structure and a list to store the quads.

#Brute Force
# def fourSum(nums, target):
#     n = len(nums) # size of the array
#     st = set()

#     # checking all possible quadruplets:
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 for l in range(k + 1, n):
#                     # taking bigger data type
#                     # to avoid integer overflow:
#                     sum = nums[i] + nums[j]
#                     sum += nums[k]
#                     sum += nums[l]

#                     if sum == target:
#                         temp = [nums[i], nums[j], nums[k], nums[l]]
#                         temp.sort()
#                         st.add(tuple(temp))

#     ans = list(st)
#     return ans
# nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
# target = 9
# ans = fourSum(nums, target)
# print("The quadruplets are:")
# for it in ans:
#     print("[", end="")
#     for ele in it:
#         print(ele, end=" ")
#     print("]", end=" ")
# print() 

#__________________________________________________________________________________________________________________________________________________________________

# Time Complexity: O(N3*log(M)), where N = size of the array, M = no. of elements in the set.
# Reason: Here, we are mainly using 3 nested loops, and inside the loops there are some operations on the set data structure which take log(M) time complexity.

# Space Complexity: O(2 * no. of the quadruplets)+O(N)
# Reason: we are using a set data structure and a list to store the quads. This results in the first term. And the second space is taken by the set data structure
# we are using to store the array elements. At most, the set can contain approximately all the array elements and so the space complexity is O(N).

#Better Approach
def fourSum(nums,target):
    n = len(nums)
    st = set()

    # checking all possible quadruplets:
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                # taking bigger data type to avoid integer overflow:
                sum_ = nums[i] + nums[j] + nums[k]
                fourth = target - sum_
                if fourth in hashset:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    st.add(tuple(temp))
                # put the kth element into the hashset:
                hashset.add(nums[k])

    ans = list(st)
    return ans

nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
ans = fourSum(nums, target)
print("The quadruplets are:")
for it in ans:
    print("[", end="")
    for ele in it:
        print(ele, end=" ")
    print("]", end=" ")
print()
#__________________________________________________________________________________________________________________________________________________________________

#Time Complexity: O(N3), where N = size of the array.
# Reason: Each of the pointers i and j, is running for approximately N times. And both the pointers k and l combined can run for approximately N times
# including the operation of skipping duplicates. So the total time complexity will be O(N3). 

# Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. So,
# from that perspective, space complexity can be written as O(1).

#Optimal Solution

# def fourSum(nums,target):
#     n = len(nums) # size of the array
#     ans = []

#     # sort the given array:
#     nums.sort()

#     # calculating the quadruplets:
#     for i in range(n):
#         # avoid the duplicates while moving i:
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         for j in range(i + 1, n):
#             # avoid the duplicates while moving j:
#             if j > i + 1 and nums[j] == nums[j - 1]:
#                 continue

#             # 2 pointers:
#             k = j + 1
#             l = n - 1
#             while k < l:
#                 _sum = nums[i] + nums[j] + nums[k] + nums[l]
#                 if _sum == target:
#                     temp = [nums[i], nums[j], nums[k], nums[l]]
#                     ans.append(temp)
#                     k += 1
#                     l -= 1

#                     # skip the duplicates:
#                     while k < l and nums[k] == nums[k - 1]:
#                         k += 1
#                     while k < l and nums[l] == nums[l + 1]:
#                         l -= 1
#                 elif _sum < target:
#                     k += 1
#                 else:
#                     l -= 1

#     return ans


# nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
# target = 9
# ans = fourSum(nums, target)
# print("The quadruplets are:")
# for it in ans:
#     print("[", end="")
#     for ele in it:
#         print(ele, end=" ")
#     print("]", end=" ")
# print()

