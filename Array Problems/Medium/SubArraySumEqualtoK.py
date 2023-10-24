# a= [0,0,0,0,0,0,0,0,0,0]
# n = len(a)
# count = 0
# k = 3
# for i in range(n):
#     for j in range(i,n):
#         s = 0
#         for l in range(i,j+1):
#             s += a[l]
#         if s == k:
#             count += 1
# print(count)

#_________________________________________________________________________

# a= [1,2,1,2,1]
# n = len(a)
# count = 0
# k = 3
# for i in range(n):
#     s = 0
#     for j in range(i,n):
#             s += a[j]
#             if s ==k:
#                 count += 1
# print(count)

#_________________________________________________________________________________________________________________________________

def find_all_subarrays_with_given_sum(arr, k):
    n = len(arr)  # size of the given array
    mpp = {}
    pre_sum = 0
    cnt = 0

    mpp[0] = 1  # Setting 0 in the dictionary
    for i in range(n):
        # Add the current element to prefix sum
        pre_sum += arr[i]

        # Calculate x-k
        remove = pre_sum - k

        # Add the number of subarrays to be removed
        cnt += mpp.get(remove, 0)

        # Update the count of prefix sum in the dictionary
        mpp[pre_sum] = mpp.get(pre_sum, 0) + 1

    return cnt

if __name__ == "__main__":
    arr = [1,1,1]
    k = 2
    cnt = find_all_subarrays_with_given_sum(arr, k)
    print("The number of subarrays is:",cnt)
