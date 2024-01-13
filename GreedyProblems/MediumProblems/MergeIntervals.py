# Same Array problem in Hard Check in Arrays merge sub-array intervals


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# n = len(intervals)
# intervals.sort()
# ans = []
# for i in range(n):
#     if not ans or intervals[i][0] > ans[-1][1]:
#         ans.append(intervals[i])
#     else:
#         ans[-1][1] = max(ans[-1][1],intervals[i][1])
# return ans
