# a = [8,8,9,9,10]
# for i in range(len(a)):
#     num = a[i]
#     for j in range(len(a)):
#         count = 0
#         if a[j] == num:
#             count += 1
#     if count == 1:
#         print(num)

# using hash map
# a = [8,8,9,9,10]
# n = len(a)
# maxi = max(a)
# hash = [0] *(maxi+1)
# for i in a:
#     hash[i] += 1

# for i in a:
#     if hash[i] == 1:
#         print(i)

#hashing using map data strucutre
# a = [8,8,9,9,10]
# n = len(a)
# freq = {}
# for i in a:
#     freq[i] = freq.get(i,0) + 1
# for i,count in freq.items():
#     if count == 1:
#         print(i)

#using the xor operation

a = [8,8,9,9,10]
n = len(a)
xor1 = 0
for i in range(len(a)):
    xor1 = xor1 ^ a[i]
print(xor1)