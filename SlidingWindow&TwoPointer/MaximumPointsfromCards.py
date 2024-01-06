# Implementation

# Calculate the sum of all cards and store it in total.

# Calculate the sum of the initial subarray of size n - k and store it in subarray_sum.

# Initialize min_sum to subarray_sum. This variable will track the overall minimum subarray sum we've seen so far. After iterating over the array, min_sum will hold the smallest possible subarray score.

# Iterate through the array starting from index remaining_length and update subarray_sum by adding the current element and subtracting the element that's no longer included in this subarray.

# Update min_sum so that it's always keeping track of the global minimum so far.

# The answer at the end is total - minSum. This is equal to the maximum sum of k elements from the beginning and end of the array.
def maxScore(cardPoints,k):
    n = len(cardPoints)
    total = sum(cardPoints)
    
    remaining_length = n - k
    subarray_sum = sum(cardPoints[:remaining_length])
    
    min_sum = subarray_sum
    for i in range(remaining_length, n):
        # Update the sliding window sum to the subarray ending at index i
        subarray_sum += cardPoints[i]
        subarray_sum -= cardPoints[i - remaining_length]
        # Update min_sum to track the overall minimum sum so far
        min_sum = min(min_sum, subarray_sum)
    return total - min_sum

cardPoints = [1,2,3,4,5,6,1]
k = 3
ans = maxScore(cardPoints,k)
print(ans)