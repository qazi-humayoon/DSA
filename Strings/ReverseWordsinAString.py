#My approach

# c = str.split()
# reversed_str = ' '.join(c[::-1])
# return reversed_str

#_________________________________________________________________________________________________________________

#Brute Force
"""
    Time Complexity: O(N * 2)
    Space Complexity: O(N)

    Where N is the length of the string.
"""

def reverseString(str: str) -> str:
    n = len(str)
    ans = ""
    i = 0

    while i < n:
        j = i

        # Skip multiple spaces.
        while j < n and str[j] == ' ':
            j += 1

        currentWord = ""

        # Get the current word.
        while j < n and str[j] != ' ':
            currentWord += str[j]
            j += 1

        # Add current word in the ans with a space.
        if len(currentWord) != 0:
            ans = currentWord + " " + ans

        i = j + 1

    if len(ans) == 0:
        return ans

    # Remove the last space.
    return ans[:-1]
str = "the sky is blue"
ans = reverseString(str)
print(ans)

#________________________________________________________________________________________________

#Optimal
'''
    Time Complexity  = O(N)
    Space Complexity = O(N)

    Where N is the length of the string.
'''

def reverseString(str: str) -> str:
    
    # if the string is " " then return "".
    if(str == "" or str == " "):
        return ""
    ans = ''

    start = len(str) - 1

    while(start >= 0):
        
        # Skip multiple spaces.
        if(str[start] == ' '):
            start-=1
        else:
            
            # Add space between words.
            if(len(ans) > 0):
                ans += (' ')

            j = start

            while(j >= 0 and str[j] != ' '):
                j-=1

            # add current word to ans.
            ans +=  (str[j+1: j+1+start-j])
            start = j

    return ans

str = "the sky is blue"
ans = reverseString(str)
print(ans)