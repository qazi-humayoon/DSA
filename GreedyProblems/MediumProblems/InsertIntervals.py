# This is a similar question to question #56: Merge Intervals, except that the array of given intervals is already sorted by starti and we need to insert a new interval in the correct spot. In both questions, there must be no overlaps and we'll have to merge intervals as necessary.

# The first while loop will simply append each interval to our result as long as intervals[i][1] < newInterval[0]. In other words, if an interval ends before newInterval starts, then it must be located entirely before newInterval, so we can just add that inteval to result.

# Once that condition becomes false, we know that we may have hit our first overlap. So in the second loop, we'll merge intervals as long as intervals[i][0] <= newInterval[1]. In other words, since we already know from the first loop that intervals[i] ends after newInterval starts, if intervals[i] starts before newInterval ends, then the two intervals must overlap.

# Once that condition becomes false, we know that all other intervals start after newInterval ends. So we can safely append the rest of the intervals to result and return result.

# Time Complexity (tc): O(N)
# Space Complexity (sc): O(N)

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         result = []
#         i = 0

#         while i < len(intervals) and intervals[i][1] < newInterval[0]:
#             result.append(intervals[i])
#             i += 1

#         while i < len(intervals) and intervals[i][0] <= newInterval[1]:
#             newInterval[0] = min(newInterval[0], intervals[i][0])
#             newInterval[1] = max(newInterval[1], intervals[i][1])
#             i += 1

#         result.append(newInterval)

#         while i < len(intervals):
#             result.append(intervals[i])
#             i += 1

#         return result