# Time Complexity is O(N^2) for worst and average time complexity
# For the best case the time complexity can be linear i.e O(N) Considering the array is already sorted.
n = 6
a = [13,46,24,52,20,9]
for i in range(n-1,0,-1): #opp of selection sort as the last element with each iteration become sorted.
    for j in range(i):
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
print(a)

#This is the way to check the best time complexity with O(N) if the array is already sorted.
n = 6
a = [1,2,3,4,5,6]
for i in range(n-1,0,-1):
    didswap = 0
    for j in range(i):
        if a[j] > a[j + 1]:
            temp = a[j + 1]
            a[j + 1] = a[j]
            a[j] = temp
            didswap = 1
    if didswap == 0:
        break
print(a)
