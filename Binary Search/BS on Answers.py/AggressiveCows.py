#Brute Force
# Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in
# stalls[] array, min(stalls[]) = minimum element in stalls[] array.
# Reason: O(NlogN) for sorting the array. We are using a loop from 1 to max(stalls[])-min(stalls[]) to check all possible distances.
#     Inside the loop, we are calling canWePlace() function for each distance. Now, inside the canWePlace() function, we are using a
#     loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls[]
    limit = stalls[n - 1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1
    return limit

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)

#_________________________________________________________________________________________________________________________________

#Optimal Binary Search
# Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = 
# maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
# Reason: O(NlogN) for sorting the array. We are applying binary search on [1, max(stalls[])-min(stalls[])]. Inside the 
# loop, we are calling canWePlace() function for each distance, ‘mid’. Now, inside the canWePlace() function, we are using 
# a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls

    low = 1
    high = stalls[n - 1] - stalls[0]
    # apply binary search
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)

