#Optimal 
# TC O(N)
# SC O(1)
def smaller(a):
    for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i] = a[i + 1]
            else:
                a[i] = -1
    a[len(a)- 1] = -1
    return a

a = [4, 7, 8, 2, 3, 1]
ans = smaller(a)
print(ans)
