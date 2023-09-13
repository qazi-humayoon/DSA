# def func(n):  #Without additonal parameters. Function calls itself with modified argument.
#     if n == 0:
#         return 0
#     return n + func(n-1) # Here the function return the value as : 0,1,3
# n = int(input("Enter the Number:- "))
# print(func(n))

#FunctionalRecursion to find the factorial of a number
# def func(n):
#     if n == 0:
#         return 1
#     return n * func(n-1)
# n = int(input())
# print(func(n))

def func(n):
    if n == 0:
        return 0
    return n**3 + func(n-1)
n = int(input("enter the no "))
print(func(n))

