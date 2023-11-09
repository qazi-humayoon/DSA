#My Approach 
# mat = []
# for i in range(m):
#     for j in range(n):
#         mat.append(matrix[i][j])
# mat.sort()
# low = 0                             # Time Complexity : O(n x m) + n x m x Log(n x m)
# high = len(mat) - 1                 # Space Complexity : O(1)    
# mid = (low + high) // 2  
# return mat[mid] # or use return mat[m * n] // 2 as multiply will give us odd like 3 * 5 = 15 -> 15//2 -> 0-14== 7 mid 

#_____________________________________________________________________________________________________________

# Optimal
# TC O(Log(10^9) x n x LogM)

def count_smaller_than_mid(row, mid):
    l = 0
    h = len(row) - 1
    while l <= h:
        md = (l + h) // 2
        if row[md] <= mid:
            l = md + 1
        else:
            h = md - 1
    return l

def find_median(A):
    low = 1
    high = 10**9
    n = len(A)
    m = len(A[0])
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        for i in range(n):
            cnt += count_smaller_than_mid(A[i], mid)
        if cnt <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low

if __name__ == "__main__":
    arr = [
        [1, 3, 8],
        [2, 3, 4],
        [1, 2, 5]
    ]
    print("The median of the row-wise sorted matrix is:", find_median(arr))
