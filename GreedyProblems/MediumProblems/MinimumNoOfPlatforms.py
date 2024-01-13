# Time Complexity: O(n^2)  (due to two nested loops).

# Space Complexity: O(1)  (no extra space used).

# def countPlatforms(n, arr, dep):
#     ans = 1  # final value
#     for i in range(n):
#         count = 1  # count of overlapping interval of only this iteration
#         for j in range(i+1, n):
#             if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i]):
#                 count += 1
#         ans = max(ans, count)  # updating the value
#     return ans



# if __name__ == "__main__":
#     arr = [900, 945, 955, 1100, 1500, 1800]
#     dep = [920, 1200, 1130, 1150, 1900, 2000]
#     n = len(dep)
#     print("Minimum number of Platforms required", countPlatforms(n, arr, dep))

#_____________________________________________________________________________________________________
    
#Optimal Sorting

# Time Complexity: O(nlogn) Sorting takes O(nlogn) and traversal of arrays takes O(n) so overall time complexity is O(nlogn).

# Space complexity: O(1)  (No extra space used).

def countPlatforms(n,arr,dep):
    arr.sort()
    dep.sort()
    ans = 1
    count = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            count += 1
            ans = max(ans,count)
            i += 1

        else:
            count -= 1
            j += 1
    return ans


arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(dep)
print("Minimum number of Platforms required", countPlatforms(n, arr, dep))