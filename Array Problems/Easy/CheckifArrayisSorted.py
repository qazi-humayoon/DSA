def is_sorted():
    for i in range(1,n):
        if a[i] < a[i - 1]:
            return False
    return True

a = [4,5,4,4,4]
n = len(a)
print(is_sorted())

#Time Complexity is O(N) and Space Complexity is O(1)


