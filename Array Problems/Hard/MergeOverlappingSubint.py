#Brute Force
# Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.
# Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j.
# But while using loop i, we skip all the intervals that are merged with loop j. So, we can conclude that every interval
# is roughly visited twice(roughly, once for checking or skipping and once for merging). So, the time complexity will be
#  2*N instead of N2.

# Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array,
# we are not using any extra space.

# def mergeover(arr):
#     n = len(arr)
#     arr.sort()
#     ans = []

#     for i in range(n): # select an interval:
#         start, end = arr[i][0], arr[i][1]

#         # Skip all the merged intervals:
#         if ans and end <= ans[-1][1]:
#             continue

#         # check the rest of the intervals:
#         for j in range(i + 1, n):
#             if arr[j][0] <= end:
#                 end = max(end, arr[j][1])
#             else:
#                 break
#         ans.append([start, end])
#     return ans


# arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
# ans = mergeover(arr)
# print("The merged intervals are:")
# for it in ans:
#     print(f"[{it[0]}, {it[1]}]", end=" ")
# print()

#_______________- ___________________ - ____________________________---__________________________----______________________


def mergeover(arr):
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans

arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = mergeover(arr)
print("The merged intervals are:")
for it in ans:
    print(f"[{it[0]}, {it[1]}]", end=" ")
print()