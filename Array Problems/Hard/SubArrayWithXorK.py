#Brute Force
# Time Complexity: O(N3) approx., where N = size of the array.
# Reason: We are using three nested loops, each running approximately N times.

# Space Complexity: O(1) as we are not using any extra space.

# def subarraysWithXorK(a,k):
#     n = len(a)  # size of the given array.
#     cnt = 0

#     # Step 1: Generating subarrays:
#     for i in range(n):
#         for j in range(i, n):

#             # step 2: calculate XOR of all elements:
#             xorr = 0
#             for l in range(i, j + 1):
#                 xorr = xorr ^ a[l]

#             # step 3: check XOR and count:
#             if (xorr == k):
#                 cnt += 1

#     return cnt

# a = [4, 2, 2, 6, 4]
# k = 6
# ans = subarraysWithXorK(a, k)
# print("The number of subarrays with XOR k is:", ans) 

#_______________________________________________________________________________________________________________________________

#Better 
# Time Complexity: O(N2), where N = size of the array.
# Reason: We are using two nested loops here. As each of them is running for N times, the time complexity will be approximately O(N2).

# Space Complexity: O(1) as we are not using any extra space.

# def subarrayWithXork(a,k):
#     n = len(a)
#     cnt = 0
#     for i in range(n):
#         xorr = 0
#         for j in range(i,n):
#             xorr = xorr ^ a[j]
#             if xorr == k:
#                 cnt += 1
#     return cnt


# a = [4,2,2,6,4]
# k = 6
# ans = subarrayWithXork(a,k)
# (a,k)
# print("The number of subarray with XOR k is: ",ans)

#_______________________________________________________________________________________________________________________________

#Optimal
# Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
# Space Complexity: O(N) as we are using a map data structure.

def subarrayWithXork(a,k):
    n = len(a)
    mpp = {}
    cnt = 0
    xr = 0
    mpp[xr] = 1
    for i in range(n):
        xr = xr ^ a[i]
        x = xr ^ k
        cnt += mpp.get(x,0)
        mpp[xr] = mpp.get(xr,0) + 1
    return cnt

a = [4,2,2,6,4]
k = 6
ans = subarrayWithXork(a,k)
(a,k)
print("The number of subarray with XOR k is: ",ans)