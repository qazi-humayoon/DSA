#BRUTE FORCE
# Time Complexity: O(N * (sum(weights[]) – max(weights[]) + 1)), where sum(weights[]) = summation of all the weights,
# max(weights[]) = maximum of all the weights, N = size of the weights array.
# Reason: We are using a loop from max(weights[]) to sum(weights[]) to check all possible weights. Inside the loop, we
# are calling findDays() function for each weight. Now, inside the findDays() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.
def findDays(weights,cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    
    return days

def leastWeightCapacity(weights,d):
    # Find the maximum and the summation
    maxi = max(weights)
    summation = sum(weights)

    for i in range(maxi, summation + 1):
        reqdays = findDays(weights,i)
        if reqdays <= d:
            return i

    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)




#_______________-------------------_______________________--------------------_________________________------------------_____

#OPTIMAL BINARY SEARCH
# Time Complexity: O(N * log(sum(weights[]) – max(weights[]) + 1)), where sum(weights[]) = summation of all the weights,
# max(weights[]) = maximum of all the weights, N = size of the weights array.
# Reason: We are applying binary search on the range [max(weights[]), sum(weights[])]. For every possible answer ‘mid’, 
# we are calling findDays() function. Now, inside the findDays() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # Size of array
    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # Move to next day
            load = weights[i]  # Load the weight
        else:
            # Load the weight on the same day
            load += weights[i]
    return days

def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)

