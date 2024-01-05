def solution(s, k):
    # Get the length of the input string
    n = len(s)
    
    # Dictionary to store the frequency of each character in the current window
    freq = {}

    # Left pointer of the window
    left = 0

    # Variable to store the result (maximum length of substring with at most k distinct characters)
    res = 0

    # Variable to store the maximum frequency of a character in the current window
    maxstr = 0

    # Iterate through the string using a sliding window approach
    for right in range(n):
        # Update the frequency of the current character in the window
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Update the maximum frequency of any character in the current window
        maxstr = max(maxstr, freq[s[right]])

        # Check if the condition (right-left+1) - maxstr > k is violated
        while (right - left + 1) - maxstr > k:
            # Decrease the frequency of the leftmost character in the window
            freq[s[left]] -= 1

            # Move the left pointer to the right to shrink the window
            left += 1

        # Update the result with the maximum length of the current valid substring
        res = max(res, (right - left + 1))

    # Return the final result
    return res

# Example usage:
s = "AABABBA"
k = 1
ans = solution(s, k)
print(ans)
