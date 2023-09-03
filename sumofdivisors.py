# n = 10
# count = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += j
# print(count)
import math
n= 10
count = 0
for i in range(1,math.sqrt(n)+1):
    for j in range(1,math.sqrt(i)+1):
        if i % j == 0:
            count += j
            count //= 10
print(count)

    

