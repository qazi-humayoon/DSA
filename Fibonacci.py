# n-th Fibonacci number Using Dynamic Programming with Space Optimization
# Time Complexity: O(N)
# Auxiliary Space: O(1)
def Fibonacci(num):
    a = 1
    b = 1
    c = 0
    if num == 1 or num == 2:
        return 1
    for i in range(2,num):
        c = a + b
        a = b
        b = c
    return b
n = int(input())
f = Fibonacci(n)
print(f)

# a = 1
# b = 1
# c = 0
# num = int(input())
# if num == 1 or num == 2:
#     print("1")
# for i in range(2,num):
#     c = a + b
#     a = b
#     b = c
#     print(b)


