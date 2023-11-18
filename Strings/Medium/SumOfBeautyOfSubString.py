def beautysum(s):
    count = 0

    for i in range(len(s)):
        freq = [0] * 26

        for j in range(i, len(s)): # if s[j] is the character 'c', then ord(s[j]) would be the ASCII value of 'c',
            freq[ord(s[j]) - ord('a')] += 1 # which is 99. Similarly, ord('a') is the ASCII value of 'a', which is 97.
            mx = float('-inf')               #So, ord(s[j]) - ord('a') would be 99 - 97 = 2. 
            mi = float('inf')

            for k in range(26):
                if freq[k] != 0:
                    mx = max(mx, freq[k])
                    mi = min(mi, freq[k])

            count += mx - mi

    return count
        
s = "aabcb"
res = beautysum(s)
print(res)