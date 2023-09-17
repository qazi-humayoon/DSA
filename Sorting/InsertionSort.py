#Time Complexity is O(N^2) for worst and average case
#For the best case the time complexity can be O(N) i.e if the array is already sorted and while loop won't run.
n = 6
a = [3,4,5,99,33,11]
for i in range(n):
    j = i
    while j > 0 and a[j - 1] > a[j]: #we take the no to extreme left so if we have no smaller we will try to take it to extreme left
        temp = a[j - 1] # for eg 11 we will compare it with 99 with i = 5 and j = 5 and then compare it with 33 with j = 4(j -= 1) then condition not satisfied break out of loop
        a[j - 1] = a[j]
        a[j] = temp
        j -= 1
print(a)
