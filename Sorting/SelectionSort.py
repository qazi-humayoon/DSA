#Time Complexity is O(N^2) For Best,Worst and Average.
a = [13,46,24,52,20,9]
n = 6
for i in range(n - 1): # taking n - 1 because the last element will always be sorted at the end of the program.then we will be comparing n = 52 with whole list which is simply waste
    mini = i
    for j in range(i,n):
        if a[mini] > a[j]:
            mini = j #using this mini to check the condition and then with the help of this swap elements
    temp = a[mini]
    a[mini] = a[i]
    a[i] = temp
print(a) 

# def f(a,n):
#     for i in range(n - 1):
#         mini = i
#         for j in range(i,n):
        
#             if a[mini] > a[j]:
#                 mini = j
#         temp = a[mini]
#         a[mini] = a[i]
#         a[i] = temp
#     return a
    
# a = [3,2,6,3,7,6]
# n = 6
# res = f(a,n)
# print(res)

