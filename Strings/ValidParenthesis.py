#LeetCode
# TC :- O(N)
def checking(s):
        cnt = 0
        ans = ""

        for ch in s:
            if ch == '(':
                cnt+=1
                if cnt > 1:
                    ans = ans + ch
            elif ch == ')':
                cnt-=1
                if cnt > 0:
                    ans = ans + ch
        return ans
s = "(()())(())"
ans = checking(s)
print(ans)

#_______________________________________________________________________________________________________________________

#Coding Ninjas
# TC :- O(N)
# SC :- O(1)
def checking(s):
    maxNestingDepth = 0
    currentDepth = 0

    # For each character 'c' in 's'.
    for c in s:
        if c == '(':
            #  Update 'currentDepth' and 'maxNestingDepth'.
            currentDepth += 1
            maxNestingDepth = max(maxNestingDepth, currentDepth)

        elif c == ')':
            # Decrement current depth.
            currentDepth -= 1

    return maxNestingDepth
s = "(3*(4*(5*(6))))"
res = checking(s)
print(res)