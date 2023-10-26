#My logic
# a = [1,2,4,7]
# m = 6
# n = len(a)
# low = 0
# high = n - 1
# ans = n
# while low <= high:
#     mid = (low + high) // 2
#     if a[mid] >= m:
#         ans = mid
#         high = mid - 1
       
#     elif a[mid] == m:
#         ans = mid
#     else:
#         low  = mid + 1
# a.insert(ans,m)   
# print(ans)

#__________________-------------------___________________----------------------_________________---------------________-

#Striver logic of applying the lower bound

def insertpos(arr,n,m):
    low,high = 0,n-1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if a[mid] >= m:
            #look for smaller index on the left
            ans = mid
            high = mid - 1
        else:
            low = mid + 1 #look on the right
    return ans

a = [1,2,4,7]
m = 6
n = len(a)
res = insertpos(a,n,m)
print(res)
