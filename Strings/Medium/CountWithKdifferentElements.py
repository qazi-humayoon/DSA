def counting(s,k):
    n = len(s)
    count = 0

    for i in range(n):
        distinct_chars = 0
        char_count = [0] * 26  # Reset character count for each starting position

        for j in range(i, n):
            if char_count[ord(s[j]) - ord('a')] == 0: #This condition checks whether the current character has not 
                distinct_chars += 1                   #been encountered before in the current substring.

            char_count[ord(s[j]) - ord('a')] += 1

            if distinct_chars == k:
                count += 1
            elif distinct_chars > k:
                break

    return count

s = "aba"
k = 2
res = counting(s,k)
print(res)