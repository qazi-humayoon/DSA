#Coding Ninjas Brute Force Solution O(N^2) and O(N)

# def nextgreaterele(a):
#     st = []
#     for i in range(len(a) - 1):
#         for j in range(i,len(a) - 1):
#             if a[i] < a[j + 1]:
#                 st.append(a[j + 1])
#                 break
#         else:
          
#             st.append(-1)
#     st.append(-1)
#     return st

# a = [7, 12, 1, 20]
# checking = nextgreaterele(a)
# print(checking)

# # Output: NGE = [12, 20, 20, -1]

#_________________________________________________________________________________________

#Coding Ninjas Optimal Solution and GFG Just loop change as compared to NGE II

def nextGreaterElements(nums):
    n = len(nums)
    nge = [-1] * n
    st = []


    for i in range(n - 1, -1, -1):
        while st and st[-1] <= nums[i % n]:
            st.pop()


        if i < n:
            if st:
                nge[i] = st[-1]
        st.append(nums[i % n])
    return nge


v = [5, 7, 1, 2, 6, 0]
res = nextGreaterElements(v)
print("The next greater elements are")
print(res)

# _________________________________________________________________________________________

#LeetCode Solution Using Stack and Dictionary O(N) and O(N) cross check TC and SC
def next_greater_element(nums1, nums2):
    stack = []
    next_greater_map = {}
    result = []

    # Build a map of the next greater element for each element in nums2
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater_map[stack.pop()] = num
        stack.append(num)

    # For each element in nums1, get the next greater element from the map
    for num in nums1:
        result.append(next_greater_map.get(num, -1))

    return result

# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
output = next_greater_element(nums1, nums2)
print(output)
