a = [1,-1,0,0,1]
n = len(a)
maxi = 0
target = 0
for i in range(n):
    for j in range(i,n):
        summ = 0
        for k in range(i,j+1):
            summ += a[k]
        if summ == target:
            maxi = max(maxi,j-i+1)
print(maxi)