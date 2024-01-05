'''
	Time Complexity  : O(N)
	Space Complexity : O(N)

	Where 'N' is the length of the given array.
'''
from typing import List

def distinctSubKOdds(arr,k):
    # Variable to count the number of odd numbers encountered so far.
    c = 0

    # Variable to store the final result.
    ans = 0

    # Dictionary to store the count of odd numbers encountered.
    mp = {}

    # Loop through each element in the array.
    for i in range(len(arr)):
        # Check if the current element in the array is odd.
        if arr[i] % 2 == 1:
            c += 1  # Increment the count of odd numbers.

        # If the count of odd numbers becomes equal to 'k', increment the answer.
        if c == k:
            ans += 1  # Increment the answer.

        # Check if there exists a subarray with exactly 'k' odd numbers before the current index.
        # If yes, then increment the answer by the count of such subarrays.
        if c - k in mp:
            ans += mp[c - k]

        # Add the current count 'c' to the dictionary to keep track of the frequency of odd numbers.
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1

    return ans  # Return the final count of distinct subarrays with 'k' odd numbers.



nums = [1,1,2,1,1]
k = 3
ans = distinctSubKOdds(nums,k)
print(ans)