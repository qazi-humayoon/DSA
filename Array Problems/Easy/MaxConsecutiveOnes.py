#Runtime Error
# count1 = 0
# count2 = 0
# n = len(a)
# i = 0
# j = (n-1)
# for k in range(n):
#     if a[k] == 1:
#         count1 += 1
#     i += 1

#     if a[j] == 1:
#         count2 += 1
#     j -= 1

#     if j <= i:
#         c = max(count1,count2)
#         print(c)
#         break

#__________________________________________________________________________________________________________________
#time complexity O(n)
#Working approach
def counting(a,n):
    maxi = 0
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0
    return maxi
a = [1,1,0,1,1,1]
n = len(a)
res = counting(a,n)
print(res)