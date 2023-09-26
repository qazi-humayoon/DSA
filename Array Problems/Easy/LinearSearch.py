
# n = len(arr)
# for i in range(n):
#     if arr[i] == num:
#         print(i)
#     else:
#         print("0")

def func(arr,num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1
    
arr = [6,7,8,4,1]
num = 4
res = func(arr,num)
print(res)
