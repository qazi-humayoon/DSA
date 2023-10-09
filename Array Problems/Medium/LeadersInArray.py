# #Brute Force
# #Tc :- O(N*2)
# #Sc :- O(N) if we consider the space use to solve the ans

def leaders(arr,n):  
    ans = []
    
    for i in range(n):
        leader = True

        # Checking whether arr[i] is greater than all 
        # the elements in its right side
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                # If any element found is greater than current leader,
                # curr element is not the leader.
                leader = False
                break

        # Push all the leaders in ans array.
        if leader:
                ans.append(arr[i])

    return ans
# Array Initialization
arr = [16, 17, 4, 3, 5, 2]
n = len(arr)

res = leaders(arr,n)
print(res)

#_________________________________________________________________________________________________________________________

# #Optimal Force
# #Tc :- O(N)
# #Sc :- O(N) if we consider the space use to solve the ans

# def printLeaders(arr, n):
#     ans = []
  
#     # Last element of an array is always a leader,
#     # push into ans array.
#     max_elem = arr[n - 1]
#     ans.append(arr[n - 1])

#     # Start checking from the end whether a number is greater
#     # than max no. from right, hence leader.
#     for i in range(n - 2, -1, -1):
#         if arr[i] > max_elem:
#             ans.append(arr[i])
#             max_elem = arr[i]

#     return ans

# # Array Initialization
# arr = [10, 22, 12, 3, 0, 6]
# n =len(arr)
# res = printLeaders(arr,n)
# print(res)


#_________________________________________________________________________________________________________________________

#For Reference as reverse or slicing is taking too much time and test cases we not passing
#so used insert to insert elements at the 0 index

# def leaders(arr, n):
#     result = []
#     max_right = arr[n - 1]  # Initialize the maximum from the right as the rightmost element

#     # The rightmost element is always a leader
#     result.append(max_right)

#     # Traverse the array from right to left
#     for i in range(n - 2, -1, -1):
#         if arr[i] >= max_right:
#             # If the current element is greater than or equal to the current maximum from the right
#             # It is a leader, append it to the result (in reverse order)
#             result.insert(0, arr[i])
#             max_right = arr[i]
    
#     return result

# # Example usage:
# n = 6
# A = [16, 17, 4, 3, 5, 2]
# print(leaders(A, n))  # Output: [17, 5, 2]


