#Brute solution
#Time Complexity :- O(2*N/2)
#Space Complexity :- O(N/2+N/2)

# a = [1,2,-3,-1,-2,2]
# n = len(a)
# temp = []
# temp1 =[]
# for i in range(n):
#     if a[i] > 0:
#         temp.append(a[i])
#     else:
#         temp1.append(a[i])
# for i in range(len(temp)):
#     a[2 * i] = temp[i]
#     a[2 * i + 1] = temp1[i]
# print(a)

#__________________________________________________________________________________________________________________

#Optimal solution
#Time Complexity :- O(N)
#Space Complexity :- O(N)
def RearrangebySign(a):
    n = len(a)
    
    # Define hash array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if a[i] < 0:
            ans[negIndex] = a[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = a[i]
            posIndex += 2
    
    return ans
    
# Test the function
a = [1,2,-4,-5]
ans = RearrangebySign(a)
print(ans)

#__________________________________________________________________________________________________________________

# def RearrangebySign(A, n):
#     # Define 2 lists, one for storing positive 
#     # and other for negative elements of the array.
#     pos = []
#     neg = []
    
#     # Segregate the array into positives and negatives.
#     for i in range(n):
#         if A[i] > 0:
#             pos.append(A[i])
#         else:
#             neg.append(A[i])
    
#     # If positives are lesser than the negatives.
#     if len(pos) < len(neg):
#         # First, fill array alternatively till the point 
#         # where positives and negatives are equal in number.
#         for i in range(len(pos)):
#             A[2*i] = pos[i]
#             A[2*i+1] = neg[i]
        
#         # Fill the remaining negatives at the end of the array.
#         index = len(pos)*2
#         for i in range(len(neg)-len(pos)):
#             A[index] = neg[len(pos)+i]
#             index += 1
    
#     # If negatives are lesser than the positives.
#     else:
#         # First, fill array alternatively till the point 
#         # where positives and negatives are equal in number.
#         for i in range(len(neg)):
#             A[2*i] = pos[i]
#             A[2*i+1] = neg[i]
        
#         # Fill the remaining positives at the end of the array.
#         index = len(neg)*2
#         for i in range(len(pos)-len(neg)):
#             A[index] = pos[len(neg)+i]
#             index += 1
    
#     return A

# # Array initialization
# n = 6
# A = [1, 2, -4, -5, 3, 4]

# ans = RearrangebySign(A, n)

# for i in range(len(ans)):
#     print(ans[i], end=" ")