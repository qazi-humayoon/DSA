# Time Complexity: O(m x n) { Since all the elements are being traversed once and there are total n x m elements ( m elements in each row and total n rows) so the time complexity will be O(n x m)}.

# Space Complexity: O(n) { Extra Space used for storing traversal in the ans array }.

def printSpiral(mat):
    # Define ans array to store the result.
    ans = []
 
    n = len(mat) # no. of rows
    m = len(mat[0]) # no. of columns
  
    # Initialize the pointers reqd for traversal.
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    # Loop until all elements are not traversed.
    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            ans.append(mat[top][i])

        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])

        right -= 1

        # For moving right to left.
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])

            bottom -= 1

        # For moving bottom to top.
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])

            left += 1

    return ans

#Matrix initialization.
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
                     
ans = printSpiral(mat)

print(ans)