#Brute Force
#Tc :- O(N^2)
#Sc :- O(1)
# def misrep(a):
#     n = len(a)  # size of the array
#     repeating, missing = -1, -1

#     # Find the repeating and missing number:
#     for i in range(1, n+1):
#         # Count the occurrences:
#         cnt = 0
#         for j in range(n):
#             if a[j] == i:
#                 cnt += 1

#         if cnt == 2:
#             repeating = i
#         elif cnt == 0:
#             missing = i

#         if repeating != -1 and missing != -1:
#             break

#     return [repeating, missing]

# a = [3, 1, 2, 5, 4, 6, 7, 5]
# res = misrep(a)
# print(res)

#__________- --------- _________________________- -------------------_____________________-----------------_______________________

#Better
#Tc :- O(2N)
#sc :-O(N)
def misrep(a):
    n = len(a) # size of the array
    hash = [0] * (n + 1) # hash array

    #update the hash array:
    for i in range(n):
        hash[a[i]] += 1

    #Find the repeating and missing number:
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

    

a = [3, 1, 2, 5, 4, 6, 7, 5]
res = misrep(a)
print(res)

#__________- --------- _________________________- -------------------_____________________-----------------_______________________

#Optimal
# Time Complexity: O(N), where N = the size of the given array.
# Reason: We are using only one loop running for N times. So, the time complexity will be O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.
def misrep(a):
    n = len(a)  # size of the array

    # Find Sn and S2n:
    SN = (n * (n + 1)) // 2
    S2N = (n * (n + 1) * (2 * n + 1)) // 6

    # Calculate S and S2:
    S, S2 = 0, 0
    for i in range(n):
        S += a[i]
        S2 += a[i] * a[i]

    # S-Sn = X-Y:
    val1 = S - SN

    # S2-S2n = X^2-Y^2:
    val2 = S2 - S2N

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]

a = [3, 1, 2, 5, 4, 6, 7, 5]
res = misrep(a)
print(res)

