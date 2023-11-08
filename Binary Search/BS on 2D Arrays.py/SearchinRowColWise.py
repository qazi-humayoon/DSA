#Brute Force
# Time Complexity: O(N X M), where N = given row number, M = given column number.
# Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

# Space Complexity: O(1) as we are not using any extra space.
def searchElement(mat,target):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
            for j in range(m):
                if mat[i][j] == target:       
                    return True

    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")

#_____________________________________________________________________________________________________________________

#Better Solution 
# Time Complexity: O(N + logM), where N = given row number, M = given column number.
# Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are 
# not applying binary search rather we are only applying it once for a particular row. That is why the
# time complexity is O(N + logM) instead of O(N*logM).

# Space Complexity: O(1) as we are not using any extra space.

def binarysearch(mat,target):
    n = len(mat)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if mat[mid] == target:
            ans = mat[mid]
            return True
        elif target > mat[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

def searchElement(mat,target):
    n = len(mat)
    for i in range(n):
            finding = binarysearch(mat[i],target)
            if finding:
                return True

    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")


#______________________________________________________________________________________________________________________

#Optimal 
# Time Complexity: O(N+M), where N = given row number, M = given column number.
# Reason: We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). 
# So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

# Space Complexity: O(1) as we are not using any extra space.

def searchElement(matrix,target):
    n = len(matrix)
    m = len(matrix[0])
    row = 0
    col = m - 1
    while row < n and m >= 0:
            if matrix[row][col] == target:
               return True
            elif matrix[row][col] < target:
                 row += 1
            else:
                 col -= 1
    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

result = searchElement(matrix, 8)
print("true" if result else "false")