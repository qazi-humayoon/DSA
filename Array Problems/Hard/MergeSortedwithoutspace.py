#Leetcode Problem
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# n = len(nums1)
# m = len(nums2)
# for i in range(m):
#     nums1[m+i] = nums2[i]
# nums1.sort()
# print(nums1)

#_--------------________________________________----------------------______________________-------------------_________________

# other approach
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# m = len(nums1)
# n = len(nums2)
# i = m - 1
# j = n - 1
# k = m + n - 1
# while j >= 0:
#     if i >= 0 and nums1[i] > nums2[j]:
#         nums1[k] = nums1[i]
#         i -= 1  # Decrement i here to move to the previous element in nums1
#     else:
#         nums1[k] = nums2[j]
#         j -= 1
#     k -= 1
# print(nums1)

#__________________-------------------___________________------------------___________________-----------------_________________-
       
# #Code Studio
nums1 = [1,2,3]
nums2 = [2,5,6]  
n = len(nums1)
m = len(nums2)
left = n - 1
right = 0
while left >= 0 and right < m:
    if nums1[left] > nums2[right]:
        nums1[left],nums2[right] = nums2[right],nums1[left]
        left -= 1
        right += 1
    else:
        break
    nums1.sort()
    nums2.sort()
print(nums1)
print(nums2)
