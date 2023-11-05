#Brute force
# Time Complexity: O(n X m), where n = given row number, m = given column number.
# Reason: We are using nested loops running for n and m times respectively.

# Space Complexity: O(1) as we are not using any extra space.
def rowWithMax1s(matrix,n,m):
    cnt_max = -1
    index = -1
    for i in range(n):
        cnt = 0
        for j in range(m):
            cnt += matrix[i][j]
        if cnt > cnt_max:
            cnt_max = cnt
            index = i
    return index

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    n = 3
    m = 3
    print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))

#____________________________________________________________________________________________________________________

#Optimal Solution
# Time Complexity: O(n X logm), where n = given row number, m = given column number.
# Reason: We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

# Space Complexity: O(1) as we are not using any extra space.
def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix =[[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 1
m = 2
print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))
