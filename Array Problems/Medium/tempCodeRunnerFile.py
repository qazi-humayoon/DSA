#Brute Force
#Tc :- O(N*2)
#Sc :- O(N) if we consider the space use to solve the ans

def leaders(arr,n):  
    ans = []
    
    for i in range(n):
        leader = True

        # Checking whether arr[i] is greater than all 
        # the elements in its right side
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                # If any element found is greater than current leader,
                # curr element is not the leader.
                leader = False
                break

        # Push all the leaders in ans array.
        if leader:
                ans.append(arr[i])

    return ans
# Array Initialization
arr = [10, 22, 12, 3, 0, 6]
n = len(arr)

res = leaders(arr,n)
print(res)