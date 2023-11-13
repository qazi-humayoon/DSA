'''
   Time Complexity  : O(n*m)
   Space Complexity : O(m*Log(n))

   where 'n' is the size of 'arr' and 'm' is the maximum length of 'arr[i]'.
'''
from typing import List

# Function to find the common prefix of two strings.
def comPrefix(out1: str, out2: str) -> str:
    out = ""
    n1, n2 = len(out1), len(out2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if out1[i] != out2[j]:
            break
        out += out1[i]
        i += 1
        j += 1
    return out


def commonPrefix(arr: List[str], n: int) -> str:
    prefix = arr[0]

    # Iterating over all the strings and finding the common prefix.
    for i in range(1, len(arr)):
        prefix = comPrefix(prefix, arr[i])

    # Base case of no common prefix.
    if prefix == "":
        return "-1"

    return prefix

arr = ["geeksforgeeks", "geeks", "geek","geezer"]
n = len(arr)
res = commonPrefix(arr,n)
print(res)