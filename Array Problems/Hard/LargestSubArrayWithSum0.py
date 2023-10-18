#Brute force 
#TC :- O(N^2)
#Sc :- O(1)

a = [1,-1,0,0,1]
n = len(a)
maxi = 0
target = 0
for i in range(n):
    summ = 0
    for j in range(i,n):
        summ += a[j]
        
        # for k in range(i,j+1):
            
        if summ == target:
            maxi = max(maxi,j-i+1)
print(maxi)

#______________________________________________________________________________________________________________________
#Optimal force 
#TC :- O(N)
#Sc :- O(N)

# a = [1,-1,0,0,1]
# n = len(a)
# mpp = {}
# maxi = 0
# summ = 0
# target = 0
# for i in range(n):
#     summ += a[i]

#     if summ == 0:
#         maxi = max(maxi,i+1)
    
#     if summ in mpp:
#         length = i - mpp[summ]
#         maxi = max(maxi,length)
#     if summ not in mpp:
#         mpp[summ] = i
# print(maxi)

