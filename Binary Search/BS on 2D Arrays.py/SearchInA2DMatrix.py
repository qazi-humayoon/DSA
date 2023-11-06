#Brute Force
# Time Complexity: O(N X M), where N = given row number, M = given column number.
# Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

# Space Complexity: O(1) as we are not using any extra space.
def another(mat,target):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
            for j in range(n):
                if mat[i][j] == target:       
                    return True

    return False

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
target = 8
res = another(mat,target)
print(res)

#_____________________________________________________________________________________________________________________

#Better Solution 
# Time Complexity: O(N + logM), where N = given row number, M = given column number.
# Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are 
# not applying binary search rather we are only applying it once for a particular row. That is why the
# time complexity is O(N + logM) instead of O(N*logM).

# Space Complexity: O(1) as we are not using any extra space.

def binarysearch(mat,n,target):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if mat[mid] == target:
            ans = mat[mid]
            return ans
        elif target > mat[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return ans

def another(mat,target):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        if mat[i][0] <= target and target <= mat[i][n - 1]: #this line is added to save TC it checks if ele is present
            finding = binarysearch(mat[i],n,target)         #at beginning and end of the array
            if finding == target:
                return True

    return False

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
target = 8
res = another(mat,target)
print(res)


#_____________________________________________________________________________________________________________________

#Optimal ``
# Time Complexity: O(log(NxM)), where N = given row number, M = given column number.
# Reason: We are applying binary search on the imaginary 1D array of size NxM.

# Space Complexity: O(1) as we are not using any extra space.\

def another(mat,target):
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high)// 2
        row = mid // m
        col = mid % m
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
target = 8
res = another(mat,target)
print(res)
