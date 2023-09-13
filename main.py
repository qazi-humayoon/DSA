#selection sort
# n = 6
# a = [3,2,6,1,5,4]
# for i in range(n):
#     mini = i
#     for j in range(i,n):
#         if a[mini] > a[j]:
#             mini = j
#     temp = a[mini]
#     a[mini] = a[i]
#     a[i] = temp
# print(a)

#bubble sort
# n = 6
# a = [3,2,6,1,5,4]
# for i  in range(n-1,0,-1):
#     for j in range(i):
#         if a[j] > a[j + 1]:
#             temp = a[j + 1]
#             a[j + 1] = a[j]
#             a[j] = temp
# print(a)

#insertion sort
n = 6
a = [3,2,6,1,5,4]
for i in range(n):
    j = i
    while j > 0 and a[j - 1] > a[j]:
        temp = a[j - 1]
        a[j - 1] = a[j]
        a[j] = temp
        j -= 1
print(a)




