# nums = [1, 2, -3, 0, -4, -5]
# #ans is 20
# maxi = float('-inf')
# n = len(nums)
# for i in range(n):
#     for j in range(i,n):
#         prod = 1
#         for k in range(i,j+1):
#             prod *= nums[k]
#         maxi = max(maxi,prod)
# print(maxi)



nums = [1, 2, -3, 0, -4, -5]
#ans is 20
maxi = float('-inf')
n = len(nums)
for i in range(n):
    prod = 1
    for j in range(i,n):
            prod *= nums[j]
            maxi = max(maxi,prod)
print(maxi)