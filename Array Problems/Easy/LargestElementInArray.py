#Brute Force
# a = [4, 7, 8, 6, 7, 6 ]
# a.sort()
# return a[-1] 
# Time Complexity is O(nlogn) with Space Complexity is O(1)

# return max(a)
# Can be done also using the return max function in python


#This is the optimal solution for this problem
a = [4, 7, 8, 6, 7, 6 ]
count = a[0]
n = len(a)
for i in range(n):
    if a[i] > count:
        count = a[i]
print(count)
# Time Complexity is O(N) with Space Complexity is O(1)



 