
#Using Hash map
# Time Compleixty : O( (m+n)log(m+n) ) . Inserting a key in map takes logN times,
# where N is no of elements in map. 
# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 
# O(1) {If Space of union ArrayList is not considered}

def find_union(arr1, arr2):
    freq = {}
    union = []
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        union.append(num)
    
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
for num in union:
    print(num, end=" ")
# ____________________________________________________________________________________________________

#Using the Set
# Time Compleixty : O( (m+n)log(m+n) ) . Inserting an element in a set takes logN time,
# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 
# O(1) {If Space of union ArrayList is not considered}

# def find_union(arr1, arr2):
#     s = set()
#     union = []
    
#     for num in arr1:
#         s.add(num)
    
#     for num in arr2:
#         s.add(num)
    
#     for num in s:
#         union.append(num)
    
#     return union

# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]

# union = find_union(arr1, arr2)

# print("Union of arr1 and arr2 is:")
# print(*union)

# ____________________________________________________________________________________________________

# Using Two Pointers
# Time Complexity: O(m+n), Because at max i runs for n times and j runs for m times
# Space Complexity : O(m+n) {If Space of Union ArrayList is considered} 
# O(1) {If Space of union ArrayList is not considered}

# def find_union(arr1,arr2):
#     i = 0
#     j = 0
#     union = []
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             if len(union) == 0 or union[-1] != arr1[i]:
#                 union.append(arr1[i])
#             i += 1
#         else:
#             if len(union) == 0 or union[-1] != arr2[j]:
#                 union.append(arr2[j])
#             j += 1
#     while i < len(arr1):
#         if union[-1] != arr1[i]:
#             union.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         if union[-1] != arr2[j]:
#             union.append(arr2[j])
#         j += 1
#     return union



# arr1 = [12,42]
# arr2 = [3 ,4 ,5, 28, 37, 42, 43, 46]
# union = find_union(arr1,arr2)
# print(*union)