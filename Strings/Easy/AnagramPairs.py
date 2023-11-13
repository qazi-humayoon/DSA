#Brute force
''' 
    Time complexity: O( (N*log(N)) + (M*log(M)) )
    Space complexity: O(1)

    where N and M are the length of two strings.
'''
def checking(s,t):
        sorted_s = sorted(s)
        sorted_t=  sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False
        
            

s = "anagram"
t = "nagaram"
res = checking(s,t)
print(res)

#_______________________________________________________________________________________________________________

#Optimal
# Tc O(N + M + O)
# SC O(LogN) 

def checking(s,t):

    count = {}
        
    # Count the frequency of characters in string s
    for x in s:
        count[x] = count.get(x,0) + 1 
        
    # Decrement the frequency of characters in string t
    for x in t:
        count[x] = count.get(x,0) - 1 
        
    # Check if any character has non-zero frequency
    for val in count.values():
        if val != 0:
            return False
        
    return True

s = "anagram"
t = "nagaram"
res = checking(s,t)
print(res)