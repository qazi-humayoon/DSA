#Two cases either return the indexes of TWO SUMS or return YES or NO if the TWO INDEXES exist

#Brute force with time complexity of O(N*2)
# Space Complexity : O(1)
# a = [2,5,5,11]
# target = 10
# for i in range(len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i] + a[j] == target:
#             print(i,j)

#_____________________________________________________________________________________________________________________________

#better force with time complexity of O(Nlogn) logn if it is ordered map. It is also optimal solution if we are returning only 
# indexes and if we are returning just yes and no then it is better approach
# Space Complexity : O(1)
a = [2,5,5,11]
target = 10
mapp = {}
for i in range(len(a)):
    num = a[i]
    moreneeded = target - num
    if moreneeded in mapp:
        print(mapp[moreneeded],i)
    mapp[num] = i
#_____________________________________________________________________________________________________________________________

#optimal approach if we are returning only YES and No and not returning the indexes
#Tc = O(N)
# def twosum(a,target):
#     left,right = 0,len(a)-1
#     while left < right:
#         Sum = a[left] + a[right] 
#         if Sum == target:
#             return("YES")
#         elif Sum < target:
#             left += 1
#         else:
#             right -= 1
#     return "NO"
# a = [2,5,5,11]
# target = 10
# res = twosum(a,target)
# print(res)