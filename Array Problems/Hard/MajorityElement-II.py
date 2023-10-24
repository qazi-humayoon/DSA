#Tc: O(N*2)
#Sc: o(2)

# def majorityele(arr):
#     n = len(arr)
#     ls = []
#     for i in range(n):
#         if len(ls) == 0 or ls[0] != arr[i]:
#             count = 0
#             for j in range(n):
#                 if arr[j] == arr[i]:
#                     count += 1
#             if count > n // 3:
#                 ls.append(arr[i])
#             if len(ls) == 2:
#                 break
#     return ls



# arr= [1,1,1,3,3,2,2,2]
# res = majorityele(arr)
# print(res)

#________________________________________________________________________________________________________________________________

#Tc: O(N)
#Sc: O(N)


# def majorityele(arr):
#     mpp = {}
#     ls = []
#     n = len(arr)
#     mini = (n // 3) + 1
#     for i in arr:
#         mpp[i] = mpp.get(i,0) + 1
    
#     for i,count in mpp.items():
#         if count >= mini:
#             ls.append(i)
#     return ls

# arr= [1,1,1,3,3,2,2,2]
# res = majorityele(arr)
# print(res)



#________________________________________________________________________________________________________________________________


#Moores Voting Algo
#Tc:O(2N)
#SC: O(1)

def majorityele(arr):
    n = len(arr)
    cnt1,cnt2 = 0,0
    el1 = float('-inf')
    el2 = float('-inf')
    for i in range(n):
        if cnt1 == 0 and el2 != arr[i]:
            cnt1 = 1
            el1 = arr[i]
        if cnt2 == 0 and el1 != arr[i]:
            cnt2 = 1
            el2 = arr[i]
        elif arr[i] == el1:
            cnt1 += 1
        elif arr[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1
    ls = []
    cnt1,cnt2 = 0,0
    for i in range(n):
        if arr[i] == el1:
            cnt1 += 1
        if  arr[i] == el2:
            cnt2 += 1
    mini = (n // 3) + 1        
    if cnt1 >= mini:
        ls.append(el1)
    if cnt2 >= mini:
        ls.append(el2)
    c = len(ls)
    if c == 0:
        return -1
    
    return ls


arr= [7, 8, 1, 7, 8, 2, 4, 4, 2, 4, 6, 4, 1, 7, 8, 6, 9, 3, 5, 6, 9, 3, 2, 7, 6, 3, 6, 3, 5, 3, 7, 2, 1, 5, 6, 6, 6, 7, 9, 6, 2, 3, 9 ,2 ,8, 5, 7, 7, 5, 9, 1]
res = majorityele(arr)
print(res)

