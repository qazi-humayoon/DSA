#Brute force
# Time Complexity: O(max(arr[])*N), where max(arr[]) = maximum element in the array, N = size of the array.
# Reason: We are using nested loops. The outer loop runs from 1 to max(arr[]) and the inner loop runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

#IMPORTANT DISCLAIMER

#_____---------------______________-------------

#In this code same approach of KOKO Eating bananas can be applied also or this appraoch can be applied in KOKO Eating bananas also.

#-----------___________________-----------___________
import math

def smallestDivisor(arr, limit):
    n = len(arr)  # size of array
    maxi = max(arr)
    # Find the smallest divisor
    for d in range(1, maxi+1):
        # Find the summation result
        sum = 0
        for i in range(n):
            sum += math.ceil(arr[i] / d)
        if sum <= limit:
            return d
    return -1

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)

#____________________________________________________________________________________________________________________________


#IMPORTANT DISCLAIMER

#_____---------------______________-------------

#In this code same approach of KOKO Eating bananas can be applied also or this appraoch can be applied in KOKO Eating bananas also.

#-----------___________________-----------___________

#OPTIMAL BINARY SEARCH
# Time Complexity: O(log(max(arr[]))*N), where max(arr[]) = maximum element in the array, N = size of the array.
# Reason: We are applying binary search on our answers that are in the range of [1, max(arr[])]. For every possible
# divisor ‘mid’, we call the sumByD() function. Inside that function, we are traversing the entire array, which results in O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

import math

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)

