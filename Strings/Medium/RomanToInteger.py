#Optimal 
# TC: O(N) Due to for loop being used which runs for O(N) in worst case
# SC: O(1) Because the size of the dictionary is fixed so that is the reaons for this TC

def roman(s):
    m = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
    ans = 0
    for i in range(len(s)):
# This part checks if the current Roman numeral represented by s[i] has a smaller
# value than the next Roman numeral represented by s[i+1]. In Roman numerals, if a smaller numeral
# appears before a larger numeral, you subtract its value. For example, in "IV," the 'I' (1) is 
# before 'V' (5), so you subtract 1 from 5, resulting in 4. The condition checks if this subtraction
# should occur.
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
        
    return ans

s = "III"
res = roman(s)
print(res)