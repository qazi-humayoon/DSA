# Time Complexity: O(c), where c = given column number.
# Reason: We are running a loop for r times, where r is c-1.

# Space Complexity: O(1) as we are not using any extra space.

# import math

# def nCr(n, r):
#     res = 1

#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)

#     return res

# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element

# if __name__ == '__main__':
#     r = 5 # row number
#     c = 3 # col number
#     element = pascalTriangle(r, c)
#     print(f"The element at position (r,c) is: {element}")

#_______________________________________________________________________________________________________________________
    
# Time Complexity: O(n*r), where n is the given row number, and r is the column index which can vary from 0 to n-1.
# Reason: We are calculating the element for each column. Now, there are total n columns, and for each column, the calculation of the element takes O(r) time where r is the column index.

# Space Complexity: O(1) as we are not using any extra space.

# import math

# def nCr(n, r):
#     res = 1
#     # calculating nCr:
#     for i in range(r):
#         res = res * (n - i)
#         res = res // (i + 1)
#     return res

# def pascalTriangle(n):
#     # printing the entire row n:
#     for c in range(1, n+1):
#         print(nCr(n-1, c-1), end=" ")
#     print()

# if __name__ == "__main__":
#     n = 5
#     pascalTriangle(n)
    
#_________________________________________________________________________________________________________________________        

# Time Complexity: O(n2), where n = number of rows(given).
# Reason: We are generating a row for each single row. The number of rows is n. And generating an entire row takes O(n) time complexity.

# Space Complexity: In this case, we are only using space to store the answer. That is why space complexity can still be considered as O(1).

from typing import *

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)

def pascalTriangle(n):
    ans = []

    #Store the entire pascal's triangle:
    for row in range(1, n+1):
        tempLst = [] # temporary list3+Q
        for col in range(1, row+1):
            tempLst.append(nCr(row - 1, col - 1))
        ans.append(tempLst)
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()
