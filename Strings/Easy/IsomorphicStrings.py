def checking(s,t):
    map1 = []
    map2 = []
    for idx in s:
        map1.append(s.index(idx))
    for idx in t:
        map2.append(t.index(idx))
    if map1 == map2:
        return True
    return False

s = "egg"
t = "add"
res = checking(s,t)
print(res)

#_____________________________________________________________________________________________________

'''

	Time complexity: O(N^2)
	Space complexity: O(1)

	where N is length of the string.

'''

def areIsomorphic(str1: str, str2: str) -> bool:

    n = len(str1)
    m = len(str2)

    # Length of both strings must be same for one to one correspondence.
    if (m != n):
      return False

    for i in range(n):

        # Character 'first' of str1 is mapped to character 'second' of str2.
        first = str1[i]
        second = str2[i]

        for j in range(m):

            # 'first' in str1 should be mapped to 'second' in whole string.
            if(str1[j] == first and str2[j] != second):
                return False

            # 'second' in str2 should be mapped to 'first.
            if(str2[j] == second and str1[j] != first):
                return False
                
    return True
str1 = "egg"
str2 = "add"
res = areIsomorphic(str1,str2)
print(res)


#_______________________________________________________________________________________________________

'''
	Time complexity: O(N)
	Space complexity: O(Number of different characters)

	where N is the length of the string.

'''

# def areIsomorphic(str1: str, str2: str) -> bool:
#     m = len(str1)
#     n = len(str2)

#     # Length of both strings must be same for one to one correspondence.
#     if m != n:
#         return False

#     # To mark visited characters in str2.
#     marked = [False] * 26

#     # To store mapping of every character from str1 to that of str2. Initialize all entries of map as -1.
#     hash_map = [-1] * 26

#     # Process all characters one by one.
#     for i in range(n):
#         # If current character of str1 is seen first time in it.
#         if hash_map[ord(str1[i]) - ord('a')] == -1:
#             # If current character of str2 is already seen, one to one mapping not possible.
#             if marked[ord(str2[i]) - ord('a')]:
#                 return False
#             # Mark current character of str2 as visited.
#             marked[ord(str2[i]) - ord('a')] = True

#             # Store mapping of current characters.
#             hash_map[ord(str1[i]) - ord('a')] = str2[i]

#         # If this is not the first appearance of the current character in str1
#         # then check if the previous appearance mapped to the same character of str2.
#         elif hash_map[ord(str1[i]) - ord('a')] != str2[i]:
#             return False

#     return True
