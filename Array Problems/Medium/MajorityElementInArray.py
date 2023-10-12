# arr = [2,2,1,1,1,2,2]
# n = len(arr)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[j] == arr[i]:
#             count += 1
#     if count > n//2:
#         print(arr[i])

#_____________________________________________________________________________________________________________________________

# from collections import Counter
# arr = [2,2,1,1,1,2,2]
# n =len(arr)
# counter = Counter(arr)
# for num,count in counter.items():
#     if count > (n//2):
#         print(num)

#_____________________________________________________________________________________________________________________________

# arr = [2,2,1,1,1,2,2]
# n =len(arr)
# mapp = {}
# for i in arr:
#     mapp[i] = mapp.get(i,0) + 1
# for num,count in mapp.items():
#     if count > (n//2):
#         print(num)

#______________________________________________________________________________________________________________



# def majorityElement(arr):
#     # Size of the given array
#     n = len(arr)
#     cnt = 0  # Count
#     el = None  # Element

#     # Applying the mooeri vooting algorithm
#     for i in range(n):
#         if cnt == 0:
#             cnt = 1
#             el = arr[i]
#         elif el == arr[i]:
#             cnt += 1
#         else:
#             cnt -= 1

#     # Checking if the stored element is the majority element
#     cnt1 = 0
#     for i in range(n):
#         if arr[i] == el:
#             cnt1 += 1

#     if cnt1 > (n / 2):
#         return el
#     return -1


# arr = [2, 2, 1, 1, 1, 2, 2]
# ans = majorityElement(arr)
# print("The majority element is:", ans)

