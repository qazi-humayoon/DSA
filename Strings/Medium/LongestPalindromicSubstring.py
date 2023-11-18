#Check Neet Code for this problem
# Time Complexity: O(N^2)
# Space Complexity: O(1)

def palindrome(s):
    res = ""
    reslen = 0
    for i in range(len(s)):
        #odd length
        l,r = i,i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r+1]
                reslen = r - l + 1
            l -= 1
            r += 1
        #even length
        l,r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l:r+1]
                reslen = r - l + 1
            l -= 1
            r += 1
    return res

s = "babad"
res = palindrome(s)
print(res)
