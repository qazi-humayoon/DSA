#Brute Force
# TC O(N^2)
# SC O(1)
def subarrayrange(nums):
    res = 0
    for i in range(len(nums)):
        min_val = max_val = nums[i]
        for j in range(i, len(nums)):
            min_val = min(min_val, nums[j])
            max_val = max(max_val, nums[j])
            res += max_val - min_val
    return res

nums = [1,2,3] # 4 ans
ans = subarrayrange(nums)
print(ans)