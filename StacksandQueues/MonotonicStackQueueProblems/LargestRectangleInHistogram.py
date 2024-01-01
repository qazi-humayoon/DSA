# Brute
def largest_area(arr, n):
    max_area = 0
    for i in range(n):
        min_height = float('inf')
        for j in range(i, n):
            min_height = min(min_height, arr[j])
            max_area = max(max_area, min_height * (j - i + 1))
    return max_area

if __name__ == "__main__":
    arr = [2, 1, 5, 6, 2, 3, 1]
    n = 7
    print("The largest area in the histogram is", largest_area(arr, n))

#_______________________________________________________________________________________________________
    
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        leftsmall = [0] * n
        rightsmall = [0] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            leftsmall[i] = 0 if not stack else stack[-1] + 1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            rightsmall[i] = n - 1 if not stack else stack[-1] - 1
            stack.append(i)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (rightsmall[i] - leftsmall[i] + 1))

        return max_area

if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3, 1]
    obj = Solution()
    print("The largest area in the histogram is", obj.largestRectangleArea(heights))

