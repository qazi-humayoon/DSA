#Brute Force time complexity O(n) + O(x) + (n-x) space complexity = O(2N)
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)
# temp = []
# for i in range(n):
#     if arr[i] != 0:
#         temp.append(arr[i])
# m = len(temp)
# for i in range(m):
#     arr[i] = temp[i]
# for i in range(m,n):
#     arr[i] = 0
# print(arr)
# ____________________________________________________________________________________________________

#Optimal Approach time complexity O(n) space complexity = O(1)
j = - 1
for i in range(n):
    if arr[i] == 0:
        j = i
        break
if j == -1: #checks if there are no zeroes in the list
    print(arr)
for i in range(j + 1,n):
    if arr[i] != 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j += 1
print(arr)
