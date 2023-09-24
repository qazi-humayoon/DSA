a = [1,2,3,4,5]
n = len(a)
temp = a[0]
for i in range(1,n):
    a[i - 1] = a[i]
a[n - 1] = temp
print(a)
# temp = []
# temp = a[1:]
# a[n - 1] = a[0]
# a[:-1] = temp

# Time Complexity is O(N) with Space Complexity is O(1)