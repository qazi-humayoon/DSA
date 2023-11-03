
#Same code as allocate books


#Brute Force
# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements,
# max(arr[]) = maximum of all array elements.
# Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible numbers of pages. Inside the loop, we are
# calling the countStudents() function for each number. Now, inside the countStudents() function, we are using a loop that
#     runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters


def findLargestMinDistance(boards, k):
    low = max(boards)
    high = sum(boards)

    for time in range(low, high+1):
        if countPainters(boards, time) <= k:
            return time
    return low


boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)



#_________________________________________________________________________________________________________________________

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, 
# max(arr[]) = maximum of all array elements.
# Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function
# for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

#Optimal binary

def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters

def findLargestMinDistance(boards, k):
    low = max(boards)
    high = sum(boards)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        painters = countPainters(boards, mid)
        if painters > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)

