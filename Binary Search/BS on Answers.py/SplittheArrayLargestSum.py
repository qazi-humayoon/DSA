#Same code as allocate books


#Brute Force
# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements,
# max(arr[]) = maximum of all array elements.
# Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible numbers of pages. Inside the loop, we are
# calling the countStudents() function for each number. Now, inside the countStudents() function, we are using a loop that
#     runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.



def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)

    for maxSum in range(low, high+1):
        if countPartitions(a, maxSum) == k:
            return maxSum
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)

#_________________________________________________________________________________________________________________________

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, 
# max(arr[]) = maximum of all array elements.
# Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function
# for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

#Optimal binary



def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        partitions = countPartitions(a, mid)
        if partitions > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)

