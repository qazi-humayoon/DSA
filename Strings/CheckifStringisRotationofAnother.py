def reversing(s,goal):
    if len(s) != len(goal):
            return False
# The specific use of s + s in this context serves a purpose in checking if the string goal can be obtained by a circular
#  rotation of string s. By concatenating s with itself, the resulting string contains all possible rotations of the original
#  string within it.

# For instance, if s = "abcd", s + s would result in "abcdabcd". This concatenated string contains all possible rotations
#  of the original string s. Therefore, if goal can be formed by rearranging the characters of s, it will be a substring
#  within s + s.

# This circular property allows the function to identify if goal can be achieved by rearranging the characters in s.
#  It's a way to detect if goal is a possible outcome of rotating the characters in s.
    ans = s + s
    if goal in ans:
            return True
    else:
            return False
# With s = "abfyg", if you concatenate s + s, you get "abfygabfyg".When you check if goal is within s + s:
# In this case, "gabfy" is found within "abfygabfyg", which means that goal can indeed be achieved by reversing
#  the characters in s. The function would return True.
s = "abfyg"
goal = "gabfy"
ans = reversing(s,goal)
print(ans)

#_______________________________________________________________________________________________________
# Another Brute Method

"""
    Time Complexity: O(N^2)
    Space Complexity: O(1)

    where 'N' denotes the lengths of both the strings 'P' and 'Q'.
"""

# def isCyclicRotation(p: str, q: str) -> int:
#     # Getting the size of the strings.
#     n = len(p)

#     # Finding each rotation one by one.
#     for j in range(n):
#         # Setting the flag variable.
#         isRotationPossible = 1

#         # Iterating through each rotation and checking character by character.
#         for i in range(n):
#             if p[(i + j) % n] != q[i]:
#                 isRotationPossible = 0
#                 break

#         # Checking if the flag is set to 1.
#         if isRotationPossible:
#             return 1

#     # If we were unable to cyclically rotate string 'p' right to form string 'q', then we will return 0.
#     return 0

# #____________________________________________________________________________________________________________________

# #Optimal using knuth morris pratt algorithm

# """
#     Time Complexity: O(N)
#     Space Complexity: O(N)

#     Where 'N' denotes the length of both strings 'P' and 'Q'.
# """

# def isSubstring(a: str, b: str) -> int:
#     # Finding the length of both strings.
#     m = len(a)
#     n = len(b)

#     # Defining and initializing the pointer variables to preprocess the string 'a'.
#     i = 1
#     j = 0

#     # Defining the lps array.
#     lps = [0] * m

#     while i < m:

#         # If the ith index of string 'a' matches with its jth index, then store the value 'j'+1 at lps[i] and increment both 'i' and 'j'.
#         if a[i] == a[j]:
#             lps[i] = j + 1
#             i += 1
#             j += 1
#         # If the ith index of 'a' does not match with its jth index of 'a' and 'j' > 0, then 'j' redirects to lps[j-1].
#         elif j > 0:
#             j = lps[j - 1]
#         # If none of the above condition matches then make lps[i] as 0 and increment 'i'.
#         else:
#             lps[i] = 0
#             i += 1

#     i = 0
#     j = 0

#     # Iterating through both the strings to find a match.
#     while i < n and j < m:
#         # If the ith character of 'b' matches with the jth character of 'a', then increment both 'i' and 'j'.
#         if b[i] == a[j]:
#             i += 1
#             j += 1
#         # If the above characters do not match and 'j' > 0, then 'j' redirects to lps[j-1].
#         elif j > 0:
#             j = lps[j - 1]
#         # If none of the above mentioned condition matches, then increment 'i'.
#         else:
#             i += 1

#     # If 'j' is equal to 'm', then we will return 1 otherwise we will return 0.
#     if j == m:
#         return 1
#     else:
#         return 0

# def isCyclicRotation(p: str, q: str) -> int:
#     # Performing the concatenation of string 'p' with itself.
#     res = p + p

#     # Checking if the substring 'q' is present in the string 'res'.
#     return isSubstring(q, res)
