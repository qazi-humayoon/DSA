




def findfloor(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]<= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans

def findceil(arr,n,x):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans



def findfloorceil(arr,n,x):
    f = findfloor(arr,n,x)
    c = findceil(arr,n,x)
    return (f,c)

arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = findfloorceil(arr,n,x)
print("The floor and ceil is :",ans)