#Intersection of two sorted arrays 
#Time Complexity is O(n1 + n2) where max i runs at n1 times and j runs at n2 times
#Space Complexity is O(m + n) it stores common elements from arr1 and arr2. it is used to return the solution not to
# solve the problem. Thus we can also say that the Space Complexity is o(1)
arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]
i = 0
j = 0
intersect = []
while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
        intersect.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
print(intersect)