# TC O(NLogN)
# Sc O(N)

def max_meetings(N, start, end):
    # Combine the start and end times into a list of tuples
    meetings = [(start[i], end[i], i+1) for i in range(N)]
    
    # Sort the meetings based on their end times
    meetings.sort(key=lambda x: x[1])
    
    # Initialize variables
    result = []
    end_time = 0
    
    # Iterate through sorted meetings and select the ones that don't overlap
    for meeting in meetings:
        if meeting[0] > end_time:
            result.append(meeting[2])
            end_time = meeting[1]
    
    return result

# Example usage
N = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]

output = max_meetings(N, start, end)
print(output)
