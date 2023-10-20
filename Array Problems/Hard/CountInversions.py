#Brute Force 
#Tc :- ~O(N^2)
#Sc :- O(1)
# def numberinversion(a):
#     n = len(a)
#     # Count the number of pairs:
#     count = 0
#     for i in range(n):
#         for j in range(i + 1,n):
#             if a[i] > a[j]:
#                 count += 1
#     return count


# a = [5, 4, 3, 2, 1]
# cnt = numberinversion(a)
# print("The number of inversions is:", cnt)

#___________------------___________________--------------------____________________---------------------_______________---------

#Optimal Approach
#Tc :- O(NLogN)
#Sc :- O(N)

def merge(a,low,mid,high):
    temp = []
    left = low
    right = mid + 1

    count = 0

    while left <= mid and right <= high:
        if a[left] <= a[right]:
            temp.append(a[left])
            left += 1
        else:
            temp.append(a[right])
            count += (mid - left + 1)
            right += 1
        
    while left <= mid:
        temp.append(a[left])
        left += 1
    while right <= high:
        temp.append(a[right])
        right += 1
    
    for i in range(low,high+1):
        a[i] = temp[i-low]
    
    return count

def numberinversion(a,low,high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += numberinversion(a,low,mid)
    count += numberinversion(a,mid+1,high)
    count += merge(a,low,mid,high)

    return count



a = [5, 4, 3, 2, 1]
n = len(a)
cnt = numberinversion(a, 0, n-1)
print("The number of inversions are:", cnt)