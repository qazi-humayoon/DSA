# Brute TC: O(N * K) Sc: O(N)
# def sliding(a, k):
#     n = len(a)
#     st = []

#     for i in range(n - k + 1):
#         maxi = a[i]
#         for j in range(i + 1, i + k):
#             maxi = max(maxi, a[j])

#         st.append(maxi)

#     return st

# a = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# ans = sliding(a, k)
# print(ans)

#_____________________________________________________________________________________________________________

#Optimal
# TC O(N + N ~ O(N)
def sliding(a, k):
    n = len(a)
    st = []
    dq = []
    
    for i in range(n):
        # Remove elements that are out of the current window
        while dq and dq[0] < i - k + 1:
            dq.pop(0)
        
        # Remove elements that are smaller than the current element
        while dq and a[dq[-1]] < a[i]:
            dq.pop()

        dq.append(i)

        # Add the maximum element of the current window to the result
        if i >= k - 1:
            st.append(a[dq[0]])

    return st

a = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
ans = sliding(a, k)
print(ans)

