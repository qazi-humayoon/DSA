#Brute Force O(N

n = 28
ans = 1
for i in range(n):
    if (i * i) <= n:
        ans = i
    else:
        break
print(ans)

#______________________________________________________________________________________________________________________________

#Optimal 1 

import math
n = 28
ans = int(math.sqrt(n))
print(ans)

#______________________________________________________________________________________________________________________________

#Optimal 2 - BINARY SEARCH O(LogN)
n = 28
low = 1
high = n
while low <= high:
    mid = (low + high) // 2
    val = mid * mid
    if val <= n:
        low = mid + 1
    
    else:
        high = mid - 1
print(high)
