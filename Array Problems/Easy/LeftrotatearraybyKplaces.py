#time complexity is O(N - k) + O(k) space complexity O(N)
#Right Rotate
# temp=[]
# k = k%len(nums)
# temp=nums[-k:]
# nums[k:]=nums[:-k]
# nums[:k]=temp

# Left Rotate Array

#Time complexity is O(N - k) + O(k) space complexity O(N)
# n = len(arr)
# k = k % n
# temp = arr[k:]
# arr[-k:] = arr[:k]
# arr[:-k] = temp
# return arr

#Time complexity is O(N) space complexity O(1)
# Right Rotate
nums = [1,2,3,4,5,6,7] 
k= 3
n = len(nums)
k = k%n
def reverse(l,r):
    while l < r :
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1 
#Right Rotate
reverse(0,n-1)
reverse(0,k-1)
reverse(k,n-1)

#Left Rotate

# reverse(0,k-1)
# reverse(k,n-1)
# reverse(0,n-1)	
print(nums) 

