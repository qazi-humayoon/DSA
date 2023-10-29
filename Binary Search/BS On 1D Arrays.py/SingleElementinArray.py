#Brute force
# Time Complexity: O(N), N = size of the given array.
# Reason: We are traversing the entire array.

# Space Complexity: O(1) as we are not using any extra space.
def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    if n == 1:
        return arr[0]

    for i in range(n):
        # Check for first index
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        # Check for last index
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]

    # Dummy return statement
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)

#_________________________________________________________________________________________________________________-____--

#Optimal Code
# Time Complexity: O(logN), N = size of the given array.
# Reason: We are basically using the Binary Search algorithm.

# Space Complexity: O(1) as we are not using any extra space.

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)

