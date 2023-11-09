#Optimal 
# Time Complexity : O(LogN * M)
# Space Complexity : O(1)

def findMaxIndex(mat, n, m, col):
    maxValue = -1
    index = -1

    for i in range(n):
        if mat[i][col] > maxValue:
            maxValue = mat[i][col]
            index = i

    return index

def findPeakGrid(mat):
    n = len(mat)
    m = len(mat[0])
    low, high = 0, m - 1

    while low <= high:
        mid = (low + high) // 2
        maxRowIndex = findMaxIndex(mat, n, m, mid)

        left = mat[maxRowIndex][mid - 1] if mid - 1 >= 0 else -1
        right = mat[maxRowIndex][mid + 1] if mid + 1 < m else -1

        if mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid] > right:
            return (maxRowIndex, mid)
        elif mat[maxRowIndex][mid] < left:
            high = mid - 1
        else:
            low = mid + 1

    return (-1, -1)
arr = [[10,20,15],[21,30,14],[7,16,32]]
ans = findPeakGrid(arr)
print("The peak is at index:", ans)