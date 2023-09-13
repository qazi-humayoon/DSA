
def f(a,n):
    for i in range(n - 1):
        mini = i
        for j in range(i,n):
        
            if a[j] < a[mini]:
                mini = j
        temp = a[mini]
        a[mini] = a[i]
        a[i] = temp
    return a
    
a = [3,2,6,3,7]
n = 6
res = f(a,n)
print(res)

