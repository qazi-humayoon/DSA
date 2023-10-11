# Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.

# Space Complexity: O(N*N) to copy it into some other matrix.

def rotate(matrix):
    n = len(matrix)
    rotated = []
    for _ in range(n):
        rotated.append([0] * n)
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated = rotate(arr)
    print("Rotated Image")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()

#_____________________________________________________________________________________________________________

# Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

# Space Complexity: O(1).

# def rotate(matrix):
#     n = len(matrix)
#     # transposing the matrix
#     for i in range(n):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     # reversing each row of the matrix
#     for i in range(n):
#         matrix[i].reverse()




# if __name__ == "__main__":
#     arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     rotate(arr)
#     print("Rotated Image")
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             print(arr[i][j], end=" ")
#         print()
