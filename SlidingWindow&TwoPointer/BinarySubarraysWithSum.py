def subarrayWithSum(arr, k):
    
    # To store the result.
    res = 0
    
    # To store count of '1s'.
    cnt = 0
    
    # To store prefix sum.
    prefix = [0] * (len(arr) + 1)
 
    # Initialize index having zero sum as 1.
    prefix[0] = 1
 
    for i in range(len(arr)):
 
        # Update count.
        cnt += int(arr[i])
 
        # Check condition.
        if cnt >= k:
 
            # Update result.
            res += prefix[cnt - k]
 
        # Update prefix array.
        prefix[cnt] += 1
    
    return res

nums = [1,0,1,0,1]
goal = 2
ans = subarrayWithSum(nums,goal)
print(ans)
