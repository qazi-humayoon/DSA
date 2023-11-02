#Brute Force
# Time Complexity: O(N), N = size of the given array.
# Reason: We are using a loop that traverses the entire given array in the worst case.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

def missingK(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1  # shifting k
        else:
            break
    return k


vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)


#__________________________________________________________________________________________________________________________


# Time Complexity: O(logN), N = size of the given array.
# Reason: We are using the simple binary search algorithm.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

#Optimal Binary Search
def missingK(vec, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = vec[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1

vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)

